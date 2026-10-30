# `VTFrameProcessor`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"VEFrameProcessor" _veFrameProcessor;
q _processorType;
@"<VTFrameProcessorImplementationPrivate>" _processor;
@"<VTFrameProcessorConfiguration>" _configuration;
@"NSObject<OS_dispatch_queue>" _processFrameQueue;
@"<MTLDevice>" _device;
@"MTLSharedEventListener" _sharedEventListener;
@"NSMutableArray" _sharedEventList;
B _sharedEventListTearingDown;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sharedEventListLock;
^{OpaqueFigReportingAgent=} _reportingAgent;
i _frameCounter;
q _timeSpentInProcessor;
q _submissionMode;
q _motionBlurStrength;
q _numberOfInterpolatedFrames;
q _sourcePixelFormat;
q _sourceFrameRateTotalMeasuredFrames;
d _sourceFrameRateTotalMeasuredDurationSeconds;
q _firstProcessCallTimeMs;
q _lastProcessCallTimeMs;
q _processCallCount;
q _lastErrorCode;
^{OpaqueFigSimpleMutex=} _telemetryMutex;
```

## Instance methods

```
-[VTFrameProcessor init];
-[VTFrameProcessor dealloc];
-[VTFrameProcessor endSession];
-[VTFrameProcessor captureTelemetryFromParametersIfNeeded:];
-[VTFrameProcessor createSharedEventListener];
-[VTFrameProcessor destroySharedEventListener];
-[VTFrameProcessor initializeReportingAgent];
-[VTFrameProcessor internalEndSession];
-[VTFrameProcessor issueReportingAgentEvent];
-[VTFrameProcessor processWithCommandBuffer:parameters:];
-[VTFrameProcessor processWithParameters:completionHandler:];
-[VTFrameProcessor processWithParameters:error:];
-[VTFrameProcessor processWithParameters:frameOutputHandler:];
-[VTFrameProcessor startSessionWithConfiguration:error:];
```
