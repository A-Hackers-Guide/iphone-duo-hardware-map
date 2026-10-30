# `SBSwitcherAnimationAttributes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 28 instance variables, 28 properties, 59 instance methods, 0 class methods

## Instance variables

```
q _updateMode;
@"SBFFluidBehaviorSettings" _layoutSettings;
@"SBFFluidBehaviorSettings" _positionSettings;
@"SBFFluidBehaviorSettings" _scaleSettings;
@"SBFFluidBehaviorSettings" _opacitySettings;
@"SBFFluidBehaviorSettings" _cornerRadiusSettings;
@"SBFFluidBehaviorSettings" _clippingSettings;
@"SBFFluidBehaviorSettings" _meshSettings;
@"SBFFluidBehaviorSettings" _dropletPositionXSettings;
@"SBFFluidBehaviorSettings" _dropletPositionYSettings;
@"SBFFluidBehaviorSettings" _pillScaleSettings;
@"SBFFluidBehaviorSettings" _pillScaleYSettings;
@"SBFFluidBehaviorSettings" _pillOffsetSettings;
@"SBFFluidBehaviorSettings" _bouncePositionSettings;
@"SBFFluidBehaviorSettings" _bounceScaleSettings;
@"SBFFluidBehaviorSettings" _pillContentAlphaSettings;
@"SBFFluidBehaviorSettings" _pillContentScaleSettings;
@"SBFFluidBehaviorSettings" _pillContentScaleYSettings;
@"SBFFluidBehaviorSettings" _pillContentBlurSettings;
@"SBFFluidBehaviorSettings" _pillMaterializationSettings;
q _layoutUpdateMode;
q _positionUpdateMode;
q _scaleUpdateMode;
q _opacityUpdateMode;
q _cornerRadiusUpdateMode;
q _clippingUpdateMode;
q _titleAndIconOpacityUpdateMode;
q _meshUpdateMode;
```

## Properties

```
@property (Tq,N,V_updateMode) updateMode;
@property (T@"SBFFluidBehaviorSettings",&,N,V_layoutSettings) layoutSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_positionSettings) positionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_scaleSettings) scaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_opacitySettings) opacitySettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_cornerRadiusSettings) cornerRadiusSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_clippingSettings) clippingSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_meshSettings) meshSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dropletPositionXSettings) dropletPositionXSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dropletPositionYSettings) dropletPositionYSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillScaleSettings) pillScaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillScaleYSettings) pillScaleYSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillOffsetSettings) pillOffsetSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_bouncePositionSettings) bouncePositionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_bounceScaleSettings) bounceScaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillContentAlphaSettings) pillContentAlphaSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillContentScaleSettings) pillContentScaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillContentScaleYSettings) pillContentScaleYSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillContentBlurSettings) pillContentBlurSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_pillMaterializationSettings) pillMaterializationSettings;
@property (Tq,N,V_layoutUpdateMode) layoutUpdateMode;
@property (Tq,N,V_positionUpdateMode) positionUpdateMode;
@property (Tq,N,V_scaleUpdateMode) scaleUpdateMode;
@property (Tq,N,V_opacityUpdateMode) opacityUpdateMode;
@property (Tq,N,V_cornerRadiusUpdateMode) cornerRadiusUpdateMode;
@property (Tq,N,V_clippingUpdateMode) clippingUpdateMode;
@property (Tq,N,V_titleAndIconOpacityUpdateMode) titleAndIconOpacityUpdateMode;
@property (Tq,N,V_meshUpdateMode) meshUpdateMode;
```

## Instance methods

