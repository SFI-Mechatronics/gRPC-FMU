# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import definitions_pb2 as definitions__pb2


class GenericFmuServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateInstanceFromCS = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/CreateInstanceFromCS',
        request_serializer=definitions__pb2.Empty.SerializeToString,
        response_deserializer=definitions__pb2.UInt.FromString,
        )
    self.CreateInstanceFromME = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/CreateInstanceFromME',
        request_serializer=definitions__pb2.Integrator.SerializeToString,
        response_deserializer=definitions__pb2.UInt.FromString,
        )
    self.GetGuid = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/GetGuid',
        request_serializer=definitions__pb2.Empty.SerializeToString,
        response_deserializer=definitions__pb2.Str.FromString,
        )
    self.GetModelName = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/GetModelName',
        request_serializer=definitions__pb2.Empty.SerializeToString,
        response_deserializer=definitions__pb2.Str.FromString,
        )
    self.GetModelVariables = channel.unary_stream(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/GetModelVariables',
        request_serializer=definitions__pb2.Empty.SerializeToString,
        response_deserializer=definitions__pb2.ScalarVariable.FromString,
        )
    self.GetCurrentTime = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/GetCurrentTime',
        request_serializer=definitions__pb2.UInt.SerializeToString,
        response_deserializer=definitions__pb2.Real.FromString,
        )
    self.IsTerminated = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/IsTerminated',
        request_serializer=definitions__pb2.UInt.SerializeToString,
        response_deserializer=definitions__pb2.Bool.FromString,
        )
    self.Init = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/Init',
        request_serializer=definitions__pb2.InitRequest.SerializeToString,
        response_deserializer=definitions__pb2.Bool.FromString,
        )
    self.Step = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/Step',
        request_serializer=definitions__pb2.StepRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.Terminate = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/Terminate',
        request_serializer=definitions__pb2.UInt.SerializeToString,
        response_deserializer=definitions__pb2.Bool.FromString,
        )
    self.Reset = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/Reset',
        request_serializer=definitions__pb2.UInt.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.ReadInteger = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/ReadInteger',
        request_serializer=definitions__pb2.ReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.Int.FromString,
        )
    self.ReadReal = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/ReadReal',
        request_serializer=definitions__pb2.ReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.Real.FromString,
        )
    self.ReadString = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/ReadString',
        request_serializer=definitions__pb2.ReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.Str.FromString,
        )
    self.ReadBoolean = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/ReadBoolean',
        request_serializer=definitions__pb2.ReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.Bool.FromString,
        )
    self.BulkReadInteger = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkReadInteger',
        request_serializer=definitions__pb2.BulkReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.IntList.FromString,
        )
    self.BulkReadReal = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkReadReal',
        request_serializer=definitions__pb2.BulkReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.RealList.FromString,
        )
    self.BulkReadString = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkReadString',
        request_serializer=definitions__pb2.BulkReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.StrList.FromString,
        )
    self.BulkReadBoolean = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkReadBoolean',
        request_serializer=definitions__pb2.BulkReadRequest.SerializeToString,
        response_deserializer=definitions__pb2.BoolList.FromString,
        )
    self.WriteInteger = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/WriteInteger',
        request_serializer=definitions__pb2.WriteIntegerRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.WriteReal = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/WriteReal',
        request_serializer=definitions__pb2.WriteRealRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.WriteString = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/WriteString',
        request_serializer=definitions__pb2.WriteStringRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.WriteBoolean = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/WriteBoolean',
        request_serializer=definitions__pb2.WriteBooleanRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.BulkWriteInteger = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkWriteInteger',
        request_serializer=definitions__pb2.BulkWriteIntegerRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.BulkWriteReal = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkWriteReal',
        request_serializer=definitions__pb2.BulkWriteRealRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.BulkWriteString = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkWriteString',
        request_serializer=definitions__pb2.BulkWriteStringRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )
    self.BulkWriteBoolean = channel.unary_unary(
        '/no.mechatronics.sfi.grpc_fmu.GenericFmuService/BulkWriteBoolean',
        request_serializer=definitions__pb2.BulkWriteBooleanRequest.SerializeToString,
        response_deserializer=definitions__pb2.Status.FromString,
        )


class GenericFmuServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateInstanceFromCS(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateInstanceFromME(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGuid(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModelName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModelVariables(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCurrentTime(self, request, context):
    """instance methods
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def IsTerminated(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Init(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Step(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Terminate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Reset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadInteger(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadReal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadBoolean(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkReadInteger(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkReadReal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkReadString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkReadBoolean(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteInteger(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteReal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteBoolean(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkWriteInteger(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkWriteReal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkWriteString(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BulkWriteBoolean(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GenericFmuServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateInstanceFromCS': grpc.unary_unary_rpc_method_handler(
          servicer.CreateInstanceFromCS,
          request_deserializer=definitions__pb2.Empty.FromString,
          response_serializer=definitions__pb2.UInt.SerializeToString,
      ),
      'CreateInstanceFromME': grpc.unary_unary_rpc_method_handler(
          servicer.CreateInstanceFromME,
          request_deserializer=definitions__pb2.Integrator.FromString,
          response_serializer=definitions__pb2.UInt.SerializeToString,
      ),
      'GetGuid': grpc.unary_unary_rpc_method_handler(
          servicer.GetGuid,
          request_deserializer=definitions__pb2.Empty.FromString,
          response_serializer=definitions__pb2.Str.SerializeToString,
      ),
      'GetModelName': grpc.unary_unary_rpc_method_handler(
          servicer.GetModelName,
          request_deserializer=definitions__pb2.Empty.FromString,
          response_serializer=definitions__pb2.Str.SerializeToString,
      ),
      'GetModelVariables': grpc.unary_stream_rpc_method_handler(
          servicer.GetModelVariables,
          request_deserializer=definitions__pb2.Empty.FromString,
          response_serializer=definitions__pb2.ScalarVariable.SerializeToString,
      ),
      'GetCurrentTime': grpc.unary_unary_rpc_method_handler(
          servicer.GetCurrentTime,
          request_deserializer=definitions__pb2.UInt.FromString,
          response_serializer=definitions__pb2.Real.SerializeToString,
      ),
      'IsTerminated': grpc.unary_unary_rpc_method_handler(
          servicer.IsTerminated,
          request_deserializer=definitions__pb2.UInt.FromString,
          response_serializer=definitions__pb2.Bool.SerializeToString,
      ),
      'Init': grpc.unary_unary_rpc_method_handler(
          servicer.Init,
          request_deserializer=definitions__pb2.InitRequest.FromString,
          response_serializer=definitions__pb2.Bool.SerializeToString,
      ),
      'Step': grpc.unary_unary_rpc_method_handler(
          servicer.Step,
          request_deserializer=definitions__pb2.StepRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'Terminate': grpc.unary_unary_rpc_method_handler(
          servicer.Terminate,
          request_deserializer=definitions__pb2.UInt.FromString,
          response_serializer=definitions__pb2.Bool.SerializeToString,
      ),
      'Reset': grpc.unary_unary_rpc_method_handler(
          servicer.Reset,
          request_deserializer=definitions__pb2.UInt.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'ReadInteger': grpc.unary_unary_rpc_method_handler(
          servicer.ReadInteger,
          request_deserializer=definitions__pb2.ReadRequest.FromString,
          response_serializer=definitions__pb2.Int.SerializeToString,
      ),
      'ReadReal': grpc.unary_unary_rpc_method_handler(
          servicer.ReadReal,
          request_deserializer=definitions__pb2.ReadRequest.FromString,
          response_serializer=definitions__pb2.Real.SerializeToString,
      ),
      'ReadString': grpc.unary_unary_rpc_method_handler(
          servicer.ReadString,
          request_deserializer=definitions__pb2.ReadRequest.FromString,
          response_serializer=definitions__pb2.Str.SerializeToString,
      ),
      'ReadBoolean': grpc.unary_unary_rpc_method_handler(
          servicer.ReadBoolean,
          request_deserializer=definitions__pb2.ReadRequest.FromString,
          response_serializer=definitions__pb2.Bool.SerializeToString,
      ),
      'BulkReadInteger': grpc.unary_unary_rpc_method_handler(
          servicer.BulkReadInteger,
          request_deserializer=definitions__pb2.BulkReadRequest.FromString,
          response_serializer=definitions__pb2.IntList.SerializeToString,
      ),
      'BulkReadReal': grpc.unary_unary_rpc_method_handler(
          servicer.BulkReadReal,
          request_deserializer=definitions__pb2.BulkReadRequest.FromString,
          response_serializer=definitions__pb2.RealList.SerializeToString,
      ),
      'BulkReadString': grpc.unary_unary_rpc_method_handler(
          servicer.BulkReadString,
          request_deserializer=definitions__pb2.BulkReadRequest.FromString,
          response_serializer=definitions__pb2.StrList.SerializeToString,
      ),
      'BulkReadBoolean': grpc.unary_unary_rpc_method_handler(
          servicer.BulkReadBoolean,
          request_deserializer=definitions__pb2.BulkReadRequest.FromString,
          response_serializer=definitions__pb2.BoolList.SerializeToString,
      ),
      'WriteInteger': grpc.unary_unary_rpc_method_handler(
          servicer.WriteInteger,
          request_deserializer=definitions__pb2.WriteIntegerRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'WriteReal': grpc.unary_unary_rpc_method_handler(
          servicer.WriteReal,
          request_deserializer=definitions__pb2.WriteRealRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'WriteString': grpc.unary_unary_rpc_method_handler(
          servicer.WriteString,
          request_deserializer=definitions__pb2.WriteStringRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'WriteBoolean': grpc.unary_unary_rpc_method_handler(
          servicer.WriteBoolean,
          request_deserializer=definitions__pb2.WriteBooleanRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'BulkWriteInteger': grpc.unary_unary_rpc_method_handler(
          servicer.BulkWriteInteger,
          request_deserializer=definitions__pb2.BulkWriteIntegerRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'BulkWriteReal': grpc.unary_unary_rpc_method_handler(
          servicer.BulkWriteReal,
          request_deserializer=definitions__pb2.BulkWriteRealRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'BulkWriteString': grpc.unary_unary_rpc_method_handler(
          servicer.BulkWriteString,
          request_deserializer=definitions__pb2.BulkWriteStringRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
      'BulkWriteBoolean': grpc.unary_unary_rpc_method_handler(
          servicer.BulkWriteBoolean,
          request_deserializer=definitions__pb2.BulkWriteBooleanRequest.FromString,
          response_serializer=definitions__pb2.Status.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'no.mechatronics.sfi.grpc_fmu.GenericFmuService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
