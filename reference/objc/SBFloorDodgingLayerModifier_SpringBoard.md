# `SBFloorDodgingLayerModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDodgingModifier`
- 1 instance variables, 1 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBDodgingModel" _overridingModel;
```

## Properties

```
@property (T@"SBDodgingModel",&,N,V_overridingModel) overridingModel;
```

## Instance methods

```
-[SBFloorDodgingLayerModifier model];
-[SBFloorDodgingLayerModifier overridingModel];
-[SBFloorDodgingLayerModifier _framesForIdentifiersInModel:];
-[SBFloorDodgingLayerModifier _identifierIfAnyIllegallyClippingOtherIdentifiers:model:intersectionSize:intersectingFrame:];
-[SBFloorDodgingLayerModifier _identifierIfAnyIllegallyOutsideContentViewBounds:model:];
-[SBFloorDodgingLayerModifier _modelByClampingOverhangingIdentifiers:];
-[SBFloorDodgingLayerModifier _modelByPerformingDodgingInModel:];
-[SBFloorDodgingLayerModifier _modelsByResizingOverlappingIdentifiers:];
-[SBFloorDodgingLayerModifier _modelsByTranslatingOverlappingIdentifiers:allowedEdges:];
-[SBFloorDodgingLayerModifier animationBehaviorModeForIdentifier:];
-[SBFloorDodgingLayerModifier framesForIdentifiers];
-[SBFloorDodgingLayerModifier layoutSettingsForIdentifier:];
-[SBFloorDodgingLayerModifier modelForInvalidatedModel:];
-[SBFloorDodgingLayerModifier setOverridingModel:];
-[SBFloorDodgingLayerModifier zOrderedIdentifiers];
```
