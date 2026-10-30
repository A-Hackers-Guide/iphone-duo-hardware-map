# `BWHVSCandidateFrameManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 72 instance variables, 5 properties, 53 instance methods, 1 class methods

## Instance variables

```
f _prevScore;
@"BWHVSFrame" _bucketFrame;
{?="value"q"timescale"i"flags"I"epoch"q} _bucketEntryTime;
{?="value"q"timescale"i"flags"I"epoch"q} _captureStartTime;
B _inPause;
{?="value"q"timescale"i"flags"I"epoch"q} _pauseStartTime;
f _previousSimScore;
f _minPauseDurationInSec;
@"BWHVSFrame" _pauseFrame;
i _pauseSegmentCounter;
i _pauseBreakCounter;
B _currentSegmentIsValid;
B _foundAnyValidCandidate;
@"BWHVSFrame" _maxScoreFrame;
i _promotedMaxScoreFrameID;
f _promotedMaxScoreValue;
B _budgetEnabled;
i _budgetType;
f _simThreshold;
f _maxRTBucketAgeInSec;
i _maxFramesPer20Sec;
i _minBudget;
B _dumpInput;
B _legacy;
B _isFinalizingBudget;
i _maxCandidates;
i _maxCandidatesPerContext;
f _maxCandidateAgeInSec;
f _minCandidateProximityInSec;
i _maxDuplicatesRemovedPerPromotion;
i _duplicateConstraintType;
@"NSDictionary" _minPercentageOfMaxScoreThresholds;
@"NSDictionary" _contextPriorities;
@"NSDictionary" _minThresholds;
@"NSDictionary" _duplicateMaxTimeInMs;
@"NSDictionary" _duplicateThresholds;
@"NSDictionary" _savePauseThresholdsInMS;
@"NSDictionary" _breakPauseThresholdsInMS;
@"NSDictionary" _contextCandidates;
@"NSMutableDictionary" _candidateEntryTimes;
@"NSMutableDictionary" _deferredPromotedRemovalsByCandidateID;
@"NSMutableDictionary" _pendingCandidateRemovalsByCandidateID;
@"NSMutableSet" _candidateIDsDiscardedByPendingRemoval;
@"NSMutableArray" _promotedFrames;
@"NSMutableArray" _allPromotedFrameMetadata;
@"NSMutableDictionary" _removedFramesForDuplicate;
@"BWStillImageDuplicateInfo" _pendingMaxScoreReplacementInfo;
i _pendingMaxScoreReplacementFrameID;
@"NSMutableDictionary" _framesToRemoveExtra;
@"NSDictionary" _mostRecentFrameDict;
@"NSString" _captureFolder;
f _tinyFaceRatio;
@"NSString" _tinyFaceReference;
@"NSDictionary" _tinyFacePerContext;
@"NSDictionary" _largeFacePerContext;
B _breakDuplicateChains;
B _recoverExtras;
B _cleanDuplicatesEnabled;
B _fixedBudgetMode;
i _fixedBudgetMaxFrames;
@"NSDictionary" _simBoostPerContext;
@"NSMutableSet" _promotedPauseFrameIDs;
@"NSMutableSet" _manualFrameIDs;
@"NSMutableSet" _autoFramesEvictedByManualIDs;
@"NSMutableSet" _failedCaptureFrameIDs;
{?="value"q"timescale"i"flags"I"epoch"q} _earliestAllowedStillImageCaptureHostPTS;
B _waitForEarliestAllowedStillImageCaptureHostPTS;
@ _handlerContext;
@? _framePromotionHandler;
@ _removalHandlerContext;
@? _frameRemovalHandler;
@"<BWHVSCandidateFrameManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",&,N,V_captureFolder) captureFolder;
@property (Tf,R,N) typicalBufferingInSeconds;
@property (T{?=qiIq},N,V_earliestAllowedStillImageCaptureHostPTS) earliestAllowedStillImageCaptureHostPTS;
@property (TB,N,V_waitForEarliestAllowedStillImageCaptureHostPTS) waitForEarliestAllowedStillImageCaptureHostPTS;
@property (TB,R,N) isFixedBudgetExhausted;
```

## Class methods

```
+[BWHVSCandidateFrameManager initialize];
```

## Instance methods

