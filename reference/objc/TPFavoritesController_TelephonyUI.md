# `TPFavoritesController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallProviderManagerDelegate`
- 11 instance variables, 15 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _needsProvidersUpdates;
@"TUCallProviderManager" _callProviderManager;
@"NSCache" _contactCache;
@"CNContactStore" _contactStore;
@"NSArray" _favoritesEntries;
@"CNFavorites" _favoritesManager;
@"NSCache" _transportNameCache;
Q _prefetchCount;
@"NSObject<OS_dispatch_queue>" _completionDispatchQueue;
@"NSObject<OS_dispatch_queue>" _serialDispatchQueue;
@? _delayedFetchBlock;
```

## Properties

```
@property (T@"NSCache",R,N,V_contactCache) contactCache;
@property (T@"NSCache",R,N,V_transportNameCache) transportNameCache;
@property (T@"TUCallProviderManager",R,N,V_callProviderManager) callProviderManager;
@property (T@"CNFavorites",R,N,V_favoritesManager) favoritesManager;
@property (TQ,R,N,V_prefetchCount) prefetchCount;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_completionDispatchQueue) completionDispatchQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialDispatchQueue) serialDispatchQueue;
@property (T@"NSArray",C,N,V_favoritesEntries) favoritesEntries;
@property (T@?,C,N,V_delayedFetchBlock) delayedFetchBlock;
@property (TB,N,V_needsProvidersUpdates) needsProvidersUpdates;
@property (T@"CNContactStore",R,N,V_contactStore) contactStore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[TPFavoritesController providersChangedForProviderManager:];
-[TPFavoritesController contactCache];
-[TPFavoritesController init];
-[TPFavoritesController dealloc];
-[TPFavoritesController addEntry:];
-[TPFavoritesController contactStore];
-[TPFavoritesController completionDispatchQueue];
-[TPFavoritesController prefetchCount];
-[TPFavoritesController moveEntryAtIndex:toIndex:];
-[TPFavoritesController callProviderManager];
-[TPFavoritesController transportNameForFavoritesEntry:];
-[TPFavoritesController absoluteIndexForIndex:];
-[TPFavoritesController canAddEntry];
-[TPFavoritesController contactCacheKeyForFavoritesEntry:];
-[TPFavoritesController contactForFavoritesEntry:];
-[TPFavoritesController contactForFavoritesEntry:keyDescriptors:];
-[TPFavoritesController contactsForFavoritesEntries:keyDescriptors:];
-[TPFavoritesController delayedFetchBlock];
-[TPFavoritesController favoritesEntries];
-[TPFavoritesController favoritesManager];
-[TPFavoritesController fetchContactForFavoritesEntries:keyDescriptors:];
-[TPFavoritesController fetchContactForFavoritesEntry:];
-[TPFavoritesController fetchContactForFavoritesEntry:keyDescriptors:];
-[TPFavoritesController fetchFavoritesEntries];
-[TPFavoritesController fetchIfNeeded];
-[TPFavoritesController fetchIfNeededWithCompletion:];
-[TPFavoritesController fetchTransportNameForFavoritesEntry:];
-[TPFavoritesController handleContactsFavoritesDidChangeNotification:];
-[TPFavoritesController initWithContactStore:prefetchCount:];
-[TPFavoritesController needsProvidersUpdates];
-[TPFavoritesController performInitialFetchIfNeeded];
-[TPFavoritesController removeEntriesAtIndexes:];
-[TPFavoritesController serialDispatchQueue];
-[TPFavoritesController setDelayedFetchBlock:];
-[TPFavoritesController setFavoritesEntries:];
-[TPFavoritesController setNeedsProvidersUpdates:];
-[TPFavoritesController transportNameCache];
-[TPFavoritesController transportNameCacheKeyForFavoritesEntry:];
```
