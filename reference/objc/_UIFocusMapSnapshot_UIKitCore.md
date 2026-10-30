# `_UIFocusMapSnapshot`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusRegionSearchContext`
- 22 instance variables, 16 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _mutableUnoccludedRegions;
@"NSHashTable" _filteredOriginalRegions;
^{__CFDictionary=} _subregionToRegionMap;
^{__CFDictionary=} _regionToOccludingRegionsMap;
^{__CFDictionary=} _regionToFocusItemCache;
^{__CFDictionary=} _regionFrameCache;
@"NSMutableArray" _stateStack;
@"NSHashTable" _eligibleEnvironments;
@"NSHashTable" _ineligibleEnvironments;
@"NSHashTable" _uncachableEnvironments;
@"NSArray" _regions;
@"NSHashTable" _visitedRegionContainers;
@"NSMutableArray" _activeFocusGuideImpls;
{?="didCaptureSnapshot"b1"isSearchingRegionsOfInterestContainer"b1"clipToSnapshotRect"b1"ignoresRootContainerClippingRect"b1} _flags;
@"UIFocusSystem" _focusSystem;
@"<_UIFocusRegionContainer>" _rootContainer;
@"_UIFocusMapRect" _mapArea;
@"_UIFocusRegion" _focusedRegion;
@"<_UIFocusRegionContainer>" _regionsContainer;
@"_UIFocusSearchInfo" _searchInfo;
@"_UIFocusMovementInfo" _movementInfo;
@"_UIFocusMapRect" _searchArea;
```

## Properties

```
@property (T@"_UIFocusSearchInfo",&,N,V_searchInfo) searchInfo;
@property (T@"_UIFocusMovementInfo",&,N,V_movementInfo) movementInfo;
@property (T@"_UIFocusMapRect",R,N,G_searchArea,V_searchArea) searchArea;
@property (TB,R,N) hasOnlyStaticContent;
@property (T@"UIFocusSystem",R,W,N,V_focusSystem) focusSystem;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (T@"<_UIFocusRegionContainer>",R,W,N,V_rootContainer) rootContainer;
@property (T@"_UIFocusMapRect",R,N,V_mapArea) mapArea;
@property (T@"_UIFocusRegion",R,C,N,V_focusedRegion) focusedRegion;
@property (T@"<_UIFocusRegionContainer>",R,W,N,V_regionsContainer) regionsContainer;
@property (T@"NSArray",R,C,N) regions;
@property (T@"NSArray",R,C,N) originalRegions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusMapSnapshot regions];
-[_UIFocusMapSnapshot coordinateSpace];
-[_UIFocusMapSnapshot addRegions:];
-[_UIFocusMapSnapshot init];
-[_UIFocusMapSnapshot dealloc];
-[_UIFocusMapSnapshot addRegion:];
-[_UIFocusMapSnapshot focusSystem];
-[_UIFocusMapSnapshot mapArea];
-[_UIFocusMapSnapshot originalRegions];
-[_UIFocusMapSnapshot _cachedNextFocusedItemForRegion:withFocusMovementRequest:inMap:];
-[_UIFocusMapSnapshot _capture];
-[_UIFocusMapSnapshot _initWithSnapshotter:mapArea:searchArea:];
-[_UIFocusMapSnapshot _searchArea];
-[_UIFocusMapSnapshot _trackOccludingRegion:forRegion:];
-[_UIFocusMapSnapshot _trackSubregion:forRegion:];
-[_UIFocusMapSnapshot addFocusGuideContainers:];
-[_UIFocusMapSnapshot addRegionsInContainer:];
-[_UIFocusMapSnapshot addRegionsInContainers:];
-[_UIFocusMapSnapshot consumeRegionInformationForRegions:fromSnapshot:];
-[_UIFocusMapSnapshot focusedRegion];
-[_UIFocusMapSnapshot hasOnlyStaticContent];
-[_UIFocusMapSnapshot markContainerAsProvidingDynamicContent];
-[_UIFocusMapSnapshot movementInfo];
-[_UIFocusMapSnapshot occludingRegionsForRegion:];
-[_UIFocusMapSnapshot originalRegionForRegion:];
-[_UIFocusMapSnapshot regionsContainer];
-[_UIFocusMapSnapshot regionsForOriginalRegion:];
-[_UIFocusMapSnapshot rootContainer];
-[_UIFocusMapSnapshot searchArea];
-[_UIFocusMapSnapshot searchInfo];
-[_UIFocusMapSnapshot setMovementInfo:];
-[_UIFocusMapSnapshot setSearchInfo:];
-[_UIFocusMapSnapshot snapshotFrameForRegion:];
```
