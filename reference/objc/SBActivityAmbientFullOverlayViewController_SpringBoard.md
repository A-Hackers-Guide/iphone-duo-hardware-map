# `SBActivityAmbientFullOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityViewController`
- 4 instance variables, 6 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"PLGrabberView" _grabberView;
@"PLPlatterView" _platterView;
@"UIView" _backgroundTintView;
@"PLPlatterView" _backdropView;
```

## Properties

```
@property (T@"PLPlatterView",R,N,V_platterView) platterView;
@property (T@"UIView",R,N,V_backgroundTintView) backgroundTintView;
@property (T@"PLPlatterView",R,N,V_backdropView) backdropView;
@property (TB,R,N) requiresBackdrop;
@property (Td,R,N) cardCornerRadius;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) cardFrame;
```

## Instance methods

```
-[SBActivityAmbientFullOverlayViewController platterView];
-[SBActivityAmbientFullOverlayViewController backdropView];
-[SBActivityAmbientFullOverlayViewController _layoutSubviews];
-[SBActivityAmbientFullOverlayViewController supportedInterfaceOrientations];
-[SBActivityAmbientFullOverlayViewController viewDidLoad];
-[SBActivityAmbientFullOverlayViewController _canShowWhileLocked];
-[SBActivityAmbientFullOverlayViewController _supportsPortraitOrientation];
-[SBActivityAmbientFullOverlayViewController viewWillLayoutSubviews];
-[SBActivityAmbientFullOverlayViewController _isInnerSurface];
-[SBActivityAmbientFullOverlayViewController activityHostViewControllerBackgroundTintColorDidChange:];
-[SBActivityAmbientFullOverlayViewController backgroundTintView];
-[SBActivityAmbientFullOverlayViewController cardCornerRadius];
-[SBActivityAmbientFullOverlayViewController cardFrame];
-[SBActivityAmbientFullOverlayViewController _activityRequiresBackdrop];
-[SBActivityAmbientFullOverlayViewController _cardCornerRadius];
-[SBActivityAmbientFullOverlayViewController _cardFrameForBounds:];
-[SBActivityAmbientFullOverlayViewController _createBackdropView];
-[SBActivityAmbientFullOverlayViewController _grabberViewFrame];
-[SBActivityAmbientFullOverlayViewController _gutterAwareBackdropCornerConfigurationForRadius:];
-[SBActivityAmbientFullOverlayViewController _hasBackgroundTintColor];
-[SBActivityAmbientFullOverlayViewController _isWidgetBasedActivity];
-[SBActivityAmbientFullOverlayViewController _scaleAndCenterActivityHostViewInBounds:requiresBackdrop:];
-[SBActivityAmbientFullOverlayViewController _scaleToFitContentSize:inAvailableSize:];
-[SBActivityAmbientFullOverlayViewController _updateBackgroundTintViewWithBounds:color:];
-[SBActivityAmbientFullOverlayViewController requiresBackdrop];
```
