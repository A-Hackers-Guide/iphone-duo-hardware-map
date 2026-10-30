# `SBTestAutomationService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemServiceServerTestAutomationDelegate`
- 7 instance variables, 4 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _clientAuthenticator;
@"<BSInvalidatable>" _idleTimerAssertion;
@"NSHashTable" _reachabilityEnabledAssertions;
@"NSHashTable" _inFlightAnimationTransactions;
@"NSMutableDictionary" _frameRecordingAssertions;
@"NSArray" _automationStateSubscriptions;
@"NSMutableDictionary" _accessoriesByType;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTestAutomationService _windowScene];
-[SBTestAutomationService init];
-[SBTestAutomationService systemServiceServer:client:deviceOrientationForSystemSpaceOrientation:withCompletion:];
-[SBTestAutomationService systemServiceServer:client:getActiveDisplayWindowSceneDisplayIdentifierWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:getDevicePoseWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:setDevicePoseOverride:];
-[SBTestAutomationService systemServiceServer:client:systemSpaceOrientationForDeviceOrientation:withCompletion:];
-[SBTestAutomationService systemServiceServer:togglePictureInPictureProminenceForClient:];
-[SBTestAutomationService _authenticateClient:];
-[SBTestAutomationService _iconGridSizeClassFromClientArgument:];
-[SBTestAutomationService _iconManager];
-[SBTestAutomationService _switcherController];
-[SBTestAutomationService systemServiceServer:addWidgetsToEachPageForClient:];
-[SBTestAutomationService systemServiceServer:availableStreamDomainsForClient:];
-[SBTestAutomationService systemServiceServer:clearAllUserNotificationsForClient:];
-[SBTestAutomationService systemServiceServer:client:addWidgetStackWithIdentifiers:toPage:withSizing:];
-[SBTestAutomationService systemServiceServer:client:addWidgetWithIdentifier:toPage:withSizing:];
-[SBTestAutomationService systemServiceServer:client:countScenesForBundleIdentifier:withCompletion:];
-[SBTestAutomationService systemServiceServer:client:getButterflySplitViewStronglyPairedWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:getChamoisPrefersDockHiddenWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:getChamoisPrefersStripHiddenWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:getDeviceOrientationWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:getDeviceSupportsSystemAperture:];
-[SBTestAutomationService systemServiceServer:client:getIsChamoisWindowingUIEnabledWithCompletion:];
-[SBTestAutomationService systemServiceServer:client:initiateSecureFlipBookRecordingForElement:withCompletion:];
-[SBTestAutomationService systemServiceServer:client:lastEntriesForDomain:count:error:];
-[SBTestAutomationService systemServiceServer:client:loadStashedSwitcherModelFromPath:];
-[SBTestAutomationService systemServiceServer:client:port:acquireAssertionForReachabilityEnabled:];
-[SBTestAutomationService systemServiceServer:client:port:acquireHUDHiddenAssertionForIdentifier:];
-[SBTestAutomationService systemServiceServer:client:resetToHomeScreenAnimated:];
-[SBTestAutomationService systemServiceServer:client:setAccessoryType:attached:];
-[SBTestAutomationService systemServiceServer:client:setAlertsEnabled:];
-[SBTestAutomationService systemServiceServer:client:setAmbientMountState:];
-[SBTestAutomationService systemServiceServer:client:setAmbientPresentationState:];
-[SBTestAutomationService systemServiceServer:client:setApplicationBundleIdentifier:blockedForScreenTime:];
-[SBTestAutomationService systemServiceServer:client:setChamoisPrefersDockHidden:];
-[SBTestAutomationService systemServiceServer:client:setChamoisPrefersStripHidden:];
-[SBTestAutomationService systemServiceServer:client:setChamoisWindowingUIEnabled:];
-[SBTestAutomationService systemServiceServer:client:setDeviceOrientation:];
-[SBTestAutomationService systemServiceServer:client:setHiddenFeaturesEnabled:];
-[SBTestAutomationService systemServiceServer:client:setIdleTimerEnabled:];
-[SBTestAutomationService systemServiceServer:client:setMallocStackLoggingEnabled:];
-[SBTestAutomationService systemServiceServer:client:setOrientationLockEnabled:];
-[SBTestAutomationService systemServiceServer:client:setReachabilityActive:];
-[SBTestAutomationService systemServiceServer:client:setSpringBoardAnimationFrameRecordingForUpdateTypes:];
-[SBTestAutomationService systemServiceServer:client:setSystemApertureUnderAutomationTesting:];
-[SBTestAutomationService systemServiceServer:client:setTestRunnerRecoveryApplicationBundleIdentifier:];
-[SBTestAutomationService systemServiceServer:client:stashSwitcherModelToPath:];
-[SBTestAutomationService systemServiceServer:enterLostModeForClient:];
-[SBTestAutomationService systemServiceServer:exitLostModeForClient:];
-[SBTestAutomationService systemServiceServer:getAnimationFrameRecordingsForClient:];
-[SBTestAutomationService systemServiceServer:getAvailableRecordableFlipBookElementIdentifiers:];
-[SBTestAutomationService systemServiceServer:getSystemApertureModelStateDumpForClient:];
-[SBTestAutomationService systemServiceServer:getSystemApertureStateDumpForClient:];
-[SBTestAutomationService systemServiceServer:getWidgetControllerStateDump:];
-[SBTestAutomationService systemServiceServer:setUserPresenceDetectedSinceWakeForClient:];
-[SBTestAutomationService systemServiceServer:streamDomainRegistryForClient:];
-[SBTestAutomationService systemServiceServer:suspendAllDisplaysForClient:];
```
