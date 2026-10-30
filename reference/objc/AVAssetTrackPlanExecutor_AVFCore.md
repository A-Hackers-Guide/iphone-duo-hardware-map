# `AVAssetTrackPlanExecutor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"AVAssetTrackPlan" _trackPlan;
@? _writingSegmentCallbackBlock;
@"NSObject<OS_dispatch_semaphore>" _writingSemaphore;
{?="value"q"timescale"i"flags"I"epoch"q} _segmentOverlapDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _segmentFlushDuration;
I _aspFrequency;
```

## Properties

```
@property (TB,R) requiresCompression;
@property (Ti,R) assemblyTrackID;
@property (T@"NSString",R) mediaType;
@property (TI,R) mediaSubType;
@property (T{?=qiIq},R) segmentOverlapDuration;
@property (T{?=qiIq},R) segmentFlushDuration;
@property (TI,R) aspFrequency;
@property (T@"AVAssetTrackPlan",R) trackPlan;
```

## Class methods

```
+[AVAssetTrackPlanExecutor executorForTrackPlan:segmentWritingCallbackBlock:];
```

## Instance methods

```
-[AVAssetTrackPlanExecutor dealloc];
-[AVAssetTrackPlanExecutor mediaType];
-[AVAssetTrackPlanExecutor mediaSubType];
-[AVAssetTrackPlanExecutor assemblyTrackID];
-[AVAssetTrackPlanExecutor callWritingSegmentCallbackForTrack:mediaType:mediaSubType:segmentOverlapDuration:segmentFlushDuration:segmentState:isFirstSegment:isLastSegment:initialClientState:finalClientState:initialCompressionSessionState:finalCompressionSessionState:progress:error:];
-[AVAssetTrackPlanExecutor makeFreshState:];
-[AVAssetTrackPlanExecutor aspFrequency];
-[AVAssetTrackPlanExecutor initWithTrackPlan:segmentWritingCallbackBlock:];
-[AVAssetTrackPlanExecutor makeSegmentURLFromBaseURL:trackID:segmentIndex:];
-[AVAssetTrackPlanExecutor requiresCompression];
-[AVAssetTrackPlanExecutor segmentFlushDuration];
-[AVAssetTrackPlanExecutor segmentOverlapDuration];
-[AVAssetTrackPlanExecutor trackPlan];
```
