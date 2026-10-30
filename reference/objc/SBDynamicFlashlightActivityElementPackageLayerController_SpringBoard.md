# `SBDynamicFlashlightActivityElementPackageLayerController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"BSUICAPackageView" _packageView;
@"CALayer" _shadowLayer;
@"CAPortalLayer" _shadowPortalLayer;
@"CALayer" _indicatorLayer;
@"CALayer" _circleLayer;
@"CALayer" _arcCropLeftLayer;
@"CALayer" _arcCropRightLayer;
@"CALayer" _tickLineLayer;
@"CAReplicatorLayer" _ticksRingLayer;
@"CALayer" _glyphHolderLayer;
@"CALayer" _glyphLayer;
@"CALayer" _maskContentsLayer;
@"CALayer" _wideRainbowLayer;
@"CALayer" _rainbowLeftLayer;
@"CALayer" _rainbowRightLayer;
@"CALayer" _spreadBeamImageLayer;
@"CALayer" _straightBeamImageLayer;
@"CALayer" _circleFlaresShifterLayer;
@"CALayer" _spreadBeamDimmerLayer;
@"CALayer" _straightBeamDimmerLayer;
@"CALayer" _rainbowLeftdimmerLayer;
@"CALayer" _rainbowRightdimmerLayer;
@"CALayer" _flashlightImageLayer;
@"CALayer" _wideRainbowDimmerLayer;
@"CALayer" _middleGlowDimmerLayer;
@"NSString" _maxLineState;
@"NSString" _touchingState;
```

## Instance methods

```
-[SBDynamicFlashlightActivityElementPackageLayerController initWithPackageView:];
-[SBDynamicFlashlightActivityElementPackageLayerController sensorShadowPortalLayer];
-[SBDynamicFlashlightActivityElementPackageLayerController setBeamIntensity:width:animated:];
-[SBDynamicFlashlightActivityElementPackageLayerController setTouching:animated:];
-[SBDynamicFlashlightActivityElementPackageLayerController updateBeamLayersForIntensity:width:animated:];
-[SBDynamicFlashlightActivityElementPackageLayerController updateIndicatorLayersForIntensity:width:animated:];
```
