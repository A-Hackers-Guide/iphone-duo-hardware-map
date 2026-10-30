# `CAMTimelapseShutterRingView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _animating;
d __smallTickRotationRadians;
d __largeTickRotationRadians;
@"CALayer" __smallTickLayer;
@"CALayer" __largeTickLayer;
@"CAReplicatorLayer" __smallTickReplicatorLayer;
@"CAReplicatorLayer" __largeTickReplicatorLayer;
@"CALayer" __timerHandLayer;
@"CALayer" __timerHandParentLayer;
{?="smallTickCount"q"largeTickCount"q"smallTickLength"d"largeTickLength"d} _spec;
```

## Properties

```
@property (Td,R,N,V__smallTickRotationRadians) _smallTickRotationRadians;
@property (Td,R,N,V__largeTickRotationRadians) _largeTickRotationRadians;
@property (T@"CALayer",R,N,V__smallTickLayer) _smallTickLayer;
@property (T@"CALayer",R,N,V__largeTickLayer) _largeTickLayer;
@property (T@"CAReplicatorLayer",R,N,V__smallTickReplicatorLayer) _smallTickReplicatorLayer;
@property (T@"CAReplicatorLayer",R,N,V__largeTickReplicatorLayer) _largeTickReplicatorLayer;
@property (T@"CALayer",R,N,V__timerHandLayer) _timerHandLayer;
@property (T@"CALayer",R,N,V__timerHandParentLayer) _timerHandParentLayer;
@property (T{?=qqdd},R,N,V_spec) spec;
@property (TB,N,GisAnimating,V_animating) animating;
```

## Instance methods

```
-[CAMTimelapseShutterRingView setSpec:];
-[CAMTimelapseShutterRingView layoutSublayersOfLayer:];
-[CAMTimelapseShutterRingView initWithSpec:];
-[CAMTimelapseShutterRingView spec];
-[CAMTimelapseShutterRingView isAnimating];
-[CAMTimelapseShutterRingView setAnimating:];
-[CAMTimelapseShutterRingView _startAnimating];
-[CAMTimelapseShutterRingView _stopAnimating];
-[CAMTimelapseShutterRingView _shouldUseAnimations];
-[CAMTimelapseShutterRingView _timerHandLayer];
-[CAMTimelapseShutterRingView _largeTickLayer];
-[CAMTimelapseShutterRingView _smallTickLayer];
-[CAMTimelapseShutterRingView _addStartAnimations];
-[CAMTimelapseShutterRingView _addStopAnimations];
-[CAMTimelapseShutterRingView _commonCAMTimelapseShutterRingViewInitializationWithSpec:];
-[CAMTimelapseShutterRingView _largeTickReplicatorLayer];
-[CAMTimelapseShutterRingView _largeTickRotationRadians];
-[CAMTimelapseShutterRingView _removeStartAnimations];
-[CAMTimelapseShutterRingView _removeStopAnimations];
-[CAMTimelapseShutterRingView _rotationRadiansFromTickCount:];
-[CAMTimelapseShutterRingView _rotationZFromTransform:];
-[CAMTimelapseShutterRingView _smallTickReplicatorLayer];
-[CAMTimelapseShutterRingView _smallTickRotationRadians];
-[CAMTimelapseShutterRingView _tickRadiusForTickSize:ringSize:];
-[CAMTimelapseShutterRingView _timerHandParentLayer];
-[CAMTimelapseShutterRingView initWithFrame:spec:];
```
