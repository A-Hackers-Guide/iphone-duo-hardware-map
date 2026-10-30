# `CTCATransmissionProgress`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _messageId;
@"NSDate" _startedAt;
@"NSNumber" _estimatedDurationSeconds;
@"NSNumber" _progressPercents;
q _payloadType;
```

## Properties

```
@property (T@"NSString",&,N,V_messageId) messageId;
@property (T@"NSDate",&,N,V_startedAt) startedAt;
@property (T@"NSNumber",&,N,V_estimatedDurationSeconds) estimatedDurationSeconds;
@property (T@"NSNumber",&,N,V_progressPercents) progressPercents;
@property (Tq,N,V_payloadType) payloadType;
```

## Class methods

```
+[CTCATransmissionProgress supportsSecureCoding];
```

## Instance methods

```
-[CTCATransmissionProgress payloadType];
-[CTCATransmissionProgress setMessageId:];
-[CTCATransmissionProgress setStartedAt:];
-[CTCATransmissionProgress messageId];
-[CTCATransmissionProgress encodeWithCoder:];
-[CTCATransmissionProgress description];
-[CTCATransmissionProgress initWithCoder:];
-[CTCATransmissionProgress copyWithZone:];
-[CTCATransmissionProgress startedAt];
-[CTCATransmissionProgress setPayloadType:];
-[CTCATransmissionProgress estimatedDurationSeconds];
-[CTCATransmissionProgress progressPercents];
-[CTCATransmissionProgress setEstimatedDurationSeconds:];
-[CTCATransmissionProgress setProgressPercents:];
```
