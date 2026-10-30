# `_UIFocusSpeedBumpRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusRegion`
- 1 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _speedBumpEdges;
```

## Properties

```
@property (TQ,N,V_speedBumpEdges) speedBumpEdges;
```

## Instance methods

```
-[_UIFocusSpeedBumpRegion isEqual:];
-[_UIFocusSpeedBumpRegion _boundariesBlockingFocusMovementRequest:];
-[_UIFocusSpeedBumpRegion _canBeOccludedByRegionsAbove];
-[_UIFocusSpeedBumpRegion _canOccludeRegionsBelow];
-[_UIFocusSpeedBumpRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusSpeedBumpRegion _shouldCropRegionToSearchArea];
-[_UIFocusSpeedBumpRegion initWithFrame:coordinateSpace:];
-[_UIFocusSpeedBumpRegion initWithFrame:coordinateSpace:speedBumpEdges:];
-[_UIFocusSpeedBumpRegion setSpeedBumpEdges:];
-[_UIFocusSpeedBumpRegion speedBumpEdges];
```
