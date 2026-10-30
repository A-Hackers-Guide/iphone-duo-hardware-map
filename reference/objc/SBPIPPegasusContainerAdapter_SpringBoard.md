# `SBPIPPegasusContainerAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PGPictureInPictureViewControllerContentContainer`, `SBPIPStashTabSuppressionPolicyProviderObserver`, `SBLayoutStateTransitionObserver`, `SBFDevicePoseProviderObserver`, `SBFStatusBarManagerObserver`, `SBPIPSplitPIPStagingTransitionAssistantDelegate`, `SBPIPContainerViewControllerAdapter`, `SBPIPInteractionControllerDataSource`
- 44 instance variables, 7 properties, 138 instance methods, 0 class methods

## Instance variables

```
@"SBPIPContainerViewController<SBPIPContainerViewControllerAdapterContextProviding>" _containerViewController;
@"UIButton" _menuButton;
B _isAnyInteractionGestureActive;
{CGSize="width"d"height"d} _minimumStashTabSize;
q _inFlightRotation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inFlightRotationContentViewFrame;
@? _inFlightRotationCompletionHandler;
Q _rotationAnimationGeneration;
B _invalidated;
B _isChangingSize;
B _isInteractivelyResizingHostedWindow;
B _isPinningWithResizeTransform;
Q _splitPIPTransformPinGeneration;
B _didChangeDisplayWhileInSplitPIP;
@"SBPIPStashTabSuppressionPolicyProvider" _stashTabVisibilityPolicyProvider;
@"<SBPIPPositionHyperregionComposing>" _pipPositionHyperregionComposer;
@"NSArray" _offScreenHyperregionComposers;
@"<BSInvalidatable>" _visibilityAssertion;
B _isInSplitPIP;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
@"SBSplitPIPSupportValidator" _splitPIPSupportValidator;
@"<BSInvalidatable>" _stateCaptureInvalidatable;
B _cachedOnPiPControlsVisible;
@"SBSplitPIPSystemChromePresentation" _splitPIPSystemChromePresentation;
d _splitPIPConcentricInset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentSplitPIPFrame;
B _isKeyboardVisible;
d _keyboardHeight;
@"<BSInvalidatable>" _splitPIPKeyboardFocusDeferringRule;
@"UITapGestureRecognizer" _splitPIPKeyboardDismissalTapGestureRecognizer;
B _wantsPinnedSplitPIP;
B _isSplitPIPEnterRequestPending;
B _isSplitPIPKeyboardResizeRequestPending;
B _needsSplitPIPKeyboardResize;
B _isAnimatingSplitPIPKeyboardResize;
d _currentSplitPIPApplicationCornerRadius;
@"NSSet" _splitPIPElementsBeforeSwitcher;
d _keyboardHeightBeforeSwitcher;
B _isApplicationKeyboardCovered;
{CGSize="width"d"height"d} _splitPIPHeldContentSize;
@"SBPIPSplitPIPStagingTransitionAssistant" _splitPIPStagingAssistant;
B _isRequestingSplitPIPTransitionForGesture;
B _dismissesKeyboardOnSplitPIPEntry;
@"PGPictureInPictureViewController" _pictureInPictureViewController;
```

## Properties

```
@property (T@"PGPictureInPictureViewController",R,N,V_pictureInPictureViewController) pictureInPictureViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSNumber",?,&,N) overrideResourcesUsageReductionTimeout;
@property (TB,?,R,N) shouldSuppressAssociatedElementsInSystemAperture;
```

## Instance methods

