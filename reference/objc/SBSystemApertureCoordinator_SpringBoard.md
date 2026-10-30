# `SBSystemApertureCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureCoordinatingTest`, `SBSystemApertureControllerProxyDelegate`, `SBMultiDisplayUserInteractionCoordinatorActiveWindowSceneObserver`, `SBSecureIndicatorElevationServerDelegate`, `PTSettingsKeyPathObserver`, `SBDisplayContentModeTransitionObserver`, `SBSystemApertureCoordinating`
- 17 instance variables, 5 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"SBSystemAperturePresentableManager" _systemAperturePresentableManager;
@"SBSystemApertureSceneHoster" _sceneHoster;
@"SBSystemApertureLayoutMonitorServer" _systemApertureLayoutMonitorServer;
@"SBSecureIndicatorElevationServer" _secureIndicatorElevationServer;
q _requestedIndicatorElevationStyle;
@"SBSystemApertureRestrictionServer" _systemApertureRestrictionServer;
@"SBSystemApertureDefaults" _systemApertureDefaults;
@"SBSystemApertureStateDumpService" _systemApertureStateDumpService;
@"SBSystemApertureStatusBarPillElementProvider" _pillElementProvider;
@"<SAInvalidatable>" _jindoDefaultsSuppressionAssertion;
@"BSCompoundAssertion" _restrictSystemApertureToInertCompoundAssertion;
@"BSCompoundAssertion" _suppressSystemApertureCompletelyCompoundAssertion;
@"BSCompoundAssertion" _suppressHidingOfEmptySystemApertureOnClonedDisplaysCompoundAssertion;
@"BSCompoundAssertion" _preventSystemApertureOnContinuityCompoundAssertion;
@"NSMapTable" _windowSceneToControllerProxies;
@"NSMutableArray" _coordinatedAssertions;
@"SBWindowScene" _activeWindowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_activeWindowScene) activeWindowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureCoordinator registerElement:];
-[SBSystemApertureCoordinator restrictSystemApertureToInertWithReason:];
-[SBSystemApertureCoordinator suppressHidingOfEmptySystemApertureOnClonedDisplaysWithReason:];
-[SBSystemApertureCoordinator setSystemApertureUnderAutomationTesting:];
-[SBSystemApertureCoordinator suppressSystemApertureCompletelyWithReason:];
-[SBSystemApertureCoordinator _allControllerProxiesForElement:];
-[SBSystemApertureCoordinator hostedScenesDidChange];
-[SBSystemApertureCoordinator activeWindowScene];
-[SBSystemApertureCoordinator init];
-[SBSystemApertureCoordinator _registerElement:windowControllerProxy:];
-[SBSystemApertureCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBSystemApertureCoordinator _updateSuppressionForSuppressSystemApertureCompletely];
-[SBSystemApertureCoordinator _invalidateCoordinatedAssertion:withReason:];
-[SBSystemApertureCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBSystemApertureCoordinator systemApertureWindowSceneDidDisconnect:];
-[SBSystemApertureCoordinator _controllerProxyForElement:];
-[SBSystemApertureCoordinator noteActiveWindowSceneChanged:reason:];
-[SBSystemApertureCoordinator systemApertureWindowSceneDidConnect:];
-[SBSystemApertureCoordinator _activeControllerProxy];
-[SBSystemApertureCoordinator systemApertureController:registerElement:];
-[SBSystemApertureCoordinator _allProxiesWithWindows];
-[SBSystemApertureCoordinator setActiveWindowScene:];
-[SBSystemApertureCoordinator _ensureElementsOnCorrectDisplays];
-[SBSystemApertureCoordinator _firstWindowScenePassingTest:];
-[SBSystemApertureCoordinator multiDisplayUserInteractionCoordinator:updatedActiveWindowScene:reason:];
-[SBSystemApertureCoordinator _updateSuppressionWithCompoundAssertion:assertionFromProxy:setAssertionOnProxy:acquireAssertionFromProxyWithReason:suppressionReason:];
-[SBSystemApertureCoordinator _coordinatedAssertionForElement:];
-[SBSystemApertureCoordinator _endPreservingAssociatedSuppressionAcrossFoldTransition];
-[SBSystemApertureCoordinator systemApertureControllerForWindowScene:];
-[SBSystemApertureCoordinator acquireActiveElementAssertionForApplication:reason:];
-[SBSystemApertureCoordinator overrideAllContainerRenderingStyleAssertion:];
-[SBSystemApertureCoordinator _registerInvalidationHandlerForAssertion:element:];
-[SBSystemApertureCoordinator _beginPreservingAssociatedSuppressionAcrossFoldTransition];
-[SBSystemApertureCoordinator _updateSuppressionForRestrictSystemApertureToInert];
-[SBSystemApertureCoordinator _controllerProxyForWindowScene:];
-[SBSystemApertureCoordinator _controllerProxyCreatingIfNeededForWindowScene:];
-[SBSystemApertureCoordinator _swapElement:fromControlling:toControlling:];
-[SBSystemApertureCoordinator windowSceneForDestinationToken:];
-[SBSystemApertureCoordinator _updateRequestedIndicatorElevationStyleForAllControllerProxies];
-[SBSystemApertureCoordinator preventSystemApertureOnContinuityWithReason:];
-[SBSystemApertureCoordinator _updateSuppressionForSuppressHidingOfEmptySystemApertureOnClonedDisplays];
-[SBSystemApertureCoordinator secureIndicatorElevationServer:didChangeRequestedElevationStyle:];
-[SBSystemApertureCoordinator settings:changedValueForKeyPath:];
-[SBSystemApertureCoordinator acquireSuppressionAssertionForBackgroundActivities:reason:];
-[SBSystemApertureCoordinator _otherWindowSceneWithWindowExcluding:];
```
