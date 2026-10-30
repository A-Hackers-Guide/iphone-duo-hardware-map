# `_UIFocusMap`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _minimumSearchAreaIsEmpty;
B _trackingSearchInfo;
B _needsSearchInfo;
B _ignoresRootContainerClippingRect;
@"<_UIFocusRegionContainer>" _rootContainerProxy;
@"UIFocusSystem" _focusSystem;
@"<_UIFocusRegionContainer>" _rootContainer;
@"<UICoordinateSpace>" _coordinateSpace;
@"_UIFocusGroupMap" _focusGroupMap;
@"_UIFocusSearchInfo" _searchInfo;
@"_UIFocusMapSearchInfo" _defaultItemSearchInfo;
@"_UIFocusMapSearchInfo" _focusMovementSearchInfo;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minimumSearchArea;
```

## Properties

```
@property (T@"_UIFocusMapSearchInfo",R,N,G_defaultItemSearchContext,V_defaultItemSearchInfo) defaultItemSearchInfo;
@property (T@"_UIFocusMapSearchInfo",R,N,G_focusMovementSearchContext,V_focusMovementSearchInfo) focusMovementSearchInfo;
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (T@"<_UIFocusRegionContainer>",R,W,N,V_rootContainer) rootContainer;
@property (T@"<UICoordinateSpace>",R,W,N,V_coordinateSpace) coordinateSpace;
@property (T@"_UIFocusGroupMap",R,N,V_focusGroupMap) focusGroupMap;
@property (T@"_UIFocusSearchInfo",R,N,V_searchInfo) searchInfo;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_minimumSearchArea) minimumSearchArea;
```

## Instance methods

```
-[_UIFocusMap coordinateSpace];
-[_UIFocusMap init];
-[_UIFocusMap focusSystem];
-[_UIFocusMap _nextFocusedItemForFocusMovementRequest:inRegions:withSnapshot:];
-[_UIFocusMap _allRegionsInContainer:intersectingRegion:];
-[_UIFocusMap _beginTrackingDefaultItemSearchInfoIfNecessary];
-[_UIFocusMap _beginTrackingFocusMovementSearchInfoIfNecessary];
-[_UIFocusMap _beginTrackingSearches];
-[_UIFocusMap _closestFocusableItemToPoint:inRect:itemFilter:distanceMeasuringUnitPoint:];
-[_UIFocusMap _defaultItemSearchContext];
-[_UIFocusMap _defaultMapSnapshotter];
-[_UIFocusMap _focusMovementSearchContext];
-[_UIFocusMap _inferredDefaultFocusItemInEnvironment:];
-[_UIFocusMap _linearlySortedFocusItemsForItems:groupFilter:];
-[_UIFocusMap _nextFocusedItemForFocusMovementRequest:];
-[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:];
-[_UIFocusMap _nextFocusedItemForFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:];
-[_UIFocusMap _nextFocusedItemForLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:];
-[_UIFocusMap _nextFocusedItemForNonLinearFocusMovementRequest:startingFromRegion:inRegions:withSnapshot:];
-[_UIFocusMap _stopTrackingSearches];
-[_UIFocusMap _trackExternalSnapshot:];
-[_UIFocusMap diagnoseFocusabilityForItem:report:];
-[_UIFocusMap focusGroupMap];
-[_UIFocusMap initWithFocusSystem:rootContainer:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:];
-[_UIFocusMap initWithFocusSystem:rootEnvironment:];
-[_UIFocusMap initWithFocusSystem:rootEnvironment:coordinateSpace:searchInfo:ignoresRootContainerClippingRect:];
-[_UIFocusMap minimumSearchArea];
-[_UIFocusMap rootContainer];
-[_UIFocusMap searchInfo];
-[_UIFocusMap setMinimumSearchArea:];
-[_UIFocusMap verifyFocusabilityForItem:];
```
