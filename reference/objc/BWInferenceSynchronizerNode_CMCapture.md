# `BWInferenceSynchronizerNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 12 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _mostRecentEmittedCaptureIdentifierByPortType;
i _indexOfInputProvidingOutputSampleBuffer;
i _indexOfInputProvidingOnlyInferences;
i _indexOfInputProvidingPreferredInferences;
[2{?="bufferQueue"@"NSMutableArray""mostRecentError"@"BWNodeError""mostRecentCaptureIdentifierByPortType"@"NSMutableDictionary""numberOfWraparoundsByPortType"@"NSMutableDictionary""inputIsLive"B}] _contexts;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferServicingLock;
C _maximumNumberOfInflightBuffers;
S _errorHandlingModel;
B _synchronizesTopLevelAttachments;
@"NSSet" _attachedMediaKeysToSkip;
B _allowOutOfOrderInputs;
@? _synchronizeInferencesResolver;
```

## Properties

```
@property (TS,R,N,V_errorHandlingModel) errorHandlingModel;
@property (T@"BWNodeInput",R,N) inputProvidingOutputSampleBuffer;
@property (T@"BWNodeInput",R,N) inputProvidingOnlyInferences;
@property (T@"BWNodeInput",R,N) inputProvidingPreferredInferences;
@property (TB,N,V_synchronizesTopLevelAttachments) synchronizesTopLevelAttachments;
@property (T@"NSSet",&,N,V_attachedMediaKeysToSkip) attachedMediaKeysToSkip;
@property (TB,N,V_allowOutOfOrderInputs) allowOutOfOrderInputs;
@property (T@?,C,N,V_synchronizeInferencesResolver) synchronizeInferencesResolver;
```

## Class methods

```
+[BWInferenceSynchronizerNode initialize];
```

## Instance methods

```
-[BWInferenceSynchronizerNode attachedMediaKeysToSkip];
-[BWInferenceSynchronizerNode renderSampleBuffer:forInput:];
-[BWInferenceSynchronizerNode synchronizesTopLevelAttachments];
-[BWInferenceSynchronizerNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:];
-[BWInferenceSynchronizerNode setSynchronizeInferencesResolver:];
-[BWInferenceSynchronizerNode synchronizeInferencesResolver];
-[BWInferenceSynchronizerNode init];
-[BWInferenceSynchronizerNode inputProvidingPreferredInferences];
-[BWInferenceSynchronizerNode dealloc];
-[BWInferenceSynchronizerNode setAllowOutOfOrderInputs:];
-[BWInferenceSynchronizerNode setAttachedMediaKeysToSkip:];
-[BWInferenceSynchronizerNode inputProvidingOnlyInferences];
-[BWInferenceSynchronizerNode initWithIndexOfInputProvidingOutputSampleBuffer:indexOfInputProvidingPreferredInferences:errorHandlingModel:];
-[BWInferenceSynchronizerNode handleDroppedSample:forInput:];
-[BWInferenceSynchronizerNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWInferenceSynchronizerNode didReachEndOfDataForConfigurationID:input:];
-[BWInferenceSynchronizerNode nodeSubType];
-[BWInferenceSynchronizerNode allowOutOfOrderInputs];
-[BWInferenceSynchronizerNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWInferenceSynchronizerNode setSynchronizesTopLevelAttachments:];
-[BWInferenceSynchronizerNode handleNodeError:forInput:];
-[BWInferenceSynchronizerNode inputProvidingOutputSampleBuffer];
-[BWInferenceSynchronizerNode nodeType];
-[BWInferenceSynchronizerNode errorHandlingModel];
```
