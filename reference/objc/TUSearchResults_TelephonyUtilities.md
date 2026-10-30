# `TUSearchResults`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 9 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSString" _searchTerm;
@"NSMutableArray" _resultGroups;
@"TUSearchController" _searchController;
@"NSMutableArray" _allSearchItemsCache;
@"NSMutableArray" _allDataItemsCache;
```

## Properties

```
@property (T@"NSString",&,N,V_searchTerm) searchTerm;
@property (T@"NSMutableArray",&,N,V_resultGroups) resultGroups;
@property (T@"NSMutableArray",&,N,V_allSearchItemsCache) allSearchItemsCache;
@property (T@"NSMutableArray",&,N,V_allDataItemsCache) allDataItemsCache;
@property (T@"NSArray",R) allSearchItems;
@property (T@"NSArray",R) allDataItems;
@property (Tq,R) numberOfSections;
@property (Tq,R) numberOfResults;
@property (T@"TUSearchController",W,V_searchController) searchController;
```

## Instance methods

```
-[TUSearchResults searchTerm];
-[TUSearchResults setSearchController:];
-[TUSearchResults setSearchTerm:];
-[TUSearchResults numberOfSections];
-[TUSearchResults _clearCaches];
-[TUSearchResults searchController];
-[TUSearchResults description];
-[TUSearchResults copyWithZone:];
-[TUSearchResults addSearchResults:];
-[TUSearchResults numberOfResults];
-[TUSearchResults addResultGroup:];
-[TUSearchResults addAdhocResultGroup];
-[TUSearchResults allDataItems];
-[TUSearchResults allDataItemsCache];
-[TUSearchResults allSearchItems];
-[TUSearchResults allSearchItemsCache];
-[TUSearchResults finalizeSearchResults];
-[TUSearchResults initWithSearchTerm:shouldAddAdhocResults:];
-[TUSearchResults numberOfTableViewRows];
-[TUSearchResults removeDuplicateResults];
-[TUSearchResults removeSearchItem:];
-[TUSearchResults resultGroupForSection:];
-[TUSearchResults resultGroups];
-[TUSearchResults setAllDataItemsCache:];
-[TUSearchResults setAllSearchItemsCache:];
-[TUSearchResults setResultGroups:];
```
