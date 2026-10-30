# `CWFDriverAvailabilityMessage`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 16 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _available;
@"NSData" _rawEventData;
@"NSDate" _timestamp;
q _flags;
q _event_id;
q _reason;
@"NSString" _reasonString;
q _sub_reason;
q _minor_reason;
q _trapInfoSequenceNum;
```

## Properties

```
@property (T@"NSData",C,N,V_rawEventData) rawEventData;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (TB,N,V_available) available;
@property (Tq,N,V_flags) flags;
@property (TB,R,N) availabilityFlagIsRetry;
@property (TB,R,N) availabilityFlagIsNonFatal;
@property (TB,R,N) availabilityFlagHasTrapInfo;
@property (TB,R,N) availabilityFlagHasJoinTimeoutInfo;
@property (TB,R,N) availabilityFlagHasTrapCrashTracerMiniDump;
@property (TB,R,N) availabilityFlagFwLoaded;
@property (Tq,N,V_event_id) event_id;
@property (Tq,N,V_reason) reason;
@property (T@"NSString",C,N,V_reasonString) reasonString;
@property (Tq,N,V_sub_reason) sub_reason;
@property (Tq,N,V_minor_reason) minor_reason;
@property (Tq,N,V_trapInfoSequenceNum) trapInfoSequenceNum;
```

## Class methods

```
+[CWFDriverAvailabilityMessage supportsSecureCoding];
```

## Instance methods

```
-[CWFDriverAvailabilityMessage setTimestamp:];
-[CWFDriverAvailabilityMessage setFlags:];
-[CWFDriverAvailabilityMessage flags];
-[CWFDriverAvailabilityMessage timestamp];
-[CWFDriverAvailabilityMessage setReason:];
-[CWFDriverAvailabilityMessage setAvailable:];
-[CWFDriverAvailabilityMessage available];
-[CWFDriverAvailabilityMessage encodeWithCoder:];
-[CWFDriverAvailabilityMessage hash];
-[CWFDriverAvailabilityMessage description];
-[CWFDriverAvailabilityMessage initWithCoder:];
-[CWFDriverAvailabilityMessage reason];
-[CWFDriverAvailabilityMessage copyWithZone:];
-[CWFDriverAvailabilityMessage isEqual:];
-[CWFDriverAvailabilityMessage reasonString];
-[CWFDriverAvailabilityMessage setReasonString:];
-[CWFDriverAvailabilityMessage availabilityFlagFwLoaded];
-[CWFDriverAvailabilityMessage availabilityFlagHasJoinTimeoutInfo];
-[CWFDriverAvailabilityMessage availabilityFlagHasTrapCrashTracerMiniDump];
-[CWFDriverAvailabilityMessage availabilityFlagHasTrapInfo];
-[CWFDriverAvailabilityMessage availabilityFlagIsNonFatal];
-[CWFDriverAvailabilityMessage availabilityFlagIsRetry];
-[CWFDriverAvailabilityMessage event_id];
-[CWFDriverAvailabilityMessage initWithDriverAvailabiltyData:];
-[CWFDriverAvailabilityMessage isEqualToDriverAvailabiltyMessage:];
-[CWFDriverAvailabilityMessage minor_reason];
-[CWFDriverAvailabilityMessage rawEventData];
-[CWFDriverAvailabilityMessage setEvent_id:];
-[CWFDriverAvailabilityMessage setMinor_reason:];
-[CWFDriverAvailabilityMessage setRawEventData:];
-[CWFDriverAvailabilityMessage setSub_reason:];
-[CWFDriverAvailabilityMessage setTrapInfoSequenceNum:];
-[CWFDriverAvailabilityMessage sub_reason];
-[CWFDriverAvailabilityMessage trapInfoSequenceNum];
```
