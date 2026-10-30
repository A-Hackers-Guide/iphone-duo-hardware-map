# `PKPencilShadowView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKRendererVSyncControllerDelegate`
- 32 instance variables, 7 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"CAMetalLayer" _metalLayer;
d _targetOpacity;
d _currentOpacity;
@"PKMetalPencilShadowRenderer" _shadowRenderer;
@"NSObject<OS_dispatch_queue>" _renderQueue;
d _contentScale;
{CGSize="width"d"height"d} _viewSize;
d _minimumFrameDuration;
d _shadowAlpha;
@"NSTimer" _idleTimer;
d _latestKeepVisibleTimestamp;
d _animatingInkBeginTimestamp;
B _animatingInk;
@"PKInk" _animatingInkOld;
@"PKInk" _animatingInkNew;
@"PKTiledView" _keepVisibleInTiledView;
B _keepAlwaysVisible;
B _updateCyclePaused;
B _shouldSkipCurrentFrame;
q _presentationCount;
^{_UIUpdateSequenceItemInternal=} _commitItem;
^{_UIUpdateSequenceItemInternal=} _vsyncItem;
B _useVSyncController;
@"PKRendererVSyncController" _currentVSyncController;
Ad _skipRendersUntilTime;
d _altitude;
d _azimuth;
d _rollAngle;
d _zPosition;
@"PKInk" _ink;
d _shadowAlphaMultiplier;
{CGPoint="x"d"y"d} _location;
```

## Properties

```
@property (Td,N,V_altitude) altitude;
@property (Td,N,V_azimuth) azimuth;
@property (Td,N,V_rollAngle) rollAngle;
@property (T{CGPoint=dd},N,V_location) location;
@property (Td,N,V_zPosition) zPosition;
@property (T@"PKInk",&,N,V_ink) ink;
@property (Td,N,V_shadowAlphaMultiplier) shadowAlphaMultiplier;
```

## Class methods

```
+[PKPencilShadowView createShadowViewForSceneIfNecessary:];
+[PKPencilShadowView hideShadowViewForSceneIfNecessary:];
+[PKPencilShadowView shadowViewForScene:];
```

## Instance methods

```
-[PKPencilShadowView didMoveToWindow];
-[PKPencilShadowView setRollAngle:];
-[PKPencilShadowView location];
-[PKPencilShadowView altitude];
-[PKPencilShadowView dealloc];
-[PKPencilShadowView layoutSubviews];
-[PKPencilShadowView setAltitude:];
-[PKPencilShadowView setLocation:];
-[PKPencilShadowView ink];
-[PKPencilShadowView rollAngle];
-[PKPencilShadowView setZPosition:];
-[PKPencilShadowView setInk:];
-[PKPencilShadowView didMoveToSuperview];
-[PKPencilShadowView initWithFrame:];
-[PKPencilShadowView zPosition];
-[PKPencilShadowView azimuth];
-[PKPencilShadowView setAzimuth:];
-[PKPencilShadowView hideShadow];
-[PKPencilShadowView keepAlwaysVisible];
-[PKPencilShadowView keepVisibleInTiledView:];
-[PKPencilShadowView setShadowAlphaMultiplier:];
-[PKPencilShadowView shadowAlphaMultiplier];
-[PKPencilShadowView signalVSyncSemaphore:presentationTime:];
-[PKPencilShadowView strokeBegan];
-[PKPencilShadowView updateInk:animated:];
-[PKPencilShadowView updateOpacity:animated:];
```
