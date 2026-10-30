# `BWDepthSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 22 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
i _numEODMessagesReceived;
AB _depthInputHasReceivedEOD;
@"NSMutableArray" _imageBufferQueue;
@"NSMutableArray" _depthBufferQueue;
i _maxQueueDepth;
i _lastEmittedFrameCaptureID;
i _lastReceivedImageID;
i _lastReceivedDepthID;
Q _lastReceivedDepthErrorSettingsID;
i _imageIDWrapAroundCounter;
i _depthIDWrapAroundCounter;
B _discardsDegradedDepthBuffers;
B _separateDepthComponentsEnabled;
@"BWNodeInput" _imageInput;
@"BWNodeInput" _depthInput;
B _streaming;
B _flushOnDepthEOD;
@"BWNodeError" _errorForImageInput;
@"BWNodeError" _errorForDepthInput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
{?="value"q"timescale"i"flags"I"epoch"q} _lastReceivedImagePTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastReceivedDepthPTS;
```

## Properties

```
@property (T@"BWNodeInput",R,V_imageInput) imageInput;
@property (T@"BWNodeInput",R,V_depthInput) depthInput;
@property (TB,N) discardsDegradedDepthBuffers;
@property (TB,N,V_flushOnDepthEOD) flushOnDepthEOD;
```

## Class methods

```
+[BWDepthSynchronizerNode initialize];
```

## Instance methods

```
-[BWDepthSynchronizerNode renderSampleBuffer:forInput:];
-[BWDepthSynchronizerNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWDepthSynchronizerNode dealloc];
-[BWDepthSynchronizerNode handleDroppedSample:forInput:];
-[BWDepthSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWDepthSynchronizerNode nodeSubType];
-[BWDepthSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWDepthSynchronizerNode handleNodeError:forInput:];
-[BWDepthSynchronizerNode nodeType];
-[BWDepthSynchronizerNode flushOnDepthEOD];
-[BWDepthSynchronizerNode depthInput];
-[BWDepthSynchronizerNode didReachEndOfDataForInput:];
-[BWDepthSynchronizerNode discardsDegradedDepthBuffers];
-[BWDepthSynchronizerNode imageInput];
-[BWDepthSynchronizerNode initForStreaming:maxQueueDepth:separateDepthComponentsEnabled:];
-[BWDepthSynchronizerNode initForStreaming:separateDepthComponentsEnabled:];
-[BWDepthSynchronizerNode setDiscardsDegradedDepthBuffers:];
-[BWDepthSynchronizerNode setFlushOnDepthEOD:];
```
