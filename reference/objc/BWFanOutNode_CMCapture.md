# `BWFanOutNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 22 instance methods, 1 class methods

## Instance variables

```
^@ _outputsCArray;
^B _outputsDiscardsAttachedMedia;
@"NSMutableDictionary" _outputsAllowedAttachedMediaKeys;
@"NSMutableDictionary" _outputsDisallowedAttachedMediaKeys;
i _outputsCount;
B _emitIfAllAttachedMediaDiscarded;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _extendedOutputsLock;
@"NSMutableArray" _extendedOutputs;
@"NSMutableArray" _workIntervalTypes;
```

## Class methods

```
+[BWFanOutNode initialize];
```

## Instance methods

```
-[BWFanOutNode activateExtendedOutput:];
-[BWFanOutNode renderSampleBuffer:forInput:];
-[BWFanOutNode makeCurrentConfigurationLive];
-[BWFanOutNode setEmitIfAllAttachedMediaDiscarded:];
-[BWFanOutNode setDisallowedAttachedMediaKeys:forOutputIndex:];
-[BWFanOutNode dealloc];
-[BWFanOutNode addExtendedOutput];
-[BWFanOutNode hasNonLiveConfigurationChanges];
-[BWFanOutNode setWorkIntervalType:forOutputIndex:];
-[BWFanOutNode initWithFanOutCount:mediaType:];
-[BWFanOutNode setDiscardsAttachedMedia:forOutputIndex:];
-[BWFanOutNode handleDroppedSample:forInput:];
-[BWFanOutNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWFanOutNode didReachEndOfDataForConfigurationID:input:];
-[BWFanOutNode setAllowedAttachedMediaKeys:forOutputIndex:];
-[BWFanOutNode emitIfAllAttachedMediaDiscarded];
-[BWFanOutNode nodeSubType];
-[BWFanOutNode didSelectFormat:forInput:];
-[BWFanOutNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWFanOutNode handleNodeError:forInput:];
-[BWFanOutNode nodeType];
-[BWFanOutNode removeExtendedOutput:];
```
