# `_UIFocusMapSearchInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _didFindFocusBlockingBoundary;
B _hasOnlyStaticContent;
@"NSArray" _linearSortedFocusItems;
@"_UIFocusGroupMap" _focusGroupMap;
@"NSMutableArray" _mutableSnapshots;
@"NSMutableArray" _mutableDestinationRegions;
@"_UIFocusSearchInfo" _searchInfo;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_mutableSnapshots) mutableSnapshots;
@property (T@"NSMutableArray",&,N,V_mutableDestinationRegions) mutableDestinationRegions;
@property (T@"_UIFocusSearchInfo",&,N,V_searchInfo) searchInfo;
@property (TB,N,V_didFindFocusBlockingBoundary) didFindFocusBlockingBoundary;
@property (T@"NSArray",&,N,V_linearSortedFocusItems) linearSortedFocusItems;
@property (T@"_UIFocusGroupMap",&,N,V_focusGroupMap) focusGroupMap;
@property (T@"NSArray",R,C,N) snapshots;
@property (T@"NSArray",R,C,N) destinationRegions;
@property (TB,R,N,V_hasOnlyStaticContent) hasOnlyStaticContent;
```

## Instance methods

```
-[_UIFocusMapSearchInfo init];
-[_UIFocusMapSearchInfo addSnapshot:];
-[_UIFocusMapSearchInfo snapshots];
-[_UIFocusMapSearchInfo addDestinationRegion:];
-[_UIFocusMapSearchInfo destinationRegions];
-[_UIFocusMapSearchInfo didFindFocusBlockingBoundary];
-[_UIFocusMapSearchInfo focusGroupMap];
-[_UIFocusMapSearchInfo hasOnlyStaticContent];
-[_UIFocusMapSearchInfo linearSortedFocusItems];
-[_UIFocusMapSearchInfo mutableDestinationRegions];
-[_UIFocusMapSearchInfo mutableSnapshots];
-[_UIFocusMapSearchInfo searchInfo];
-[_UIFocusMapSearchInfo setDidFindFocusBlockingBoundary:];
-[_UIFocusMapSearchInfo setFocusGroupMap:];
-[_UIFocusMapSearchInfo setLinearSortedFocusItems:];
-[_UIFocusMapSearchInfo setMutableDestinationRegions:];
-[_UIFocusMapSearchInfo setMutableSnapshots:];
-[_UIFocusMapSearchInfo setSearchInfo:];
```
