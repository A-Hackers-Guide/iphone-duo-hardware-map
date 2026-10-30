# `LDCMMobileAssetManager`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
i _lastProcessedAssetVersion;
I _queryFrequencySec;
I _queryFrequencyToleranceSec;
I _retryQueryFrequencySec;
I _retryQueryFrequencyToleranceSec;
@"<LDCMMobileAssetManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _assetManagerQueue;
@"NSObject<OS_dispatch_source>" _timer;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_assetManagerQueue) assetManagerQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_timer) timer;
@property (Ti,N,V_lastProcessedAssetVersion) lastProcessedAssetVersion;
@property (TI,N,V_queryFrequencySec) queryFrequencySec;
@property (TI,N,V_queryFrequencyToleranceSec) queryFrequencyToleranceSec;
@property (TI,N,V_retryQueryFrequencySec) retryQueryFrequencySec;
@property (TI,N,V_retryQueryFrequencyToleranceSec) retryQueryFrequencyToleranceSec;
@property (T@"<LDCMMobileAssetManagerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[LDCMMobileAssetManager setTimer:];
-[LDCMMobileAssetManager init];
-[LDCMMobileAssetManager timer];
-[LDCMMobileAssetManager setDelegate:];
-[LDCMMobileAssetManager delegate];
-[LDCMMobileAssetManager updateMetadata];
-[LDCMMobileAssetManager queryMetadata];
-[LDCMMobileAssetManager processAsset:];
-[LDCMMobileAssetManager retryQueryFrequencyToleranceSec];
-[LDCMMobileAssetManager downloadCatalog];
-[LDCMMobileAssetManager assetManagerQueue];
-[LDCMMobileAssetManager downloadAsset:];
-[LDCMMobileAssetManager lastProcessedAssetVersion];
-[LDCMMobileAssetManager queryFrequencySec];
-[LDCMMobileAssetManager queryFrequencyToleranceSec];
-[LDCMMobileAssetManager retryQueryFrequencySec];
-[LDCMMobileAssetManager scheduleNextQueryAsRetry:];
-[LDCMMobileAssetManager setAssetManagerQueue:];
-[LDCMMobileAssetManager setLastProcessedAssetVersion:];
-[LDCMMobileAssetManager setQueryFrequencySec:];
-[LDCMMobileAssetManager setQueryFrequencyToleranceSec:];
-[LDCMMobileAssetManager setRetryQueryFrequencySec:];
-[LDCMMobileAssetManager setRetryQueryFrequencyToleranceSec:];
-[LDCMMobileAssetManager supportsCompatabilityVersion:];
```
