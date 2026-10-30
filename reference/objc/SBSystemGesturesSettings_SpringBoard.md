# `SBSystemGesturesSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _disableSystemGestures;
d _occludedCoverSurfaceTopEdgeRegionHeight;
d _coverSurfaceTopEdgeRegionHeight;
d _innerSurfaceTopEdgeRegionHeight;
d _controlCenterStatusBarRegionScrollerGutterWidth;
d _controlCenterStatusBarRegionScrollerGutterHoldDuration;
```

## Properties

```
@property (TB,V_disableSystemGestures) disableSystemGestures;
@property (Td,N,V_occludedCoverSurfaceTopEdgeRegionHeight) occludedCoverSurfaceTopEdgeRegionHeight;
@property (Td,N,V_coverSurfaceTopEdgeRegionHeight) coverSurfaceTopEdgeRegionHeight;
@property (Td,N,V_innerSurfaceTopEdgeRegionHeight) innerSurfaceTopEdgeRegionHeight;
@property (Td,N,V_controlCenterStatusBarRegionScrollerGutterWidth) controlCenterStatusBarRegionScrollerGutterWidth;
@property (Td,N,V_controlCenterStatusBarRegionScrollerGutterHoldDuration) controlCenterStatusBarRegionScrollerGutterHoldDuration;
```

## Class methods

```
+[SBSystemGesturesSettings settingsControllerModule];
```

## Instance methods

```
-[SBSystemGesturesSettings setDefaultValues];
-[SBSystemGesturesSettings coverSurfaceTopEdgeRegionHeight];
-[SBSystemGesturesSettings innerSurfaceTopEdgeRegionHeight];
-[SBSystemGesturesSettings controlCenterStatusBarRegionScrollerGutterHoldDuration];
-[SBSystemGesturesSettings controlCenterStatusBarRegionScrollerGutterWidth];
-[SBSystemGesturesSettings disableSystemGestures];
-[SBSystemGesturesSettings occludedCoverSurfaceTopEdgeRegionHeight];
-[SBSystemGesturesSettings setControlCenterStatusBarRegionScrollerGutterHoldDuration:];
-[SBSystemGesturesSettings setControlCenterStatusBarRegionScrollerGutterWidth:];
-[SBSystemGesturesSettings setCoverSurfaceTopEdgeRegionHeight:];
-[SBSystemGesturesSettings setDisableSystemGestures:];
-[SBSystemGesturesSettings setInnerSurfaceTopEdgeRegionHeight:];
-[SBSystemGesturesSettings setOccludedCoverSurfaceTopEdgeRegionHeight:];
-[SBSystemGesturesSettings topEdgeRegionHeightForSurfaceType:occluded:];
```
