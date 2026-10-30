# `SBAmbientPresentationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlwaysOnPolicy`, `SBDisplayContentModeTransitionObserver`, `AMAmbientPresentationTriggerManagerObserver`, `SBFDevicePoseProviderObserver`, `SBSecureAppObserver`, `SBLiftToWakeManagerBumpWakeArbiter`
- 14 instance variables, 11 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"SBAlwaysOnPolicyCoordinator" _alwaysOnPolicyCoordinator;
@"NSHashTable" _controllers;
@"SBWindowScene" _primaryWindowScene;
@"SBFDevicePoseProvider" _poseProvider;
@"AMAmbientDefaults" _ambientDefaults;
@"AMAmbientPresentationTriggerManager" _triggerManager;
q _triggeredSurfaceType;
q _magicPose;
@"_SBAmbientPresentationTriggerSuspensionYoinkAssertion" _presentationTriggerSuspensionYoinkAssertion;
@"<BSInvalidatable>" _bookPoseYoinkAssertion;
@"BLSAssertion" _disableAlwaysOnAssertion;
@"BLSAssertion" _alwaysOnOverrideAssertion;
@"BLSAssertion" _alwaysOnUserPreferenceOverrideAssertion;
@"BLSAssertion" _highLuminanceAlwaysOnAssertion;
```

## Properties

```
@property (T@"AMAmbientPresentationTriggerManager",R,N) triggerManager;
@property (T@"AMAmbientDefaults",R,N) ambientDefaults;
@property (Tq,R,N) effectiveAlwaysOnMode;
@property (Tq,R,N) triggeredSurfaceType;
@property (TB,R,N,GisAlwaysOnPolicyActive) alwaysOnPolicyActive;
@property (T@"NSString",R,C,N) analyticsPolicyName;
@property (T@,R,C,N) analyticsPolicyValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAmbientPresentationCoordinator isAmbientPresentingAnywhereIn:];
```

## Instance methods

```
-[SBAmbientPresentationCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBAmbientPresentationCoordinator dealloc];
-[SBAmbientPresentationCoordinator releaseInactivityTimerSuppressionIfSuppressed];
-[SBAmbientPresentationCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBAmbientPresentationCoordinator poseProvider:didUpdateFromPose:toPose:];
-[SBAmbientPresentationCoordinator ambientDefaults];
-[SBAmbientPresentationCoordinator triggerManager];
-[SBAmbientPresentationCoordinator isOnAC];
-[SBAmbientPresentationCoordinator secureAppOfTypeDidEnd:];
-[SBAmbientPresentationCoordinator secureAppOfTypeDidBegin:];
-[SBAmbientPresentationCoordinator initWithDevicePoseProvider:];
-[SBAmbientPresentationCoordinator _allowsAlwaysOn];
-[SBAmbientPresentationCoordinator registerPresentationController:];
-[SBAmbientPresentationCoordinator _acquirePresentationTriggerSuspensionYoinkAssertion];
-[SBAmbientPresentationCoordinator _anyPresentationControllerCoverSheetIsHostingAnApp];
-[SBAmbientPresentationCoordinator _effectiveSurfaceType:];
-[SBAmbientPresentationCoordinator _effectiveSurfaceTypeFromControllerWindowScene:];
-[SBAmbientPresentationCoordinator _innerWindowScene];
-[SBAmbientPresentationCoordinator _isBookPoseYoinkEligible];
-[SBAmbientPresentationCoordinator _lockStateDidChangeForBookPoseYoink:];
-[SBAmbientPresentationCoordinator _noteBookPoseYoinkAssertionExternallyInvalidated];
-[SBAmbientPresentationCoordinator _notifyControllersOfMountStateChange:];
-[SBAmbientPresentationCoordinator _notifyControllersOfTriggerStateChange:analogousTriggerEvents:];
-[SBAmbientPresentationCoordinator _releasePresentationTriggerSuspensionYoinkAssertion];
-[SBAmbientPresentationCoordinator _shouldReleasePresentationTriggerSuspensionYoinkForPose:];
-[SBAmbientPresentationCoordinator _surfaceTypeForCurrentTrigger];
-[SBAmbientPresentationCoordinator _updateBookPoseYoinkAssertion];
-[SBAmbientPresentationCoordinator _updateTriggeredSurfaceType:analogousTriggerEvents:];
-[SBAmbientPresentationCoordinator activateAlwaysOnPolicy];
-[SBAmbientPresentationCoordinator ambientPresentationManager:didUpdateMagicPose:];
-[SBAmbientPresentationCoordinator ambientPresentationManager:didUpdateMountState:];
-[SBAmbientPresentationCoordinator ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:];
-[SBAmbientPresentationCoordinator analyticsPolicyName];
-[SBAmbientPresentationCoordinator analyticsPolicyValue];
-[SBAmbientPresentationCoordinator effectiveAlwaysOnMode];
-[SBAmbientPresentationCoordinator ignorePresentationTriggers:];
-[SBAmbientPresentationCoordinator isAlwaysOnPolicyActive];
-[SBAmbientPresentationCoordinator liftToWakeManagerShouldSuppressHardWakeForBump];
-[SBAmbientPresentationCoordinator presentationAllowedForController:];
-[SBAmbientPresentationCoordinator test_setTriggeredSurfaceType:];
-[SBAmbientPresentationCoordinator triggeredSurfaceType];
-[SBAmbientPresentationCoordinator unregisterPresentationController:];
-[SBAmbientPresentationCoordinator updateAlwaysOnAssertions];
-[SBAmbientPresentationCoordinator updateAmbientWidgetHostPresentation];
```
