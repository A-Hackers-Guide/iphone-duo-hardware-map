# `AVAssetWritingPlanner`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSURL" _sessionSegmentFileDirectory;
^{OpaqueFigSimpleMutex=} _sessionMutex;
B _writingSessionStarted;
@"NSMutableArray" _trackPlanExecutors;
@? _completionHandlerBlock;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"AVAssetWritingPlannerIncrementalState" _incrementalState;
@"AVAssetWritingPlannerProgress" _progress;
B _wasResumedFromPriorRun;
```

## Properties

```
@property (T@"AVAssetWritingPlannerProgress",R,V_progress) progress;
```

## Class methods

```
+[AVAssetWritingPlanner segmentBoundaryGuidelinesForVideoCodecType:videoEncoderSpecification:];
+[AVAssetWritingPlanner segmentBoundaryRecommendationsForVideoAVAssetTrack:minimumSegmentDuration:minimumSegmentFrameCount:];
+[AVAssetWritingPlanner validateDirectoryForTemporaryFiles:failureReason:];
```

## Instance methods

```
-[AVAssetWritingPlanner dealloc];
-[AVAssetWritingPlanner progress];
-[AVAssetWritingPlanner buildAssemblyComposition:];
-[AVAssetWritingPlanner executePlanOnQueue:withCompletionHandler:];
-[AVAssetWritingPlanner executePlanWithCompletionHandler:];
-[AVAssetWritingPlanner hasTrackPlanExecutorForTrack:];
-[AVAssetWritingPlanner initWithDirectoryForTemporaryFiles:];
-[AVAssetWritingPlanner issuePlannerTelemetry];
-[AVAssetWritingPlanner makeFreshIncrementalState];
-[AVAssetWritingPlanner makeIncrementalStateByResumptionOrStartFresh:];
-[AVAssetWritingPlanner planTrack:withSegmentsGeneratedBy:];
-[AVAssetWritingPlanner saveIncrementalState:];
-[AVAssetWritingPlanner writeSegmentsInTracks];
```
