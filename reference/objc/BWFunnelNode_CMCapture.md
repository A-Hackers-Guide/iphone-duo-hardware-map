# `BWFunnelNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _holdMessagesUntilAllInputsAreLive;
@"NSMutableArray" _queuedMessages;
@"NSMutableArray" _inputsForQueuedMessages;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
B _running;
@"NSMutableDictionary" _tagsByInputIndices;
```

## Class methods

```
+[BWFunnelNode initialize];
```

## Instance methods

```
-[BWFunnelNode prepareForCurrentConfigurationToBecomeLive];
-[BWFunnelNode renderSampleBuffer:forInput:];
-[BWFunnelNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWFunnelNode initWithNumberOfInputs:mediaType:holdMessages:];
-[BWFunnelNode initWithNumberOfInputs:mediaType:];
-[BWFunnelNode dealloc];
-[BWFunnelNode setTag:forInput:];
-[BWFunnelNode handleDroppedSample:forInput:];
-[BWFunnelNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWFunnelNode addExtendedInput];
-[BWFunnelNode didReachEndOfDataForConfigurationID:input:];
-[BWFunnelNode nodeSubType];
-[BWFunnelNode _handleMessage:fromInput:];
-[BWFunnelNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFunnelNode handleNodeError:forInput:];
-[BWFunnelNode nodeType];
```
