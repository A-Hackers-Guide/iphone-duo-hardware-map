# `SBSwitcherContentViewControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBButtonEventsHandler`, `SBLayoutStateTransitionObserver`, `SBSwitcherAnimatedTransitioning`, `UITraitEnvironment`
- 0 instance variables, 6 properties, 71 instance methods, 0 class methods

## Properties

```
@property (T@"<SBSwitcherContentViewControllerDelegate>",W,N) delegate;
@property (T@"<SBSwitcherContentViewControllerDataSource>",W,N) dataSource;
@property (T@"SBBestAppSuggestion",&,N) bestAppSuggestion;
@property (TB,N,GisShowingModifierTimeline) showModifierTimeline;
@property (Tq,N) contentOrientation;
@property (TB,N,GisAsyncRenderingDisabled) asyncRenderingDisabled;
```

## Instance methods

```
-[SBSwitcherContentViewControlling jetsamModeForAppLayout:];
-[SBSwitcherContentViewControlling foregroundAppLayouts];
-[SBSwitcherContentViewControlling minimumHomeScreenScale];
-[SBSwitcherContentViewControlling noteKeyboardFocusDidChangeToSceneID:];
-[SBSwitcherContentViewControlling contentAspectRatio];
-[SBSwitcherContentViewControlling leadingStatusBarStyleRequest];
-[SBSwitcherContentViewControlling isUserInteractionEnabled];
-[SBSwitcherContentViewControlling animationControllerForTransitionRequest:];
-[SBSwitcherContentViewControlling shouldRubberbandFullScreenHomeGrabberView];
-[SBSwitcherContentViewControlling trailingStatusBarStyleRequest];
-[SBSwitcherContentViewControlling activityModeForAppLayout:];
-[SBSwitcherContentViewControlling appLayouts];
-[SBSwitcherContentViewControlling shouldAcceleratedHomeButtonPressBegin];
-[SBSwitcherContentViewControlling setBestAppSuggestion:];
-[SBSwitcherContentViewControlling contentOrientation];
-[SBSwitcherContentViewControlling setContentOrientation:];
-[SBSwitcherContentViewControlling setDataSource:];
-[SBSwitcherContentViewControlling invalidate];
-[SBSwitcherContentViewControlling setDelegate:];
-[SBSwitcherContentViewControlling bestAppSuggestion];
-[SBSwitcherContentViewControlling dataSource];
-[SBSwitcherContentViewControlling delegate];
-[SBSwitcherContentViewControlling handleFluidSwitcherGestureManager:didBeginGesture:];
-[SBSwitcherContentViewControlling handleFluidSwitcherGestureManager:didEndGesture:];
-[SBSwitcherContentViewControlling liveContentOverlayForAppLayout:];
-[SBSwitcherContentViewControlling isWindowVisible];
-[SBSwitcherContentViewControlling acquiredViewController:forTransientOverlayAppLayout:];
-[SBSwitcherContentViewControlling appLeadingStatusBarStyleAttributes];
-[SBSwitcherContentViewControlling appTrailingStatusBarStyleAttributes];
-[SBSwitcherContentViewControlling canPerformKeyboardShortcutAction:forBundleIdentifier:orSceneIdentifier:];
-[SBSwitcherContentViewControlling canPerformSwitcherShortcutAction:forSceneIdentifier:];
-[SBSwitcherContentViewControlling canShowMenuBar];
-[SBSwitcherContentViewControlling clickReceivedForHomeGrabberView:];
-[SBSwitcherContentViewControlling effectiveLeadingStatusBarPartFrame];
-[SBSwitcherContentViewControlling effectiveTrailingStatusBarPartFrame];
-[SBSwitcherContentViewControlling handleContinuousFoldDidBegin];
-[SBSwitcherContentViewControlling handleContinuousFoldDidEnd];
-[SBSwitcherContentViewControlling handleContinuousFoldDidSwap];
-[SBSwitcherContentViewControlling handleContinuousFoldWillSwap];
-[SBSwitcherContentViewControlling handleFluidSwitcherGestureManager:didUpdateGesture:];
-[SBSwitcherContentViewControlling iconForAppLayout:];
-[SBSwitcherContentViewControlling isAsyncRenderingDisabled];
-[SBSwitcherContentViewControlling isShowingModifierTimeline];
-[SBSwitcherContentViewControlling isStatusBarHiddenForAppLayout:];
-[SBSwitcherContentViewControlling isStatusBarPartPreferredHiddenByApp:];
-[SBSwitcherContentViewControlling isStatusBarStyleControlledBySystem];
-[SBSwitcherContentViewControlling isTransitioningToEnvironmentWithoutStatusBar];
-[SBSwitcherContentViewControlling liveOverlayForSceneHandle:];
-[SBSwitcherContentViewControlling liveOverlayForSceneIdentityToken:];
-[SBSwitcherContentViewControlling liveScenesIdentityTokens];
-[SBSwitcherContentViewControlling noteAppLayoutsDidChange];
-[SBSwitcherContentViewControlling noteCoordinatedSwitcherControllersDidChange];
-[SBSwitcherContentViewControlling noteModelDidMutateForInsertionOfAppLayouts:atIndexes:willAnimate:];
-[SBSwitcherContentViewControlling noteModelWillMutateForInsertionOfAppLayouts:atIndexes:];
-[SBSwitcherContentViewControlling noteWindowManagementContextDidChange];
-[SBSwitcherContentViewControlling performAnimatedInsertionOfAppLayouts:atIndexes:completion:];
-[SBSwitcherContentViewControlling performKeyboardShortcutAction:withSceneIdentifier:];
-[SBSwitcherContentViewControlling performSwitcherShortcutAction:forSceneIdentifier:];
-[SBSwitcherContentViewControlling prepareAnimatedInsertionOfAppLayouts:atIndexes:];
-[SBSwitcherContentViewControlling prepareContentForMoveToWindowScene:];
-[SBSwitcherContentViewControlling relinquishTransientOverlayViewController:];
-[SBSwitcherContentViewControlling removeLayoutRole:inSpace:mutationBlock:reason:];
-[SBSwitcherContentViewControlling respondToInAppStatusBarRequestedHiddenUpdateAnimated:];
-[SBSwitcherContentViewControlling sceneLayoutTransitionWillStartWithTransitionContext:];
-[SBSwitcherContentViewControlling setAsyncRenderingDisabled:];
-[SBSwitcherContentViewControlling setShowModifierTimeline:];
-[SBSwitcherContentViewControlling shouldAddAppLayoutToFront:forTransitionWithContext:transitionCompleted:];
-[SBSwitcherContentViewControlling shouldAnimateInsertionOfAppLayouts:atIndexes:];
-[SBSwitcherContentViewControlling snapshotScaleForSceneHandle:];
-[SBSwitcherContentViewControlling tapReceivedForGrabberTongueAtEdge:];
-[SBSwitcherContentViewControlling updateAppNameVisibilityInStatusBarOwningLeadingPartWithBlock:];
```
