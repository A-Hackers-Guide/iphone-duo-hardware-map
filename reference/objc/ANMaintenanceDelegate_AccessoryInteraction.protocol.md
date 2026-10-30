# `ANMaintenanceDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance methods

```
-[ANMaintenanceDelegate submitMaintenanceMetrics:forDevice:withReason:andCategory:andDuration:leashable:];
-[ANMaintenanceDelegate getNearOwnerTimeoutForDevice:checkingForNetwork:checkingHele:];
-[ANMaintenanceDelegate submitCarMaintConnectionMetrics:];
-[ANMaintenanceDelegate attemptConnectToDevice:onCondition:requestContext:];
-[ANMaintenanceDelegate shouldConnectUsingLeashToDevice:];
-[ANMaintenanceDelegate sendObservationForDevice:type:includeLocation:];
-[ANMaintenanceDelegate cancelConnectionAttemptToDevice:];
-[ANMaintenanceDelegate notifyOnMaintenanceCompleteForAllDevices];
-[ANMaintenanceDelegate shouldSkipConnectAttemptToDevice:];
-[ANMaintenanceDelegate getDeviceList];
-[ANMaintenanceDelegate submitMaintenanceTimerPowerLog:actualInterval:];
-[ANMaintenanceDelegate restartConnectionAttemptToDevice:];
-[ANMaintenanceDelegate submitCompletedMaintenanceMetrics:];
```
