# `TUCallHistoryController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUCallProviderManagerDelegate`
- 18 instance variables, 22 properties, 64 instance methods, 5 class methods

## Instance variables

```
B _shouldUpdateMetadataCache;
B _isPerformingRecentCallsRefresh;
B _recentCallsRefreshRequestedDuringFetch;
Q _coalescingStrategy;
Q _options;
@"NSPredicate" _preFetchingPredicate;
@"NSArray" _recentCalls;
Q _unreadCallCount;
@"NSOperationQueue" _searchQueue;
@"TUFeatureFlags" _featureFlags;
@"CHManager" _callHistoryManager;
@"<TUCallHistoryControllerRecentsDataSource>" _recentsDataSource;
@"TUCallProviderManager" _callProviderManager;
@"TUDispatcher" _dispatcher;
@"TUDispatcher" _simpleIvarDispatcher;
@"NSArray" _thirdPartyCallProviders;
@"NSMutableSet" _metadataPreCachedOptions;
@"<TUCallHistoryControllerDataSource>" _dataSource;
```

## Properties

```
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (T@"CHManager",&,N,V_callHistoryManager) callHistoryManager;
@property (T@"<TUCallHistoryControllerRecentsDataSource>",&,N,V_recentsDataSource) recentsDataSource;
@property (T@"TUCallProviderManager",&,N,V_callProviderManager) callProviderManager;
@property (T@"TUDispatcher",&,N,V_dispatcher) dispatcher;
@property (T@"TUDispatcher",&,N,V_simpleIvarDispatcher) simpleIvarDispatcher;
@property (TB,N,V_isPerformingRecentCallsRefresh) isPerformingRecentCallsRefresh;
@property (TB,N,V_recentCallsRefreshRequestedDuringFetch) recentCallsRefreshRequestedDuringFetch;
@property (T@"NSArray",&,N,V_recentCalls) recentCalls;
@property (TQ,N,V_unreadCallCount) unreadCallCount;
@property (T@"NSArray",C,N,V_thirdPartyCallProviders) thirdPartyCallProviders;
@property (TB,R,N,V_shouldUpdateMetadataCache) shouldUpdateMetadataCache;
@property (T@"NSMutableSet",&,N,V_metadataPreCachedOptions) metadataPreCachedOptions;
@property (T@"<TUCallHistoryControllerDataSource>",R,N,V_dataSource) dataSource;
@property (T@"NSOperationQueue",&,N,V_searchQueue) searchQueue;
@property (T@"NSPredicate",N,V_preFetchingPredicate) preFetchingPredicate;
@property (TQ,N,V_coalescingStrategy) coalescingStrategy;
@property (TQ,N,V_options) options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallHistoryController sharedController];
+[TUCallHistoryController callHistoryControllerWithCoalescingStrategy:options:];
+[TUCallHistoryController callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:];
+[TUCallHistoryController callHistoryControllerWithCoalescingStrategy:options:shouldUpdateMetadataCache:recentsDataSource:];
+[TUCallHistoryController sharedControllerWithCoalescingStrategy:options:];
```

## Instance methods

```
-[TUCallHistoryController dispatcher];
-[TUCallHistoryController providersChangedForProviderManager:];
-[TUCallHistoryController recentCallsWithPredicate:];
-[TUCallHistoryController setDispatcher:];
-[TUCallHistoryController setOptions:];
-[TUCallHistoryController init];
-[TUCallHistoryController dealloc];
-[TUCallHistoryController setPreFetchingPredicate:];
-[TUCallHistoryController setCoalescingStrategy:];
-[TUCallHistoryController dataSource];
-[TUCallHistoryController callsWithPredicate:limit:offset:batchSize:];
-[TUCallHistoryController recentCalls];
-[TUCallHistoryController updateReminderUUID:forRecentCall:];
-[TUCallHistoryController setCallHistoryManager:];
-[TUCallHistoryController coalescingStrategy];
-[TUCallHistoryController options];
-[TUCallHistoryController loadOlderRecentCalls];
-[TUCallHistoryController preFetchingPredicate];
-[TUCallHistoryController setRecentCalls:];
-[TUCallHistoryController canLoadOlderRecentCalls];
-[TUCallHistoryController callHistoryManager];
-[TUCallHistoryController featureFlags];
-[TUCallHistoryController setSearchQueue:];
-[TUCallHistoryController unreadCallCount];
-[TUCallHistoryController _callHistoryCoalescingStrategyForCoalescingStrategy:];
-[TUCallHistoryController _updateCallHistoryManagerUsingCurrentOptions];
-[TUCallHistoryController boostQualityOfService];
-[TUCallHistoryController callHistoryControllerCallHistoryFetchLimit];
-[TUCallHistoryController callHistoryDatabaseChanged:];
-[TUCallHistoryController callHistoryManagerInitializationDispatchBlock];
-[TUCallHistoryController callHistoryManagerLoadOlderRecentCallsDispatchBlock];
-[TUCallHistoryController callHistoryManagerRecentCallsDispatchBlock];
-[TUCallHistoryController callProviderManager];
-[TUCallHistoryController cancelSearchFetchOperations];
-[TUCallHistoryController deleteAllRecentCalls];
-[TUCallHistoryController deleteRecentCall:];
-[TUCallHistoryController deleteRecentCalls:];
-[TUCallHistoryController dispatcherDidFinishBoost:];
-[TUCallHistoryController initWithCoalescingStrategy:options:dataSource:recentsDataSource:shouldUpdateMetadataCache:];
-[TUCallHistoryController isPerformingRecentCallsRefresh];
-[TUCallHistoryController loadDispatchQueue];
-[TUCallHistoryController markRecentAudioCallsAsRead];
-[TUCallHistoryController markRecentCallsAsRead];
-[TUCallHistoryController markRecentCallsAsReadWithPredicate:];
-[TUCallHistoryController markRecentVideoCallsAsRead];
-[TUCallHistoryController markUnreadRecentCallsAsReadWithPredicate:];
-[TUCallHistoryController metadataPreCachedOptions];
-[TUCallHistoryController performRecentCallsRefresh];
-[TUCallHistoryController recentCallsRefreshRequestedDuringFetch];
-[TUCallHistoryController recentsDataSource];
-[TUCallHistoryController reloadWithOptions:];
-[TUCallHistoryController requestRecentCallsRefresh];
-[TUCallHistoryController searchQueue];
-[TUCallHistoryController setCallProviderManager:];
-[TUCallHistoryController setIsPerformingRecentCallsRefresh:];
-[TUCallHistoryController setMetadataPreCachedOptions:];
-[TUCallHistoryController setRecentCallsRefreshRequestedDuringFetch:];
-[TUCallHistoryController setRecentsDataSource:];
-[TUCallHistoryController setSimpleIvarDispatcher:];
-[TUCallHistoryController setThirdPartyCallProviders:];
-[TUCallHistoryController setUnreadCallCount:];
-[TUCallHistoryController shouldUpdateMetadataCache];
-[TUCallHistoryController simpleIvarDispatcher];
-[TUCallHistoryController thirdPartyCallProviders];
```
