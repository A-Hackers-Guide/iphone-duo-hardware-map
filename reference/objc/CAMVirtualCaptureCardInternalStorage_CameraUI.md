# `CAMVirtualCaptureCardInternalStorage`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStorageContainer`
- 10 instance variables, 16 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _proVideoStorageConfigured;
B _replenishEligible;
B __fetchInFlight;
B __recoveryRequired;
@"<CAMPurgeableStorageContainerDelegate>" _delegate;
@"CAMCaptureGraphConfiguration" _graphConfiguration;
@"NSSet" _busyReasons;
@"NSObject<OS_dispatch_queue>" __operationQueue;
q __cachedTotalFreeBytes;
q __cachedInitialCapacity;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__operationQueue) _operationQueue;
@property (TB,N,V__fetchInFlight) _fetchInFlight;
@property (Tq,N,V__cachedTotalFreeBytes) _cachedTotalFreeBytes;
@property (Tq,N,V__cachedInitialCapacity) _cachedInitialCapacity;
@property (T@"NSSet",C,N,V_busyReasons) busyReasons;
@property (TB,N,V__recoveryRequired) _recoveryRequired;
@property (TB,N,GisProVideoStorageConfigured,V_proVideoStorageConfigured) proVideoStorageConfigured;
@property (TB,N,GisReplenishEligible,V_replenishEligible) replenishEligible;
@property (TB,R,N,GisRecoveryRequired) recoveryRequired;
@property (Tq,R,N) totalFreeBytes;
@property (T@"CAMCaptureGraphConfiguration",&,N,V_graphConfiguration) graphConfiguration;
@property (T@"<CAMPurgeableStorageContainerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMVirtualCaptureCardInternalStorage observeValueForKeyPath:ofObject:change:context:];
-[CAMVirtualCaptureCardInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:verbose:];
-[CAMVirtualCaptureCardInternalStorage init];
-[CAMVirtualCaptureCardInternalStorage dealloc];
-[CAMVirtualCaptureCardInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:completion:];
-[CAMVirtualCaptureCardInternalStorage minimumDiskUsageThresholdInBytesForGraphConfiguration:];
-[CAMVirtualCaptureCardInternalStorage graphConfiguration];
-[CAMVirtualCaptureCardInternalStorage hasDiskSpaceToAllowCaptureWithConfiguration:allowPurging:];
-[CAMVirtualCaptureCardInternalStorage setDelegate:];
-[CAMVirtualCaptureCardInternalStorage totalFreeBytes];
-[CAMVirtualCaptureCardInternalStorage availableRecordingTimeInSecondsForGraphConfiguration:];
-[CAMVirtualCaptureCardInternalStorage setGraphConfiguration:];
-[CAMVirtualCaptureCardInternalStorage delegate];
-[CAMVirtualCaptureCardInternalStorage _operationQueue];
-[CAMVirtualCaptureCardInternalStorage busyReasons];
-[CAMVirtualCaptureCardInternalStorage isRecoveryRequired];
-[CAMVirtualCaptureCardInternalStorage setBusyReasons:];
-[CAMVirtualCaptureCardInternalStorage _cachedInitialCapacity];
-[CAMVirtualCaptureCardInternalStorage _cachedTotalFreeBytes];
-[CAMVirtualCaptureCardInternalStorage _fetchInFlight];
-[CAMVirtualCaptureCardInternalStorage _fetchVirtualCaptureCardStateWithCompletion:];
-[CAMVirtualCaptureCardInternalStorage _recoveryRequired];
-[CAMVirtualCaptureCardInternalStorage _registerForVirtualCaptureCardBusyReasonsUpdates];
-[CAMVirtualCaptureCardInternalStorage _registerForVirtualCaptureCardRecoveryRequiredUpdates];
-[CAMVirtualCaptureCardInternalStorage isProVideoStorageConfigured];
-[CAMVirtualCaptureCardInternalStorage isReplenishEligible];
-[CAMVirtualCaptureCardInternalStorage setProVideoStorageConfigured:];
-[CAMVirtualCaptureCardInternalStorage setReplenishEligible:];
-[CAMVirtualCaptureCardInternalStorage set_cachedInitialCapacity:];
-[CAMVirtualCaptureCardInternalStorage set_cachedTotalFreeBytes:];
-[CAMVirtualCaptureCardInternalStorage set_fetchInFlight:];
-[CAMVirtualCaptureCardInternalStorage set_recoveryRequired:];
```
