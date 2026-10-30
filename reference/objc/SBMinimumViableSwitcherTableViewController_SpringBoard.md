# `SBMinimumViableSwitcherTableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- Protocols: `SBSwitcherContentViewControlling`
- 7 instance variables, 13 properties, 96 instance methods, 0 class methods

## Instance variables

```
@"<SBSwitcherContentViewControllerDelegate>" _delegate;
@"SBApplicationSceneView" _temporaryAppView;
@"SBApplicationSceneView" _temporarySideAppView;
@"SBBestAppSuggestion" _bestAppSuggestion;
B _asyncRenderingDisabled;
@"<SBSwitcherContentViewControllerDataSource>" _dataSource;
q _contentOrientation;
```

## Properties

```
@property (T@"<SBSwitcherContentViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBSwitcherContentViewControllerDataSource>",W,N,V_dataSource) dataSource;
@property (T@"SBBestAppSuggestion",&,N,V_bestAppSuggestion) bestAppSuggestion;
@property (TB,N,GisShowingModifierTimeline) showModifierTimeline;
@property (Tq,N,V_contentOrientation) contentOrientation;
@property (TB,N,GisAsyncRenderingDisabled,V_asyncRenderingDisabled) asyncRenderingDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) canInterruptActiveTransition;
@property (T@"BSAnimationSettings",R,C,N) defaultTransitionAnimationSettings;
@property (T@"UITraitCollection",R,N) traitCollection;
```

## Instance methods

