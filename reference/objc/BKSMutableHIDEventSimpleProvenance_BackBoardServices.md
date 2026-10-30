# `BKSMutableHIDEventSimpleProvenance`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventSimpleProvenance`
- Protocols: `BSProtobufSerializable`, `NSSecureCoding`, `BSDescriptionStreaming`
- 0 instance variables, 8 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"NSData",&,D,N) signature;
@property (TQ,D,N) timestamp;
@property (Tq,D,N) versionedPID;
@property (TI,D,N) eventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSMutableHIDEventSimpleProvenance setTimestamp:];
-[BKSMutableHIDEventSimpleProvenance setSignature:];
-[BKSMutableHIDEventSimpleProvenance setEventType:];
-[BKSMutableHIDEventSimpleProvenance setVersionedPID:];
-[BKSMutableHIDEventSimpleProvenance copyWithZone:];
```
