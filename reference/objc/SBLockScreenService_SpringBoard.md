# `SBLockScreenService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `SBSLockScreenServiceServerInterface`, `SBPasscodeEntryTransientOverlayViewControllerDelegate`, `SBAlwaysOnPolicy`
- 20 instance variables, 11 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@"SBMainWorkspace" _mainWorkspace;
@"<SBFAuthenticationAssertionProviding>" _authenticationAssertionProvider;
@"SBRemoteTransientOverlaySessionManager" _remoteTransientOverlaySessionManager;
@"FBServiceClientAuthenticator" _requestDeviceUnlockAuthenticator;
@"BSServiceConnectionListener" _listener;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionsLock;
@"NSMutableSet" _connectionsLock_connections;
@"NSMutableSet" _connectionsPreventingPasscodeLock;
@"SBFAuthenticationAssertion" _preventPasscodeLockAssertion;
@"NSMutableSet" _connectionsPreventingSpuriousScreenUndim;
@"SBSpuriousScreenUndimmingAssertion" _preventSpuriousScreenUndimAssertion;
@"BLSAssertion" _preventSpuriousScreenUndimDisableAlwaysOnAssertion;
@"NSString" _passcodeTitle;
@"NSString" _passcodeSubtitle;
@? _passcodeCheckCompletion;
@"SBPasscodeEntryTransientOverlayViewController" _passcodeEntryTransientOverlayViewController;
@"SBFUserAuthenticationController" _userAuthController;
@"<SBFLockOutStatusProvider>" _lockOutController;
```

## Properties

```
@property (T@"SBPasscodeEntryTransientOverlayViewController",&,N,V_passcodeEntryTransientOverlayViewController) passcodeEntryTransientOverlayViewController;
@property (T@"SBFUserAuthenticationController",&,N,V_userAuthController) userAuthController;
@property (T@"<SBFLockOutStatusProvider>",&,N,V_lockOutController) lockOutController;
@property (T@"<SBAlwaysOnPolicy>",R,N) alwaysOnPolicyProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisAlwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
```

## Instance methods

```
-[SBLockScreenService passcodeEntryTransientOverlayViewController:authenticatePasscode:];
-[SBLockScreenService listener:didReceiveConnection:withContext:];
-[SBLockScreenService passcodeEntryTransientOverlayViewControllerStatusSubtitleText];
-[SBLockScreenService setLockOutController:];
-[SBLockScreenService lockOutController];
-[SBLockScreenService passcodeEntryTransientOverlayViewControllerRequestsDismissal:];
-[SBLockScreenService passcodeEntryTransientOverlayViewControllerStatusText];
-[SBLockScreenService requestPasscodeUnlockUIWithOptions:withCompletion:];
-[SBLockScreenService fetchDeviceDeterminedConfigurationsWithCompletionHandler:];
-[SBLockScreenService fetchDisplayConfigurationsWithCompletionHandler:];
-[SBLockScreenService fetchLockScreenContentCutoutReadout:displayContext:orientation:completionHandler:];
-[SBLockScreenService fetchLockScreenContentCutoutReadouts:displayContext:orientation:completionHandler:];
-[SBLockScreenService launchEmergencyDialerWithCompletion:];
-[SBLockScreenService lockDeviceAnimated:withCompletion:];
-[SBLockScreenService migrateIncomingNotificationsToHistory];
-[SBLockScreenService requestPasscodeCheckUIWithOptions:withCompletion:];
-[SBLockScreenService setPreventPasscodeLock:];
-[SBLockScreenService setPreventSpuriousScreenUndim:];
-[SBLockScreenService simulateCaptureLaunchFromSource:bundleIdentifier:completion:];
-[SBLockScreenService _setPasscodeVisible:animated:];
-[SBLockScreenService _targetWindowScene];
-[SBLockScreenService activateAlwaysOnPolicy];
-[SBLockScreenService alwaysOnPolicyProvider];
-[SBLockScreenService analyticsPolicyName];
-[SBLockScreenService analyticsPolicyValue];
-[SBLockScreenService initWithLockScreenCoordinator:workspace:windowSceneManager:authenticationAssertionProvider:remoteTransientOverlaySessionManager:];
-[SBLockScreenService isAlwaysOnPolicyActive];
-[SBLockScreenService passcodeEntryTransientOverlayViewController];
-[SBLockScreenService requestPasscodeCheckUIForClient:options:description:withCompletion:];
-[SBLockScreenService requestPasscodeUnlockUIForClient:options:description:withCompletion:];
-[SBLockScreenService setPasscodeEntryTransientOverlayViewController:];
-[SBLockScreenService setUserAuthController:];
-[SBLockScreenService userAuthController];
```
