# `CAMZoomSlider`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISlider`
- 11 instance variables, 12 properties, 53 instance methods, 1 class methods

## Instance variables

```
B _minimumAutozooming;
B _maximumAutozooming;
B _visibilityTimerSuspended;
B __autozooming;
q _layoutStyle;
@"<CAMZoomSliderDelegate>" _delegate;
q _orientation;
@"NSTimer" __visibilityTimer;
@"UIView" __minTrackMaskView;
@"UIView" __maxTrackMaskView;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
```

## Properties

```
@property (T@"NSTimer",R,N,V__visibilityTimer) _visibilityTimer;
@property (TB,N,G_isAutozooming,S_setAutozooming:,V__autozooming) _autozooming;
@property (TB,N,GisMinimumAutozooming,S_setMinimumAutozooming:,V_minimumAutozooming) minimumAutozooming;
@property (TB,N,GisMaximumAutozooming,S_setMaximumAutozooming:,V_maximumAutozooming) maximumAutozooming;
@property (T@"UIView",R,N,V__minTrackMaskView) _minTrackMaskView;
@property (T@"UIView",R,N,V__maxTrackMaskView) _maxTrackMaskView;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (T@"<CAMZoomSliderDelegate>",W,N,V_delegate) delegate;
@property (T{UIEdgeInsets=dddd},N,V_alignmentRectInsets) alignmentRectInsets;
@property (TB,R,N,GisAutozooming) autozooming;
@property (TB,N,GisVisibilityTimerSuspended,V_visibilityTimerSuspended) visibilityTimerSuspended;
@property (Tq,N,V_orientation) orientation;
```

## Class methods

```
+[CAMZoomSlider shouldFadeOutZoomSliderForLayoutStyle:];
```

## Instance methods

```
-[CAMZoomSlider setLayoutStyle:];
-[CAMZoomSlider setOrientation:animated:];
-[CAMZoomSlider setOrientation:];
-[CAMZoomSlider layoutStyle];
-[CAMZoomSlider minimumValueImageRectForBounds:];
-[CAMZoomSlider intrinsicContentSize];
-[CAMZoomSlider alignmentRectInsets];
-[CAMZoomSlider initWithLayoutStyle:];
-[CAMZoomSlider cancelTrackingWithEvent:];
-[CAMZoomSlider endTrackingWithTouch:withEvent:];
-[CAMZoomSlider orientation];
-[CAMZoomSlider continueTrackingWithTouch:withEvent:];
-[CAMZoomSlider dealloc];
-[CAMZoomSlider layoutSubviews];
-[CAMZoomSlider beginTrackingWithTouch:withEvent:];
-[CAMZoomSlider setDelegate:];
-[CAMZoomSlider maximumValueImageRectForBounds:];
-[CAMZoomSlider delegate];
-[CAMZoomSlider thumbRectForBounds:trackRect:value:];
-[CAMZoomSlider setAlignmentRectInsets:];
-[CAMZoomSlider initWithCoder:];
-[CAMZoomSlider trackRectForBounds:];
-[CAMZoomSlider initWithFrame:];
-[CAMZoomSlider _hideZoomSlider:];
-[CAMZoomSlider _endAutozooming];
-[CAMZoomSlider _beginAutozooming];
-[CAMZoomSlider _commonCAMZoomSliderInitializationWithLayoutStyle:];
-[CAMZoomSlider _handleTouchUpInside:];
-[CAMZoomSlider _isAutozooming];
-[CAMZoomSlider _makeInvisibleAnimationDuration:];
-[CAMZoomSlider _maxTrackMaskView];
-[CAMZoomSlider _minTrackMaskView];
-[CAMZoomSlider _setAutozooming:];
-[CAMZoomSlider _setMaximumAutozooming:];
-[CAMZoomSlider _setMinimumAutozooming:];
-[CAMZoomSlider _startVisibilityTimer];
-[CAMZoomSlider _stopVisibilityTimer];
-[CAMZoomSlider _thumbCenterMaximumXForTrackRect:];
-[CAMZoomSlider _thumbCenterMinimumXForTrackRect:];
-[CAMZoomSlider _thumbCenterXForValue:trackRect:];
-[CAMZoomSlider _updateAutozooming];
-[CAMZoomSlider _updateForLayoutStyle];
-[CAMZoomSlider _valueForThumbCenterX:trackRect:];
-[CAMZoomSlider _visibilityTimer];
-[CAMZoomSlider isAutozooming];
-[CAMZoomSlider isMaximumAutozooming];
-[CAMZoomSlider isMinimumAutozooming];
-[CAMZoomSlider isVisibilityTimerSuspended];
-[CAMZoomSlider locationOfTouch:];
-[CAMZoomSlider makeInvisibleAnimated:];
-[CAMZoomSlider makeVisibleAnimated:];
-[CAMZoomSlider setVisibilityTimerSuspended:];
-[CAMZoomSlider shouldHideForExpiredVisibilityTimer];
```
