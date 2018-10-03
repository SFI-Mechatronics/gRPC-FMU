/*
 * The MIT License
 *
 * Copyright 2017-2018. Norwegian University of Technology
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

package no.mechatronics.sfi.fmuproxy.grpc.services

import com.google.protobuf.ByteString
import io.grpc.Status
import io.grpc.stub.StreamObserver
import no.mechatronics.sfi.fmi4j.common.FmiStatus
import no.mechatronics.sfi.fmi4j.common.FmuSlave
import no.mechatronics.sfi.fmi4j.common.RealArray
import no.mechatronics.sfi.fmi4j.common.StringArray
import no.mechatronics.sfi.fmi4j.importer.Fmu
import no.mechatronics.sfi.fmuproxy.fmu.FmuSlaves
import no.mechatronics.sfi.fmuproxy.grpc.*
import no.mechatronics.sfi.fmuproxy.solver.parseSolver
import no.sfi.mechatronics.fmi4j.me.ApacheSolvers
import org.slf4j.Logger
import org.slf4j.LoggerFactory

class GrpcFmuServiceImpl(
        private val fmus: Map<String, Fmu>
): FmuServiceGrpc.FmuServiceImplBase() {

    private inline fun getFmu(fmuId: String, responseObserver: StreamObserver<*>, block: Fmu.() -> Unit) {
        fmus[fmuId]?.apply(block) ?: noSuchFmuReply(fmuId, responseObserver)
    }

    private inline fun getSlave(instanceId: String, responseObserver: StreamObserver<*>, block: FmuSlave.() -> Unit) {
        FmuSlaves[instanceId]?.apply(block) ?: noSuchInstanceReply(instanceId, responseObserver)
    }

    override fun getModelDescription(request: Service.GetModelDescriptionRequest, responseObserver: StreamObserver<Proto.ModelDescription>) {
        getFmu(request.fmuId, responseObserver) {
            responseObserver.onNext(modelDescription.protoType())
            responseObserver.onCompleted()
        }
    }

    override fun canCreateInstanceFromCS(request: Service.CanCreateInstanceFromCSRequest, responseObserver: StreamObserver<Service.Bool>) {
        getFmu(request.fmuId, responseObserver) {
            responseObserver.onNext(supportsCoSimulation.protoType())
            responseObserver.onCompleted()
        }
    }

    override fun canCreateInstanceFromME(request: Service.CanCreateInstanceFromMERequest, responseObserver: StreamObserver<Service.Bool>) {
        getFmu(request.fmuId, responseObserver) {
            responseObserver.onNext(supportsModelExchange.protoType())
            responseObserver.onCompleted()
        }
    }

    override fun createInstanceFromCS(request: Service.CreateInstanceFromCSRequest, responseObserver: StreamObserver<Service.InstanceId>) {

        getFmu(request.fmuId, responseObserver) {
            if (!supportsCoSimulation) {
                unSupportedOperationException(responseObserver, "FMU does not support Co-simulation!")
            } else {
                FmuSlaves.put(asCoSimulationFmu().newInstance()).also { id ->
                    Service.InstanceId.newBuilder().setValue(id).also {
                        responseObserver.onNext(it.build())
                        responseObserver.onCompleted()
                    }
                }
            }
        }
    }

    override fun createInstanceFromME(request: Service.CreateInstanceFromMERequest, responseObserver: StreamObserver<Service.InstanceId>) {

        getFmu(request.fmuId, responseObserver) {
            if (!supportsModelExchange) {
                unSupportedOperationException(responseObserver, "FMU does not support Model Exchange!")
            } else {
                fun selectDefaultIntegrator(): no.mechatronics.sfi.fmi4j.solvers.Solver {
                    val stepSize = modelDescription.defaultExperiment?.stepSize ?: 1E-3
                    LOG.warn("No valid solver found.. Defaulting to Euler with $stepSize stepSize")
                    return ApacheSolvers.euler(stepSize)
                }

                val solver = parseSolver(request.solver.name, request.solver.settings) ?: selectDefaultIntegrator()
                FmuSlaves.put(asModelExchangeFmu().newInstance(solver)).also { id ->
                    Service.InstanceId.newBuilder().setValue(id).also {
                        responseObserver.onNext(it.build())
                        responseObserver.onCompleted()
                    }
                }
            }
        }
    }

    override fun getCoSimulationModelDescription(request: Service.GetCoSimulationModelDescriptionRequest, responseObserver: StreamObserver<Proto.CoSimulationModelDescription>) {
        getSlave(request.instanceId, responseObserver) {
            responseObserver.onNext(modelDescription.protoType())
            responseObserver.onCompleted()
        }
    }
    
    override fun readInteger(request: Service.ReadRequest, responseObserver: StreamObserver<Service.IntegerRead>) {
       
        getSlave(request.instanceId, responseObserver) {
            val vr = request.valueReferencesList.toLongArray()
            val values = IntArray(vr.size)
            val status = variableAccessor.readInteger(vr, values)
            Service.IntegerRead.newBuilder().setStatus(status.protoType()).apply {
                values.forEach { addValues(it) }
                responseObserver.onNext(build())
                responseObserver.onCompleted()
            }
        }
    }

    override fun readReal(request: Service.ReadRequest, responseObserver: StreamObserver<Service.RealRead>) {
        getSlave(request.instanceId, responseObserver) {
            val vr = request.valueReferencesList.toLongArray()
            val values = RealArray(vr.size)
            val status = variableAccessor.readReal(vr, values)
            Service.RealRead.newBuilder().setStatus(status.protoType()).apply {
                values.forEach { addValues(it) }
                responseObserver.onNext(build())
                responseObserver.onCompleted()
            }
        }
    }

    override fun readString(request: Service.ReadRequest, responseObserver: StreamObserver<Service.StringRead>) {
        getSlave(request.instanceId, responseObserver) {
            val vr = request.valueReferencesList.toLongArray()
            val values = StringArray(vr.size) {""}
            val status = variableAccessor.readString(vr, values)
            Service.StringRead.newBuilder().setStatus(status.protoType()).apply {
                values.forEach { addValues(it) }
                responseObserver.onNext(build())
                responseObserver.onCompleted()
            }
        }
    }

    override fun readBoolean(request: Service.ReadRequest, responseObserver: StreamObserver<Service.BooleanRead>) {
        getSlave(request.instanceId, responseObserver) {
            val vr = request.valueReferencesList.toLongArray()
            val values = BooleanArray(vr.size)
            val status = variableAccessor.readBoolean(vr, values)
            Service.BooleanRead.newBuilder().setStatus(status.protoType()).apply {
                values.forEach { addValues(it) }
                responseObserver.onNext(build())
                responseObserver.onCompleted()
            }
        }
    }

    override fun writeInteger(request: Service.WriteIntegerRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            val status = variableAccessor.writeInteger(request.valueReferencesList.toLongArray(), request.valuesList.toIntArray())
            statusReply(status, responseObserver)
        }
    }

    override fun writeReal(request: Service.WriteRealRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            val status = variableAccessor.writeReal(request.valueReferencesList.toLongArray(), request.valuesList.toDoubleArray())
            statusReply(status, responseObserver)
        }
    }

    override fun writeString(request: Service.WriteStringRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            val status = variableAccessor.writeString(request.valueReferencesList.toLongArray(), request.valuesList.toTypedArray())
            statusReply(status, responseObserver)
        }
    }

    override fun writeBoolean(request: Service.WriteBooleanRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            val status = variableAccessor.writeBoolean(request.valueReferencesList.toLongArray(), request.valuesList.toBooleanArray())
            statusReply(status, responseObserver)
        }
    }

    override fun init(request: Service.InitRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            val start = request.start
            val stop = request.stop
            val hasStart = start > 0
            val hasStop = stop > start
            if (hasStart && hasStop) {
                init(start, stop)
            } else if (hasStart) {
                init(start)
            } else {
                init()
            }
            statusReply(lastStatus, responseObserver)
        }
    }

    override fun step(request: Service.StepRequest, responseObserver: StreamObserver<Service.StepResponse>) {
        getSlave(request.instanceId, responseObserver) {
            doStep(request.stepSize)
            Service.StepResponse.newBuilder()
                    .setSimulationTime(simulationTime)
                    .setStatus(lastStatus.protoType()).also {
                        responseObserver.onNext(it.build())
                        responseObserver.onCompleted()
                    }

        }
    }

    override fun terminate(request: Service.TerminateRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            terminate()
            lastStatus.also { status ->
                LOG.debug("Terminated fmu with status: $status")
                statusReply(status, responseObserver)
            }
        }
    }

    override fun reset(request: Service.ResetRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
       getSlave(request.instanceId, responseObserver) {
            reset().also {
                statusReply(lastStatus, responseObserver)
            }
        }
    }

    override fun getFMUstate(request: Service.GetFMUstateRequest, responseObserver: StreamObserver<Service.GetFMUstateResponse>) {
        getSlave(request.instanceId, responseObserver) {
            if (!modelDescription.canGetAndSetFMUstate) {
                unSupportedOperationException(responseObserver, "FMU does not have capability 'canGetAndSetFMUstate'!")
            } else {

                Service.GetFMUstateResponse.newBuilder()
                        .setState(getFMUstate())
                        .setStatus(lastStatus.protoType()).also {
                            responseObserver.onNext(it.build())
                            responseObserver.onCompleted()
                        }

            }
        }
    }

    override fun setFMUstate(request: Service.SetFMUstateRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            if (!modelDescription.canGetAndSetFMUstate) {
                unSupportedOperationException(responseObserver, "FMU does not have capability 'canGetAndSetFMUstate'!")
            } else {

                setFMUstate(request.state)
                statusReply(lastStatus, responseObserver)

            }
        }
    }

    override fun freeFMUstate(request: Service.FreeFMUstateRequest, responseObserver: StreamObserver<Service.StatusResponse>) {
        getSlave(request.instanceId, responseObserver) {
            if (!modelDescription.canGetAndSetFMUstate) {
                unSupportedOperationException(responseObserver, "FMU does not have capability 'canGetAndSetFMUstate'!")
            } else {

                freeFMUstate(request.state)
                statusReply(lastStatus, responseObserver)

            }
        }
    }

    override fun serializeFMUstate(request: Service.SerializeFMUstateRequest, responseObserver: StreamObserver<Service.SerializeFMUstateResponse>) {
        getSlave(request.instanceId, responseObserver) {
            if (!modelDescription.canSerializeFMUstate) {
                unSupportedOperationException(responseObserver, "FMU does not have capability 'canSerializeFMUstate'!")
            } else {

                Service.SerializeFMUstateResponse.newBuilder()
                        .setState(ByteString.copyFrom(serializeFMUstate(request.state)))
                        .setStatus(lastStatus.protoType()).also {
                            responseObserver.onNext(it.build())
                            responseObserver.onCompleted()
                        }

            }
        }
    }

    override fun deSerializeFMUstate(request: Service.DeSerializeFMUstateRequest, responseObserver: StreamObserver<Service.DeSerializeFMUstateResponse>) {
        getSlave(request.instanceId, responseObserver) {

            if (!modelDescription.canSerializeFMUstate) {
                unSupportedOperationException(responseObserver, "FMU does not have capability 'canSerializeFMUstate'!")
            } else {

                Service.DeSerializeFMUstateResponse.newBuilder()
                        .setState(getFMUstate())
                        .setStatus(lastStatus.protoType()).also {
                            responseObserver.onNext(it.build())
                            responseObserver.onCompleted()
                        }
            }
        }
    }

    private companion object {
        val LOG: Logger = LoggerFactory.getLogger(GrpcFmuServiceImpl::class.java)

        fun statusReply(status: FmiStatus, responseObserver: StreamObserver<Service.StatusResponse>) {
            Service.StatusResponse.newBuilder()
                    .setStatus(status.protoType())
                    .build().also {
                        responseObserver.onNext(it)
                        responseObserver.onCompleted()
                    }
        }

        fun noSuchFmuReply(id: String, responseObserver: StreamObserver<*>) {
            responseObserver.onError(Status.INVALID_ARGUMENT
                            .augmentDescription("NoSuchFmuException")
                            .withDescription("No FMU with id=$id!")
                            .asRuntimeException()
            )
        }


        fun noSuchInstanceReply(id: String, responseObserver: StreamObserver<*>) {
            responseObserver.onError(Status.INVALID_ARGUMENT
                            .augmentDescription("NoSuchInstanceException")
                            .withDescription( "No instance with id=$id!")
                            .asRuntimeException()
            )
        }

        fun unSupportedOperationException(responseObserver: StreamObserver<*>, description: String) {
            responseObserver.onError(Status.UNAVAILABLE
                    .augmentDescription("UnsupportedOperationException")
                    .withDescription(description)
                    .asRuntimeException())
        }


    }

}


