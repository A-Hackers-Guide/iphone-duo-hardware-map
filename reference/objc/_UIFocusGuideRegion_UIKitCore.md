# `_UIFocusGuideRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusRegion`
- 6 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
B __isUnoccludable;
B __ignoresSpeedBumpEdges;
B __isUnclippable;
f __focusPriority;
@"<_UIFocusGuideRegionDelegate>" _delegate;
@"<UIFocusEnvironment>" _owningEnvironment;
```

## Properties

```
@property (TB,N,S_setIsUnoccludable:,V__isUnoccludable) _isUnoccludable;
@property (Tf,N,S_setFocusPriority:,V__focusPriority) _focusPriority;
@property (TB,N,S_setIgnoresSpeedBumpEdges:,V__ignoresSpeedBumpEdges) _ignoresSpeedBumpEdges;
@property (TB,N,S_setIsUnclippable:,V__isUnclippable) _isUnclippable;
@property (T@"<_UIFocusGuideRegionDelegate>",W,N,V_delegate) delegate;
@property (T@"<UIFocusEnvironment>",W,N,V_owningEnvironment) owningEnvironment;
```

## Instance methods

```
-[_UIFocusGuideRegion setDelegate:];
-[_UIFocusGuideRegion delegate];
-[_UIFocusGuideRegion isEqual:];
-[_UIFocusGuideRegion _isUnoccludable];
-[_UIFocusGuideRegion _canBeOccludedByRegionsAbove];
-[_UIFocusGuideRegion _canOccludeRegionsBelow];
-[_UIFocusGuideRegion _debugAssociatedObject];
-[_UIFocusGuideRegion _delegatePreferredFocusEnvironmentsForMovementRequest:];
-[_UIFocusGuideRegion _fallbackFocusItemForMovementRequest:inFocusMap:withSnapshot:];
-[_UIFocusGuideRegion _focusPriority];
-[_UIFocusGuideRegion _focusRegionWithAdjustedFrame:coordinateSpace:];
-[_UIFocusGuideRegion _focusableBoundaries];
-[_UIFocusGuideRegion _focusedItemForLinearSorting:inMap:withSnapshot:];
-[_UIFocusGuideRegion _ignoresSpeedBumpEdges];
-[_UIFocusGuideRegion _isEnabledForFocusedRegion:inSnapshot:];
-[_UIFocusGuideRegion _isUnclippable];
-[_UIFocusGuideRegion _nextFocusedItemForFocusMovementRequest:inMap:withSnapshot:];
-[_UIFocusGuideRegion _preferredDistanceComparisonType];
-[_UIFocusGuideRegion _setFocusPriority:];
-[_UIFocusGuideRegion _setIgnoresSpeedBumpEdges:];
-[_UIFocusGuideRegion _setIsUnclippable:];
-[_UIFocusGuideRegion _setIsUnoccludable:];
-[_UIFocusGuideRegion _shouldCropRegionToSearchArea];
-[_UIFocusGuideRegion _shouldUseNextFocusedItemForLinearSorting];
-[_UIFocusGuideRegion _willParticipateAsDestinationRegionInFocusUpdate:];
-[_UIFocusGuideRegion initWithFrame:coordinateSpace:];
-[_UIFocusGuideRegion owningEnvironment];
-[_UIFocusGuideRegion setOwningEnvironment:];
```
