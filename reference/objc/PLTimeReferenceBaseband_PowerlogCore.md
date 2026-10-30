# `PLTimeReferenceBaseband`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLTimeReferenceDynamic`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _followupCurrentTimeRunning;
@"PLNSNotificationOperatorComposition" _basebandTimeNotification;
```

## Properties

```
@property (T@"PLNSNotificationOperatorComposition",&,V_basebandTimeNotification) basebandTimeNotification;
@property (TB,V_followupCurrentTimeRunning) followupCurrentTimeRunning;
```

## Instance methods

```
-[PLTimeReferenceBaseband registerForTimeChangedNotification];
-[PLTimeReferenceBaseband timeChangedNotificationReceived:];
-[PLTimeReferenceBaseband setFollowupCurrentTimeRunning:];
-[PLTimeReferenceBaseband setBasebandTimeNotification:];
-[PLTimeReferenceBaseband dealloc];
-[PLTimeReferenceBaseband currentTime];
-[PLTimeReferenceBaseband initWithTimeManager:entryDefinitionKey:timeReferenceType:];
-[PLTimeReferenceBaseband basebandTimeNotification];
-[PLTimeReferenceBaseband followupCurrentTimeRunning];
```
