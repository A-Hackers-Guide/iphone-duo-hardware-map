# `SRPhoneUsageReport`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `SRSampling`, `NSCopying`
- 7 instance variables, 11 properties, 22 instance methods, 2 class methods

## Instance variables

```
q _totalUniqueContacts;
d _duration;
q _totalOutgoingCalls;
q _totalIncomingCalls;
d _totalPhoneCallDuration;
d _startTime;
@"NSMutableSet" _uniqueContacts;
```

## Properties

```
@property (Td,V_startTime) startTime;
@property (Td,V_duration) duration;
@property (Tq,V_totalOutgoingCalls) totalOutgoingCalls;
@property (Tq,V_totalIncomingCalls) totalIncomingCalls;
@property (T@"NSMutableSet",&,V_uniqueContacts) uniqueContacts;
@property (Td,V_totalPhoneCallDuration) totalPhoneCallDuration;
@property (Tq,R) totalUniqueContacts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRPhoneUsageReport supportsSecureCoding];
+[SRPhoneUsageReport usageReportWithInterval:];
```

## Instance methods

```
-[SRPhoneUsageReport startTime];
-[SRPhoneUsageReport dealloc];
-[SRPhoneUsageReport duration];
-[SRPhoneUsageReport setStartTime:];
-[SRPhoneUsageReport encodeWithCoder:];
-[SRPhoneUsageReport description];
-[SRPhoneUsageReport initWithCoder:];
-[SRPhoneUsageReport setDuration:];
-[SRPhoneUsageReport copyWithZone:];
-[SRPhoneUsageReport isEqual:];
-[SRPhoneUsageReport binarySampleRepresentation];
-[SRPhoneUsageReport initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRPhoneUsageReport sr_dictionaryRepresentation];
-[SRPhoneUsageReport setTotalIncomingCalls:];
-[SRPhoneUsageReport setTotalOutgoingCalls:];
-[SRPhoneUsageReport setTotalPhoneCallDuration:];
-[SRPhoneUsageReport setUniqueContacts:];
-[SRPhoneUsageReport totalIncomingCalls];
-[SRPhoneUsageReport totalOutgoingCalls];
-[SRPhoneUsageReport totalPhoneCallDuration];
-[SRPhoneUsageReport totalUniqueContacts];
-[SRPhoneUsageReport uniqueContacts];
```
