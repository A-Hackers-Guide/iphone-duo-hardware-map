# `SBControlCenterModuleTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `CCUIModuleAlertViewControllerDelegate`
- 2 instance variables, 6 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"CCUIModuleAlertViewController" _moduleOverlayViewController;
@"<SBControlCenterModuleTransientOverlayViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBControlCenterModuleTransientOverlayViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"CCSModulePresentationOptions",R,C,D,N) presentationOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBControlCenterModuleTransientOverlayViewController _dismiss];
-[SBControlCenterModuleTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBControlCenterModuleTransientOverlayViewController handleGestureDismissal];
-[SBControlCenterModuleTransientOverlayViewController preferredInterfaceOrientationForPresentation];
-[SBControlCenterModuleTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBControlCenterModuleTransientOverlayViewController presentationOptions];
-[SBControlCenterModuleTransientOverlayViewController init];
-[SBControlCenterModuleTransientOverlayViewController supportedInterfaceOrientations];
-[SBControlCenterModuleTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBControlCenterModuleTransientOverlayViewController viewDidLoad];
-[SBControlCenterModuleTransientOverlayViewController shouldDisableOrientationUpdates];
-[SBControlCenterModuleTransientOverlayViewController _preferredStatusBarVisibility];
-[SBControlCenterModuleTransientOverlayViewController initWithNibName:bundle:];
-[SBControlCenterModuleTransientOverlayViewController shouldDisableControlCenter];
-[SBControlCenterModuleTransientOverlayViewController _canShowWhileLocked];
-[SBControlCenterModuleTransientOverlayViewController setDelegate:];
-[SBControlCenterModuleTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBControlCenterModuleTransientOverlayViewController delegate];
-[SBControlCenterModuleTransientOverlayViewController initWithCoder:];
-[SBControlCenterModuleTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBControlCenterModuleTransientOverlayViewController handleHomeButtonPress];
-[SBControlCenterModuleTransientOverlayViewController contentModuleAlertViewControllerNeedsDismissal:];
-[SBControlCenterModuleTransientOverlayViewController _animateTransitionFromViewController:toViewController:containerView:isAnimated:otherAnimations:completion:];
-[SBControlCenterModuleTransientOverlayViewController _shouldBlurBackground];
-[SBControlCenterModuleTransientOverlayViewController initWithWindowScene:moduleIdentifier:presentationOptions:];
```
