# `_UIFocusRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<UICoordinateSpace>" _regionCoordinateSpace;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _regionFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_regionFrame) regionFrame;
@property (T@"<UICoordinateSpace>",R,N,V_regionCoordinateSpace) regionCoordinateSpace;
@property (T@,R,W,N,G_debugAssociatedObject) debugAssociatedObject;
```

## Instance methods

```
-[_UIFocusRegion hash];
-[_UIFocusRegion description];
-[_UIFocusRegion isEqual:];
-[_UIFocusRegion _boundariesBlockingFocusMovementRequest:];
-[_UIFocusRegion _canBeOccludedByRegionsAbove];
-[_UIFocusRegion _canOccludeRegionsBelow];
-[_UIFocusRegion _debugAssociatedObject];
-[_UIFocusRegion _defaultFocusItem];
-[_UIFocusRegion _descriptionBuilder];
-[_UIFocusRegion _didParticipateAsDestinationRegionInFocusUpdate:];
-[_UIFocusRegion _effectiveBoundariesBlockingFocusMovementRequest:];
-[_UIFocusRegion _effectiveFocusableBoundariesForHeading:];
-[_UIFocusRegion _focusPriority];
-[_UIFocusRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusRegion _focusableBoundaries];
-[_UIFocusRegion _focusedItemForLinearSorting:inMap:withSnapshot:];
-[_UIFocusRegion _ignoresSpeedBumpEdges];
-[_UIFocusRegion _isUnclippable];
-[_UIFocusRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:];
-[_UIFocusRegion _preferredDistanceComparisonType];
-[_UIFocusRegion _shouldCropRegionToSearchArea];
-[_UIFocusRegion _shouldUseNextFocusedItemForLinearSorting];
-[_UIFocusRegion _willParticipateAsDestinationRegionInFocusUpdate:];
-[_UIFocusRegion initWithFrame:coordinateSpace:];
-[_UIFocusRegion regionCoordinateSpace];
-[_UIFocusRegion regionFrame];
```
