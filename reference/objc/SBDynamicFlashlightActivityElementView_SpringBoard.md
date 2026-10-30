# `SBDynamicFlashlightActivityElementView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"BSUICAPackageView" _packageView;
@"UIViewVectorAnimatableProperty" _beamState;
B _touching;
@"SBDynamicFlashlightActivityElementPackageLayerController" _layerManager;
@"CALayer" _sensorShadowLayer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sensorAreaRect;
@"<SBDynamicFlashlightOptionsProvider>" _optionsProvider;
@"NSString" _packageState;
B _isExpanded;
B _sensorShadowHidden;
```

## Properties

```
@property (TB,R,N,V_isExpanded) isExpanded;
@property (TB,N,GisTouching,V_touching) touching;
@property (TB,N,V_sensorShadowHidden) sensorShadowHidden;
```

## Instance methods

```
-[SBDynamicFlashlightActivityElementView isExpanded];
-[SBDynamicFlashlightActivityElementView layoutSubviews];
-[SBDynamicFlashlightActivityElementView isTouching];
-[SBDynamicFlashlightActivityElementView sizeThatFits:];
-[SBDynamicFlashlightActivityElementView _setupLayers];
-[SBDynamicFlashlightActivityElementView setTouching:];
-[SBDynamicFlashlightActivityElementView _transitionToCollapsedState];
-[SBDynamicFlashlightActivityElementView _transitionToExpandedStateWithIntensity:width:];
-[SBDynamicFlashlightActivityElementView _applyBeamState];
-[SBDynamicFlashlightActivityElementView _flashlightStateForWidth:intensity:];
-[SBDynamicFlashlightActivityElementView _layoutSensorShadow];
-[SBDynamicFlashlightActivityElementView _setupBeamState:];
-[SBDynamicFlashlightActivityElementView initWithBeamState:optionsProvider:];
-[SBDynamicFlashlightActivityElementView initWithFrame:beamState:optionsProvider:];
-[SBDynamicFlashlightActivityElementView sensorShadowHidden];
-[SBDynamicFlashlightActivityElementView setBeamState:];
-[SBDynamicFlashlightActivityElementView setExpanded:intensity:width:];
-[SBDynamicFlashlightActivityElementView setSensorShadowHidden:];
```
