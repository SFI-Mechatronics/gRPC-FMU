package no.mechatronics.sfi.fmuproxy

import no.mechatronics.sfi.fmi4j.fmu.Fmu
import no.mechatronics.sfi.fmuproxy.avro.AvroFmuClient
import no.mechatronics.sfi.fmuproxy.avro.AvroFmuServer
import no.mechatronics.sfi.fmuproxy.grpc.GrpcFmuClient
import no.mechatronics.sfi.fmuproxy.grpc.GrpcFmuServer
import no.mechatronics.sfi.fmuproxy.grpc.Proto
import no.mechatronics.sfi.fmuproxy.thrift.StatusCode
import no.mechatronics.sfi.fmuproxy.thrift.ThriftFmuClient
import no.mechatronics.sfi.fmuproxy.thrift.ThriftFmuServer
import org.junit.Assert
import org.junit.Test
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.io.File
import kotlin.system.measureTimeMillis

class Benchmark {

    companion object {

        private val LOG: Logger = LoggerFactory.getLogger(Benchmark::class.java)

        private val fmuPath = File(System.getenv("TEST_FMUs"), "FMI_2.0/CoSimulation/win64/FMUSDK/2.0.4/BouncingBall/bouncingBall.fmu")

        private const val dt = 1E-3
        private const val stop = 50


    }

    @Test
    fun measureTimeLocal() {

        Fmu.from(fmuPath).use {

            it.asCoSimulationFmu().newInstance().use { instance ->

                instance.init()

                measureTimeMillis {
                    while (instance.currentTime < stop) {
                        val status = instance.doStep(dt)
                        Assert.assertTrue(status)
                    }
                }.also {
                    LOG.info("Local duration=${it}ms")
                }

            }

        }

    }


    @Test
    fun measureTimeThrift() {

        Fmu.from(fmuPath).use {

            val server = ThriftFmuServer(it)
            val port = server.start()

            val client = ThriftFmuClient("localhost", port)

            client.createInstance().use { instance ->

                Assert.assertEquals(StatusCode.OK_STATUS, instance.init())

                measureTimeMillis {
                    while (instance.currentTime < stop) {
                        val status = instance.step(dt)
                        Assert.assertEquals(StatusCode.OK_STATUS, status)
                    }
                }.also {
                    LOG.info("Thrift duration=${it}ms")
                }

            }

            client.close()
            server.close()

        }

    }

    @Test
    fun measureTimeAvro() {

        Fmu.from(fmuPath).use {

            val server = AvroFmuServer(it)
            val port = server.start()

            val client = AvroFmuClient("localhost", port)

            client.createInstance().use { instance ->

                Assert.assertEquals(no.mechatronics.sfi.fmuproxy.avro.StatusCode.OK_STATUS, instance.init())

                measureTimeMillis {
                    while (instance.currentTime < stop) {
                        val status = instance.step(dt)
                        Assert.assertEquals(no.mechatronics.sfi.fmuproxy.avro.StatusCode.OK_STATUS, status)
                    }
                }.also {
                    LOG.info("Avro duration=${it}ms")
                }

            }

            client.close()
            server.close()

        }

    }

    @Test
    fun measureTimeGrpc() {

        Fmu.from(fmuPath).use {

            val server = GrpcFmuServer(it)
            val port = server.start()

            val client = GrpcFmuClient("localhost", port)

            client.createInstance().use { instance ->

                Assert.assertEquals(Proto.StatusCode.OK_STATUS, instance.init().code)

                measureTimeMillis {
                    while (instance.currentTime < stop) {
                        val status = instance.step(dt)
                        Assert.assertEquals(Proto.StatusCode.OK_STATUS, status.code)
                    }
                }.also {
                    LOG.info("gRPC duration=${it}ms")
                }

            }

            client.close()
            server.close()

        }

    }

}