# `TUAutocompleteResultPartitioner`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"TUSearchController" _searchController;
@"NSMutableArray" _normalResultsArray;
@"NSMutableArray" _foundInMailResultsArray;
@"NSMutableArray" _foundOnServersResultsArray;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_normalResultsArray) normalResultsArray;
@property (T@"NSMutableArray",&,N,V_foundInMailResultsArray) foundInMailResultsArray;
@property (T@"NSMutableArray",&,N,V_foundOnServersResultsArray) foundOnServersResultsArray;
@property (T@"TUSearchController",W,V_searchController) searchController;
```

## Class methods

```
+[TUAutocompleteResultPartitioner sourceTypeIsFoundInMail:];
+[TUAutocompleteResultPartitioner sourceTypeIsFoundOnServers:];
```

## Instance methods

```
-[TUAutocompleteResultPartitioner searchResults];
-[TUAutocompleteResultPartitioner setSearchController:];
-[TUAutocompleteResultPartitioner init];
-[TUAutocompleteResultPartitioner searchController];
-[TUAutocompleteResultPartitioner addResult:];
-[TUAutocompleteResultPartitioner foundInMailResultsArray];
-[TUAutocompleteResultPartitioner foundOnServersResultsArray];
-[TUAutocompleteResultPartitioner normalResultsArray];
-[TUAutocompleteResultPartitioner setFoundInMailResultsArray:];
-[TUAutocompleteResultPartitioner setFoundOnServersResultsArray:];
-[TUAutocompleteResultPartitioner setNormalResultsArray:];
```
