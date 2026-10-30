# `BWSlaveFrameSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 13 instance variables, 1 properties, 16 instance methods, 1 class methods

## Instance variables

```
i _numEODMessagesReceived;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
^^{opaqueCMSimpleQueue} _inputSampleBufferQueues;
i _numBufferedFrames;
B _slaveStreamHasStarted;
i _numSlaveFramesReceived;
i _numSlaveFramesToSkip;
B _startEmittingMasterFramesBeforeSlaveStreamStarts;
@"NSMutableArray" _droppedFramePTSs;
i _mostRecentMasterInputIndex;
@"NSArray" _syncSlaveForMasterPortTypes;
B _differentInputFormatsSupported;
B _emitsUnsynchronizedFramesWhileStopping;
```

## Properties

```
@property (TB,N,V_emitsUnsynchronizedFramesWhileStopping) emitsUnsynchronizedFramesWhileStopping;
```

## Class methods

```
+[BWSlaveFrameSynchronizerNode initialize];
```

## Instance methods

```
-[BWSlaveFrameSynchronizerNode prepareForCurrentConfigurationToBecomeLive];
-[BWSlaveFrameSynchronizerNode initWithDepthEnabled:numberOfInputs:syncSlaveForMasterPortTypes:separateDepthComponentsEnabled:preLTMThumbnailEnabled:postColorProcessingThumbnailEnabled:weightSegmentMapEnabled:styledFrameEnabled:lowLightVideoNoiseReductionEnabled:numberOfSecondaryFramesToSkip:sourceNodeSensorRawOutputsEnabled:];
-[BWSlaveFrameSynchronizerNode renderSampleBuffer:forInput:];
-[BWSlaveFrameSynchronizerNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWSlaveFrameSynchronizerNode setEmitsUnsynchronizedFramesWhileStopping:];
-[BWSlaveFrameSynchronizerNode dealloc];
-[BWSlaveFrameSynchronizerNode hasNonLiveConfigurationChanges];
-[BWSlaveFrameSynchronizerNode emitsUnsynchronizedFramesWhileStopping];
-[BWSlaveFrameSynchronizerNode initWithDepthEnabled:numberOfInputs:syncSlaveForMasterPortTypes:separateDepthComponentsEnabled:preLTMThumbnailEnabledInputs:postColorProcessingThumbnailEnabledInputs:weightSegmentMapEnabledInputs:styledFrameEnabledInputs:lowLightVideoNoiseReductionEnabled:differentInputFormatsSupported:numberOfSlaveFramesToSkip:startEmittingMasterFramesBeforeSlaveStreamStarts:sourceNodeSensorRawOutputsEnabled:];
-[BWSlaveFrameSynchronizerNode handleDroppedSample:forInput:];
-[BWSlaveFrameSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWSlaveFrameSynchronizerNode didReachEndOfDataForConfigurationID:input:];
-[BWSlaveFrameSynchronizerNode nodeSubType];
-[BWSlaveFrameSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSlaveFrameSynchronizerNode handleNodeError:forInput:];
-[BWSlaveFrameSynchronizerNode nodeType];
```
