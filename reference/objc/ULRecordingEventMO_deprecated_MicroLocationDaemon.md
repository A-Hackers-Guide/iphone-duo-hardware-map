# `ULRecordingEventMO_deprecated`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSManagedObject`
- 0 instance variables, 9 properties, 1 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",&,D,N) recordingUUID;
@property (Td,D,N) recordingTimestamp;
@property (T@"NSString",&,D,N) loiType;
@property (Td,D,N) receivedTimestamp;
@property (Ti,D,N) eventType;
@property (Ti,D,N) eventSubType;
@property (T@"NSData",&,D,N) event;
@property (T@"NSString",&,D,N) triggerUUID;
@property (T@"NSString",&,D,N) loiId;
```

## Class methods

```
+[ULRecordingEventMO_deprecated fetchRequest];
+[ULRecordingEventMO_deprecated createFromDO:inManagedObjectContext:];
```

## Instance methods

```
-[ULRecordingEventMO_deprecated convertToDO];
```
