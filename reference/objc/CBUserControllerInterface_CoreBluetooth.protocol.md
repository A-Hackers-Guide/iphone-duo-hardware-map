# `CBUserControllerInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance methods

```
-[CBUserControllerInterface diagnosticShow:completion:];
-[CBUserControllerInterface appleAudioAccessoryLimitedLoggingWithCompletion:];
-[CBUserControllerInterface setAppleAudioAccessoryLimitedLogging:completion:];
-[CBUserControllerInterface readPrefKeys:source:completion:];
-[CBUserControllerInterface storeControllerInfo:completion:];
-[CBUserControllerInterface deleteControllerInfoForDevice:completion:];
-[CBUserControllerInterface getCloudPairedDevicesWithCompletionHandler:];
-[CBUserControllerInterface getControllerInfoForDevice:completion:];
-[CBUserControllerInterface getCurrentUserGivenNameWithCompletion:];
-[CBUserControllerInterface getDistributedLoggingStatusWithCompletion:];
-[CBUserControllerInterface recordEventWithDeviceIdentifier:initiator:starting:useCase:];
-[CBUserControllerInterface recordEventWithStarting:useCase:];
-[CBUserControllerInterface setDistributedLoggingStatus:completion:];
-[CBUserControllerInterface userNotificationEvent:completion:];
-[CBUserControllerInterface writePrefKey:value:source:completion:];
```