```
-[SBMinimumViableSwitcherTableViewController jetsamModeForAppLayout:];
-[SBMinimumViableSwitcherTableViewController foregroundAppLayouts];
-[SBMinimumViableSwitcherTableViewController minimumHomeScreenScale];
-[SBMinimumViableSwitcherTableViewController tableView:numberOfRowsInSection:];
-[SBMinimumViableSwitcherTableViewController numberOfSectionsInTableView:];
-[SBMinimumViableSwitcherTableViewController tableView:commitEditingStyle:forRowAtIndexPath:];
-[SBMinimumViableSwitcherTableViewController tableView:cellForRowAtIndexPath:];
-[SBMinimumViableSwitcherTableViewController noteKeyboardFocusDidChangeToSceneID:];
-[SBMinimumViableSwitcherTableViewController contentAspectRatio];
-[SBMinimumViableSwitcherTableViewController handleVolumeDownButtonPress];
-[SBMinimumViableSwitcherTableViewController leadingStatusBarStyleRequest];
-[SBMinimumViableSwitcherTableViewController isUserInteractionEnabled];
-[SBMinimumViableSwitcherTableViewController animationControllerForTransitionRequest:];
-[SBMinimumViableSwitcherTableViewController shouldRubberbandFullScreenHomeGrabberView];
-[SBMinimumViableSwitcherTableViewController trailingStatusBarStyleRequest];
-[SBMinimumViableSwitcherTableViewController activityModeForAppLayout:];
-[SBMinimumViableSwitcherTableViewController overlaySceneHandle];
-[SBMinimumViableSwitcherTableViewController appLayouts];
-[SBMinimumViableSwitcherTableViewController handleHomeButtonLongPress];
-[SBMinimumViableSwitcherTableViewController switcherCardScale];
-[SBMinimumViableSwitcherTableViewController shouldAcceleratedHomeButtonPressBegin];
-[SBMinimumViableSwitcherTableViewController setBestAppSuggestion:];
-[SBMinimumViableSwitcherTableViewController handleVoiceCommandButtonPress];
-[SBMinimumViableSwitcherTableViewController contentOrientation];
-[SBMinimumViableSwitcherTableViewController tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:];
-[SBMinimumViableSwitcherTableViewController setContentOrientation:];
-[SBMinimumViableSwitcherTableViewController handleHeadsetButtonPress:];
-[SBMinimumViableSwitcherTableViewController viewDidLoad];
-[SBMinimumViableSwitcherTableViewController setDataSource:];
-[SBMinimumViableSwitcherTableViewController handleLockButtonPress];
-[SBMinimumViableSwitcherTableViewController prepareOverlayForContentRotation];
-[SBMinimumViableSwitcherTableViewController handleVolumeUpButtonPress];
-[SBMinimumViableSwitcherTableViewController failMultitaskingGesturesForReason:];
-[SBMinimumViableSwitcherTableViewController handleHomeButtonDoublePress];
-[SBMinimumViableSwitcherTableViewController invalidate];
-[SBMinimumViableSwitcherTableViewController setDelegate:];
-[SBMinimumViableSwitcherTableViewController bestAppSuggestion];
-[SBMinimumViableSwitcherTableViewController dataSource];
-[SBMinimumViableSwitcherTableViewController tableView:didSelectRowAtIndexPath:];
-[SBMinimumViableSwitcherTableViewController delegate];
-[SBMinimumViableSwitcherTableViewController handleHomeButtonPress];
-[SBMinimumViableSwitcherTableViewController tableView:canEditRowAtIndexPath:];
-[SBMinimumViableSwitcherTableViewController handleFluidSwitcherGestureManager:didBeginGesture:];
-[SBMinimumViableSwitcherTableViewController handleFluidSwitcherGestureManager:didEndGesture:];
-[SBMinimumViableSwitcherTableViewController performTransitionWithContext:animated:completion:];
-[SBMinimumViableSwitcherTableViewController liveContentOverlayForAppLayout:];
-[SBMinimumViableSwitcherTableViewController isWindowVisible];
-[SBMinimumViableSwitcherTableViewController _appLayouts];
-[SBMinimumViableSwitcherTableViewController _statusBarStyleRequestForDefaultStyle];
-[SBMinimumViableSwitcherTableViewController acquiredViewController:forTransientOverlayAppLayout:];
-[SBMinimumViableSwitcherTableViewController appLeadingStatusBarStyleAttributes];
-[SBMinimumViableSwitcherTableViewController appTrailingStatusBarStyleAttributes];
-[SBMinimumViableSwitcherTableViewController canInterruptActiveTransition];
-[SBMinimumViableSwitcherTableViewController canPerformKeyboardShortcutAction:forBundleIdentifier:orSceneIdentifier:];
-[SBMinimumViableSwitcherTableViewController canPerformSwitcherShortcutAction:forSceneIdentifier:];
-[SBMinimumViableSwitcherTableViewController canShowMenuBar];
-[SBMinimumViableSwitcherTableViewController clickReceivedForHomeGrabberView:];
-[SBMinimumViableSwitcherTableViewController defaultTransitionAnimationSettings];
-[SBMinimumViableSwitcherTableViewController effectiveLeadingStatusBarPartFrame];
-[SBMinimumViableSwitcherTableViewController effectiveTrailingStatusBarPartFrame];
-[SBMinimumViableSwitcherTableViewController handleContinuousFoldDidBegin];
-[SBMinimumViableSwitcherTableViewController handleContinuousFoldDidEnd];
-[SBMinimumViableSwitcherTableViewController handleContinuousFoldDidSwap];
-[SBMinimumViableSwitcherTableViewController handleContinuousFoldWillSwap];
-[SBMinimumViableSwitcherTableViewController handleFluidSwitcherGestureManager:didUpdateGesture:];
-[SBMinimumViableSwitcherTableViewController iconForAppLayout:];
-[SBMinimumViableSwitcherTableViewController isAsyncRenderingDisabled];
-[SBMinimumViableSwitcherTableViewController isShowingModifierTimeline];
-[SBMinimumViableSwitcherTableViewController isStatusBarHiddenForAppLayout:];
-[SBMinimumViableSwitcherTableViewController isStatusBarPartPreferredHiddenByApp:];
-[SBMinimumViableSwitcherTableViewController isStatusBarStyleControlledBySystem];
-[SBMinimumViableSwitcherTableViewController isTransitioningToEnvironmentWithoutStatusBar];
-[SBMinimumViableSwitcherTableViewController liveOverlayForSceneHandle:];
-[SBMinimumViableSwitcherTableViewController liveOverlayForSceneIdentityToken:];
-[SBMinimumViableSwitcherTableViewController liveScenesIdentityTokens];
-[SBMinimumViableSwitcherTableViewController noteAppLayoutsDidChange];
-[SBMinimumViableSwitcherTableViewController noteCoordinatedSwitcherControllersDidChange];
-[SBMinimumViableSwitcherTableViewController noteModelDidMutateForInsertionOfAppLayouts:atIndexes:willAnimate:];
-[SBMinimumViableSwitcherTableViewController noteModelWillMutateForInsertionOfAppLayouts:atIndexes:];
-[SBMinimumViableSwitcherTableViewController noteWindowManagementContextDidChange];
-[SBMinimumViableSwitcherTableViewController performAnimatedInsertionOfAppLayouts:atIndexes:completion:];
-[SBMinimumViableSwitcherTableViewController performKeyboardShortcutAction:withSceneIdentifier:];
-[SBMinimumViableSwitcherTableViewController performSwitcherShortcutAction:forSceneIdentifier:];
-[SBMinimumViableSwitcherTableViewController prepareAnimatedInsertionOfAppLayouts:atIndexes:];
-[SBMinimumViableSwitcherTableViewController prepareContentForMoveToWindowScene:];
-[SBMinimumViableSwitcherTableViewController relinquishTransientOverlayViewController:];
-[SBMinimumViableSwitcherTableViewController removeLayoutRole:inSpace:mutationBlock:reason:];
-[SBMinimumViableSwitcherTableViewController respondToInAppStatusBarRequestedHiddenUpdateAnimated:];
-[SBMinimumViableSwitcherTableViewController sceneLayoutTransitionWillStartWithTransitionContext:];
-[SBMinimumViableSwitcherTableViewController setAsyncRenderingDisabled:];
-[SBMinimumViableSwitcherTableViewController setShowModifierTimeline:];
-[SBMinimumViableSwitcherTableViewController shouldAddAppLayoutToFront:forTransitionWithContext:transitionCompleted:];
-[SBMinimumViableSwitcherTableViewController shouldAnimateInsertionOfAppLayouts:atIndexes:];
-[SBMinimumViableSwitcherTableViewController snapshotScaleForSceneHandle:];
-[SBMinimumViableSwitcherTableViewController tapReceivedForGrabberTongueAtEdge:];
-[SBMinimumViableSwitcherTableViewController updateAppNameVisibilityInStatusBarOwningLeadingPartWithBlock:];
```
