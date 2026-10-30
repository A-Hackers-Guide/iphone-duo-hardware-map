# `BWCrossoverNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 1 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
```

## Class methods

```
+[BWCrossoverNode initialize];
```

## Instance methods

```
-[BWCrossoverNode prepareForCurrentConfigurationToBecomeLive];
-[BWCrossoverNode renderSampleBuffer:forInput:];
-[BWCrossoverNode initWithMediaType:numberOfInputs:];
-[BWCrossoverNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWCrossoverNode allInputsHaveReachedState:];
-[BWCrossoverNode handleDroppedSample:forInput:];
-[BWCrossoverNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWCrossoverNode didReachEndOfDataForConfigurationID:input:];
-[BWCrossoverNode nodeSubType];
-[BWCrossoverNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCrossoverNode handleNodeError:forInput:];
-[BWCrossoverNode nodeType];
```
