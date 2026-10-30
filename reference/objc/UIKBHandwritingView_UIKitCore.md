# `UIKBHandwritingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKBKeyView`
- Protocols: `UIGestureRecognizerDelegate`
- 18 instance variables, 22 properties, 68 instance methods, 0 class methods

## Instance variables

```
B _initialPointPosted;
d _inkWidth;
^{CGColor=} _inkColor;
^{CGImage=} _inkMask;
@"NSMutableArray" _interpolatedPoints;
@"UIBezierPath" _currentPath;
@"NSMutableArray" _currentPoints;
@"UIKBHandwritingStrokePointFIFO" _strokeFIFO;
@"UIKBHandwritingBoxcarFilterPointFIFO" _smoothingFIFO;
@"UIKBHandwritingQuadCurvePointFIFO" _interpolatingFIFO;
@"UIKBHandwritingBezierPathPointFIFO" _bezierPathFIFO;
@"UIKBHandwritingStrokeView" _strokeView;
@"UIView" _snapshotView;
@"NSMutableSet" _activeTouches;
d _pageOffset;
@"UIDelayedAction" _nextPageTimer;
@"UIKBHandwritingInputSpeedModel" _inputSpeedModel;
{?="point"{CGPoint="x"d"y"d}"force"d} _previousPoint;
```

## Properties

```
@property (T@"UIKBHandwritingStrokeView",&,N,V_strokeView) strokeView;
@property (T@"UIView",&,N,V_snapshotView) snapshotView;
@property (T@"NSMutableSet",&,N,V_activeTouches) activeTouches;
@property (TB,N,V_initialPointPosted) initialPointPosted;
@property (T{?={CGPoint=dd}d},N,V_previousPoint) previousPoint;
@property (Td,N,V_pageOffset) pageOffset;
@property (T@"UIDelayedAction",&,N,V_nextPageTimer) nextPageTimer;
@property (T@"UIKBHandwritingInputSpeedModel",&,N,V_inputSpeedModel) inputSpeedModel;
@property (Td,N,V_inkWidth) inkWidth;
@property (T^{CGColor=},N,V_inkColor) inkColor;
@property (T^{CGImage=},N,V_inkMask) inkMask;
@property (T@"NSMutableArray",&,N,V_interpolatedPoints) interpolatedPoints;
@property (T@"UIBezierPath",&,N,V_currentPath) currentPath;
@property (T@"NSMutableArray",&,N,V_currentPoints) currentPoints;
@property (T@"UIKBHandwritingStrokePointFIFO",&,N,V_strokeFIFO) strokeFIFO;
@property (T@"UIKBHandwritingBoxcarFilterPointFIFO",&,N,V_smoothingFIFO) smoothingFIFO;
@property (T@"UIKBHandwritingQuadCurvePointFIFO",&,N,V_interpolatingFIFO) interpolatingFIFO;
@property (T@"UIKBHandwritingBezierPathPointFIFO",&,N,V_bezierPathFIFO) bezierPathFIFO;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBHandwritingView snapshotView];
-[UIKBHandwritingView cancelTouchTracking];
-[UIKBHandwritingView touchesEnded:withEvent:];
-[UIKBHandwritingView send];
-[UIKBHandwritingView setPreviousPoint:];
-[UIKBHandwritingView layerForRenderFlags:];
-[UIKBHandwritingView didMoveToWindow];
-[UIKBHandwritingView setActiveTouches:];
-[UIKBHandwritingView initWithFrame:keyplane:key:];
-[UIKBHandwritingView touchesCancelled:withEvent:];
-[UIKBHandwritingView setRenderConfig:];
-[UIKBHandwritingView displayLayer:];
-[UIKBHandwritingView updateForKeyplane:key:];
-[UIKBHandwritingView clearTouches];
-[UIKBHandwritingView previousPoint];
-[UIKBHandwritingView dealloc];
-[UIKBHandwritingView layoutSubviews];
-[UIKBHandwritingView setSnapshotView:];
-[UIKBHandwritingView touchesBegan:withEvent:];
-[UIKBHandwritingView touchesMoved:withEvent:];
-[UIKBHandwritingView activeTouches];
-[UIKBHandwritingView log];
-[UIKBHandwritingView pointInside:withEvent:];
-[UIKBHandwritingView setCurrentPath:];
-[UIKBHandwritingView currentPath];
-[UIKBHandwritingView _kb_keyFrameCoordinateSpaceView];
-[UIKBHandwritingView clearAndNotify:];
-[UIKBHandwritingView inkMask];
-[UIKBHandwritingView inputSpeedModel];
-[UIKBHandwritingView numberOfStrokes];
-[UIKBHandwritingView addInkPoint:value:];
-[UIKBHandwritingView bezierPathFIFO];
-[UIKBHandwritingView cancelPageOffsetTimer];
-[UIKBHandwritingView currentPoints];
-[UIKBHandwritingView deleteStrokesAtIndexes:];
-[UIKBHandwritingView endStrokeWithTouches:event:];
-[UIKBHandwritingView initialPointPosted];
-[UIKBHandwritingView inkColor];
-[UIKBHandwritingView inkWidth];
-[UIKBHandwritingView interpolatedPoints];
-[UIKBHandwritingView interpolatingFIFO];
-[UIKBHandwritingView nextPageTimer];
-[UIKBHandwritingView pageOffset];
-[UIKBHandwritingView pageOffsetTimerFired];
-[UIKBHandwritingView recreateInkMaskIfNeeded];
-[UIKBHandwritingView setBezierPathFIFO:];
-[UIKBHandwritingView setCurrentPoints:];
-[UIKBHandwritingView setInitialPointPosted:];
-[UIKBHandwritingView setInkColor:];
-[UIKBHandwritingView setInkMask:];
-[UIKBHandwritingView setInkWidth:];
-[UIKBHandwritingView setInputSpeedModel:];
-[UIKBHandwritingView setInterpolatedPoints:];
-[UIKBHandwritingView setInterpolatingFIFO:];
-[UIKBHandwritingView setNextPageTimer:];
-[UIKBHandwritingView setPageOffset:];
-[UIKBHandwritingView setSmoothingFIFO:];
-[UIKBHandwritingView setStrokeFIFO:];
-[UIKBHandwritingView setStrokeView:];
-[UIKBHandwritingView shouldAllowSelectionGestures:];
-[UIKBHandwritingView shouldCache];
-[UIKBHandwritingView smoothingFIFO];
-[UIKBHandwritingView startFadeOutAnimation];
-[UIKBHandwritingView strokeFIFO];
-[UIKBHandwritingView strokeView];
-[UIKBHandwritingView touchPageOffsetTimer];
-[UIKBHandwritingView updateCornerRadius];
-[UIKBHandwritingView updateInkColor];
```