```
-[SBPIPPegasusContainerAdapter layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBPIPPegasusContainerAdapter statusBarManager:didUpdateAvoidanceFrameForStatusBar:withAnimationSettings:];
-[SBPIPPegasusContainerAdapter _keyboardWillShow:];
-[SBPIPPegasusContainerAdapter statusBarManager:didUpdateOcclusionFrameForStatusBar:];
-[SBPIPPegasusContainerAdapter _keyboardWillHide:];
-[SBPIPPegasusContainerAdapter containerViewControllerStopReducingResourcesUsage:];
-[SBPIPPegasusContainerAdapter containerViewControllerStartReducingResourcesUsage:];
-[SBPIPPegasusContainerAdapter pictureInPictureViewController];
-[SBPIPPegasusContainerAdapter dealloc];
-[SBPIPPegasusContainerAdapter setContainerViewController:];
-[SBPIPPegasusContainerAdapter _acquireVisibilityAssertionIfNeeded];
-[SBPIPPegasusContainerAdapter poseProvider:didUpdateFromPose:toPose:];
-[SBPIPPegasusContainerAdapter invalidate];
-[SBPIPPegasusContainerAdapter layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPPegasusContainerAdapter _invalidateVisibilityAssertion];
-[SBPIPPegasusContainerAdapter debugName];
-[SBPIPPegasusContainerAdapter layoutSettings];
-[SBPIPPegasusContainerAdapter _displayCornerRadius];
-[SBPIPPegasusContainerAdapter acquireInterfaceOrientationLock];
-[SBPIPPegasusContainerAdapter updateMenuItems];
-[SBPIPPegasusContainerAdapter _performStopAnimationWithFinalInterfaceOrientation:finalLayerFrame:completionHandler:];
-[SBPIPPegasusContainerAdapter didChangePiPControlsVisible:];
-[SBPIPPegasusContainerAdapter handleDoubleTapGesture];
-[SBPIPPegasusContainerAdapter handleTapWhileStashedGesture];
-[SBPIPPegasusContainerAdapter handleToggleProminenceTapGesture];
-[SBPIPPegasusContainerAdapter notePictureInPictureViewControllerPrefersHiddenFromClonedDisplayDidChange];
-[SBPIPPegasusContainerAdapter notePictureInPictureViewControllerTetheringDidUpdate];
-[SBPIPPegasusContainerAdapter performRotateAnimationWithRotation:completionHandler:];
-[SBPIPPegasusContainerAdapter performStartAnimationWithCompletionHandler:];
-[SBPIPPegasusContainerAdapter performStartInIsolationWithCompletionHandler:];
-[SBPIPPegasusContainerAdapter performStopAnimationWithFinalInterfaceOrientation:finalLayerFrame:completionHandler:];
-[SBPIPPegasusContainerAdapter performStopInIsolationWithCompletionHandler:];
-[SBPIPPegasusContainerAdapter pictureInPictureClientDidRequestStashing];
-[SBPIPPegasusContainerAdapter preferredContentSizeDidChangeForPictureInPictureViewController];
-[SBPIPPegasusContainerAdapter prepareStartAnimationWithInitialInterfaceOrientation:initialLayerFrame:completionHandler:];
-[SBPIPPegasusContainerAdapter relinquishInterfaceOrientationLock];
-[SBPIPPegasusContainerAdapter _requestSplitPIPTransitionForCurrentStateWithAnimationSettings:];
-[SBPIPPegasusContainerAdapter _scheduleSplitPIPKeyboardResize];
-[SBPIPPegasusContainerAdapter _acquireSplitPIPSystemChromePresentation];
-[SBPIPPegasusContainerAdapter _animateSplitPIPPinnedToFrame:animationSettings:];
-[SBPIPPegasusContainerAdapter _animationSettingsMatchingKeyboardNotification:];
-[SBPIPPegasusContainerAdapter _applicationCanHostPinnedSplitPIPForLayoutElements:];
-[SBPIPPegasusContainerAdapter _applySplitPIPAspectRatioIfChanged];
-[SBPIPPegasusContainerAdapter _applySplitPIPShapeForCompact:];
-[SBPIPPegasusContainerAdapter _canFormSplitPIPInCurrentLayoutState];
-[SBPIPPegasusContainerAdapter _changeSplitPIPCornersWithSettings:changes:completion:];
-[SBPIPPegasusContainerAdapter _configureSplitPIPAppearanceForContainerSize:];
-[SBPIPPegasusContainerAdapter _containerSizeForInterfaceOrientation:];
-[SBPIPPegasusContainerAdapter _createOrInvalidateStashTabVisibilityPolicyProvider];
-[SBPIPPegasusContainerAdapter _defaultSplitPIPAnimationSettings];
-[SBPIPPegasusContainerAdapter _dismissApplicationKeyboard];
-[SBPIPPegasusContainerAdapter _endHostedWindowSizeChangeIfNeeded];
-[SBPIPPegasusContainerAdapter _exitSplitPIPForDisplayChange];
-[SBPIPPegasusContainerAdapter _forceApplicationKeyboardAway];
-[SBPIPPegasusContainerAdapter _handleKeyboardVisibilityChange:animationSettings:];
-[SBPIPPegasusContainerAdapter _handleSplitPIPKeyboardDismissalTap:];
-[SBPIPPegasusContainerAdapter _isApplicationKeyboardCoveredByKeyboardWillHideLocal:];
-[SBPIPPegasusContainerAdapter _isApplicationSettledForLayoutState:];
-[SBPIPPegasusContainerAdapter _isKeyboardServicingApplicationSplitWithPIP];
-[SBPIPPegasusContainerAdapter _isRotationFromLayoutState:toLayoutState:];
-[SBPIPPegasusContainerAdapter _isSplitPIPCompact];
-[SBPIPPegasusContainerAdapter _isSplitPIPPositionAnimationInFlight];
-[SBPIPPegasusContainerAdapter _obscuringHeightForKeyboardFrame:];
-[SBPIPPegasusContainerAdapter _releaseSplitPIPKeyboardFocusDeferral];
-[SBPIPPegasusContainerAdapter _reloadMenuButton];
-[SBPIPPegasusContainerAdapter _requestSplitPIPKeyboardResizeIfNeeded];
-[SBPIPPegasusContainerAdapter _requestSplitPIPTransitionForFoldAvoidanceActive:animationSettings:];
-[SBPIPPegasusContainerAdapter _requestTransitionToEnterSplitPIP];
-[SBPIPPegasusContainerAdapter _requestTransitionToExitSplitPIP];
-[SBPIPPegasusContainerAdapter _requestTransitionToExitSplitPIPWithAnimationSettings:];
-[SBPIPPegasusContainerAdapter _resetSplitPIPAppearance];
-[SBPIPPegasusContainerAdapter _settleInFlightRotationAnimation];
-[SBPIPPegasusContainerAdapter _shouldEnableSplitPIPForLayoutElements:interfaceOrientation:];
-[SBPIPPegasusContainerAdapter _shouldEnableSplitPIPForLayoutState:];
-[SBPIPPegasusContainerAdapter _splitPIPContextForFoldAvoidanceActive:];
-[SBPIPPegasusContainerAdapter _splitPIPContextForFoldAvoidanceActive:containerSize:];
-[SBPIPPegasusContainerAdapter _splitPIPStatusBarClockFrameReturningStatusBar:];
-[SBPIPPegasusContainerAdapter _splitPIPStatusBarContentTrailingDodgeForClockFrame:statusBar:];
-[SBPIPPegasusContainerAdapter _updateSplitPIPAdditionalControlsInsets];
-[SBPIPPegasusContainerAdapter _updateSplitPIPAdditionalControlsInsetsWithAnimationSettings:];
-[SBPIPPegasusContainerAdapter _updateSplitPIPControlsSuppression];
-[SBPIPPegasusContainerAdapter _updateSplitPIPForCurrentStateAllowingRestore:animationSettings:];
-[SBPIPPegasusContainerAdapter _updateSplitPIPKeyboardAvoidance];
-[SBPIPPegasusContainerAdapter _wantsSplitPIPCompactLayout];
-[SBPIPPegasusContainerAdapter bundleIdentifierForContainerViewController:];
-[SBPIPPegasusContainerAdapter canFormSplitPIPForSplitPIPStagingTransitionAssistant:];
-[SBPIPPegasusContainerAdapter containerViewController:didEndSplitPIPStagingWithCommit:];
-[SBPIPPegasusContainerAdapter containerViewController:didMoveToWindow:];
-[SBPIPPegasusContainerAdapter containerViewController:didUpdateContentViewFrame:reason:];
-[SBPIPPegasusContainerAdapter containerViewController:didUpdateStashProgress:];
-[SBPIPPegasusContainerAdapter containerViewController:didUpdateStashState:springSettings:];
-[SBPIPPegasusContainerAdapter containerViewController:wantsStashTabHidden:left:springSettings:completion:];
-[SBPIPPegasusContainerAdapter containerViewController:willBeginInteractionWithGestureRecognizer:];
-[SBPIPPegasusContainerAdapter containerViewControllerDidEndInteraction:];
-[SBPIPPegasusContainerAdapter containerViewControllerDidEndSizeChange:];
-[SBPIPPegasusContainerAdapter containerViewControllerInterruptionDidEnd:];
-[SBPIPPegasusContainerAdapter containerViewControllerShouldBeginSplitPIPStaging:];
-[SBPIPPegasusContainerAdapter containerViewControllerWillBeginSizeChange:behavior:];
-[SBPIPPegasusContainerAdapter contentViewControllerForContainerViewController:];
-[SBPIPPegasusContainerAdapter currentCornerRadiusForInteractionController:];
-[SBPIPPegasusContainerAdapter defaultPositionHyperregionComposers];
-[SBPIPPegasusContainerAdapter initWithPictureInPictureViewController:];
-[SBPIPPegasusContainerAdapter interactionController:edgeInsetsForWindowScene:];
-[SBPIPPegasusContainerAdapter interactionController:stashedOcclusionRectForWindowScene:];
-[SBPIPPegasusContainerAdapter interactionController:stashedPaddingForWindowScene:];
-[SBPIPPegasusContainerAdapter interactionController:updateScaleInteractor:pipSize:forPanGesture:];
-[SBPIPPegasusContainerAdapter interactionControllerAnimatesAspectRatioChanges:];
-[SBPIPPegasusContainerAdapter interactionControllerConnectedWindowScenes:];
-[SBPIPPegasusContainerAdapter interactionControllerScalesDuringPanGesture:];
-[SBPIPPegasusContainerAdapter isEnterTransitionPendingForSplitPIPStagingTransitionAssistant:];
-[SBPIPPegasusContainerAdapter isInSplitPIPForSplitPIPStagingTransitionAssistant:];
-[SBPIPPegasusContainerAdapter isResizingForSplitPIPStagingTransitionAssistant:];
-[SBPIPPegasusContainerAdapter isStashTabHiddenForContainerViewController:];
-[SBPIPPegasusContainerAdapter layoutSubviewsForContainerViewController:];
-[SBPIPPegasusContainerAdapter loadSubviewsForContainerViewController:];
-[SBPIPPegasusContainerAdapter morphAnimatorTargetContainerViewForContainerViewController:];
-[SBPIPPegasusContainerAdapter morphAnimatorTargetViewForContainerViewController:];
-[SBPIPPegasusContainerAdapter overrideResourcesUsageReductionTimeout];
-[SBPIPPegasusContainerAdapter processIdentifierForContainerViewController:];
-[SBPIPPegasusContainerAdapter scenePersistenceIdentifierForContainerViewController:];
-[SBPIPPegasusContainerAdapter shouldDisableIdleTimerForContainerViewController:];
-[SBPIPPegasusContainerAdapter shouldPointerInteractionBeginForInteractionController:atLocation:inView:];
-[SBPIPPegasusContainerAdapter shouldSuppressAssociatedElementsInSystemAperture];
-[SBPIPPegasusContainerAdapter splitPIPContextForRestoreWithLayoutElements:interfaceOrientation:];
-[SBPIPPegasusContainerAdapter splitPIPStagingSlotRectForInteractionController:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistant:setWantsPinnedSplitPIP:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantCanDragOutOfSplitPIP:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantDidUpdateInteraction:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantPinIntoSplitPIP:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantRequestEnterTransition:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantRequestExitTransition:];
-[SBPIPPegasusContainerAdapter splitPIPStagingTransitionAssistantUnpinForDrag:];
-[SBPIPPegasusContainerAdapter stashTabVisibilityPolicyProviderDidUpdatePolicy:];
-[SBPIPPegasusContainerAdapter systemGestureManagerForInteractionControllerResizing:];
-[SBPIPPegasusContainerAdapter systemPointerInteractionManagerForInteractionController:];
-[SBPIPPegasusContainerAdapter transitionAnimationDidEndForContainerViewController:];
-[SBPIPPegasusContainerAdapter transitionAnimationWillBeginForContainerViewController:];
-[SBPIPPegasusContainerAdapter updateSplitPIPEnabled:forContainerViewController:];
```
