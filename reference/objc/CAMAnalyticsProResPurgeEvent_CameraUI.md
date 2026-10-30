# `CAMAnalyticsProResPurgeEvent`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAnalyticsEvent`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B __didUpdateForFirstPurgeOperation;
d __startTime;
@"CAMCaptureGraphConfiguration" __graphConfiguration;
q __totalBytesPurged;
q __purgeOperationCount;
```

## Properties

```
@property (Td,R,N,V__startTime) _startTime;
@property (T@"CAMCaptureGraphConfiguration",R,N,V__graphConfiguration) _graphConfiguration;
@property (TB,N,S_setDidUpdateForFirstPurgeOperation:,V__didUpdateForFirstPurgeOperation) _didUpdateForFirstPurgeOperation;
@property (Tq,N,S_setTotalBytesPurged:,V__totalBytesPurged) _totalBytesPurged;
@property (Tq,N,S_setPurgeOperationCount:,V__purgeOperationCount) _purgeOperationCount;
```

## Instance methods

```
-[CAMAnalyticsProResPurgeEvent _startTime];
-[CAMAnalyticsProResPurgeEvent publish];
-[CAMAnalyticsProResPurgeEvent _graphConfiguration];
-[CAMAnalyticsProResPurgeEvent eventName];
-[CAMAnalyticsProResPurgeEvent _bucketedCount:];
-[CAMAnalyticsProResPurgeEvent _didUpdateForFirstPurgeOperation];
-[CAMAnalyticsProResPurgeEvent _purgeOperationCount];
-[CAMAnalyticsProResPurgeEvent _setDidUpdateForFirstPurgeOperation:];
-[CAMAnalyticsProResPurgeEvent _setPurgeOperationCount:];
-[CAMAnalyticsProResPurgeEvent _setTotalBytesPurged:];
-[CAMAnalyticsProResPurgeEvent _totalBytesPurged];
-[CAMAnalyticsProResPurgeEvent _updateForIsBeforePurge:withFreeBytes:fastPurgeableBytes:slowPurgeableBytes:maxRecordingTimeSeconds:];
-[CAMAnalyticsProResPurgeEvent initWithRequestType:graphConfiguration:totalBytesInSystem:];
-[CAMAnalyticsProResPurgeEvent updateAfterPurgeOperationWithFreeBytes:fastPurgeableBytes:slowPurgeableBytes:maxRecordingTimeSeconds:bytesPurged:];
-[CAMAnalyticsProResPurgeEvent updateBeforePurgeOperationWithFreeBytes:fastPurgeableBytes:slowPurgeableBytes:maxRecordingTimeSeconds:];
-[CAMAnalyticsProResPurgeEvent updateForCancelRequest];
-[CAMAnalyticsProResPurgeEvent updateForSkippedPurgeOperationWithFreeBytes:fastPurgeableBytes:slowPurgeableBytes:maxRecordingTimeSeconds:];
```
