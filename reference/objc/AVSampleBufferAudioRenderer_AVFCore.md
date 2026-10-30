# `AVSampleBufferAudioRenderer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVContentKeyRecipientInternal`, `AVContentKeyRecipient`, `AVIntegrityChecking`, `AVMediaDataRequesterConsumer`, `AVQueuedSampleBufferRenderingInternal`, `AVQueuedSampleBufferRendering`
- 1 instance variables, 27 properties, 52 instance methods, 3 class methods

## Instance variables

```
@"AVSampleBufferAudioRendererInternal" _audioRendererInternal;
```

## Properties

```
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (T@"NSUUID",?,R,N) uniqueIdentifier;
@property (TB,?,R,N) disallowsLoggingURLs;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@?,C,N,G_cancelPendingSwiftAsyncEnqueueHandler,S_setCancelPendingSwiftAsyncEnqueueHandler:) cancelPendingSwiftAsyncEnqueueHandler;
@property (T@?,C,N,G_readyForMoreMediaDataHandler,S_setReadyForMoreMediaDataHandler:) readyForMoreMediaDataHandler;
@property (Tq,R,N) status;
@property (T@"NSError",R,N) error;
@property (T@"NSString",C,N) audioOutputDeviceUniqueID;
@property (T@"NSString",C,N) audioTimePitchAlgorithm;
@property (TQ,N) allowedAudioSpatializationFormats;
@property (TB,R,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,R,N) hasSufficientMediaDataForReliablePlaybackStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{OpaqueCMTimebase=},R,&) timebase;
```

## Class methods

```
+[AVSampleBufferAudioRenderer currentFigAudioRendererFactory];
+[AVSampleBufferAudioRenderer sampleBufferAudioRenderer];
+[AVSampleBufferAudioRenderer setFigAudioRendererFactory:forQueue:];
```

## Instance methods

```
-[AVSampleBufferAudioRenderer setMuted:];
-[AVSampleBufferAudioRenderer timebase];
-[AVSampleBufferAudioRenderer isMuted];
-[AVSampleBufferAudioRenderer outputContext];
-[AVSampleBufferAudioRenderer audioSession];
-[AVSampleBufferAudioRenderer _cancelPendingSwiftAsyncEnqueueHandler];
-[AVSampleBufferAudioRenderer loggingIdentifier];
-[AVSampleBufferAudioRenderer isReadyForMoreMediaData];
-[AVSampleBufferAudioRenderer volume];
-[AVSampleBufferAudioRenderer stopRequestingMediaData];
-[AVSampleBufferAudioRenderer init];
-[AVSampleBufferAudioRenderer flush];
-[AVSampleBufferAudioRenderer hasSufficientMediaDataForReliablePlaybackStart];
-[AVSampleBufferAudioRenderer dealloc];
-[AVSampleBufferAudioRenderer requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVSampleBufferAudioRenderer enqueueSampleBuffer:];
-[AVSampleBufferAudioRenderer setVolume:];
-[AVSampleBufferAudioRenderer status];
-[AVSampleBufferAudioRenderer audioTimePitchAlgorithm];
-[AVSampleBufferAudioRenderer error];
-[AVSampleBufferAudioRenderer isDefunct];
-[AVSampleBufferAudioRenderer setOutputContext:];
-[AVSampleBufferAudioRenderer setSTSLabel:];
-[AVSampleBufferAudioRenderer _nameForLogging];
-[AVSampleBufferAudioRenderer setAudioSession:];
-[AVSampleBufferAudioRenderer expire];
-[AVSampleBufferAudioRenderer copyFigSampleBufferAudioRenderer:];
-[AVSampleBufferAudioRenderer _readyForMoreMediaDataHandler];
-[AVSampleBufferAudioRenderer _setReadyForMoreMediaDataHandler:];
-[AVSampleBufferAudioRenderer setRenderSynchronizer:error:];
-[AVSampleBufferAudioRenderer contentKeySession];
-[AVSampleBufferAudioRenderer setAudioTimePitchAlgorithm:];
-[AVSampleBufferAudioRenderer _setCancelPendingSwiftAsyncEnqueueHandler:];
-[AVSampleBufferAudioRenderer _wasFlushedAutomaticallyAtTime:];
-[AVSampleBufferAudioRenderer _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVSampleBufferAudioRenderer _attachedToExternalContentKeySession];
-[AVSampleBufferAudioRenderer _initializeTimebase];
-[AVSampleBufferAudioRenderer _installNotificationHandlers];
-[AVSampleBufferAudioRenderer _transitionToFailedStatusWithOSStatus:];
-[AVSampleBufferAudioRenderer _transitionToStatus:error:];
-[AVSampleBufferAudioRenderer _triggerMediaRequestCallback];
-[AVSampleBufferAudioRenderer _uninstallNotificationHandlers];
-[AVSampleBufferAudioRenderer allowedAudioSpatializationFormats];
-[AVSampleBufferAudioRenderer audioOutputDeviceUniqueID];
-[AVSampleBufferAudioRenderer audioTapProcessor];
-[AVSampleBufferAudioRenderer flushFromSourceTime:completionHandler:];
-[AVSampleBufferAudioRenderer mayRequireContentKeysForMediaDataProcessing];
-[AVSampleBufferAudioRenderer setAllowedAudioSpatializationFormats:];
-[AVSampleBufferAudioRenderer setAudioOutputDeviceUniqueID:];
-[AVSampleBufferAudioRenderer setAudioTapProcessor:];
-[AVSampleBufferAudioRenderer setLoggingIdentifier:];
-[AVSampleBufferAudioRenderer willTrimShortDurationSamples];
```
