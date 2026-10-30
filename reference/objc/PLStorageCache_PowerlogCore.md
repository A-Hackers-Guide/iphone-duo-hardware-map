# `PLStorageCache`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 68 instance methods, 4 class methods

## Instance variables

```
B _bgsqlDedicatedCacheEnabled;
@"NSDate" _lastCacheFlushDate;
q _lastEntryCacheSize;
q _stagingEntryCacheSize;
@"NSMutableDictionary" _cacheContent;
@"NSMutableDictionary" _lastEntryCache;
@"NSMutableDictionary" _stagingEntryCache;
@"NSMutableDictionary" _stagingAggregateEntryCache;
@"NSMutableDictionary" _countWarnings;
@"NSMutableDictionary" _countSafetyDrop;
@"NSMutableDictionary" _bgsqlStagingCache;
Q _bgsqlFlushCountThisWindow;
@"NSDate" _bgsqlFlushWindowStart;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_lastEntryCache) lastEntryCache;
@property (T@"NSMutableDictionary",&,V_stagingEntryCache) stagingEntryCache;
@property (T@"NSMutableDictionary",&,V_stagingAggregateEntryCache) stagingAggregateEntryCache;
@property (T@"NSDate",&,N,V_lastCacheFlushDate) lastCacheFlushDate;
@property (T@"NSMutableDictionary",&,V_countWarnings) countWarnings;
@property (T@"NSMutableDictionary",&,V_countSafetyDrop) countSafetyDrop;
@property (T@"NSMutableDictionary",&,V_bgsqlStagingCache) bgsqlStagingCache;
@property (TQ,V_bgsqlFlushCountThisWindow) bgsqlFlushCountThisWindow;
@property (T@"NSDate",&,V_bgsqlFlushWindowStart) bgsqlFlushWindowStart;
@property (TB,R,N,V_bgsqlDedicatedCacheEnabled) bgsqlDedicatedCacheEnabled;
@property (Tq,V_lastEntryCacheSize) lastEntryCacheSize;
@property (Tq,V_stagingEntryCacheSize) stagingEntryCacheSize;
@property (T@"NSMutableDictionary",&,V_cacheContent) cacheContent;
```

## Class methods

```
+[PLStorageCache bgsqlCacheLimit];
+[PLStorageCache isBGSQLEntryKey:];
+[PLStorageCache sharedStorageCache];
+[PLStorageCache syncAndDispatchForEntryCache:forEntryKey:withBlock:];
```

## Instance methods

```
-[PLStorageCache bgsqlStagingCacheSize];
-[PLStorageCache countSafetyDrop];
-[PLStorageCache setLastEntryCache:];
-[PLStorageCache enumerateStagingEntryCacheForEntryKey:withBlock:];
-[PLStorageCache setStagingAggregateEntryCache:];
-[PLStorageCache getEntryFromDBForEntryKey:withMatchingKeyToValue:];
-[PLStorageCache connectionForKey:];
-[PLStorageCache bgsqlStagingCache];
-[PLStorageCache getQueryForAggregateEntryKey:withMatchingKeyToValue:];
-[PLStorageCache matchingPairs:];
-[PLStorageCache countWarnings];
-[PLStorageCache bgsqlFlushCountThisWindow];
-[PLStorageCache dumpStagingEntryCache];
-[PLStorageCache stagingEntryCacheIDsForEntryKey:];
-[PLStorageCache addToStagingEntryCache:];
-[PLStorageCache enumerateStagingEntryCacheWithBlock:];
-[PLStorageCache init];
-[PLStorageCache addToStagingAggregateEntryCache:];
-[PLStorageCache setStagingEntryCacheSize:];
-[PLStorageCache bgsqlDedicatedCacheEnabled];
-[PLStorageCache entryIDForNewEntry:];
-[PLStorageCache logBGSQLCacheSizeWithInsertCount:updateCount:flushDate:];
-[PLStorageCache logSizeOfEntryCache:];
-[PLStorageCache setCacheContent:];
-[PLStorageCache logSizeOfLastEntryCache];
-[PLStorageCache stagingEntryCacheForEntryKey:withID:];
-[PLStorageCache flushStagingEntryCacheToDatabase];
-[PLStorageCache stagingEntryCacheSizeForEntryKey:];
-[PLStorageCache enumerateEntryCache:withBlock:];
-[PLStorageCache lastEntryCacheForEntryKey:];
-[PLStorageCache cacheContent];
-[PLStorageCache setStagingEntryCache:];
-[PLStorageCache setLastEntryCacheSize:];
-[PLStorageCache stagingEntryCacheForEntryKey:withIDLessThan:];
-[PLStorageCache flushStagingAggregateEntryCacheToDatabase];
-[PLStorageCache clearLastEntryCacheForEntryKey:];
-[PLStorageCache limitOfType:forEntryKey:];
-[PLStorageCache insertIntoStagingEntryCache:];
-[PLStorageCache stagingEntryCache];
-[PLStorageCache updateStagingEntryCacheWithEntry:withBlock:];
-[PLStorageCache logStagingEntryCacheForEntryKey:];
-[PLStorageCache lastEntryCache];
-[PLStorageCache stagingEntryCacheSize];
-[PLStorageCache cachedEntryForEntryKey:withEntryID:];
-[PLStorageCache dumpEntryCache:];
-[PLStorageCache setLastCacheFlushDate:];
-[PLStorageCache trackBGSQLFlushFrequencyWithDate:];
-[PLStorageCache addToLastEntryCache:];
-[PLStorageCache setBgsqlFlushWindowStart:];
-[PLStorageCache flushBGSQLStagingCacheToDatabase];
-[PLStorageCache dumpLastEntryCache];
-[PLStorageCache lastEntryCacheForEntryKey:withSubEntryKey:];
-[PLStorageCache setCountWarnings:];
-[PLStorageCache lastEntryCachePruneToDate:];
-[PLStorageCache lastEntryCacheSize];
-[PLStorageCache lastCacheFlushDate];
-[PLStorageCache setCountSafetyDrop:];
-[PLStorageCache setNextEntryIDForEntryKey:toEntryID:];
-[PLStorageCache addToBGSQLStagingCache:];
-[PLStorageCache setBgsqlStagingCache:];
-[PLStorageCache stagingAggregateEntryCache];
-[PLStorageCache logFullLastEntryCacheForEntryKey:];
-[PLStorageCache stagingEntryCacheForEntryKey:];
-[PLStorageCache logSizeOfStagingEntryCache];
-[PLStorageCache bgsqlFlushWindowStart];
-[PLStorageCache stagingEntryCacheForEntryKey:withComparisons:isSingleton:];
-[PLStorageCache setBgsqlFlushCountThisWindow:];
-[PLStorageCache addToLastEntryCacheSubKey:];
```
