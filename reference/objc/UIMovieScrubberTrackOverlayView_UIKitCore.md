# `UIMovieScrubberTrackOverlayView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
d _value;
d _minimumValue;
d _maximumValue;
d _startValue;
d _endValue;
@"UIImageView" _leftFillView;
@"UIImageView" _rightFillView;
I _editingHandle;
b1 _editing;
b1 _zoomed;
```

## Instance methods

```
-[UIMovieScrubberTrackOverlayView setMaximumValue:];
-[UIMovieScrubberTrackOverlayView layoutSubviews];
-[UIMovieScrubberTrackOverlayView setValue:];
-[UIMovieScrubberTrackOverlayView setEditing:];
-[UIMovieScrubberTrackOverlayView setMinimumValue:];
-[UIMovieScrubberTrackOverlayView initWithFrame:];
-[UIMovieScrubberTrackOverlayView _updateLeftFill];
-[UIMovieScrubberTrackOverlayView _clampValueAndLayout];
-[UIMovieScrubberTrackOverlayView _updateRightFill];
-[UIMovieScrubberTrackOverlayView animateFillFramesAway];
-[UIMovieScrubberTrackOverlayView setEditingHandle:];
-[UIMovieScrubberTrackOverlayView setEndValue:];
-[UIMovieScrubberTrackOverlayView setIsZoomed:];
-[UIMovieScrubberTrackOverlayView setStartValue:];
```
