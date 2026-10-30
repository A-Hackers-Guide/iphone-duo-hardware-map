# `TUSearchController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _searchModulesLock;
@"NSMutableSet" _idsDestinations;
@"CNContactStore" _contactStore;
@"NSMutableDictionary" _searchModules;
@"NSMutableArray" _recentsModules;
@"NSObject<OS_dispatch_queue>" _searchQueue;
```

## Properties

```
@property (T@"CNContactStore",&,N,V_contactStore) contactStore;
@property (T@"NSMutableDictionary",&,N,V_searchModules) searchModules;
@property (T@"NSMutableArray",&,N,V_recentsModules) recentsModules;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_searchQueue) searchQueue;
```

## Class methods

```
+[TUSearchController sharedInstance];
```

## Instance methods

```
-[TUSearchController init];
-[TUSearchController setContactStore:];
-[TUSearchController contactStore];
-[TUSearchController setSearchQueue:];
-[TUSearchController _cancelRecentSearches];
-[TUSearchController _cancelSearchsForSearchTerm:];
-[TUSearchController _clearIdsDestinations];
-[TUSearchController _fetchIdsDestinationsIfNeeded:withReason:];
-[TUSearchController _searchModuleCompletionWithModules:searchTerm:resultsClass:completion:];
-[TUSearchController recentsModuleCompletionWithCompletion:];
-[TUSearchController recentsModules];
-[TUSearchController recentsWithCompletion:];
-[TUSearchController searchForString:completion:];
-[TUSearchController searchModuleCompletionWithSearchTerm:completion:];
-[TUSearchController searchModules];
-[TUSearchController searchQueue];
-[TUSearchController setRecentsModules:];
-[TUSearchController setSearchModules:];
```
