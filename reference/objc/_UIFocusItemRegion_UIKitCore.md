# `_UIFocusItemRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusRegion`
- 2 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
{?="itemIsEligibleForFocusOcclusion"b1"itemIsFocusable"b1"itemIsTransparent"b1} _flags;
@"<UIFocusItem>" _item;
```

## Properties

```
@property (T@"<UIFocusItem>",R,W,N,V_item) item;
```

## Instance methods

```
-[_UIFocusItemRegion item];
-[_UIFocusItemRegion isEqual:];
-[_UIFocusItemRegion _canBeOccludedByRegionsAbove];
-[_UIFocusItemRegion _canOccludeRegionsBelow];
-[_UIFocusItemRegion _debugAssociatedObject];
-[_UIFocusItemRegion _defaultFocusItem];
-[_UIFocusItemRegion _descriptionBuilder];
-[_UIFocusItemRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusItemRegion _focusableBoundaries];
-[_UIFocusItemRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:];
-[_UIFocusItemRegion _preferredDistanceComparisonType];
-[_UIFocusItemRegion initWithFrame:coordinateSpace:];
-[_UIFocusItemRegion initWithFrame:coordinateSpace:item:focusSystem:];
```
