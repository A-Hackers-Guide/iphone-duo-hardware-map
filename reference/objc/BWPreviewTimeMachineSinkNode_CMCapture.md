# `BWPreviewTimeMachineSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- Protocols: `BWPreviewTimeMachineProcessor`
- 15 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _device;
@"NSObject<OS_dispatch_queue>" _processingQueue;
@"NSMutableArray" _timeMachineFrames;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _timeMachineLock;
i _timeMachineCapacity;
@"FigStateMachine" _stateMachine;
{?="value"q"timescale"i"flags"I"epoch"q} _earliestAllowedPTS;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _requestedSuspendPTSRange;
@? _suspendCompletionHandler;
@"FigCaptureImageMotionDetector" _motionDetector;
B _faceMotionDetectionEnabled;
B _smartCameraMotionDetectionEnabled;
B _haveFrameRotationAndMirror;
i _frameRotationDegrees;
B _frameMirrored;
```

## Properties

```
@property (T{?=qiIq}) earliestAllowedPTS;
@property (T{?=ii},R) frameDimensions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPreviewTimeMachineSinkNode initialize];
```

## Instance methods

```
-[BWPreviewTimeMachineSinkNode prepareForCurrentConfigurationToBecomeLive];
-[BWPreviewTimeMachineSinkNode renderSampleBuffer:forInput:];
-[BWPreviewTimeMachineSinkNode dealloc];
-[BWPreviewTimeMachineSinkNode handleDroppedSample:forInput:];
-[BWPreviewTimeMachineSinkNode nodeSubType];
-[BWPreviewTimeMachineSinkNode resume];
-[BWPreviewTimeMachineSinkNode frameDimensions];
-[BWPreviewTimeMachineSinkNode detectMotionOnStoredFramesWithSmartCameraDiagnostics:completionHandler:];
-[BWPreviewTimeMachineSinkNode didReachEndOfDataForInput:];
-[BWPreviewTimeMachineSinkNode earliestAllowedPTS];
-[BWPreviewTimeMachineSinkNode initWithCaptureDevice:processingQueuePriority:timeMachineCapacity:smartCameraMotionDetectionEnabled:sinkID:];
-[BWPreviewTimeMachineSinkNode setEarliestAllowedPTS:];
-[BWPreviewTimeMachineSinkNode suspendWithPTSRange:completionHandler:];
```
