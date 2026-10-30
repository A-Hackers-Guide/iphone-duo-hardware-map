# `SBPIPController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlertItemsControllerObserver`, `SBAssistantObserver`, `SBLayoutStateTransitionObserver`, `SBPIPContainerViewControllerInteractionObserver`, `SBPIPContainerViewControllerObserver`, `SBPIPControllerAdapterContextProviding`, `SBSensorActivityObserver`, `SBKeyboardFocusControllerObserver`, `SBExternalDisplayServiceObserver`, `SBIdleTimerProviding`, `SBPIPMorphAnimatorControllerDelegate`, `SBLockStateObserving`
- 47 instance variables, 10 properties, 122 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _stateCaptureInvalidatable;
@"NSMapTable" _containerViewControllerToContextMap;
@"SBPIPInteractionSettings" _interactionSettings;
d _windowLevel;
B _hasIdleTimerBehaviors;
@"<SBIdleTimerCoordinating>" _idleTimerCoordinator;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"SBApplicationController" _applicationController;
@"NSHashTable" _connectedWindowScenes;
@"NSHashTable" _lockStateProviders;
@"NSMutableSet" _pictureInPictureWindowHiddenReasons;
@"NSMapTable" _windowSceneToWindowMarginsMap;
@"NSMapTable" _windowSceneToInsetAssertionMap;
@"NSMapTable" _windowSceneToStashAssertionsMap;
@"NSHashTable" _interruptionAssertions;
@"NSMutableDictionary" _cameraInterruptionAssertions;
@"SBPIPInterruptionAssertion" _lockedInterruptionAssertion;
@"<BSInvalidatable>" _fullscreenModalElementInsetOverrideAssertion;
@"SBPIPStashAssertion" _stashForInterruptionAssertion;
@"SBPIPStashAssertion" _transitionStashAssertion;
@"SBPIPInterruptionDebouncingTimer" _interruptionEndDebouncingTimer;
B _defaultToStashed;
@"NSString" _bundleIDForAppAnimatingPIPStartInBackground;
@"NSString" _bundleIDForAppRecentlyStoppingPIP;
@"NSMutableSet" _pictureInPictureMorphAnimatorControllers;
@"UIView" _keyboardInsetsVisualizerView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardFrameInMainScreenFromNotifications;
q _unlockedEnvironmentModeWhenKeyboardFocusChanged;
@"FBSDisplayLayoutMonitor" _displayLayoutMonitor;
B _isReducingResourcesUsage;
@"<BSInvalidatable>" _keyboardFocusObserver;
@"<SBPIPControllerAdapter>" _adapter;
b1 _adapterWants_didAddContainerViewController;
b1 _adapterWants_willRemoveContainerViewController;
b1 _adapterWants_willBeginPIPInterruptionForAssertion;
b1 _adapterWants_willEndPIPInterruptionForAssertion;
b1 _adapterWants_didStartPictureInPictureCallback;
b1 _adapterWants_didCancelPictureInPictureCallback;
b1 _adapterWants_morphAnimatorDataSourceForMorphAnimatorController;
b1 _adapterWants_willStartPictureInPictureTestActionForApplication;
b1 _adapterWants_willRestorePictureInPictureForTestForApplication;
b1 _adapterWants_windowLevelChanged;
b1 _adapterWants_windowVisibilityChanged;
b1 _adapterWants_preventStashAssertions;
b1 _adapterWants_enhancedWindowingEnabled;
Q _inFlightWindowSceneUpdates;
@"SBWindowSceneManager" _windowSceneManager;
```

## Properties

```
@property (Tq,R,N) contentType;
@property (T@"SBWindowSceneManager",W,N,V_windowSceneManager) windowSceneManager;
@property (T@"NSArray",R,C,N) hostedAppSceneHandles;
@property (TB,R,N,GisPresentingPictureInPictureRequiringFullScreenKeyboard) presentingPictureInPictureRequiringFullScreenKeyboard;
@property (TB,R,N,GisHandlingContextWindowSceneUpdate) handlingContextWindowSceneUpdate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBPIPController activityDidChangeForSensorActivityDataProvider:];
-[SBPIPController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBPIPController _edgeInsetsForSource:onWindowScene:exists:];
-[SBPIPController _keyboardWillChangeFrame:];
-[SBPIPController shouldStartPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPController _setAlpha:forWindowsOnWindowScene:];
-[SBPIPController alertItemsController:willActivateAlertItem:];
-[SBPIPController alertItemsController:didActivateAlertItem:];
-[SBPIPController handleDestructionRequestForSceneHandles:];
-[SBPIPController updateZStackParticipantPreferencesIfNeeded:windowScene:];
-[SBPIPController keyboardFocusController:externalSceneDidAcquireFocus:];
-[SBPIPController _pictureInPictureWindowMarginsOnWindowScene:];
-[SBPIPController restoreContentViewController:appSceneEntity:morphAnimatorConfigurationBlock:completion:];
-[SBPIPController _createNewWindowForContainerViewController:onWindowScene:];
-[SBPIPController addContainerViewController:dataSource:];
-[SBPIPController morphAnimatorControllerDidTerminate:];
-[SBPIPController _allContainerViewControllers];
-[SBPIPController assistantDidDisappear:windowScene:];
-[SBPIPController _setWindowsLevel:forWindowsOnWindowScene:];
-[SBPIPController homeScreenInitialPIPFrameForWindowScene:withContentViewSize:position:padding:fromOrientation:toOrientation:shouldUpdate:gestureInitiated:];
-[SBPIPController restorePictureInPictureForApplicationBundleIdentifier:forDisplayContentModeSwap:];
-[SBPIPController _didLockStateProviderLock:];
-[SBPIPController _restorePictureInPictureForTestForApplicationWithBundleIdentifier:];
-[SBPIPController invalidateIdleTimerBehaviors];
-[SBPIPController prepareContainerViewControllerForHidingContentViewController:];
-[SBPIPController _edgeInsetsDidChangeOnWindowScene:];
-[SBPIPController _shouldHideWindowScene:];
-[SBPIPController _keyboardWillShowOrHide:];
-[SBPIPController windowSceneDidDisconnect:];
-[SBPIPController _acquireStashAssertionForWindowScene:withReason:identifier:customAllowedEnvironmentModes:];
-[SBPIPController displayLayoutMonitor:didUpdateDisplayLayout:withContext:];
-[SBPIPController isPictureInPictureWindowVisibleOnWindowScene:];
-[SBPIPController _edgeInsetsDidChangeForKeyboardOnIntegratedWindowScenes];
-[SBPIPController contentType];
-[SBPIPController cancelPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:];
-[SBPIPController dealloc];
-[SBPIPController _leadingWindowForWindowScene:];
-[SBPIPController containerViewController:userDidUpdateStashState:];
-[SBPIPController _contextForContainerViewController:creatingWithWindowSceneIfNeeded:];
-[SBPIPController _startPictureInPictureTestActionForApplicationWithBundleIdentifier:];
-[SBPIPController _contextForContainerViewController:];
-[SBPIPController containerViewControllerUserMayUpdateStashState:];
-[SBPIPController containerViewControllerForContentViewController:];
-[SBPIPController dataSourceForMorphAnimatorController:];
-[SBPIPController _shouldStashForTransitionContext:onWindowScene:];
-[SBPIPController isStoppingOrCancellingPictureInPictureForApplicationWithBundleIdentifier:scenePersistenceIdentifier:];
-[SBPIPController containerViewControllerDidBeginInteraction:];
-[SBPIPController _acquireInterruptionAssertionForReason:identifier:cameraSensorBundleIdentifier:];
-[SBPIPController _isPointInsidePictureInPictureContent:onWindowScene:];
-[SBPIPController _refreshLockStateProviderInterruptionAssertions];
-[SBPIPController acquireStashAssertionForWindowScene:withReason:identifier:];
-[SBPIPController _connectedWindowScenesIncludesExternalDisplay];
-[SBPIPController connectedWindowScenes];
-[SBPIPController _didLockStateProviderUnlock:];
-[SBPIPController _updateHyperregionComposers];
-[SBPIPController _cancelInterruptionDebouncingTimer];
-[SBPIPController containerViewControllersOnWindowScene:];
-[SBPIPController _isContentViewAlignedTopWithPosition:orientation:];
-[SBPIPController _enumerateContextsForWindowScene:usingBlock:];
-[SBPIPController windowSceneManager];
-[SBPIPController startPictureInPictureForApplicationWithProcessIdentifierEnteringBackground:scenePersistenceIdentifier:animated:completionHandler:];
-[SBPIPController lockStateProvider:didUpdateIsUILocked:];
-[SBPIPController _isContentViewAlignedLeftWithPosition:orientation:];
-[SBPIPController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPController _addPictureInPictureMorphAnimatorController:];
-[SBPIPController alertItemsController:didDeactivateAlertItem:forReason:];
-[SBPIPController hideContainersExcludingContainerForContentViewControllerAndTetheredOnes:animated:];
-[SBPIPController initWithIdleTimerCoordinator:windowLevel:interactionSettings:adapter:applicationController:];
-[SBPIPController _managePictureInPictureWindowVisibilityForWindowScene:animated:];
-[SBPIPController _hasStashAssertionForWindowScene:];
-[SBPIPController _acquirePIPStashAssertionIfNecessaryForTransitionContext:onWindowScene:];
-[SBPIPController _updateZStackIfNeededForDisappearingContainerViewController:];
-[SBPIPController isPresentingPictureInPictureForApplicationBundleIdentifier:];
-[SBPIPController _suspendPIPForInterruptionAssertion:];
-[SBPIPController windowLevelForWindowScene:];
-[SBPIPController hasCameraInterruptionForBundleIdentifier:];
-[SBPIPController externalDisplayServiceDidUpdatePreferredDisplayArrangement:];
-[SBPIPController _performWithoutAnimation:];
-[SBPIPController _relinquishPIPStashAssertionIfNecessaryForTransitionContext:];
-[SBPIPController _setHidden:forWindowsOnWindowScene:];
-[SBPIPController hostedAppSceneHandles];
-[SBPIPController pictureInPictureWindowMarginsOnWindowScene:];
-[SBPIPController isPresentingPictureInPictureRequiringFullScreenKeyboard];
-[SBPIPController _overrideInsetsOnWindowScene:forReason:identifier:];
-[SBPIPController _removePictureInPictureMorphAnimatorController:];
-[SBPIPController _allWindowScenesLocked];
-[SBPIPController setWindowSceneManager:];
-[SBPIPController hasIdleTimerBehaviors];
-[SBPIPController _minimumStashedPaddingDidChangeOnWindowScene:];
-[SBPIPController _keyboardInsetsForWindowScene:];
-[SBPIPController bringTetheredContentToFrontOnWindowScene:];
-[SBPIPController setPictureInPictureWindowsHidden:forReason:];
-[SBPIPController endPIPInterruptionForAssertion:];
-[SBPIPController containerViewController:didFinishStartAnimationWithInitialInterfaceOrientation:];
-[SBPIPController removeContainerViewController:];
-[SBPIPController _updateContainerViewControllersContentPaddingOnWindowScene:];
-[SBPIPController windowSceneDidConnect:];
-[SBPIPController anyContentViewPresentedOnWindowScene:];
-[SBPIPController showAllContentOnWindowScene:animated:];
-[SBPIPController _lockStateDidChange:];
-[SBPIPController isHandlingContextWindowSceneUpdate];
-[SBPIPController _invalidateInterruptionAssertion:];
-[SBPIPController _keyboardWillRotate:];
-[SBPIPController _windowScenesDisplayingPIPContent];
-[SBPIPController pictureInPictureMorphAnimatorControllerForProcessIdentifier:scenePersistenceIdentifier:];
-[SBPIPController updatePictureInPictureWindowLevelForWindowScene:];
-[SBPIPController createAndRegisterPictureInPictureMorphAnimatorControllerWithTargetProcessIdentifier:uuid:scenePersistenceIdentifier:appLayout:layoutRole:appLayoutBoundingBox:gestureInitiated:direction:];
-[SBPIPController movePIPContentToWindowScene:];
-[SBPIPController _updatePictureInPictureOverlayInsetsOnWindowScene:withCurrentLayoutState:toHomeScreen:toInterfaceOrientation:shouldUpdate:];
-[SBPIPController containerViewControllerDidEndInteraction:targetWindowScene:];
-[SBPIPController setEnhancedWindowingModeEnabled:windowScene:];
-[SBPIPController _registerForLockStateNotificationsForWindowScene:];
-[SBPIPController _moveContext:toWindowScene:];
-[SBPIPController _isInSplitPIP];
-[SBPIPController assistantWillAppear:windowScene:];
-[SBPIPController _setAdapter:];
-[SBPIPController _unregisterForLockStateNotificationsForWindowScene:];
-[SBPIPController tetheringModeForScenePersistenceIdentifier:];
-[SBPIPController coordinatorRequestedIdleTimerBehavior:];
-[SBPIPController _visualizeKeyboardFrameIfNeeded];
-[SBPIPController _notifyContainerViewControllersInterruptionDidEnd];
-[SBPIPController _setContainersStashed:forWindowScene:];
```
