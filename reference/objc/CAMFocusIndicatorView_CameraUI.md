# `CAMFocusIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 11 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _inactive;
B _showExposureBias;
f _exposureBiasMaximum;
f _exposureBiasMinimum;
f _exposureBiasValue;
i __exposureBiasSide;
q _style;
@"<CAMFocusIndicatorViewDelegate>" _delegate;
@"CAMFocusIndicatorRectView" __rectView;
@"CAMExposureBiasSlider" __exposureBiasSlider;
```

## Properties

```
@property (T@"CAMFocusIndicatorRectView",R,N,V__rectView) _rectView;
@property (T@"CAMExposureBiasSlider",R,N,V__exposureBiasSlider) _exposureBiasSlider;
@property (Ti,N,V__exposureBiasSide) _exposureBiasSide;
@property (Tq,N,V_style) style;
@property (T@"<CAMFocusIndicatorViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisInactive,V_inactive) inactive;
@property (TB,N,GisPulsing) pulsing;
@property (TB,N,V_showExposureBias) showExposureBias;
@property (Tf,N,V_exposureBiasMaximum) exposureBiasMaximum;
@property (Tf,N,V_exposureBiasMinimum) exposureBiasMinimum;
@property (Tf,N,V_exposureBiasValue) exposureBiasValue;
```

## Instance methods

```
-[CAMFocusIndicatorView setStyle:animated:completion:];
-[CAMFocusIndicatorView showExposureBias];
-[CAMFocusIndicatorView setInactive:];
-[CAMFocusIndicatorView _layoutRectView:];
-[CAMFocusIndicatorView _commonCAMFocusIndicatorViewInitialization];
-[CAMFocusIndicatorView intrinsicContentSize];
-[CAMFocusIndicatorView _exposureBiasSlider];
-[CAMFocusIndicatorView setExposureBiasMinimum:];
-[CAMFocusIndicatorView exposureBiasValue];
-[CAMFocusIndicatorView _rectView];
-[CAMFocusIndicatorView setExposureBiasValue:];
-[CAMFocusIndicatorView setCenter:];
-[CAMFocusIndicatorView layoutSubviews];
-[CAMFocusIndicatorView initWithStyle:];
-[CAMFocusIndicatorView style];
-[CAMFocusIndicatorView exposureBiasMinimum];
-[CAMFocusIndicatorView setStyle:];
-[CAMFocusIndicatorView _updateTintColor];
-[CAMFocusIndicatorView setDelegate:];
-[CAMFocusIndicatorView isPulsing];
-[CAMFocusIndicatorView setExposureBiasSide:animated:];
-[CAMFocusIndicatorView isInactive];
-[CAMFocusIndicatorView delegate];
-[CAMFocusIndicatorView _createRectViewAndUpdateBounds];
-[CAMFocusIndicatorView _layoutExposureBiasSlider];
-[CAMFocusIndicatorView _exposureBiasSide];
-[CAMFocusIndicatorView setPulsing:];
-[CAMFocusIndicatorView _createExposureBiasSlider];
-[CAMFocusIndicatorView set_exposureBiasSide:];
-[CAMFocusIndicatorView exposureBiasMaximum];
-[CAMFocusIndicatorView boundsIncludingExposureBiasSlider];
-[CAMFocusIndicatorView startScalingWithExpansionWidth:duration:repeatCount:];
-[CAMFocusIndicatorView setShowExposureBias:];
-[CAMFocusIndicatorView setExposureBiasMaximum:];
```
