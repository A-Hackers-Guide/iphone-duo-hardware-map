# `TUCallHistorySearchModule`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSearchModuleProtocol`
- 4 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _searchComplete;
@"TUSearchController" _searchController;
@"NSMutableArray" _currentResultsList;
@"NSString" _previousSearchString;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_currentResultsList) currentResultsList;
@property (T@"NSString",C,N,V_previousSearchString) previousSearchString;
@property (TB,N,GisSearchComplete,V_searchComplete) searchComplete;
@property (T@"TUSearchResults",R) searchResults;
@property (T@"TUSearchController",?,W,V_searchController) searchController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TUCallHistorySearchModule searchResults];
-[TUCallHistorySearchModule setSearchController:];
-[TUCallHistorySearchModule searchController];
-[TUCallHistorySearchModule cancelSearch];
-[TUCallHistorySearchModule setSearchComplete:];
-[TUCallHistorySearchModule currentResultsList];
-[TUCallHistorySearchModule isSearchComplete];
-[TUCallHistorySearchModule previousSearchString];
-[TUCallHistorySearchModule searchForString:completion:];
-[TUCallHistorySearchModule setCurrentResultsList:];
-[TUCallHistorySearchModule setPreviousSearchString:];
```
