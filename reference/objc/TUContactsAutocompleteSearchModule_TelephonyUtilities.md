# `TUContactsAutocompleteSearchModule`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CNAutocompleteFetchDelegate`, `TUSearchModuleProtocol`
- 8 instance variables, 13 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _searchComplete;
B _cancelled;
@"TUSearchController" _searchController;
@"CNAutocompleteStore" _autocompleteStore;
@"<CNAutocompleteCancelable>" _fetchRequest;
@"TUAutocompleteResultPartitioner" _autocompleteResultPartitioner;
@"NSObject<OS_dispatch_queue>" _queue;
@? _completion;
```

## Properties

```
@property (T@"CNAutocompleteStore",&,N,V_autocompleteStore) autocompleteStore;
@property (T@"<CNAutocompleteCancelable>",&,N,V_fetchRequest) fetchRequest;
@property (T@"TUAutocompleteResultPartitioner",&,N,V_autocompleteResultPartitioner) autocompleteResultPartitioner;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@?,C,N,V_completion) completion;
@property (TB,N,GisSearchComplete,V_searchComplete) searchComplete;
@property (TB,N,GisCancelled,V_cancelled) cancelled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"TUSearchResults",R) searchResults;
@property (T@"TUSearchController",?,W,V_searchController) searchController;
```

## Instance methods

```
-[TUContactsAutocompleteSearchModule setCompletion:];
-[TUContactsAutocompleteSearchModule searchResults];
-[TUContactsAutocompleteSearchModule setSearchController:];
-[TUContactsAutocompleteSearchModule completion];
-[TUContactsAutocompleteSearchModule fetchRequest];
-[TUContactsAutocompleteSearchModule setFetchRequest:];
-[TUContactsAutocompleteSearchModule setCancelled:];
-[TUContactsAutocompleteSearchModule init];
-[TUContactsAutocompleteSearchModule searchController];
-[TUContactsAutocompleteSearchModule _cleanup];
-[TUContactsAutocompleteSearchModule dealloc];
-[TUContactsAutocompleteSearchModule isCancelled];
-[TUContactsAutocompleteSearchModule queue];
-[TUContactsAutocompleteSearchModule setAutocompleteStore:];
-[TUContactsAutocompleteSearchModule autocompleteFetch:didFailWithError:];
-[TUContactsAutocompleteSearchModule autocompleteStore];
-[TUContactsAutocompleteSearchModule autocompleteFetchDidFinish:];
-[TUContactsAutocompleteSearchModule cancelSearch];
-[TUContactsAutocompleteSearchModule autocompleteFetch:didReceiveResults:];
-[TUContactsAutocompleteSearchModule setQueue:];
-[TUContactsAutocompleteSearchModule setSearchComplete:];
-[TUContactsAutocompleteSearchModule autocompleteResultPartitioner];
-[TUContactsAutocompleteSearchModule isSearchComplete];
-[TUContactsAutocompleteSearchModule searchForString:completion:];
-[TUContactsAutocompleteSearchModule setAutocompleteResultPartitioner:];
```
