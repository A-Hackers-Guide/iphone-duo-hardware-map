# `SBSystemApertureStatusBarPillElementProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIStatusBarServerClient`, `SBWindowSceneStatusBarAssertionManagerObserver`, `SBLayoutStateTransitionObserver`, `SBDeviceApplicationSceneStatusBarStateObserver`, `STBackgroundActivityManagerClient`, `SBSystemApertureBackgroundActivitiesSuppressing`
- 11 instance variables, 18 properties, 52 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"UIStatusBarServer" __statusBarServer;
@"NSMutableSet" __registeredElements;
@"NSSet" _currentBackgroundActivityIdentifiers;
@"SBDeviceApplicationSceneHandle" _observedSceneHandle;
@"NSHashTable" _suppressionAssertions;
@"NSMutableSet" _applicationsWithActiveElements;
@"NSMutableSet" _assertionsForApplicationsWithActiveElements;
@"NSString" _resolvedBackgroundActivityIdentifier;
@"NSTimer" _applyOverridesDebounceTimer;
@"SBSystemApertureSettings" _settings;
```

## Properties

```
@property (T@"UIStatusBarServer",R,N,V__statusBarServer) _statusBarServer;
@property (T@"NSMutableSet",&,N,V__registeredElements) _registeredElements;
@property (T@"SBSystemApertureStatusBarPillElement",R,N) _activeElement;
@property (T@"SBSystemApertureStatusBarPillElement",R,N) _nowLocatingElement;
@property (T@"SBSystemApertureStatusBarPillElement",R,N) _nowRecordingElement;
@property (T@"NSSet",C,N,V_currentBackgroundActivityIdentifiers) currentBackgroundActivityIdentifiers;
@property (T@"SBDeviceApplicationSceneHandle",W,N,V_observedSceneHandle) observedSceneHandle;
@property (T@"NSHashTable",R,N,V_suppressionAssertions) suppressionAssertions;
@property (T@"NSMutableSet",R,N,V_applicationsWithActiveElements) applicationsWithActiveElements;
@property (T@"NSMutableSet",R,N,V_assertionsForApplicationsWithActiveElements) assertionsForApplicationsWithActiveElements;
@property (T@"NSString",&,N,V_resolvedBackgroundActivityIdentifier) resolvedBackgroundActivityIdentifier;
@property (T@"NSTimer",&,N,V_applyOverridesDebounceTimer) applyOverridesDebounceTimer;
@property (T@"SBSystemApertureSettings",&,N,V_settings) settings;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureStatusBarPillElementProvider layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBSystemApertureStatusBarPillElementProvider sceneWithIdentifier:didChangeBackgroundActivitiesToSuppressTo:];
-[SBSystemApertureStatusBarPillElementProvider _managesDedicatedElementForBackgroundActivityIdentifiers:];
-[SBSystemApertureStatusBarPillElementProvider layoutStateTransitionCoordinator:transitionWillEndWithTransitionContext:];
-[SBSystemApertureStatusBarPillElementProvider setWindowScene:];
-[SBSystemApertureStatusBarPillElementProvider _activeElement];
-[SBSystemApertureStatusBarPillElementProvider _managesDedicatedElementForBackgroundActivityIdentifier:];
-[SBSystemApertureStatusBarPillElementProvider suppressionAssertions];
-[SBSystemApertureStatusBarPillElementProvider setSettings:];
-[SBSystemApertureStatusBarPillElementProvider assertionsForApplicationsWithActiveElements];
-[SBSystemApertureStatusBarPillElementProvider settings];
-[SBSystemApertureStatusBarPillElementProvider _invalidateElement:withReason:];
-[SBSystemApertureStatusBarPillElementProvider dealloc];
-[SBSystemApertureStatusBarPillElementProvider _nowRecordingAppDidChange];
-[SBSystemApertureStatusBarPillElementProvider statusBarServer:didReceiveGlowAnimationState:forStyle:];
-[SBSystemApertureStatusBarPillElementProvider _registeredElements];
-[SBSystemApertureStatusBarPillElementProvider _updateNowRecordingElementWithReason:];
-[SBSystemApertureStatusBarPillElementProvider _registerElement:];
-[SBSystemApertureStatusBarPillElementProvider activeBackgroundActivitiesDidUpdate:];
-[SBSystemApertureStatusBarPillElementProvider initWithWindowScene:];
-[SBSystemApertureStatusBarPillElementProvider _statusBarServer];
-[SBSystemApertureStatusBarPillElementProvider _nowLocatingAppsDidChange];
-[SBSystemApertureStatusBarPillElementProvider statusBarAssertionManager:addStatusBarSettingsAssertion:];
-[SBSystemApertureStatusBarPillElementProvider layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBSystemApertureStatusBarPillElementProvider setResolvedBackgroundActivityIdentifier:];
-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededForReason:];
-[SBSystemApertureStatusBarPillElementProvider set_registeredElements:];
-[SBSystemApertureStatusBarPillElementProvider _updateNowLocatingElementWithReason:];
-[SBSystemApertureStatusBarPillElementProvider statusBarAssertionManager:statusBarSettingsDidChange:];
-[SBSystemApertureStatusBarPillElementProvider statusBarAssertionManager:removeStatusBarSettingsAssertion:];
-[SBSystemApertureStatusBarPillElementProvider acquireActiveElementAssertionForApplication:reason:];
-[SBSystemApertureStatusBarPillElementProvider currentBackgroundActivityIdentifiers];
-[SBSystemApertureStatusBarPillElementProvider _lockStateChanged];
-[SBSystemApertureStatusBarPillElementProvider setCurrentBackgroundActivityIdentifiers:];
-[SBSystemApertureStatusBarPillElementProvider _updateNowRecordingAndNowLocatingElementsWithReason:];
-[SBSystemApertureStatusBarPillElementProvider setApplyOverridesDebounceTimer:];
-[SBSystemApertureStatusBarPillElementProvider statusBarServer:didReceiveDoubleHeightStatusString:forStyle:];
-[SBSystemApertureStatusBarPillElementProvider applicationsWithActiveElements];
-[SBSystemApertureStatusBarPillElementProvider statusBarServer:didReceiveStatusBarData:withActions:];
-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededWithLayoutState:reason:notifyingElementsIfNecessary:];
-[SBSystemApertureStatusBarPillElementProvider _nowRecordingElement];
-[SBSystemApertureStatusBarPillElementProvider applyOverridesDebounceTimer];
-[SBSystemApertureStatusBarPillElementProvider observedSceneHandle];
-[SBSystemApertureStatusBarPillElementProvider windowScene];
-[SBSystemApertureStatusBarPillElementProvider statusBarServer:didReceiveStyleOverrides:];
-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededForReason:notifyingElementsIfNecessary:];
-[SBSystemApertureStatusBarPillElementProvider _updateCurrentBackgroundActivityIdentifiersWithStatusBarOverrides:];
-[SBSystemApertureStatusBarPillElementProvider acquireSuppressionAssertionForBackgroundActivities:reason:];
-[SBSystemApertureStatusBarPillElementProvider resolvedBackgroundActivityIdentifier];
-[SBSystemApertureStatusBarPillElementProvider _nowLocatingElement];
-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededWithLayoutState:reason:];
-[SBSystemApertureStatusBarPillElementProvider setObservedSceneHandle:];
```
