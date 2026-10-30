# `PLStreamingMetricAggregator`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 49 instance methods, 0 class methods

## Instance variables

```
Q _totalEntriesProcessed;
Q _entriesUnattributed;
Q _entriesOutsideChunks;
Q _stateTransitionsProcessed;
@"NSArray" _sortedChunks;
@"SRReportedStateAggregationManager" _chunkBuckets;
@"NSMutableDictionary" _chunkKeyToAggregationKey;
@"NSMutableDictionary" _activeStatesByBundle;
@"NSMutableDictionary" _stateHistoryByBundle;
@"NSMapTable" _implicitEndTimestamps;
@"SRReportedStateAggregationManager" _stateBuckets;
@"NSMutableDictionary" _pendingAnimationIntervalsByBucket;
@"NSMutableDictionary" _processedTotalDurationByBucket;
@"NSMutableDictionary" _processedWeightedRatioSumByBucket;
```

## Properties

```
@property (T@"NSArray",&,N,V_sortedChunks) sortedChunks;
@property (T@"SRReportedStateAggregationManager",&,N,V_chunkBuckets) chunkBuckets;
@property (T@"NSMutableDictionary",&,N,V_chunkKeyToAggregationKey) chunkKeyToAggregationKey;
@property (T@"NSMutableDictionary",&,N,V_activeStatesByBundle) activeStatesByBundle;
@property (T@"NSMutableDictionary",&,N,V_stateHistoryByBundle) stateHistoryByBundle;
@property (T@"NSMapTable",&,N,V_implicitEndTimestamps) implicitEndTimestamps;
@property (T@"SRReportedStateAggregationManager",&,N,V_stateBuckets) stateBuckets;
@property (T@"NSMutableDictionary",&,N,V_pendingAnimationIntervalsByBucket) pendingAnimationIntervalsByBucket;
@property (T@"NSMutableDictionary",&,N,V_processedTotalDurationByBucket) processedTotalDurationByBucket;
@property (T@"NSMutableDictionary",&,N,V_processedWeightedRatioSumByBucket) processedWeightedRatioSumByBucket;
@property (TQ,N,V_totalEntriesProcessed) totalEntriesProcessed;
@property (TQ,N,V_entriesUnattributed) entriesUnattributed;
@property (TQ,N,V_entriesOutsideChunks) entriesOutsideChunks;
@property (TQ,N,V_stateTransitionsProcessed) stateTransitionsProcessed;
```

## Instance methods

```
-[PLStreamingMetricAggregator finalizeResults];
-[PLStreamingMetricAggregator _addMetricWithBundleID:timestamp:addToState:addToChunk:];
-[PLStreamingMetricAggregator _bufferAnimationInterval:forBucketKey:];
-[PLStreamingMetricAggregator _processBatchForBucketKey:];
-[PLStreamingMetricAggregator activeStatesByBundle];
-[PLStreamingMetricAggregator activeStatesForBundleID:timestamp:];
-[PLStreamingMetricAggregator addActivationWithBundleID:timestamp:durationMs:foreground:activationFlag:];
-[PLStreamingMetricAggregator addAnimationHitchWithBundleID:interval:];
-[PLStreamingMetricAggregator addExitWithBundleID:timestamp:foreground:domain:code:];
-[PLStreamingMetricAggregator addExtendedLaunchWithBundleID:timestamp:durationMs:foreground:];
-[PLStreamingMetricAggregator addGlitchWithBundleID:timestamp:glitchDurationMs:scrollDurationMs:glitchCount:isScrollStart:];
-[PLStreamingMetricAggregator addHangWithBundleID:timestamp:durationMs:];
-[PLStreamingMetricAggregator addLaunchWithBundleID:timestamp:durationMs:foreground:];
-[PLStreamingMetricAggregator addMetalFrameRateWithBundleID:layerName:timestamp:frameCount:activeSeconds:];
-[PLStreamingMetricAggregator addResumeWithBundleID:timestamp:durationMs:];
-[PLStreamingMetricAggregator addSignpostIntervalWithBundleID:timestamp:entry:];
-[PLStreamingMetricAggregator aggregationKeyFromState:bundleID:];
-[PLStreamingMetricAggregator chunkBuckets];
-[PLStreamingMetricAggregator chunkKeyToAggregationKey];
-[PLStreamingMetricAggregator chunksContainingTimestamp:];
-[PLStreamingMetricAggregator entriesOutsideChunks];
-[PLStreamingMetricAggregator entriesUnattributed];
-[PLStreamingMetricAggregator handleStateTransitionWithEndingState:endingBundleID:startingState:startingBundleID:];
-[PLStreamingMetricAggregator implicitEndTimestamps];
-[PLStreamingMetricAggregator initWithChunkIntervals:];
-[PLStreamingMetricAggregator pendingAnimationIntervalsByBucket];
-[PLStreamingMetricAggregator processedTotalDurationByBucket];
-[PLStreamingMetricAggregator processedWeightedRatioSumByBucket];
-[PLStreamingMetricAggregator setActiveStatesByBundle:];
-[PLStreamingMetricAggregator setChunkBuckets:];
-[PLStreamingMetricAggregator setChunkKeyToAggregationKey:];
-[PLStreamingMetricAggregator setEntriesOutsideChunks:];
-[PLStreamingMetricAggregator setEntriesUnattributed:];
-[PLStreamingMetricAggregator setImplicitEndTimestamps:];
-[PLStreamingMetricAggregator setPendingAnimationIntervalsByBucket:];
-[PLStreamingMetricAggregator setProcessedTotalDurationByBucket:];
-[PLStreamingMetricAggregator setProcessedWeightedRatioSumByBucket:];
-[PLStreamingMetricAggregator setSortedChunks:];
-[PLStreamingMetricAggregator setStateBuckets:];
-[PLStreamingMetricAggregator setStateHistoryByBundle:];
-[PLStreamingMetricAggregator setStateTransitionsProcessed:];
-[PLStreamingMetricAggregator setTotalEntriesProcessed:];
-[PLStreamingMetricAggregator sortedChunks];
-[PLStreamingMetricAggregator stateBuckets];
-[PLStreamingMetricAggregator stateHistoryByBundle];
-[PLStreamingMetricAggregator stateTransitionsProcessed];
-[PLStreamingMetricAggregator stringKeyFromAggregationKey:];
-[PLStreamingMetricAggregator totalEntriesProcessed];
-[PLStreamingMetricAggregator unattributedKeyForBundleID:];
```
