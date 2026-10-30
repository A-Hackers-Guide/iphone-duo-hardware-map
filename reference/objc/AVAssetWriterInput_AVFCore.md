# `AVAssetWriterInput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVWeakObservable`, `AVKeyPathDependencyHost`
- 1 instance variables, 23 properties, 98 instance methods, 3 class methods

## Instance variables

```
@"AVAssetWriterInputInternal" _internal;
```

## Properties

```
@property (TB,N,GhasReceiver,SsetHasReceiver:) hasReceiver;
@property (Tq,R) numberOfAppendFailures;
@property (TB,R,G_markAsFinishedCalled) markAsFinishedCalled;
@property (T@"AVAssetWriterInputHelper",&,N,G_helper,S_setHelper:) helper;
@property (T@"NSDictionary",C,N,G_sourcePixelBufferAttributes,S_setSourcePixelBufferAttributes:) sourcePixelBufferAttributes;
@property (T^{__CVPixelBufferPool=},R,N,G_pixelBufferPool) pixelBufferPool;
@property (T@"AVOutputSettings",R,N,G_outputSettingsObject) outputSettingsObject;
@property (Tq,R,N,G_status) status;
@property (TB,R,N,G_isAttachedToAdaptor) attachedToAdaptor;
@property (T@"AVWeakReference",&,N,G_weakReferenceToAssetWriter,S_setWeakReferenceToAssetWriter:) weakReferenceToAssetWriter;
@property (Ts,N,G_alternateGroupID,S_setAlternateGroupID:) alternateGroupID;
@property (Ts,N,G_provisionalAlternateGroupID,S_setProvisionalAlternateGroupID:) provisionalAlternateGroupID;
@property (T@"NSDictionary",R,N,G_trackReferences) trackReferences;
@property (T@"NSString",R,N) mediaType;
@property (T@"NSDictionary",R,N) outputSettings;
@property (T^{opaqueCMFormatDescription=},R,N) sourceFormatHint;
@property (T@"NSArray",C,N) metadata;
@property (TB,R,N,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,N) expectsMediaDataInRealTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAssetWriterInput initialize];
+[AVAssetWriterInput assetWriterInputWithMediaType:outputSettings:];
+[AVAssetWriterInput assetWriterInputWithMediaType:outputSettings:sourceFormatHint:];
```

## Instance methods

