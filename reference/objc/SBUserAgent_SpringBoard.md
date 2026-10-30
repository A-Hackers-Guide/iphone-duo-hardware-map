# `SBUserAgent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIUserAgent_Internal`
- 4 instance variables, 5 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _idleTimerDisableAssertions;
@"SBIdleTimerPolicyAggregator" _idleTimerPolicyAggregator;
@"<BSInvalidatable>" _bannerSuppressionAssertion;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"SBIdleTimerPolicyAggregator",&,N,S_setIdleTimerPolicyAggregator:,V_idleTimerPolicyAggregator) _idleTimerPolicyAggregator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUserAgent setIdleText:];
-[SBUserAgent isInternalInstall];
-[SBUserAgent isScreenOn];
-[SBUserAgent deviceIsPasscodeLocked];
-[SBUserAgent deviceIsThermallyBlocked];
-[SBUserAgent lockScreenIsShowing];
-[SBUserAgent initWithApplicationController:];
-[SBUserAgent wifiRunLoopRef];
-[SBUserAgent deviceIsBlocked];
-[SBUserAgent activeInterfaceOrientation];
-[SBUserAgent setIdleTimerDisabled:forReason:];
-[SBUserAgent folderNameForDisplayID:];
-[SBUserAgent acquireCaptureButtonSuppressionAssertionWithOptions:reason:];
-[SBUserAgent deviceIsLocked];
-[SBUserAgent undimScreen];
-[SBUserAgent addActiveInterfaceOrientationObserver:];
-[SBUserAgent removeActiveInterfaceOrientationObserver:];
-[SBUserAgent topSuspendedEventsOnlyDisplayID];
-[SBUserAgent _cleanupFromBannerLaunch];
-[SBUserAgent _hasConnectedWindowScenes];
-[SBUserAgent _idleTimerPolicyAggregator];
-[SBUserAgent _launchFromSource:withURL:bundleID:allowUnlock:animate:];
-[SBUserAgent _openApplication:withURL:fromSource:animated:options:];
-[SBUserAgent _safeValue:forKey:ofType:];
-[SBUserAgent _setIdleTimerPolicyAggregator:];
-[SBUserAgent activateModalBulletinAlert:];
-[SBUserAgent activateRemoteAlertService:options:];
-[SBUserAgent applicationInstalledForDisplayID:];
-[SBUserAgent canLaunchFromSource:withURL:bundleID:];
-[SBUserAgent deviceIsPasscodeLockedRemotely];
-[SBUserAgent deviceIsTethered];
-[SBUserAgent disableLockScreenBundleNamed:deactivationContext:];
-[SBUserAgent enableLockScreenBundleNamed:activationContext:];
-[SBUserAgent foregroundApplicationDisplayID];
-[SBUserAgent isApplicationForegroundObscured:];
-[SBUserAgent isApplicationRestrictedOrHidden:];
-[SBUserAgent isIdleTimerDisabledForReason:];
-[SBUserAgent isNamedRemoteAlertServiceActive:controllerClassName:];
-[SBUserAgent launchApplicationFromSource:withDisplayID:options:];
-[SBUserAgent launchApplicationFromSource:withURL:options:];
-[SBUserAgent launchFromSource:withURL:bundleID:allowUnlock:];
-[SBUserAgent localizedDisplayNameForDisplayID:];
-[SBUserAgent lockAndDimDevice];
-[SBUserAgent lockAndDimDeviceDisconnectingCallIfNecessary:];
-[SBUserAgent lockAndDimDeviceDisconnectingCallIfNecessary:andDimScreen:];
-[SBUserAgent networkUsageTypeForAppWithDisplayID:];
-[SBUserAgent openURL:allowUnlock:animated:];
-[SBUserAgent setBadgeNumberOrString:forApplicationWithID:];
-[SBUserAgent setMinimumBacklightLevel:animated:];
-[SBUserAgent springBoardIsActive];
```
