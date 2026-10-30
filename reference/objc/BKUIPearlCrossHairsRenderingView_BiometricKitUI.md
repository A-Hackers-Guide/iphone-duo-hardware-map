# `BKUIPearlCrossHairsRenderingView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTKView`
- 13 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _inFlightSemaphore;
@"<MTLCommandQueue>" _commandQueue;
d _time;
f _pathBlend;
f _pathBlendDest;
Q _state;
@"MTLSAnimatablePathCollection" _crosshairsPathCollection;
@"BKUIPearlCrossHairsManager" _crosshairsInstanceManager;
@"MTLSPathBufferData" _crosshairsData;
@"MTLSAnimatablePathCollection" _checkMarkPathCollection;
@"MTLSPathBufferData" _checkMarkData;
@"MTLSplineRenderer" _renderer;
_axis;
```

## Properties

```
@property (TQ,N,V_state) state;
@property (T,V_axis) axis;
@property (T@"MTLSAnimatablePathCollection",&,V_crosshairsPathCollection) crosshairsPathCollection;
@property (T@"BKUIPearlCrossHairsManager",&,V_crosshairsInstanceManager) crosshairsInstanceManager;
@property (T@"MTLSPathBufferData",&,V_crosshairsData) crosshairsData;
@property (T@"MTLSAnimatablePathCollection",&,V_checkMarkPathCollection) checkMarkPathCollection;
@property (T@"MTLSPathBufferData",&,V_checkMarkData) checkMarkData;
@property (T@"MTLSplineRenderer",&,V_renderer) renderer;
@property (TB,N) grayscale;
```

## Instance methods

```
-[BKUIPearlCrossHairsRenderingView axis];
-[BKUIPearlCrossHairsRenderingView setGrayscale:];
-[BKUIPearlCrossHairsRenderingView setState:];
-[BKUIPearlCrossHairsRenderingView renderer];
-[BKUIPearlCrossHairsRenderingView setAxis:];
-[BKUIPearlCrossHairsRenderingView setSampleCount:];
-[BKUIPearlCrossHairsRenderingView drawRect:];
-[BKUIPearlCrossHairsRenderingView grayscale];
-[BKUIPearlCrossHairsRenderingView setRenderer:];
-[BKUIPearlCrossHairsRenderingView getState];
-[BKUIPearlCrossHairsRenderingView state];
-[BKUIPearlCrossHairsRenderingView initWithFrame:device:];
-[BKUIPearlCrossHairsRenderingView checkMarkData];
-[BKUIPearlCrossHairsRenderingView checkMarkPathCollection];
-[BKUIPearlCrossHairsRenderingView crosshairsData];
-[BKUIPearlCrossHairsRenderingView crosshairsInstanceManager];
-[BKUIPearlCrossHairsRenderingView crosshairsPathCollection];
-[BKUIPearlCrossHairsRenderingView setAxis:animated:];
-[BKUIPearlCrossHairsRenderingView setCheckMarkData:];
-[BKUIPearlCrossHairsRenderingView setCheckMarkPathCollection:];
-[BKUIPearlCrossHairsRenderingView setCrosshairsData:];
-[BKUIPearlCrossHairsRenderingView setCrosshairsInstanceManager:];
-[BKUIPearlCrossHairsRenderingView setCrosshairsPathCollection:];
```