```
-[SBSwitcherAnimationAttributes mutableCopyWithZone:];
-[SBSwitcherAnimationAttributes opacitySettings];
-[SBSwitcherAnimationAttributes updateMode];
-[SBSwitcherAnimationAttributes scaleSettings];
-[SBSwitcherAnimationAttributes setScaleSettings:];
-[SBSwitcherAnimationAttributes setOpacitySettings:];
-[SBSwitcherAnimationAttributes setLayoutSettings:];
-[SBSwitcherAnimationAttributes copyWithZone:];
-[SBSwitcherAnimationAttributes layoutSettings];
-[SBSwitcherAnimationAttributes setUpdateMode:];
-[SBSwitcherAnimationAttributes _copyWithClass:];
-[SBSwitcherAnimationAttributes setPillMaterializationSettings:];
-[SBSwitcherAnimationAttributes scaleUpdateMode];
-[SBSwitcherAnimationAttributes bouncePositionSettings];
-[SBSwitcherAnimationAttributes bounceScaleSettings];
-[SBSwitcherAnimationAttributes clippingSettings];
-[SBSwitcherAnimationAttributes clippingUpdateMode];
-[SBSwitcherAnimationAttributes cornerRadiusSettings];
-[SBSwitcherAnimationAttributes cornerRadiusUpdateMode];
-[SBSwitcherAnimationAttributes dropletPositionXSettings];
-[SBSwitcherAnimationAttributes dropletPositionYSettings];
-[SBSwitcherAnimationAttributes layoutUpdateMode];
-[SBSwitcherAnimationAttributes meshSettings];
-[SBSwitcherAnimationAttributes meshUpdateMode];
-[SBSwitcherAnimationAttributes opacityUpdateMode];
-[SBSwitcherAnimationAttributes pillContentAlphaSettings];
-[SBSwitcherAnimationAttributes pillContentBlurSettings];
-[SBSwitcherAnimationAttributes pillContentScaleSettings];
-[SBSwitcherAnimationAttributes pillContentScaleYSettings];
-[SBSwitcherAnimationAttributes pillMaterializationSettings];
-[SBSwitcherAnimationAttributes pillOffsetSettings];
-[SBSwitcherAnimationAttributes pillScaleSettings];
-[SBSwitcherAnimationAttributes pillScaleYSettings];
-[SBSwitcherAnimationAttributes positionSettings];
-[SBSwitcherAnimationAttributes positionUpdateMode];
-[SBSwitcherAnimationAttributes setBouncePositionSettings:];
-[SBSwitcherAnimationAttributes setBounceScaleSettings:];
-[SBSwitcherAnimationAttributes setClippingSettings:];
-[SBSwitcherAnimationAttributes setClippingUpdateMode:];
-[SBSwitcherAnimationAttributes setCornerRadiusSettings:];
-[SBSwitcherAnimationAttributes setCornerRadiusUpdateMode:];
-[SBSwitcherAnimationAttributes setDropletPositionXSettings:];
-[SBSwitcherAnimationAttributes setDropletPositionYSettings:];
-[SBSwitcherAnimationAttributes setLayoutUpdateMode:];
-[SBSwitcherAnimationAttributes setMeshSettings:];
-[SBSwitcherAnimationAttributes setMeshUpdateMode:];
-[SBSwitcherAnimationAttributes setOpacityUpdateMode:];
-[SBSwitcherAnimationAttributes setPillContentAlphaSettings:];
-[SBSwitcherAnimationAttributes setPillContentBlurSettings:];
-[SBSwitcherAnimationAttributes setPillContentScaleSettings:];
-[SBSwitcherAnimationAttributes setPillContentScaleYSettings:];
-[SBSwitcherAnimationAttributes setPillOffsetSettings:];
-[SBSwitcherAnimationAttributes setPillScaleSettings:];
-[SBSwitcherAnimationAttributes setPillScaleYSettings:];
-[SBSwitcherAnimationAttributes setPositionSettings:];
-[SBSwitcherAnimationAttributes setPositionUpdateMode:];
-[SBSwitcherAnimationAttributes setScaleUpdateMode:];
-[SBSwitcherAnimationAttributes setTitleAndIconOpacityUpdateMode:];
-[SBSwitcherAnimationAttributes titleAndIconOpacityUpdateMode];
```
