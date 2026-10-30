# `SBUIUserAgent` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 41 instance methods, 0 class methods

## Instance methods

```
-[SBUIUserAgent setIdleText:];
-[SBUIUserAgent isInternalInstall];
-[SBUIUserAgent isScreenOn];
-[SBUIUserAgent deviceIsPasscodeLocked];
-[SBUIUserAgent deviceIsThermallyBlocked];
-[SBUIUserAgent lockScreenIsShowing];
-[SBUIUserAgent wifiRunLoopRef];
-[SBUIUserAgent deviceIsBlocked];
-[SBUIUserAgent activeInterfaceOrientation];
-[SBUIUserAgent setIdleTimerDisabled:forReason:];
-[SBUIUserAgent folderNameForDisplayID:];
-[SBUIUserAgent acquireCaptureButtonSuppressionAssertionWithOptions:reason:];
-[SBUIUserAgent deviceIsLocked];
-[SBUIUserAgent undimScreen];
-[SBUIUserAgent addActiveInterfaceOrientationObserver:];
-[SBUIUserAgent removeActiveInterfaceOrientationObserver:];
-[SBUIUserAgent topSuspendedEventsOnlyDisplayID];
-[SBUIUserAgent activateModalBulletinAlert:];
-[SBUIUserAgent activateRemoteAlertService:options:];
-[SBUIUserAgent applicationInstalledForDisplayID:];
-[SBUIUserAgent canLaunchFromSource:withURL:bundleID:];
-[SBUIUserAgent deviceIsPasscodeLockedRemotely];
-[SBUIUserAgent deviceIsTethered];
-[SBUIUserAgent disableLockScreenBundleNamed:deactivationContext:];
-[SBUIUserAgent enableLockScreenBundleNamed:activationContext:];
-[SBUIUserAgent foregroundApplicationDisplayID];
-[SBUIUserAgent isApplicationForegroundObscured:];
-[SBUIUserAgent isApplicationRestrictedOrHidden:];
-[SBUIUserAgent isIdleTimerDisabledForReason:];
-[SBUIUserAgent isNamedRemoteAlertServiceActive:controllerClassName:];
-[SBUIUserAgent launchApplicationFromSource:withDisplayID:options:];
-[SBUIUserAgent launchApplicationFromSource:withURL:options:];
-[SBUIUserAgent localizedDisplayNameForDisplayID:];
-[SBUIUserAgent lockAndDimDevice];
-[SBUIUserAgent lockAndDimDeviceDisconnectingCallIfNecessary:];
-[SBUIUserAgent lockAndDimDeviceDisconnectingCallIfNecessary:andDimScreen:];
-[SBUIUserAgent networkUsageTypeForAppWithDisplayID:];
-[SBUIUserAgent openURL:allowUnlock:animated:];
-[SBUIUserAgent setBadgeNumberOrString:forApplicationWithID:];
-[SBUIUserAgent setMinimumBacklightLevel:animated:];
-[SBUIUserAgent springBoardIsActive];
```
