# `CAMPowerController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
Ai _assertionIdentifierGenerator;
i __powerPressureNotificationToken;
I __powerControllerQueue_powerPressureLevel;
@"NSMutableDictionary" __assertionsByIdentifier;
@"NSObject<OS_dispatch_queue>" __powerControllerQueue;
Q __backgroundTaskIdentifier;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V__assertionsByIdentifier) _assertionsByIdentifier;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__powerControllerQueue) _powerControllerQueue;
@property (TQ,R,N,V__backgroundTaskIdentifier) _backgroundTaskIdentifier;
@property (Ti,R,N,V__powerPressureNotificationToken) _powerPressureNotificationToken;
@property (TI,N,S_powerControllerQueue_setPowerPressureLevel:,V__powerControllerQueue_powerPressureLevel) _powerControllerQueue_powerPressureLevel;
```

## Instance methods

```
-[CAMPowerController init];
-[CAMPowerController dealloc];
-[CAMPowerController description];
-[CAMPowerController _backgroundTaskIdentifier];
-[CAMPowerController generateAssertionIdentifier];
-[CAMPowerController powerPressureLevel];
-[CAMPowerController _powerPressureNotificationToken];
-[CAMPowerController _assertionsByIdentifier];
-[CAMPowerController _endBackgroundTaskIfNeeded];
-[CAMPowerController _powerControllerQueue];
-[CAMPowerController _powerControllerQueue_powerPressureLevel];
-[CAMPowerController _powerControllerQueue_setPowerPressureLevel:];
-[CAMPowerController _startBackgroundTaskIfNeeded];
-[CAMPowerController addAssertionForIndentifier:withReason:];
-[CAMPowerController removeAssertionForIdentifier:withReason:];
```
