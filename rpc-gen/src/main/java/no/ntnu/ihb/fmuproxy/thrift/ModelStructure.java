/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package no.ntnu.ihb.fmuproxy.thrift;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.13.0)", date = "2020-09-18")
public class ModelStructure implements org.apache.thrift.TBase<ModelStructure, ModelStructure._Fields>, java.io.Serializable, Cloneable, Comparable<ModelStructure> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("ModelStructure");

  private static final org.apache.thrift.protocol.TField OUTPUTS_FIELD_DESC = new org.apache.thrift.protocol.TField("outputs", org.apache.thrift.protocol.TType.LIST, (short)1);
  private static final org.apache.thrift.protocol.TField DERIVATIVES_FIELD_DESC = new org.apache.thrift.protocol.TField("derivatives", org.apache.thrift.protocol.TType.LIST, (short)2);
  private static final org.apache.thrift.protocol.TField INITIAL_UNKNOWNS_FIELD_DESC = new org.apache.thrift.protocol.TField("initial_unknowns", org.apache.thrift.protocol.TType.LIST, (short)3);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new ModelStructureStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new ModelStructureTupleSchemeFactory();

  private @org.apache.thrift.annotation.Nullable java.util.List<Unknown> outputs; // required
  private @org.apache.thrift.annotation.Nullable java.util.List<Unknown> derivatives; // required
  private @org.apache.thrift.annotation.Nullable java.util.List<Unknown> initial_unknowns; // required

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    OUTPUTS((short)1, "outputs"),
    DERIVATIVES((short)2, "derivatives"),
    INITIAL_UNKNOWNS((short)3, "initial_unknowns");

    private static final java.util.Map<java.lang.String, _Fields> byName = new java.util.HashMap<java.lang.String, _Fields>();

    static {
      for (_Fields field : java.util.EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    @org.apache.thrift.annotation.Nullable
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // OUTPUTS
          return OUTPUTS;
        case 2: // DERIVATIVES
          return DERIVATIVES;
        case 3: // INITIAL_UNKNOWNS
          return INITIAL_UNKNOWNS;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new java.lang.IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    @org.apache.thrift.annotation.Nullable
    public static _Fields findByName(java.lang.String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final java.lang.String _fieldName;

    _Fields(short thriftId, java.lang.String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public java.lang.String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.OUTPUTS, new org.apache.thrift.meta_data.FieldMetaData("outputs", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.ListMetaData(org.apache.thrift.protocol.TType.LIST, 
            new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, Unknown.class))));
    tmpMap.put(_Fields.DERIVATIVES, new org.apache.thrift.meta_data.FieldMetaData("derivatives", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.ListMetaData(org.apache.thrift.protocol.TType.LIST, 
            new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, Unknown.class))));
    tmpMap.put(_Fields.INITIAL_UNKNOWNS, new org.apache.thrift.meta_data.FieldMetaData("initial_unknowns", org.apache.thrift.TFieldRequirementType.DEFAULT, 
        new org.apache.thrift.meta_data.ListMetaData(org.apache.thrift.protocol.TType.LIST, 
            new org.apache.thrift.meta_data.StructMetaData(org.apache.thrift.protocol.TType.STRUCT, Unknown.class))));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(ModelStructure.class, metaDataMap);
  }

  public ModelStructure() {
  }

  public ModelStructure(
    java.util.List<Unknown> outputs,
    java.util.List<Unknown> derivatives,
    java.util.List<Unknown> initial_unknowns)
  {
    this();
    this.outputs = outputs;
    this.derivatives = derivatives;
    this.initial_unknowns = initial_unknowns;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public ModelStructure(ModelStructure other) {
    if (other.isSetOutputs()) {
      java.util.List<Unknown> __this__outputs = new java.util.ArrayList<Unknown>(other.outputs.size());
      for (Unknown other_element : other.outputs) {
        __this__outputs.add(new Unknown(other_element));
      }
      this.outputs = __this__outputs;
    }
    if (other.isSetDerivatives()) {
      java.util.List<Unknown> __this__derivatives = new java.util.ArrayList<Unknown>(other.derivatives.size());
      for (Unknown other_element : other.derivatives) {
        __this__derivatives.add(new Unknown(other_element));
      }
      this.derivatives = __this__derivatives;
    }
    if (other.isSetInitialUnknowns()) {
      java.util.List<Unknown> __this__initial_unknowns = new java.util.ArrayList<Unknown>(other.initial_unknowns.size());
      for (Unknown other_element : other.initial_unknowns) {
        __this__initial_unknowns.add(new Unknown(other_element));
      }
      this.initial_unknowns = __this__initial_unknowns;
    }
  }

  public ModelStructure deepCopy() {
    return new ModelStructure(this);
  }

  @Override
  public void clear() {
    this.outputs = null;
    this.derivatives = null;
    this.initial_unknowns = null;
  }

  public int getOutputsSize() {
    return (this.outputs == null) ? 0 : this.outputs.size();
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.Iterator<Unknown> getOutputsIterator() {
    return (this.outputs == null) ? null : this.outputs.iterator();
  }

  public void addToOutputs(Unknown elem) {
    if (this.outputs == null) {
      this.outputs = new java.util.ArrayList<Unknown>();
    }
    this.outputs.add(elem);
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.List<Unknown> getOutputs() {
    return this.outputs;
  }

  public ModelStructure setOutputs(@org.apache.thrift.annotation.Nullable java.util.List<Unknown> outputs) {
    this.outputs = outputs;
    return this;
  }

  public void unsetOutputs() {
    this.outputs = null;
  }

  /** Returns true if field outputs is set (has been assigned a value) and false otherwise */
  public boolean isSetOutputs() {
    return this.outputs != null;
  }

  public void setOutputsIsSet(boolean value) {
    if (!value) {
      this.outputs = null;
    }
  }

  public int getDerivativesSize() {
    return (this.derivatives == null) ? 0 : this.derivatives.size();
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.Iterator<Unknown> getDerivativesIterator() {
    return (this.derivatives == null) ? null : this.derivatives.iterator();
  }

  public void addToDerivatives(Unknown elem) {
    if (this.derivatives == null) {
      this.derivatives = new java.util.ArrayList<Unknown>();
    }
    this.derivatives.add(elem);
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.List<Unknown> getDerivatives() {
    return this.derivatives;
  }

  public ModelStructure setDerivatives(@org.apache.thrift.annotation.Nullable java.util.List<Unknown> derivatives) {
    this.derivatives = derivatives;
    return this;
  }

  public void unsetDerivatives() {
    this.derivatives = null;
  }

  /** Returns true if field derivatives is set (has been assigned a value) and false otherwise */
  public boolean isSetDerivatives() {
    return this.derivatives != null;
  }

  public void setDerivativesIsSet(boolean value) {
    if (!value) {
      this.derivatives = null;
    }
  }

  public int getInitialUnknownsSize() {
    return (this.initial_unknowns == null) ? 0 : this.initial_unknowns.size();
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.Iterator<Unknown> getInitialUnknownsIterator() {
    return (this.initial_unknowns == null) ? null : this.initial_unknowns.iterator();
  }

  public void addToInitialUnknowns(Unknown elem) {
    if (this.initial_unknowns == null) {
      this.initial_unknowns = new java.util.ArrayList<Unknown>();
    }
    this.initial_unknowns.add(elem);
  }

  @org.apache.thrift.annotation.Nullable
  public java.util.List<Unknown> getInitialUnknowns() {
    return this.initial_unknowns;
  }

  public ModelStructure setInitialUnknowns(@org.apache.thrift.annotation.Nullable java.util.List<Unknown> initial_unknowns) {
    this.initial_unknowns = initial_unknowns;
    return this;
  }

  public void unsetInitialUnknowns() {
    this.initial_unknowns = null;
  }

  /** Returns true if field initial_unknowns is set (has been assigned a value) and false otherwise */
  public boolean isSetInitialUnknowns() {
    return this.initial_unknowns != null;
  }

  public void setInitialUnknownsIsSet(boolean value) {
    if (!value) {
      this.initial_unknowns = null;
    }
  }

  public void setFieldValue(_Fields field, @org.apache.thrift.annotation.Nullable java.lang.Object value) {
    switch (field) {
    case OUTPUTS:
      if (value == null) {
        unsetOutputs();
      } else {
        setOutputs((java.util.List<Unknown>)value);
      }
      break;

    case DERIVATIVES:
      if (value == null) {
        unsetDerivatives();
      } else {
        setDerivatives((java.util.List<Unknown>)value);
      }
      break;

    case INITIAL_UNKNOWNS:
      if (value == null) {
        unsetInitialUnknowns();
      } else {
        setInitialUnknowns((java.util.List<Unknown>)value);
      }
      break;

    }
  }

  @org.apache.thrift.annotation.Nullable
  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case OUTPUTS:
      return getOutputs();

    case DERIVATIVES:
      return getDerivatives();

    case INITIAL_UNKNOWNS:
      return getInitialUnknowns();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case OUTPUTS:
      return isSetOutputs();
    case DERIVATIVES:
      return isSetDerivatives();
    case INITIAL_UNKNOWNS:
      return isSetInitialUnknowns();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof ModelStructure)
      return this.equals((ModelStructure)that);
    return false;
  }

  public boolean equals(ModelStructure that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_outputs = true && this.isSetOutputs();
    boolean that_present_outputs = true && that.isSetOutputs();
    if (this_present_outputs || that_present_outputs) {
      if (!(this_present_outputs && that_present_outputs))
        return false;
      if (!this.outputs.equals(that.outputs))
        return false;
    }

    boolean this_present_derivatives = true && this.isSetDerivatives();
    boolean that_present_derivatives = true && that.isSetDerivatives();
    if (this_present_derivatives || that_present_derivatives) {
      if (!(this_present_derivatives && that_present_derivatives))
        return false;
      if (!this.derivatives.equals(that.derivatives))
        return false;
    }

    boolean this_present_initial_unknowns = true && this.isSetInitialUnknowns();
    boolean that_present_initial_unknowns = true && that.isSetInitialUnknowns();
    if (this_present_initial_unknowns || that_present_initial_unknowns) {
      if (!(this_present_initial_unknowns && that_present_initial_unknowns))
        return false;
      if (!this.initial_unknowns.equals(that.initial_unknowns))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetOutputs()) ? 131071 : 524287);
    if (isSetOutputs())
      hashCode = hashCode * 8191 + outputs.hashCode();

    hashCode = hashCode * 8191 + ((isSetDerivatives()) ? 131071 : 524287);
    if (isSetDerivatives())
      hashCode = hashCode * 8191 + derivatives.hashCode();

    hashCode = hashCode * 8191 + ((isSetInitialUnknowns()) ? 131071 : 524287);
    if (isSetInitialUnknowns())
      hashCode = hashCode * 8191 + initial_unknowns.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(ModelStructure other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetOutputs()).compareTo(other.isSetOutputs());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetOutputs()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.outputs, other.outputs);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetDerivatives()).compareTo(other.isSetDerivatives());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDerivatives()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.derivatives, other.derivatives);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetInitialUnknowns()).compareTo(other.isSetInitialUnknowns());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetInitialUnknowns()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.initial_unknowns, other.initial_unknowns);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  @org.apache.thrift.annotation.Nullable
  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    scheme(iprot).read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    scheme(oprot).write(oprot, this);
  }

  @Override
  public java.lang.String toString() {
    java.lang.StringBuilder sb = new java.lang.StringBuilder("ModelStructure(");
    boolean first = true;

    sb.append("outputs:");
    if (this.outputs == null) {
      sb.append("null");
    } else {
      sb.append(this.outputs);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("derivatives:");
    if (this.derivatives == null) {
      sb.append("null");
    } else {
      sb.append(this.derivatives);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("initial_unknowns:");
    if (this.initial_unknowns == null) {
      sb.append("null");
    } else {
      sb.append(this.initial_unknowns);
    }
    first = false;
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, java.lang.ClassNotFoundException {
    try {
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class ModelStructureStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ModelStructureStandardScheme getScheme() {
      return new ModelStructureStandardScheme();
    }
  }

  private static class ModelStructureStandardScheme extends org.apache.thrift.scheme.StandardScheme<ModelStructure> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, ModelStructure struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // OUTPUTS
            if (schemeField.type == org.apache.thrift.protocol.TType.LIST) {
              {
                org.apache.thrift.protocol.TList _list16 = iprot.readListBegin();
                struct.outputs = new java.util.ArrayList<Unknown>(_list16.size);
                @org.apache.thrift.annotation.Nullable Unknown _elem17;
                for (int _i18 = 0; _i18 < _list16.size; ++_i18)
                {
                  _elem17 = new Unknown();
                  _elem17.read(iprot);
                  struct.outputs.add(_elem17);
                }
                iprot.readListEnd();
              }
              struct.setOutputsIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // DERIVATIVES
            if (schemeField.type == org.apache.thrift.protocol.TType.LIST) {
              {
                org.apache.thrift.protocol.TList _list19 = iprot.readListBegin();
                struct.derivatives = new java.util.ArrayList<Unknown>(_list19.size);
                @org.apache.thrift.annotation.Nullable Unknown _elem20;
                for (int _i21 = 0; _i21 < _list19.size; ++_i21)
                {
                  _elem20 = new Unknown();
                  _elem20.read(iprot);
                  struct.derivatives.add(_elem20);
                }
                iprot.readListEnd();
              }
              struct.setDerivativesIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // INITIAL_UNKNOWNS
            if (schemeField.type == org.apache.thrift.protocol.TType.LIST) {
              {
                org.apache.thrift.protocol.TList _list22 = iprot.readListBegin();
                struct.initial_unknowns = new java.util.ArrayList<Unknown>(_list22.size);
                @org.apache.thrift.annotation.Nullable Unknown _elem23;
                for (int _i24 = 0; _i24 < _list22.size; ++_i24)
                {
                  _elem23 = new Unknown();
                  _elem23.read(iprot);
                  struct.initial_unknowns.add(_elem23);
                }
                iprot.readListEnd();
              }
              struct.setInitialUnknownsIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, ModelStructure struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.outputs != null) {
        oprot.writeFieldBegin(OUTPUTS_FIELD_DESC);
        {
          oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, struct.outputs.size()));
          for (Unknown _iter25 : struct.outputs)
          {
            _iter25.write(oprot);
          }
          oprot.writeListEnd();
        }
        oprot.writeFieldEnd();
      }
      if (struct.derivatives != null) {
        oprot.writeFieldBegin(DERIVATIVES_FIELD_DESC);
        {
          oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, struct.derivatives.size()));
          for (Unknown _iter26 : struct.derivatives)
          {
            _iter26.write(oprot);
          }
          oprot.writeListEnd();
        }
        oprot.writeFieldEnd();
      }
      if (struct.initial_unknowns != null) {
        oprot.writeFieldBegin(INITIAL_UNKNOWNS_FIELD_DESC);
        {
          oprot.writeListBegin(new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, struct.initial_unknowns.size()));
          for (Unknown _iter27 : struct.initial_unknowns)
          {
            _iter27.write(oprot);
          }
          oprot.writeListEnd();
        }
        oprot.writeFieldEnd();
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class ModelStructureTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public ModelStructureTupleScheme getScheme() {
      return new ModelStructureTupleScheme();
    }
  }

  private static class ModelStructureTupleScheme extends org.apache.thrift.scheme.TupleScheme<ModelStructure> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, ModelStructure struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      java.util.BitSet optionals = new java.util.BitSet();
      if (struct.isSetOutputs()) {
        optionals.set(0);
      }
      if (struct.isSetDerivatives()) {
        optionals.set(1);
      }
      if (struct.isSetInitialUnknowns()) {
        optionals.set(2);
      }
      oprot.writeBitSet(optionals, 3);
      if (struct.isSetOutputs()) {
        {
          oprot.writeI32(struct.outputs.size());
          for (Unknown _iter28 : struct.outputs)
          {
            _iter28.write(oprot);
          }
        }
      }
      if (struct.isSetDerivatives()) {
        {
          oprot.writeI32(struct.derivatives.size());
          for (Unknown _iter29 : struct.derivatives)
          {
            _iter29.write(oprot);
          }
        }
      }
      if (struct.isSetInitialUnknowns()) {
        {
          oprot.writeI32(struct.initial_unknowns.size());
          for (Unknown _iter30 : struct.initial_unknowns)
          {
            _iter30.write(oprot);
          }
        }
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, ModelStructure struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      java.util.BitSet incoming = iprot.readBitSet(3);
      if (incoming.get(0)) {
        {
          org.apache.thrift.protocol.TList _list31 = new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, iprot.readI32());
          struct.outputs = new java.util.ArrayList<Unknown>(_list31.size);
          @org.apache.thrift.annotation.Nullable Unknown _elem32;
          for (int _i33 = 0; _i33 < _list31.size; ++_i33)
          {
            _elem32 = new Unknown();
            _elem32.read(iprot);
            struct.outputs.add(_elem32);
          }
        }
        struct.setOutputsIsSet(true);
      }
      if (incoming.get(1)) {
        {
          org.apache.thrift.protocol.TList _list34 = new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, iprot.readI32());
          struct.derivatives = new java.util.ArrayList<Unknown>(_list34.size);
          @org.apache.thrift.annotation.Nullable Unknown _elem35;
          for (int _i36 = 0; _i36 < _list34.size; ++_i36)
          {
            _elem35 = new Unknown();
            _elem35.read(iprot);
            struct.derivatives.add(_elem35);
          }
        }
        struct.setDerivativesIsSet(true);
      }
      if (incoming.get(2)) {
        {
          org.apache.thrift.protocol.TList _list37 = new org.apache.thrift.protocol.TList(org.apache.thrift.protocol.TType.STRUCT, iprot.readI32());
          struct.initial_unknowns = new java.util.ArrayList<Unknown>(_list37.size);
          @org.apache.thrift.annotation.Nullable Unknown _elem38;
          for (int _i39 = 0; _i39 < _list37.size; ++_i39)
          {
            _elem38 = new Unknown();
            _elem38.read(iprot);
            struct.initial_unknowns.add(_elem38);
          }
        }
        struct.setInitialUnknownsIsSet(true);
      }
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}

