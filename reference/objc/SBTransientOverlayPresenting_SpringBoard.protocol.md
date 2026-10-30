# `SBTransientOverlayPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `SBButtonEventsHandler`
- 0 instance variables, 21 properties, 36 instance methods, 0 class methods

## Properties

```
@property (T@"SBWindowScene",R,W,N) windowScene;
@property (TB,R,N) hasActivePresentation;
@property (TB,R,N) canActivePresentationBecomeLocalFirstResponder;
@property (Tq,R,N) presentedViewControllerCount;
@property (TB,R,N) shouldUseSceneBasedKeyboardFocusForActivePresentation;
@property (TB,R,N) canHandleButtonEvents;
@property (T@"UIStatusBarStyleRequest",R,C,N) currentStatusBarStyleRequest;
@property (TB,R,N) hasVisibleStatusBar;
@property (TB,R,N) prefersStatusBarActivityItemVisible;
@property (T@"NSNumber",R,N) preferredWhitePointAdaptivityStyleValue;
@property (T@"SBTransientOverlayViewController",R,N) topmostPresentedViewController;
@property (Tq,R,N) topmostViewControllerInterfaceOrientation;
@property (Td,R,N) topmostWindowLevel;
@property (T@"NSArray",R,N) presentedViewControllers;
@property (TB,R,N) ownsHomeGesture;
@property (Tq,R,N) preferredGestureDismissalStyle;
@property (T@"SBTransientOverlayViewController",R,N) viewControllerForGestureDismissal;
@property (TB,R,N) shouldDisableControlCenter;
@property (TB,R,N) shouldDisableCoverSheetGesture;
@property (TB,R,N) shouldDisableSiri;
@property (TB,R,N) activePresentationPreventsDragAndDrop;
```

## Instance methods

```
-[SBTransientOverlayPresenting isTopmostPresentedViewController:];
-[SBTransientOverlayPresenting isPresentingViewController:];
-[SBTransientOverlayPresenting hasActivePresentationFromBundleIdentifier:];
-[SBTransientOverlayPresenting topmostPresentedViewController];
-[SBTransientOverlayPresenting hasActivePresentation];
-[SBTransientOverlayPresenting shouldUseSceneBasedKeyboardFocusForActivePresentation];
-[SBTransientOverlayPresenting canActivePresentationBecomeLocalFirstResponder];
-[SBTransientOverlayPresenting shouldDisableCoverSheetGesture];
-[SBTransientOverlayPresenting presentedViewControllerCount];
-[SBTransientOverlayPresenting hasActiveSpotlightPresentation];
-[SBTransientOverlayPresenting isTopmostPresentationFromSceneWithIdentityTokenString:];
-[SBTransientOverlayPresenting keyboardFocusTargetForTopmostPresentingScene];
-[SBTransientOverlayPresenting ownsHomeGesture];
-[SBTransientOverlayPresenting hasActivePresentationFromProcess:];
-[SBTransientOverlayPresenting prefersStatusBarActivityItemVisible];
-[SBTransientOverlayPresenting hasPresentationAboveWindowLevel:];
-[SBTransientOverlayPresenting activePresentationPreventsDragAndDrop];
-[SBTransientOverlayPresenting newContentStatusBarHiddenAssertionWithReason:];
-[SBTransientOverlayPresenting removeObserver:];
-[SBTransientOverlayPresenting windowSceneDidDisconnect:];
-[SBTransientOverlayPresenting handleDoubleHeightStatusBarTap];
-[SBTransientOverlayPresenting presentedViewControllers];
-[SBTransientOverlayPresenting hasVisibleStatusBar];
-[SBTransientOverlayPresenting shouldDisableSiri];
-[SBTransientOverlayPresenting topmostViewControllerInterfaceOrientation];
-[SBTransientOverlayPresenting addObserver:];
-[SBTransientOverlayPresenting shouldDisableControlCenter];
-[SBTransientOverlayPresenting viewControllerForGestureDismissal];
-[SBTransientOverlayPresenting preferredWhitePointAdaptivityStyleValue];
-[SBTransientOverlayPresenting preferredGestureDismissalStyle];
-[SBTransientOverlayPresenting currentStatusBarStyleRequest];
-[SBTransientOverlayPresenting canHandleButtonEvents];
-[SBTransientOverlayPresenting topmostWindowLevel];
-[SBTransientOverlayPresenting setFluidDismissalState:forViewController:];
-[SBTransientOverlayPresenting windowScene];
-[SBTransientOverlayPresenting systemModalAlertVisibilityDidChange];
```
