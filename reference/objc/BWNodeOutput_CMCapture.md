# `BWNodeOutput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureOSStateDataProvider`
- 35 instance variables, 45 properties, 94 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"<BWNodeOutputConsumer>" _consumer;
B _consumerIsANodeConnection;
B _mediaTypeIsVideo;
B _mediaTypeIsPointCloud;
B _mediaTypeIsSecureVideo;
I _mediaType;
@"BWNode" _node;
f _maxSampleDataOutputRate;
B _dropsSampleBuffersWithUnexpectedPTS;
q _requestedConfigurationID;
q _liveConfigurationID;
B _discardsSampleData;
I _numberOfBuffersReceived;
I _numberOfBuffersDropped;
I _numberOfConfigurationDidBecomeLiveMessagesReceived;
I _numberOfConfigurationEndOfDataReceived;
I _numberOfEndOfDataMessagesReceived;
I _numberOfDataDroppedMessagesReceived;
{?="value"q"timescale"i"flags"I"epoch"q} _lastValidPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastEmittedPTS;
^{OpaqueFigSimpleMutex=} _poolPreallocationMutex;
@"NSMutableArray" _poolPreallocationCompletionHandlers;
B _poolPreallocationEnabled;
B _poolPreallocationDone;
B _receivedEOD;
@"BWNodeOutputMediaConfiguration" _primaryMediaConfiguration;
@"BWNodeOutputMediaConfiguration" _unspecifiedAttachedMediaConfiguration;
@"NSMutableDictionary" _attachedMediaConfigurations;
@"BWNodeOutputMediaProperties" _primaryMediaProperties;
@"NSMutableDictionary" _attachedMediaProperties;
@"BWMemoryPool" _memoryPool;
@"NSObject<OS_dispatch_semaphore>" _sourceEmitSemaphore;
I _numberOfBuffersEmitted;
q _preparedConfigurationID;
```

## Properties

```
@property (T@"BWFormatRequirements",C,N) formatRequirements;
@property (TB,N) providesPixelBufferPool;
@property (TB,N) providesDataBufferPool;
@property (TB,N) pixelBufferPoolProvidesBackPressure;
@property (TB,N) pixelBufferPoolReportSlowBackPressureAllocations;
@property (T@"BWPixelBufferPool",R,N) preparedPixelBufferPool;
@property (T@"BWDataBufferPool",R,N) preparedDataBufferPool;
@property (Ti,N) passthroughMode;
@property (Ti,N) indexOfInputWhichDrivesThisOutput;
@property (Ti,N) retainedBufferCount;
@property (Ti,N) owningNodeRetainedBufferCount;
@property (T@"BWFormat",C,N) format;
@property (T@"BWVideoFormat",R,N) videoFormat;
@property (T@"BWPointCloudFormat",R,N) pointCloudFormat;
@property (T@"BWFormat",R,N) liveFormat;
@property (T@"BWPixelBufferPool",R,N) livePixelBufferPool;
@property (T@"BWDataBufferPool",R,N) liveDataBufferPool;
@property (TB,R,N,V_mediaTypeIsVideo) mediaTypeIsVideo;
@property (TB,R,N,V_mediaTypeIsPointCloud) mediaTypeIsPointCloud;
@property (TB,R,N,V_mediaTypeIsSecureVideo) mediaTypeIsSecureVideo;
@property (T@"NSString",C,N) name;
@property (TI,R,N,V_mediaType) mediaType;
@property (T@"BWNode",R,W,N,V_node) node;
@property (T@"<BWNodeOutputConsumer>",N) consumer;
@property (T@"BWNodeConnection",R,N) connection;
@property (Tq,N,V_requestedConfigurationID) requestedConfigurationID;
@property (Tq,N,V_preparedConfigurationID) preparedConfigurationID;
@property (T@"BWNodeOutputMediaConfiguration",R,N,V_primaryMediaConfiguration) primaryMediaConfiguration;
@property (T@"NSArray",R,N) specifiedAttachedMediaKeys;
@property (T@"BWNodeOutputMediaConfiguration",&,N,V_unspecifiedAttachedMediaConfiguration) unspecifiedAttachedMediaConfiguration;
@property (T@"BWNodeOutputMediaProperties",R,N,V_primaryMediaProperties) primaryMediaProperties;
@property (T@"NSArray",R,N) resolvedAttachedMediaKeys;
@property (Tf,N,V_maxSampleDataOutputRate) maxSampleDataOutputRate;
@property (TB,N,V_dropsSampleBuffersWithUnexpectedPTS) dropsSampleBuffersWithUnexpectedPTS;
@property (Tq,R,N,V_liveConfigurationID) liveConfigurationID;
@property (TB,N,V_discardsSampleData) discardsSampleData;
@property (TB,N,V_poolPreallocationEnabled) poolPreallocationEnabled;
@property (TI,R,N,V_numberOfBuffersEmitted) numberOfBuffersEmitted;
@property (TI,R,N,V_numberOfBuffersDropped) numberOfBuffersDropped;
@property (T@"BWMemoryPool",&,N,V_memoryPool) memoryPool;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_sourceEmitSemaphore) sourceEmitSemaphore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWNodeOutput initialize];
```

## Instance methods

```
-[BWNodeOutput pixelBufferPoolProvidesBackPressure];
-[BWNodeOutput _passthroughModeForAttachedMediaKey:];
-[BWNodeOutput mediaTypeIsSecureVideo];
-[BWNodeOutput resolvedAttachedMediaKeys];
-[BWNodeOutput pixelBufferPoolReportSlowBackPressureAllocations];
-[BWNodeOutput videoFormat];
-[BWNodeOutput numberOfBuffersDropped];
-[BWNodeOutput indexOfInputWhichDrivesThisOutput];
-[BWNodeOutput primaryMediaProperties];
-[BWNodeOutput osStatePropertyList];
-[BWNodeOutput providesPixelBufferPool];
-[BWNodeOutput liveConfigurationID];
-[BWNodeOutput logGraphTimeoutState];
-[BWNodeOutput setUnspecifiedAttachedMediaConfiguration:];
-[BWNodeOutput setProvidesPixelBufferPool:];
-[BWNodeOutput setRequestedConfigurationID:];
-[BWNodeOutput setFormatRequirements:];
-[BWNodeOutput unspecifiedAttachedMediaConfiguration];
-[BWNodeOutput liveFormat];
-[BWNodeOutput mediaTypeIsPointCloud];
-[BWNodeOutput suspendResources];
-[BWNodeOutput initWithMediaType:node:];
-[BWNodeOutput mediaPropertiesForAttachedMediaKey:];
-[BWNodeOutput specifiedAttachedMediaKeys];
-[BWNodeOutput primaryMediaConfiguration];
-[BWNodeOutput mediaTypeIsVideo];
-[BWNodeOutput setOwningNodeRetainedBufferCount:];
-[BWNodeOutput setProvidesDataBufferPool:];
-[BWNodeOutput setIndexOfInputWhichDrivesThisOutput:];
-[BWNodeOutput setPixelBufferPoolReportSlowBackPressureAllocations:];
-[BWNodeOutput setPixelBufferPoolProvidesBackPressure:];
-[BWNodeOutput formatRequirements];
-[BWNodeOutput owningNodeRetainedBufferCount];
-[BWNodeOutput setDropsSampleBuffersWithUnexpectedPTS:];
-[BWNodeOutput setPassthroughMode:];
-[BWNodeOutput _mediaPropertiesForPossiblyUnspecifiedAttachedMediaKey:];
-[BWNodeOutput passthroughMode];
-[BWNodeOutput setMemoryPool:];
-[BWNodeOutput _clearAllMediaProperties];
-[BWNodeOutput emitDroppedSample:];
-[BWNodeOutput setRetainedBufferCount:];
-[BWNodeOutput setPreparedSharedPixelBufferPool:];
-[BWNodeOutput markEndOfLiveOutput];
-[BWNodeOutput dealloc];
-[BWNodeOutput makeConfiguredFormatLive];
-[BWNodeOutput preparedPixelBufferPool];
-[BWNodeOutput emitStillImageReferenceFrameBracketedCaptureSequenceNumberMessageWithSequenceNumber:];
-[BWNodeOutput prepareForConfiguredFormatToBecomeLive];
-[BWNodeOutput pointCloudFormat];
-[BWNodeOutput sourceEmitSemaphore];
-[BWNodeOutput setPoolPreallocationEnabled:];
-[BWNodeOutput retainedBufferCount];
-[BWNodeOutput emitSampleBuffer:];
-[BWNodeOutput node];
-[BWNodeOutput invalidate];
-[BWNodeOutput setNodePreparedDataBufferPool:];
-[BWNodeOutput mediaConfigurationForAttachedMediaKey:];
-[BWNodeOutput setMediaConfiguration:forAttachedMediaKey:];
-[BWNodeOutput _mediaConfigurationForBufferCountOfPossiblyUnspecifiedAttachedMediaKey:];
-[BWNodeOutput liveDataBufferPool];
-[BWNodeOutput _mediaConfigurationForPossiblyUnspecifiedAttachedMediaKey:];
-[BWNodeOutput setPreparedConfigurationID:];
-[BWNodeOutput attachedMediaKeyDrivenByInputAttachedMediaKey:inputIndex:];
-[BWNodeOutput numberOfBuffersEmitted];
-[BWNodeOutput connection];
-[BWNodeOutput _setMediaProperties:forAttachedMediaKey:];
-[BWNodeOutput emitNodeError:];
-[BWNodeOutput poolPreallocationEnabled];
-[BWNodeOutput description];
-[BWNodeOutput setName:];
-[BWNodeOutput setConsumer:];
-[BWNodeOutput setMaxSampleDataOutputRate:];
-[BWNodeOutput emitStillImagePrewarmMessageWithSettings:resourceConfig:];
-[BWNodeOutput discardsSampleData];
-[BWNodeOutput setFormat:];
-[BWNodeOutput preparedConfigurationID];
-[BWNodeOutput setPreparedSharedDataBufferPool:];
-[BWNodeOutput providesDataBufferPool];
-[BWNodeOutput _passthroughModeForUnspecifiedAttachedMedia];
-[BWNodeOutput mediaType];
-[BWNodeOutput livePixelBufferPool];
-[BWNodeOutput preparedDataBufferPool];
-[BWNodeOutput dropsSampleBuffersWithUnexpectedPTS];
-[BWNodeOutput consumer];
-[BWNodeOutput memoryPool];
-[BWNodeOutput setNodePreparedPixelBufferPool:];
-[BWNodeOutput setSourceEmitSemaphore:];
-[BWNodeOutput requestedConfigurationID];
-[BWNodeOutput addPoolPreallocationCompletionHandler:];
-[BWNodeOutput format];
-[BWNodeOutput name];
-[BWNodeOutput markEndOfLiveOutputForConfigurationID:];
-[BWNodeOutput maxSampleDataOutputRate];
-[BWNodeOutput setDiscardsSampleData:];
```
