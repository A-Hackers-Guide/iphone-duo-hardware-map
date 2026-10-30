# `SRMessagesUsageReport`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `SRSampling`, `NSCopying`
- 6 instance variables, 10 properties, 20 instance methods, 2 class methods

## Instance variables

```
q _totalUniqueContacts;
d _duration;
q _totalOutgoingMessages;
q _totalIncomingMessages;
d _startTime;
@"NSMutableSet" _uniqueContacts;
```

## Properties

```
@property (Td,V_startTime) startTime;
@property (Td,V_duration) duration;
@property (Tq,V_totalOutgoingMessages) totalOutgoingMessages;
@property (Tq,V_totalIncomingMessages) totalIncomingMessages;
@property (T@"NSMutableSet",&,V_uniqueContacts) uniqueContacts;
@property (Tq,R) totalUniqueContacts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRMessagesUsageReport supportsSecureCoding];
+[SRMessagesUsageReport usageReportWithInterval:];
```

## Instance methods

```
-[SRMessagesUsageReport startTime];
-[SRMessagesUsageReport dealloc];
-[SRMessagesUsageReport duration];
-[SRMessagesUsageReport setStartTime:];
-[SRMessagesUsageReport encodeWithCoder:];
-[SRMessagesUsageReport description];
-[SRMessagesUsageReport initWithCoder:];
-[SRMessagesUsageReport setDuration:];
-[SRMessagesUsageReport copyWithZone:];
-[SRMessagesUsageReport isEqual:];
-[SRMessagesUsageReport binarySampleRepresentation];
-[SRMessagesUsageReport initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRMessagesUsageReport sr_dictionaryRepresentation];
-[SRMessagesUsageReport setTotalIncomingMessages:];
-[SRMessagesUsageReport setTotalOutgoingMessages:];
-[SRMessagesUsageReport setUniqueContacts:];
-[SRMessagesUsageReport totalIncomingMessages];
-[SRMessagesUsageReport totalOutgoingMessages];
-[SRMessagesUsageReport totalUniqueContacts];
-[SRMessagesUsageReport uniqueContacts];
```
