# `BWTimeOfFlightSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 11 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
i _numEODMessagesReceived;
d _lastEmittedPTS;
@"BWNodeInput" _videoInput;
@"BWNodeInput" _pointCloudInput;
@"NSMutableArray" _pointCloudBufferQueue;
@"NSMutableArray" _videoBufferQueue;
^{opaqueCMFormatDescription=} _pointCloudFormatDescription;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
i _maxVideoBufferQueueDepth;
i _maxPointCloudBufferQueueDepth;
@"BWDataBufferPool" _dataBufferPool;
```

## Properties

```
@property (T@"BWNodeInput",R,V_videoInput) videoInput;
@property (T@"BWNodeInput",R,V_pointCloudInput) pointCloudInput;
```

## Class methods

```
+[BWTimeOfFlightSynchronizerNode initialize];
```

## Instance methods

```
-[BWTimeOfFlightSynchronizerNode renderSampleBuffer:forInput:];
-[BWTimeOfFlightSynchronizerNode init];
-[BWTimeOfFlightSynchronizerNode dealloc];
-[BWTimeOfFlightSynchronizerNode pointCloudInput];
-[BWTimeOfFlightSynchronizerNode handleDroppedSample:forInput:];
-[BWTimeOfFlightSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWTimeOfFlightSynchronizerNode nodeSubType];
-[BWTimeOfFlightSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWTimeOfFlightSynchronizerNode handleNodeError:forInput:];
-[BWTimeOfFlightSynchronizerNode nodeType];
-[BWTimeOfFlightSynchronizerNode didReachEndOfDataForInput:];
-[BWTimeOfFlightSynchronizerNode videoInput];
```