```
-[BWHVSCandidateFrameManager dealloc];
-[BWHVSCandidateFrameManager reset];
-[BWHVSCandidateFrameManager setFrameRemovalHandler:context:];
-[BWHVSCandidateFrameManager _contextExistsInPromotedFrames:];
-[BWHVSCandidateFrameManager _analyzeDuplicateChains];
-[BWHVSCandidateFrameManager _applyLargeFaceRecovery:faceAreas:];
-[BWHVSCandidateFrameManager _applyMaxScoresPerContext];
-[BWHVSCandidateFrameManager _applyTinyFaceFiltering];
-[BWHVSCandidateFrameManager _availableBudget];
-[BWHVSCandidateFrameManager _candidateHasDeferredRemovalObligation:];
-[BWHVSCandidateFrameManager _cleanupRemovalFlagsForUnpromotedCauses];
-[BWHVSCandidateFrameManager _clearRemovalObligationsForCandidateID:];
-[BWHVSCandidateFrameManager _dupsToRemoveWithinRemovalBudget:similarities:removalsSoFar:frameID:checkName:];
-[BWHVSCandidateFrameManager _findLowestScoreFrameFromMostPopulatedContext];
-[BWHVSCandidateFrameManager _findWeakestPromotedFrameForContext:];
-[BWHVSCandidateFrameManager _isDuplicateOfFrame:comparedToFrame:];
-[BWHVSCandidateFrameManager _isDuplicateOfFrame:comparedToFrameDict:];
-[BWHVSCandidateFrameManager _isDuplicateOfFrame:comparedToFrameDict:dampedSimilarity:];
-[BWHVSCandidateFrameManager _isDuplicateWithEmbedding:timestamp:context:andEmbedding:timestamp:context:simBoost:minProximitySec:dampedSimilarity:];
-[BWHVSCandidateFrameManager _isFailedCaptureFrameID:];
-[BWHVSCandidateFrameManager _isManualPromotedFrameID:];
-[BWHVSCandidateFrameManager _matchBudgetByManagingExtras];
-[BWHVSCandidateFrameManager _newCandidateFrameFromRealtimeBucket:];
-[BWHVSCandidateFrameManager _newPauseFrameFromInputFrame:];
-[BWHVSCandidateFrameManager _payOffPendingRemovalsForCandidate:];
-[BWHVSCandidateFrameManager _postCleanupBudgetReverification];
-[BWHVSCandidateFrameManager _promoteAgedOutCandidatesWithCurrentTime:];
-[BWHVSCandidateFrameManager _promoteFrame:];
-[BWHVSCandidateFrameManager _promotedFrameSharingRawCaptureWithFrame:];
-[BWHVSCandidateFrameManager _recoverExtrasWithinBudget];
-[BWHVSCandidateFrameManager _resolveBreakPauseDuplicateForNewFrame:comparedToFrame:];
-[BWHVSCandidateFrameManager _resolveBreakPauseDuplicateForNewFrame:comparedToFrameDict:];
-[BWHVSCandidateFrameManager _resolveBreakPauseDuplicateForNewIsPause:newSegmentIdx:newTimestamp:dupIsPause:dupSegmentIdx:dupTimestamp:];
-[BWHVSCandidateFrameManager _resolvePromotedFrameDuplicatesForFrame:removeOnWin:deferredRemovalsOut:];
-[BWHVSCandidateFrameManager _shouldAddCandidate:];
-[BWHVSCandidateFrameManager _silentlyRemoveMaxScoreFrameID:causingFrameID:];
-[BWHVSCandidateFrameManager _totalBudget];
-[BWHVSCandidateFrameManager _tryPromoteFrame:];
-[BWHVSCandidateFrameManager _tryReplaceLowestCandidateOnBudgetFailure:];
-[BWHVSCandidateFrameManager captureFolder];
-[BWHVSCandidateFrameManager earliestAllowedStillImageCaptureHostPTS];
-[BWHVSCandidateFrameManager finalizeCandidates];
-[BWHVSCandidateFrameManager initWithDelegate:hvsConfig:];
-[BWHVSCandidateFrameManager isFixedBudgetExhausted];
-[BWHVSCandidateFrameManager processFrame:];
-[BWHVSCandidateFrameManager registerFailedCaptureFrame:];
-[BWHVSCandidateFrameManager registerManualCaptureFrame:];
-[BWHVSCandidateFrameManager setCaptureFolder:];
-[BWHVSCandidateFrameManager setEarliestAllowedStillImageCaptureHostPTS:];
-[BWHVSCandidateFrameManager setFramePromotionHandler:context:];
-[BWHVSCandidateFrameManager setWaitForEarliestAllowedStillImageCaptureHostPTS:];
-[BWHVSCandidateFrameManager typicalBufferingInSeconds];
-[BWHVSCandidateFrameManager waitForEarliestAllowedStillImageCaptureHostPTS];
```
