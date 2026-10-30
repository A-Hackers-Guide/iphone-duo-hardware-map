# `CAMInternalStorage`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMPurgeableStorageContainer`
- 15 instance variables, 24 properties, 63 instance methods, 0 class methods

## Instance variables

```
B __purging;
B __shouldCancelNextPurge;
B __isLockScreenExtension;
@"<CAMPurgeableStorageContainerDelegate>" _delegate;
@"CAMCaptureGraphConfiguration" _graphConfiguration;
q __cachedLowDiskThreshold;
@"NSDate" __lastPurgeRequestUpdateTime;
@"NSObject<OS_dispatch_queue>" __cacheDeleteQueryQueue;
^{CacheDeleteToken=} __queryQueue_currentToken;
@"NSByteCountFormatter" __byteFormatter;
q __proResMinimumDiskUsageThreshold;
q __fastPurgeThreshold;
@"NSURL" __storageMountPoint;
@"NSObject<OS_dispatch_queue>" __diskSpaceQueue;
{?="freeBytes"q"fastPurgeableBytes"q"slowPurgeableBytes"q} __cachedEstimatedSpace;
```

## Properties

```
@property (Tq,N,V__cachedLowDiskThreshold) _cachedLowDiskThreshold;
@property (T@"NSDate",&,N,V__lastPurgeRequestUpdateTime) _lastPurgeRequestUpdateTime;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__cacheDeleteQueryQueue) _cacheDeleteQueryQueue;
@property (T^{CacheDeleteToken=},N,V__queryQueue_currentToken) _queryQueue_currentToken;
@property (TB,N,S_setPurging:,V__purging) _purging;
@property (TB,N,S_setShouldCancelNextPurge:,V__shouldCancelNextPurge) _shouldCancelNextPurge;
@property (T{?=qqq},N,S_setCachedEstimatedSpace:,V__cachedEstimatedSpace) _cachedEstimatedSpace;
@property (T@"NSByteCountFormatter",R,N,V__byteFormatter) _byteFormatter;
@property (Tq,N,S_setProResMinimumDiskUsageThreshold:,V__proResMinimumDiskUsageThreshold) _proResMinimumDiskUsageThreshold;
@property (Tq,N,S_setFastPurgeThreshold:,V__fastPurgeThreshold) _fastPurgeThreshold;
@property (T@"NSURL",&,N,V__storageMountPoint) _storageMountPoint;
@property (Tq,R,N) _totalBytes;
@property (TB,R,N,V__isLockScreenExtension) _isLockScreenExtension;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__diskSpaceQueue) _diskSpaceQueue;
@property (TB,R,N,GisPurging) purging;
@property (TB,R,N,GisCancelingPurge) cancelingPurge;
@property (TB,R,N,GhasPurgeableResources) hasPurgeableResources;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N) totalFreeBytes;
@property (T@"CAMCaptureGraphConfiguration",&,N,V_graphConfiguration) graphConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMInternalStorage set_queryQueue_currentToken:];
-[CAMInternalStorage _cachedLowDiskThreshold];
-[CAMInternalStorage _absoluteMinimumBytesForMode:];
-[CAMInternalStorage _cacheDeleteVolume];
-[CAMInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:verbose:];
-[CAMInternalStorage _purging];
-[CAMInternalStorage _queryQueue_purgeFastPurgeableResourcesWithThreshold:analyticsEvent:];
-[CAMInternalStorage _hasDiskSpaceToAllowCaptureWithConfiguration:totalFreeBytes:allowPurging:verbose:];
-[CAMInternalStorage _updatePurgeRequestStateForConfiguration:totalFreeBytes:];
-[CAMInternalStorage init];
-[CAMInternalStorage _notifyDelegateOfPurgeCompletionAndUpdateContinuousPurgeWithForceStopWithReason:analyticsEvent:];
-[CAMInternalStorage _queryQueue_cancelCurrentPurge];
-[CAMInternalStorage cancelPurge];
-[CAMInternalStorage _statMountPoint:];
-[CAMInternalStorage _setProResMinimumDiskUsageThreshold:];
-[CAMInternalStorage _availableRecordingTimeInMinutesForFreeBytes:minimumDiskUsageThreshold:bytesPerMinute:];
-[CAMInternalStorage _stringFromAvailableSpace:];
-[CAMInternalStorage _cacheDeleteQueryQueue];
-[CAMInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:completion:];
-[CAMInternalStorage _storageMountPoint];
-[CAMInternalStorage _totalBytes];
-[CAMInternalStorage minimumDiskUsageThresholdInBytesForGraphConfiguration:];
-[CAMInternalStorage _setCachedEstimatedSpace:];
-[CAMInternalStorage graphConfiguration];
-[CAMInternalStorage set_cachedLowDiskThreshold:];
-[CAMInternalStorage _shouldCancelNextPurge];
-[CAMInternalStorage _setPurging:];
-[CAMInternalStorage _setFastPurgeThreshold:];
-[CAMInternalStorage hasPurgeableResources];
-[CAMInternalStorage _updateAvailablePurgeableSpaceAsync];
-[CAMInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:];
-[CAMInternalStorage setDelegate:];
-[CAMInternalStorage purgeFastPurgeableSpaceWithRequestType:];
-[CAMInternalStorage totalFreeBytes];
-[CAMInternalStorage isCancelingPurge];
-[CAMInternalStorage _preferredMinimumBytesForConfiguration:];
-[CAMInternalStorage _queryQueue_queryAvailableSpaceAndUpdateCachedEstimatesForBytesPerMinute:minimumDiskUsageThreshold:];
-[CAMInternalStorage _cachedEstimatedSpace];
-[CAMInternalStorage _fastPurgeThreshold];
-[CAMInternalStorage _requestTypeFromNonZeroFastPurgeThreshold:];
-[CAMInternalStorage _loadFreeDiskThresholds];
-[CAMInternalStorage _copyAndApplyByteStringFormattingFromDictionary:toDictionary:keys:];
-[CAMInternalStorage availableRecordingTimeInSecondsForGraphConfiguration:];
-[CAMInternalStorage setGraphConfiguration:];
-[CAMInternalStorage delegate];
-[CAMInternalStorage _queryQueue_updatePurgeRequestStateForTotalFreeBytes:preferredFreeBytes:];
-[CAMInternalStorage _stringFromByteCount:];
-[CAMInternalStorage _resourceValueForKey:];
-[CAMInternalStorage _isLockScreenExtension];
-[CAMInternalStorage _purgeFastPurgeableSpaceWithThreshold:calledFromPurgeCompletion:forceStopReason:analyticsEvent:];
-[CAMInternalStorage _byteFormatter];
-[CAMInternalStorage _queryQueue_currentToken];
-[CAMInternalStorage _lastPurgeRequestUpdateTime];
-[CAMInternalStorage _queryQueue_aggregateLowDiskEventWithIdentifier:];
-[CAMInternalStorage _proResMinimumDiskUsageThreshold];
-[CAMInternalStorage set_lastPurgeRequestUpdateTime:];
-[CAMInternalStorage reportLowDiskEventWithIdentifier:];
-[CAMInternalStorage _fastPurgeThresholdForRequestType:];
-[CAMInternalStorage isPurging];
-[CAMInternalStorage set_storageMountPoint:];
-[CAMInternalStorage _copyFromDictionary:toDictionary:keys:];
-[CAMInternalStorage _setShouldCancelNextPurge:];
-[CAMInternalStorage _diskSpaceQueue];
```
