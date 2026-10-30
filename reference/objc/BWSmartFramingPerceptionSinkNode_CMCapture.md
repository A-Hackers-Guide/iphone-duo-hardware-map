# `BWSmartFramingPerceptionSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- Protocols: `BWInferenceFormatProvider`
- 14 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _captureDevice;
@"BWInferenceScheduler" _inferenceScheduler;
@"BWInferenceEngine" _inferenceEngine;
@"BWInferenceProcessingConfiguration" _inferenceProcessingConfiguration;
i _camGazeInferenceType;
I _camGazeInferenceMajorVersion;
I _maxFaceCountForInference;
@"NSObject<OS_dispatch_queue>" _inferenceQueue;
B _previousInferenceComplete;
{?="value"q"timescale"i"flags"I"epoch"q} _inferenceSkipInterval;
{?="value"q"timescale"i"flags"I"epoch"q} _lastInferenceFramePTS;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _inferenceLock;
@"NSMutableArray" _faceGroupIDsForInference;
^{opaqueCMSampleBuffer=} _lastSampleBuffer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSmartFramingPerceptionSinkNode initialize];
```

## Instance methods

```
-[BWSmartFramingPerceptionSinkNode prepareForCurrentConfigurationToBecomeLive];
-[BWSmartFramingPerceptionSinkNode _waitForInferenceToComplete];
-[BWSmartFramingPerceptionSinkNode renderSampleBuffer:forInput:];
-[BWSmartFramingPerceptionSinkNode outputFormatForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode inputVideoFormatForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode dealloc];
-[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:];
-[BWSmartFramingPerceptionSinkNode hasNonLiveConfigurationChanges];
-[BWSmartFramingPerceptionSinkNode _releaseResources];
-[BWSmartFramingPerceptionSinkNode inputInferenceVideoFormatForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode outputVideoFormatForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode inputFormatForAttachedMediaKey:];
-[BWSmartFramingPerceptionSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWSmartFramingPerceptionSinkNode nodeSubType];
-[BWSmartFramingPerceptionSinkNode nodeType];
```
