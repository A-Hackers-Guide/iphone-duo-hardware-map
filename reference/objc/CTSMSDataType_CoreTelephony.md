# `CTSMSDataType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _parseSMSC;
B _waitForAck;
@"NSNumber" _transport;
@"NSNumber" _ctFormat;
@"NSData" _hexPdu;
```

## Properties

```
@property (T@"NSNumber",N,V_transport) transport;
@property (T@"NSNumber",N,V_ctFormat) ctFormat;
@property (TB,N,V_parseSMSC) parseSMSC;
@property (TB,N,V_waitForAck) waitForAck;
@property (T@"NSData",&,N,V_hexPdu) hexPdu;
```

## Class methods

```
+[CTSMSDataType supportsSecureCoding];
```

## Instance methods

```
-[CTSMSDataType init];
-[CTSMSDataType transport];
-[CTSMSDataType encodeWithCoder:];
-[CTSMSDataType setTransport:];
-[CTSMSDataType description];
-[CTSMSDataType initWithCoder:];
-[CTSMSDataType copyWithZone:];
-[CTSMSDataType isEqual:];
-[CTSMSDataType ctFormat];
-[CTSMSDataType hexPdu];
-[CTSMSDataType isEqualToCTSMSDataType:];
-[CTSMSDataType parseSMSC];
-[CTSMSDataType setCtFormat:];
-[CTSMSDataType setHexPdu:];
-[CTSMSDataType setParseSMSC:];
-[CTSMSDataType setWaitForAck:];
-[CTSMSDataType waitForAck];
```
