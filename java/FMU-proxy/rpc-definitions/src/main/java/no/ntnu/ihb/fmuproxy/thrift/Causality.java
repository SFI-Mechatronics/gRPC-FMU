/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package no.ntnu.ihb.fmuproxy.thrift;


public enum Causality implements org.apache.thrift.TEnum {
  INPUT_CAUSALITY(0),
  OUTPUT_CAUSALITY(1),
  PARAMETER_CAUSALITY(2),
  CALCULATED_PARAMETER_CAUSALITY(3),
  LOCAL_CAUSALITY(4),
  INDEPENDENT_CAUSALITY(5),
  UNKNOWN_CAUSALITY(6);

  private final int value;

  private Causality(int value) {
    this.value = value;
  }

  /**
   * Get the integer value of this enum value, as defined in the Thrift IDL.
   */
  public int getValue() {
    return value;
  }

  /**
   * Find a the enum type by its integer value, as defined in the Thrift IDL.
   * @return null if the value is not found.
   */
  public static Causality findByValue(int value) { 
    switch (value) {
      case 0:
        return INPUT_CAUSALITY;
      case 1:
        return OUTPUT_CAUSALITY;
      case 2:
        return PARAMETER_CAUSALITY;
      case 3:
        return CALCULATED_PARAMETER_CAUSALITY;
      case 4:
        return LOCAL_CAUSALITY;
      case 5:
        return INDEPENDENT_CAUSALITY;
      case 6:
        return UNKNOWN_CAUSALITY;
      default:
        return null;
    }
  }
}