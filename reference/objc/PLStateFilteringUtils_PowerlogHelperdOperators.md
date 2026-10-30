# `PLStateFilteringUtils`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 31 class methods

## Class methods

```
+[PLStateFilteringUtils _dateFromValue:];
+[PLStateFilteringUtils mergeOverlappingStateIntervals:];
+[PLStateFilteringUtils _assignIntervalEntry:withInterval:withParsedStates:intoFiltered:];
+[PLStateFilteringUtils _assignIntervalEntryToChunks:withInterval:withParsedChunks:intoFiltered:];
+[PLStateFilteringUtils _assignPointEntry:atTimestamp:withParsedStates:intoFiltered:];
+[PLStateFilteringUtils _assignPointEntryToChunks:atTimestamp:withParsedChunks:intoFiltered:];
+[PLStateFilteringUtils _binarySearchFirstCandidateInParsedStates:forTimestamp:];
+[PLStateFilteringUtils _durationFromStateDict:];
+[PLStateFilteringUtils _endDateFromStateDict:];
+[PLStateFilteringUtils _enforceStateLimitOnGroupedIntervals:];
+[PLStateFilteringUtils _limitIntervals:toMaxCount:forBundleID:];
+[PLStateFilteringUtils _limitStates:toMaxCount:forBundleID:];
+[PLStateFilteringUtils _parseAndSortChunkDicts:];
+[PLStateFilteringUtils _parseAndSortStateDicts:];
+[PLStateFilteringUtils _stateUniqueKeyFromDict:];
+[PLStateFilteringUtils aggregationKeyFromStateDict:];
+[PLStateFilteringUtils aggregationKeyFromStateInterval:];
+[PLStateFilteringUtils bundleIDFromProcessImagePath:];
+[PLStateFilteringUtils deduplicateStateIntervals:];
+[PLStateFilteringUtils deduplicatedStatesForChunkIntervals:fromStateIntervals:];
+[PLStateFilteringUtils enforceStateLimitOnGroupedStates:];
+[PLStateFilteringUtils filterEntries:byStateDicts:andChunkDicts:timestampStartKey:timestampEndKey:];
+[PLStateFilteringUtils filterEntries:byStateDicts:timestampStartKey:timestampEndKey:];
+[PLStateFilteringUtils filterEntries:byStateIntervals:timestampStartKey:timestampEndKey:];
+[PLStateFilteringUtils groupAndLimitStateDictsByBundle:];
+[PLStateFilteringUtils groupAndLimitStateIntervalsByBundle:];
+[PLStateFilteringUtils groupStateDicts:outRawByBundle:outLimitedByBundle:];
+[PLStateFilteringUtils groupStateDictsByBundle:];
+[PLStateFilteringUtils groupStateIntervals:outRawByBundle:outLimitedByBundle:];
+[PLStateFilteringUtils groupStateIntervalsByBundle:];
+[PLStateFilteringUtils unattributedKeyStringForBundleID:];
```
