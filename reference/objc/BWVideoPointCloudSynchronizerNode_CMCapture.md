# `BWVideoPointCloudSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWFigVideoCaptureDeviceMaxDepthFrameRateChangedDelegate`
- 15 instance variables, 6 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"BWFigVideoCaptureDevice" _captureDevice;
@"BWNodeInput" _imageInput;
@"BWNodeInput" _pointCloudInput;
f _depthMaxFrameRate;
B _depthMaxFrameRateAdjustmentPending;
s _numberOfReceivedRGBFramesBeforeEmittingDepthFrame;
s _numberOfReceivedRGBFramesSinceLastDepthFrameEmission;
B _shouldLetThroughFrames;
@"NSMutableArray" _latestPointCloudBuffers;
Q _numberOfReceivedPointCloudFramesBeforeEmitted;
i _latestPointCloudBuffersCapacity;
i _indexForLatestReceivedPointCloudFrame;
B _multiplePointCloudAttachmentsEnabled;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _numEODMessagesReceived;
```

## Properties

```
@property (T@"BWNodeInput",R,N,V_imageInput) imageInput;
@property (T@"BWNodeInput",R,N,V_pointCloudInput) pointCloudInput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWVideoPointCloudSynchronizerNode initialize];
```

## Instance methods

```
-[BWVideoPointCloudSynchronizerNode renderSampleBuffer:forInput:];
-[BWVideoPointCloudSynchronizerNode dealloc];
-[BWVideoPointCloudSynchronizerNode pointCloudInput];
-[BWVideoPointCloudSynchronizerNode handleDroppedSample:forInput:];
-[BWVideoPointCloudSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWVideoPointCloudSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWVideoPointCloudSynchronizerNode _tryToEmitBuffersWithRGBBuffer:];
-[BWVideoPointCloudSynchronizerNode _attachPointCloudDataToSampleBuffer:];
-[BWVideoPointCloudSynchronizerNode _setUpPointCloudMediaConfigurationForOutput:inputAttachedMediaKey:outputAttachedMediaKey:];
-[BWVideoPointCloudSynchronizerNode _shouldEmitBuffer];
-[BWVideoPointCloudSynchronizerNode _updateNumberOfReceivedRGBFramesBeforeEmittingDepthFrameWithDepthMaxFrameRate:rgbMaxFrameRate:];
-[BWVideoPointCloudSynchronizerNode didChangeDepthMaxFrameRate:];
-[BWVideoPointCloudSynchronizerNode didReachEndOfDataForInput:];
-[BWVideoPointCloudSynchronizerNode imageInput];
-[BWVideoPointCloudSynchronizerNode initWithCaptureDevice:timeOfFlightCameraType:];
```
