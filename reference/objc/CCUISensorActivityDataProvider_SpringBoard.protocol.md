# `CCUISensorActivityDataProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",R,N) activeSensorActivityData;
@property (T@"CCUISensorActivityData",R,C,N) inactiveSensorActivityDataEligibleForMicModeSelection;
@property (T@"CCUISensorActivityData",R,C,N) mostRecentSensorActivityData;
@property (T@"NSSet",?,R,N) mutedMicrophoneSensorActivityData;
```

## Instance methods

```
-[CCUISensorActivityDataProvider inactiveSensorActivityDataEligibleForMicModeSelection];
-[CCUISensorActivityDataProvider activeSensorActivityData];
-[CCUISensorActivityDataProvider mostRecentSensorActivityData];
-[CCUISensorActivityDataProvider mutedMicrophoneSensorActivityData];
```
