# `ANMaintenanceUtilities`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ANSystemUtilsProtocol>" _systemUtils;
@"PCPersistentTimer" _timer;
Q _startTime;
d _scheduledInterval;
^v _powerAssertion;
i _assertId;
d _assertTime;
d _assertDuration;
B _isHeleOnly;
d _intervalOverride;
@"<ANMaintenanceUtilitiesDelegate>" _delegate;
```

## Properties

```
@property (T@"<ANMaintenanceUtilitiesDelegate>",N,V_delegate) delegate;
```

## Instance methods

```
-[ANMaintenanceUtilities setDeviceType:];
-[ANMaintenanceUtilities clearTimer];
-[ANMaintenanceUtilities isWatch];
-[ANMaintenanceUtilities init];
-[ANMaintenanceUtilities dealloc];
-[ANMaintenanceUtilities setDelegate:];
-[ANMaintenanceUtilities stopTimer];
-[ANMaintenanceUtilities startTimer:];
-[ANMaintenanceUtilities delegate];
-[ANMaintenanceUtilities isTinkerWatch];
-[ANMaintenanceUtilities restartTimer];
-[ANMaintenanceUtilities getMaintenanceAssertionDuration];
-[ANMaintenanceUtilities initWithQueue:systemUtils:settings:];
-[ANMaintenanceUtilities isPowerAssertionAsserted];
-[ANMaintenanceUtilities isTimerOn];
-[ANMaintenanceUtilities onTimer:];
-[ANMaintenanceUtilities releaseMaintenancePowerAssertion:];
-[ANMaintenanceUtilities takeMaintenancePowerAssertion];
```
