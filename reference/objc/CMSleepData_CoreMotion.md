# `CMSleepData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 14 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSUUID" fSourceId;
@"NSUUID" fSessionId;
@"NSDate" fEventTime;
q fEventType;
```

## Properties

```
@property (TQ,R,N) recordId;
@property (T@"NSUUID",R,N) sourceId;
@property (T@"NSUUID",R,N) sessionId;
@property (T@"NSDate",R,N) eventTime;
@property (Tq,R,N) eventType;
```

## Class methods

```
+[CMSleepData supportsSecureCoding];
+[CMSleepData eventTypeName:];
```

## Instance methods

```
-[CMSleepData eventTime];
-[CMSleepData eventType];
-[CMSleepData sourceId];
-[CMSleepData sessionId];
-[CMSleepData recordId];
-[CMSleepData dealloc];
-[CMSleepData encodeWithCoder:];
-[CMSleepData description];
-[CMSleepData initWithCoder:];
-[CMSleepData copyWithZone:];
-[CMSleepData convertToSpringTrackerEntry:];
-[CMSleepData initWithRecordId:sourceId:sessionId:eventTime:eventType:];
-[CMSleepData initWithSessionId:];
-[CMSleepData initWithSpringEntry:];
```
