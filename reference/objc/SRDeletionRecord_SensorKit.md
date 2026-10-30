# `SRDeletionRecord`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `SRSampling`, `NSCopying`, `NSSecureCoding`
- 5 instance variables, 9 properties, 19 instance methods, 6 class methods

## Instance variables

```
Aq _reason;
d _startTime;
d _endTime;
q _extendedReason;
@"NSString" __originatingDeviceIdentifier;
```

## Properties

```
@property (Td,V_startTime) startTime;
@property (Td,V_endTime) endTime;
@property (Tq) reason;
@property (Tq,V_extendedReason) extendedReason;
@property (T@"NSString",C,V__originatingDeviceIdentifier) _originatingDeviceIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRDeletionRecord supportsSecureCoding];
+[SRDeletionRecord initialize];
+[SRDeletionRecord tombstoneWithStartTime:endTime:extendedReason:];
+[SRDeletionRecord tombstoneWithStartTime:endTime:extendedReason:originatingDeviceIdentifier:];
+[SRDeletionRecord tombstoneWithStartTime:endTime:reason:];
+[SRDeletionRecord tombstoneWithStartTime:endTime:reason:originatingDeviceIdentifier:];
```

## Instance methods

```
-[SRDeletionRecord endTime];
-[SRDeletionRecord setEndTime:];
-[SRDeletionRecord startTime];
-[SRDeletionRecord dealloc];
-[SRDeletionRecord setReason:];
-[SRDeletionRecord setStartTime:];
-[SRDeletionRecord encodeWithCoder:];
-[SRDeletionRecord description];
-[SRDeletionRecord initWithCoder:];
-[SRDeletionRecord reason];
-[SRDeletionRecord copyWithZone:];
-[SRDeletionRecord isEqual:];
-[SRDeletionRecord binarySampleRepresentation];
-[SRDeletionRecord initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRDeletionRecord sr_dictionaryRepresentation];
-[SRDeletionRecord _originatingDeviceIdentifier];
-[SRDeletionRecord extendedReason];
-[SRDeletionRecord setExtendedReason:];
-[SRDeletionRecord set_originatingDeviceIdentifier:];
```
