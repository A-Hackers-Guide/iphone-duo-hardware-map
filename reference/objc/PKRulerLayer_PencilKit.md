# `PKRulerLayer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `UIGestureRecognizerDelegate`
- 22 instance variables, 27 properties, 77 instance methods, 0 class methods

## Instance variables

```
B _isInlineResizing;
B _isExpandedInline;
B _isRulerDrawingMovingToEndOfRuler;
B _zooming;
@"PKRulerController" _rulerController;
d _rulerAlpha;
@"CALayer" _rulerAngleMarker;
@"NSTimer" _imageTransformTimer;
d _initialDrawingBoundsYOrigin;
@"CALayer" _rulerLayer;
@"CALayer" _rulerAngleTick;
@"CATextLayer" _rulerAngleText;
@"CALayer" _rulerDistanceHUD;
@"CATextLayer" _rulerDistanceText;
d _currentTValueForSnappedDrawing;
d _minTValueForSnappedDrawing;
d _maxTValueForSnappedDrawing;
d _originTValueForSnappedDrawing;
d _rulerZoomStartCenterTValueOnScreen;
d _rulerZoomStartScale;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _previousRulerTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _rulerZoomStartTransform;
```

## Properties

```
@property (T@"NSTimer",&,N,V_imageTransformTimer) imageTransformTimer;
@property (Td,N,V_initialDrawingBoundsYOrigin) initialDrawingBoundsYOrigin;
@property (TB,N,V_isInlineResizing) isInlineResizing;
@property (TB,N,V_isExpandedInline) isExpandedInline;
@property (T@"CALayer",&,N,V_rulerLayer) rulerLayer;
@property (T{CGAffineTransform=dddddd},N) rulerTransform;
@property (T{CGAffineTransform=dddddd},N,V_previousRulerTransform) previousRulerTransform;
@property (T@"CALayer",&,N,V_rulerAngleTick) rulerAngleTick;
@property (T@"CATextLayer",&,N,V_rulerAngleText) rulerAngleText;
@property (T@"CALayer",&,N,V_rulerDistanceHUD) rulerDistanceHUD;
@property (T@"CATextLayer",&,N,V_rulerDistanceText) rulerDistanceText;
@property (TB,N,V_isRulerDrawingMovingToEndOfRuler) isRulerDrawingMovingToEndOfRuler;
@property (Td,N,V_currentTValueForSnappedDrawing) currentTValueForSnappedDrawing;
@property (Td,N,V_minTValueForSnappedDrawing) minTValueForSnappedDrawing;
@property (Td,N,V_maxTValueForSnappedDrawing) maxTValueForSnappedDrawing;
@property (Td,N,V_originTValueForSnappedDrawing) originTValueForSnappedDrawing;
@property (Td,N,V_rulerZoomStartCenterTValueOnScreen) rulerZoomStartCenterTValueOnScreen;
@property (Td,N,V_rulerZoomStartScale) rulerZoomStartScale;
@property (T{CGAffineTransform=dddddd},N,V_rulerZoomStartTransform) rulerZoomStartTransform;
@property (TB,N,V_zooming) zooming;
@property (T@"PKRulerController",W,N,V_rulerController) rulerController;
@property (Td,N,V_rulerAlpha) rulerAlpha;
@property (T@"CALayer",&,N,V_rulerAngleMarker) rulerAngleMarker;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKRulerLayer rulerController];
-[PKRulerLayer animationDidStop:finished:];
-[PKRulerLayer setZooming:];
-[PKRulerLayer setRulerController:];
-[PKRulerLayer currentAngle];
-[PKRulerLayer rulerAlignInset];
-[PKRulerLayer setInitialDrawingBoundsYOrigin:];
-[PKRulerLayer zooming];
-[PKRulerLayer _distanceMarkerFontSize];
-[PKRulerLayer _fontSizeForRulerTextHUD:];
-[PKRulerLayer _rulerImage];
-[PKRulerLayer _textForRulerHUD:];
-[PKRulerLayer addOpacityAnimationOnLayer:delegate:toOpacity:];
-[PKRulerLayer addScaleAndOpacityAnimationOnLayer:delegate:fromScale:toScale:fromAlpha:toAlpha:];
-[PKRulerLayer addScaleAnimationOnLayer:delegate:fromScale:toScale:];
-[PKRulerLayer compactRuler];
-[PKRulerLayer currentTValueForSnappedDrawing];
-[PKRulerLayer getRulerCenterLineOriginAndTangent:];
-[PKRulerLayer hideRulerAngleMarker];
-[PKRulerLayer hideRulerAnimated:];
-[PKRulerLayer imageTransformTimer];
-[PKRulerLayer initWithRulerController:];
-[PKRulerLayer initialDrawingBoundsYOrigin];
-[PKRulerLayer isExpandedInline];
-[PKRulerLayer isInlineResizing];
-[PKRulerLayer isRulerDrawingMovingToEndOfRuler];
-[PKRulerLayer maxTValueForSnappedDrawing];
-[PKRulerLayer minTValueForSnappedDrawing];
-[PKRulerLayer originTValueForSnappedDrawing];
-[PKRulerLayer previousRulerTransform];
-[PKRulerLayer removeRulerMarkers];
-[PKRulerLayer rulerAlpha];
-[PKRulerLayer rulerAngleMarker];
-[PKRulerLayer rulerAngleText];
-[PKRulerLayer rulerAngleTick];
-[PKRulerLayer rulerDialImage];
-[PKRulerLayer rulerDialLevelImage];
-[PKRulerLayer rulerDistanceHUD];
-[PKRulerLayer rulerDistanceText];
-[PKRulerLayer rulerLayer];
-[PKRulerLayer rulerTickMarkInset];
-[PKRulerLayer rulerTransform];
-[PKRulerLayer rulerWidth];
-[PKRulerLayer rulerZoomStartCenterTValueOnScreen];
-[PKRulerLayer rulerZoomStartScale];
-[PKRulerLayer rulerZoomStartTransform];
-[PKRulerLayer setCurrentTValueForSnappedDrawing:];
-[PKRulerLayer setImageTransformFrom:toTransform:animated:duration:];
-[PKRulerLayer setImageTransformTimer:];
-[PKRulerLayer setIsExpandedInline:];
-[PKRulerLayer setIsInlineResizing:];
-[PKRulerLayer setIsRulerDrawingMovingToEndOfRuler:];
-[PKRulerLayer setMaxTValueForSnappedDrawing:];
-[PKRulerLayer setMinTValueForSnappedDrawing:];
-[PKRulerLayer setOriginTValueForSnappedDrawing:];
-[PKRulerLayer setPreviousRulerTransform:];
-[PKRulerLayer setRulerAlpha:];
-[PKRulerLayer setRulerAngleMarker:];
-[PKRulerLayer setRulerAngleText:];
-[PKRulerLayer setRulerAngleTick:];
-[PKRulerLayer setRulerDistanceHUD:];
-[PKRulerLayer setRulerDistanceText:];
-[PKRulerLayer setRulerLayer:];
-[PKRulerLayer setRulerTransform:];
-[PKRulerLayer setRulerZoomStartCenterTValueOnScreen:];
-[PKRulerLayer setRulerZoomStartScale:];
-[PKRulerLayer setRulerZoomStartTransform:];
-[PKRulerLayer shouldUseLargestRulerTextFontSize];
-[PKRulerLayer showRuler];
-[PKRulerLayer updateAngleWithAngleMarkerPosition:];
-[PKRulerLayer updateDistanceMarkerWithSpacing:];
-[PKRulerLayer updateImageTransform:];
-[PKRulerLayer updateRulerAlpha:];
-[PKRulerLayer updateRulerMarkerForLocation:firstTouch:];
-[PKRulerLayer updateRulerTickMarkImage];
-[PKRulerLayer userAngle];
-[PKRulerLayer viewPointInRuler:];
```
