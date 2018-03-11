// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: service.proto

package no.mechatronics.sfi.fmu_proxy.grpc;

public final class Service {
  private Service() {}
  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistryLite registry) {
  }

  public static void registerAllExtensions(
      com.google.protobuf.ExtensionRegistry registry) {
    registerAllExtensions(
        (com.google.protobuf.ExtensionRegistryLite) registry);
  }

  public static com.google.protobuf.Descriptors.FileDescriptor
      getDescriptor() {
    return descriptor;
  }
  private static  com.google.protobuf.Descriptors.FileDescriptor
      descriptor;
  static {
    java.lang.String[] descriptorData = {
      "\n\rservice.proto\022\"no.mechatronics.sfi.fmu" +
      "_proxy.grpc\032\033google/protobuf/empty.proto" +
      "\032\021definitions.proto2\347\030\n\nFmuService\022j\n\024Su" +
      "pportsCoSimulation\022(.no.mechatronics.sfi" +
      ".fmu_proxy.grpc.UInt\032(.no.mechatronics.s" +
      "fi.fmu_proxy.grpc.Bool\022k\n\025SupportsModelE" +
      "xchange\022(.no.mechatronics.sfi.fmu_proxy." +
      "grpc.UInt\032(.no.mechatronics.sfi.fmu_prox" +
      "y.grpc.Bool\022Y\n\026GetModelDescriptionXml\022\026." +
      "google.protobuf.Empty\032\'.no.mechatronics." +
      "sfi.fmu_proxy.grpc.Str\022c\n\023GetModelDescri" +
      "ption\022\026.google.protobuf.Empty\0324.no.mecha" +
      "tronics.sfi.fmu_proxy.grpc.ModelDescript" +
      "ion\022X\n\024CreateInstanceFromCS\022\026.google.pro" +
      "tobuf.Empty\032(.no.mechatronics.sfi.fmu_pr" +
      "oxy.grpc.UInt\022p\n\024CreateInstanceFromME\022.." +
      "no.mechatronics.sfi.fmu_proxy.grpc.Integ" +
      "rator\032(.no.mechatronics.sfi.fmu_proxy.gr" +
      "pc.UInt\022d\n\016GetCurrentTime\022(.no.mechatron" +
      "ics.sfi.fmu_proxy.grpc.UInt\032(.no.mechatr" +
      "onics.sfi.fmu_proxy.grpc.Real\022b\n\014IsTermi" +
      "nated\022(.no.mechatronics.sfi.fmu_proxy.gr" +
      "pc.UInt\032(.no.mechatronics.sfi.fmu_proxy." +
      "grpc.Bool\022j\n\024CanGetAndSetFMUstate\022(.no.m" +
      "echatronics.sfi.fmu_proxy.grpc.UInt\032(.no" +
      ".mechatronics.sfi.fmu_proxy.grpc.Bool\022a\n" +
      "\004Init\022/.no.mechatronics.sfi.fmu_proxy.gr" +
      "pc.InitRequest\032(.no.mechatronics.sfi.fmu" +
      "_proxy.grpc.Bool\022c\n\004Step\022/.no.mechatroni" +
      "cs.sfi.fmu_proxy.grpc.StepRequest\032*.no.m" +
      "echatronics.sfi.fmu_proxy.grpc.Status\022_\n" +
      "\tTerminate\022(.no.mechatronics.sfi.fmu_pro" +
      "xy.grpc.UInt\032(.no.mechatronics.sfi.fmu_p" +
      "roxy.grpc.Bool\022]\n\005Reset\022(.no.mechatronic" +
      "s.sfi.fmu_proxy.grpc.UInt\032*.no.mechatron" +
      "ics.sfi.fmu_proxy.grpc.Status\022k\n\013ReadInt" +
      "eger\022/.no.mechatronics.sfi.fmu_proxy.grp" +
      "c.ReadRequest\032+.no.mechatronics.sfi.fmu_" +
      "proxy.grpc.IntRead\022i\n\010ReadReal\022/.no.mech" +
      "atronics.sfi.fmu_proxy.grpc.ReadRequest\032" +
      ",.no.mechatronics.sfi.fmu_proxy.grpc.Rea" +
      "lRead\022j\n\nReadString\022/.no.mechatronics.sf" +
      "i.fmu_proxy.grpc.ReadRequest\032+.no.mechat" +
      "ronics.sfi.fmu_proxy.grpc.StrRead\022l\n\013Rea" +
      "dBoolean\022/.no.mechatronics.sfi.fmu_proxy" +
      ".grpc.ReadRequest\032,.no.mechatronics.sfi." +
      "fmu_proxy.grpc.BoolRead\022w\n\017BulkReadInteg" +
      "er\0223.no.mechatronics.sfi.fmu_proxy.grpc." +
      "BulkReadRequest\032/.no.mechatronics.sfi.fm" +
      "u_proxy.grpc.IntListRead\022u\n\014BulkReadReal" +
      "\0223.no.mechatronics.sfi.fmu_proxy.grpc.Bu" +
      "lkReadRequest\0320.no.mechatronics.sfi.fmu_" +
      "proxy.grpc.RealListRead\022v\n\016BulkReadStrin" +
      "g\0223.no.mechatronics.sfi.fmu_proxy.grpc.B" +
      "ulkReadRequest\032/.no.mechatronics.sfi.fmu" +
      "_proxy.grpc.StrListRead\022x\n\017BulkReadBoole" +
      "an\0223.no.mechatronics.sfi.fmu_proxy.grpc." +
      "BulkReadRequest\0320.no.mechatronics.sfi.fm" +
      "u_proxy.grpc.BoolListRead\022o\n\014WriteIntege" +
      "r\0223.no.mechatronics.sfi.fmu_proxy.grpc.W" +
      "riteIntRequest\032*.no.mechatronics.sfi.fmu" +
      "_proxy.grpc.Status\022m\n\tWriteReal\0224.no.mec" +
      "hatronics.sfi.fmu_proxy.grpc.WriteRealRe" +
      "quest\032*.no.mechatronics.sfi.fmu_proxy.gr" +
      "pc.Status\022n\n\013WriteString\0223.no.mechatroni" +
      "cs.sfi.fmu_proxy.grpc.WriteStrRequest\032*." +
      "no.mechatronics.sfi.fmu_proxy.grpc.Statu" +
      "s\022p\n\014WriteBoolean\0224.no.mechatronics.sfi." +
      "fmu_proxy.grpc.WriteBoolRequest\032*.no.mec" +
      "hatronics.sfi.fmu_proxy.grpc.Status\022w\n\020B" +
      "ulkWriteInteger\0227.no.mechatronics.sfi.fm" +
      "u_proxy.grpc.BulkWriteIntRequest\032*.no.me" +
      "chatronics.sfi.fmu_proxy.grpc.Status\022u\n\r" +
      "BulkWriteReal\0228.no.mechatronics.sfi.fmu_" +
      "proxy.grpc.BulkWriteRealRequest\032*.no.mec" +
      "hatronics.sfi.fmu_proxy.grpc.Status\022v\n\017B" +
      "ulkWriteString\0227.no.mechatronics.sfi.fmu" +
      "_proxy.grpc.BulkWriteStrRequest\032*.no.mec" +
      "hatronics.sfi.fmu_proxy.grpc.Status\022x\n\020B" +
      "ulkWriteBoolean\0228.no.mechatronics.sfi.fm" +
      "u_proxy.grpc.BulkWriteBoolRequest\032*.no.m" +
      "echatronics.sfi.fmu_proxy.grpc.Statusb\006p" +
      "roto3"
    };
    com.google.protobuf.Descriptors.FileDescriptor.InternalDescriptorAssigner assigner =
        new com.google.protobuf.Descriptors.FileDescriptor.    InternalDescriptorAssigner() {
          public com.google.protobuf.ExtensionRegistry assignDescriptors(
              com.google.protobuf.Descriptors.FileDescriptor root) {
            descriptor = root;
            return null;
          }
        };
    com.google.protobuf.Descriptors.FileDescriptor
      .internalBuildGeneratedFileFrom(descriptorData,
        new com.google.protobuf.Descriptors.FileDescriptor[] {
          com.google.protobuf.EmptyProto.getDescriptor(),
          no.mechatronics.sfi.fmu_proxy.grpc.Proto.getDescriptor(),
        }, assigner);
    com.google.protobuf.EmptyProto.getDescriptor();
    no.mechatronics.sfi.fmu_proxy.grpc.Proto.getDescriptor();
  }

  // @@protoc_insertion_point(outer_class_scope)
}
