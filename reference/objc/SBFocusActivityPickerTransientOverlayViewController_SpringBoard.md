# `SBFocusActivityPickerTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- 4 instance variables, 1 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"FCUIActivityPickerViewController" _activityPickerViewController;
@"MTMaterialView" _backgroundMaterialView;
@"UITapGestureRecognizer" _tapGesture;
@"<SBFocusActivityPickerTransientOverlayViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBFocusActivityPickerTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBFocusActivityPickerTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBFocusActivityPickerTransientOverlayViewController handleGestureDismissal];
-[SBFocusActivityPickerTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBFocusActivityPickerTransientOverlayViewController _handleTap:];
-[SBFocusActivityPickerTransientOverlayViewController viewWillDisappear:];
-[SBFocusActivityPickerTransientOverlayViewController supportedInterfaceOrientations];
-[SBFocusActivityPickerTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBFocusActivityPickerTransientOverlayViewController viewDidLoad];
-[SBFocusActivityPickerTransientOverlayViewController prefersHomeIndicatorAutoHidden];
-[SBFocusActivityPickerTransientOverlayViewController shouldAutorotate];
-[SBFocusActivityPickerTransientOverlayViewController shouldDisableControlCenter];
-[SBFocusActivityPickerTransientOverlayViewController _canShowWhileLocked];
-[SBFocusActivityPickerTransientOverlayViewController setDelegate:];
-[SBFocusActivityPickerTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBFocusActivityPickerTransientOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBFocusActivityPickerTransientOverlayViewController delegate];
-[SBFocusActivityPickerTransientOverlayViewController prefersStatusBarHidden];
-[SBFocusActivityPickerTransientOverlayViewController sizeForChildContentContainer:withParentContainerSize:];
-[SBFocusActivityPickerTransientOverlayViewController _dismiss:];
-[SBFocusActivityPickerTransientOverlayViewController _contractedFrame];
-[SBFocusActivityPickerTransientOverlayViewController _contractedFrameNotTargetingSystemAperture];
-[SBFocusActivityPickerTransientOverlayViewController _performTransitionForPresentation:contextProvider:actions:usingAnimationWorkaround:];
-[SBFocusActivityPickerTransientOverlayViewController _shouldUseCondensedFrame:];
```
