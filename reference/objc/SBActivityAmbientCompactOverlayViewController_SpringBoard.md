# `SBActivityAmbientCompactOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityViewController`
- 2 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<SBActivityAmbientCompactOverlayViewControllerDelegate>" _compactOverlayDelegate;
@"PLPlatterView" _platterView;
```

## Properties

```
@property (T@"PLPlatterView",R,N,V_platterView) platterView;
@property (T@"<SBActivityAmbientCompactOverlayViewControllerDelegate>",W,N,V_compactOverlayDelegate) compactOverlayDelegate;
@property (T{CGSize=dd},R,N) contentSize;
@property (Td,R,N) cornerRadius;
```

## Instance methods

```
-[SBActivityAmbientCompactOverlayViewController platterView];
-[SBActivityAmbientCompactOverlayViewController _layoutSubviews];
-[SBActivityAmbientCompactOverlayViewController supportedInterfaceOrientations];
-[SBActivityAmbientCompactOverlayViewController setBackgroundAlpha:];
-[SBActivityAmbientCompactOverlayViewController setContentAlpha:];
-[SBActivityAmbientCompactOverlayViewController viewDidLoad];
-[SBActivityAmbientCompactOverlayViewController contentSize];
-[SBActivityAmbientCompactOverlayViewController _canShowWhileLocked];
-[SBActivityAmbientCompactOverlayViewController cornerRadius];
-[SBActivityAmbientCompactOverlayViewController viewWillLayoutSubviews];
-[SBActivityAmbientCompactOverlayViewController activityHostViewController:requestsLaunchWithAction:];
-[SBActivityAmbientCompactOverlayViewController _activityContentExceedsCompactOverlaySize];
-[SBActivityAmbientCompactOverlayViewController _configureTapGesture];
-[SBActivityAmbientCompactOverlayViewController _handleTapGesture];
-[SBActivityAmbientCompactOverlayViewController _isWidgetBasedActivity];
-[SBActivityAmbientCompactOverlayViewController _resetActivityHostViewTransformIfNecessary];
-[SBActivityAmbientCompactOverlayViewController _scaleAndCenterActivityHostViewInBounds:];
-[SBActivityAmbientCompactOverlayViewController compactOverlayDelegate];
-[SBActivityAmbientCompactOverlayViewController setCompactOverlayDelegate:];
```
