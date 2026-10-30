# `SBSLockScreenServiceServerInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance methods

```
-[SBSLockScreenServiceServerInterface requestPasscodeUnlockUIWithOptions:withCompletion:];
-[SBSLockScreenServiceServerInterface fetchDeviceDeterminedConfigurationsWithCompletionHandler:];
-[SBSLockScreenServiceServerInterface fetchDisplayConfigurationsWithCompletionHandler:];
-[SBSLockScreenServiceServerInterface fetchLockScreenContentCutoutReadout:displayContext:orientation:completionHandler:];
-[SBSLockScreenServiceServerInterface fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:];
-[SBSLockScreenServiceServerInterface launchEmergencyDialerWithCompletion:];
-[SBSLockScreenServiceServerInterface lockDeviceAnimated:withCompletion:];
-[SBSLockScreenServiceServerInterface migrateIncomingNotificationsToHistory];
-[SBSLockScreenServiceServerInterface requestPasscodeCheckUIWithOptions:withCompletion:];
-[SBSLockScreenServiceServerInterface setPreventPasscodeLock:];
-[SBSLockScreenServiceServerInterface setPreventSpuriousScreenUndim:];
-[SBSLockScreenServiceServerInterface simulateCaptureLaunchFromSource:bundleIdentifier:completion:];
```