```
-[AVAssetWriterInput setNaturalSize:];
-[AVAssetWriterInput outputSettings];
-[AVAssetWriterInput setExtendedLanguageTag:];
-[AVAssetWriterInput _isAttachedToAdaptor];
-[AVAssetWriterInput setPreferredVolume:];
-[AVAssetWriterInput observeValueForKeyPath:ofObject:change:context:];
-[AVAssetWriterInput layer];
-[AVAssetWriterInput isReadyForMoreMediaData];
-[AVAssetWriterInput stopRequestingMediaData];
-[AVAssetWriterInput init];
-[AVAssetWriterInput naturalSize];
-[AVAssetWriterInput dealloc];
-[AVAssetWriterInput requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInput _status];
-[AVAssetWriterInput setTransform:];
-[AVAssetWriterInput transform];
-[AVAssetWriterInput metadata];
-[AVAssetWriterInput preferredVolume];
-[AVAssetWriterInput languageCode];
-[AVAssetWriterInput _trackReferences];
-[AVAssetWriterInput _attachedAdaptor];
-[AVAssetWriterInput setMetadata:];
-[AVAssetWriterInput description];
-[AVAssetWriterInput _helper];
-[AVAssetWriterInput extendedLanguageTag];
-[AVAssetWriterInput mediaType];
-[AVAssetWriterInput _setAttachedAdaptor:];
-[AVAssetWriterInput setLanguageCode:];
-[AVAssetWriterInput setLayer:];
-[AVAssetWriterInput initWithMediaType:outputSettings:];
-[AVAssetWriterInput markAsFinished];
-[AVAssetWriterInput _setWeakReferenceToAssetWriter:];
-[AVAssetWriterInput setPreferredMediaChunkDuration:];
-[AVAssetWriterInput setHasReceiver:];
-[AVAssetWriterInput _alternateGroupID];
-[AVAssetWriterInput _appendCaption:error:];
-[AVAssetWriterInput _appendCaptionGroup:error:];
-[AVAssetWriterInput _appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInput _appendSampleBuffer:error:];
-[AVAssetWriterInput _appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInput _canBecomeReadyForMoreMediaDataAndReturnError:];
-[AVAssetWriterInput _didStartInitialSession];
-[AVAssetWriterInput _errorForNotReadyForMoreMediaData];
-[AVAssetWriterInput _invokeWhenReadyForMoreMediaDataUsingBlock:];
-[AVAssetWriterInput _markAsFinishedCalled];
-[AVAssetWriterInput _outputSettingsObject];
-[AVAssetWriterInput _pixelBufferPool];
-[AVAssetWriterInput _prepareForWritingWithFigAssetWriter:mediaFileType:error:];
-[AVAssetWriterInput _prepareToEndSession];
-[AVAssetWriterInput _prepareToFinishWritingReturningError:];
-[AVAssetWriterInput _provisionalAlternateGroupID];
-[AVAssetWriterInput _readyForMoreMediaDataMayHaveChanged];
-[AVAssetWriterInput _setAlternateGroupID:];
-[AVAssetWriterInput _setHelper:];
-[AVAssetWriterInput _setProvisionalAlternateGroupID:];
-[AVAssetWriterInput _setSourcePixelBufferAttributes:];
-[AVAssetWriterInput _sourcePixelBufferAttributes];
-[AVAssetWriterInput _tellAssetWriterToTransitionToFailedStatusWithError:];
-[AVAssetWriterInput _transitionToTerminalStatus:];
-[AVAssetWriterInput _weakReferenceToAssetWriter];
-[AVAssetWriterInput addCallbackToCancelDuringDeallocation:];
-[AVAssetWriterInput addTrackAssociationWithTrackOfInput:type:];
-[AVAssetWriterInput appendSampleBuffer:];
-[AVAssetWriterInput associatedInputsWithTrackAssociationType:];
-[AVAssetWriterInput availableTrackAssociationTypes];
-[AVAssetWriterInput canAddTrackAssociationWithTrackOfInput:type:];
-[AVAssetWriterInput canPerformMultiplePasses];
-[AVAssetWriterInput currentPassDescription];
-[AVAssetWriterInput declareKeyPathDependenciesWithRegistry:];
-[AVAssetWriterInput expectsMediaDataInRealTime];
-[AVAssetWriterInput finalVTCompressionSessionStateReturningError:];
-[AVAssetWriterInput hasReceiver];
-[AVAssetWriterInput initWithMediaType:outputSettings:sourceFormatHint:];
-[AVAssetWriterInput markCurrentPassAsFinished];
-[AVAssetWriterInput marksOutputTrackAsEnabled];
-[AVAssetWriterInput maximizePowerEfficiency];
-[AVAssetWriterInput mediaDataLocation];
-[AVAssetWriterInput mediaTimeScale];
-[AVAssetWriterInput numberOfAppendFailures];
-[AVAssetWriterInput outputTrackID];
-[AVAssetWriterInput performsMultiPassEncodingIfSupported];
-[AVAssetWriterInput preferredMediaChunkAlignment];
-[AVAssetWriterInput preferredMediaChunkDuration];
-[AVAssetWriterInput preferredMediaChunkSize];
-[AVAssetWriterInput respondToEachPassDescriptionOnQueue:usingBlock:];
-[AVAssetWriterInput sampleReferenceBaseURL];
-[AVAssetWriterInput setExpectsMediaDataInRealTime:];
-[AVAssetWriterInput setMarksOutputTrackAsEnabled:];
-[AVAssetWriterInput setMaximizePowerEfficiency:];
-[AVAssetWriterInput setMediaDataLocation:];
-[AVAssetWriterInput setMediaTimeScale:];
-[AVAssetWriterInput setPerformsMultiPassEncodingIfSupported:];
-[AVAssetWriterInput setPreferredMediaChunkAlignment:];
-[AVAssetWriterInput setPreferredMediaChunkSize:];
-[AVAssetWriterInput setSampleReferenceBaseURL:];
-[AVAssetWriterInput setWritesMediaDataToBeginningOfFile:];
-[AVAssetWriterInput sourceFormatHint];
-[AVAssetWriterInput writesMediaDataToBeginningOfFile];
```
