# `AVAssetWriterInputHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 33 properties, 77 instance methods, 0 class methods

## Instance variables

```
@"AVAssetWriterInputConfigurationState" _configurationState;
@"AVWeakReference" _weakReferenceToAssetWriterInput;
```

## Properties

```
@property (T@"AVAssetWriterInputConfigurationState",R,N,V_configurationState) configurationState;
@property (T@"AVWeakReference",&,V_weakReferenceToAssetWriterInput) weakReferenceToAssetWriterInput;
@property (Tq,R,N) status;
@property (Ti,R,N) trackID;
@property (T@"NSString",R,N) mediaType;
@property (T@"AVOutputSettings",R,N) outputSettings;
@property (T^{opaqueCMFormatDescription=},R,N) sourceFormatHint;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (T@"NSArray",C,N) metadata;
@property (Ti,N) mediaTimeScale;
@property (TB,R,N,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,N) expectsMediaDataInRealTime;
@property (T{CGSize=dd},N) naturalSize;
@property (T@"NSString",C,N) languageCode;
@property (T@"NSString",C,N) extendedLanguageTag;
@property (TB,N) marksOutputTrackAsEnabled;
@property (Tf,N) preferredVolume;
@property (Tq,N) layer;
@property (Ts,N) alternateGroupID;
@property (Ts,N) provisionalAlternateGroupID;
@property (T@"NSDictionary",R,N) trackReferences;
@property (TB,N) performsMultiPassEncodingIfSupported;
@property (TB,R,N) canPerformMultiplePasses;
@property (T@"AVAssetWriterInputPassDescription",R,N) currentPassDescription;
@property (TB,R,N) shouldRespondToInitialPassDescription;
@property (T{?=qiIq},N) preferredMediaChunkDuration;
@property (Tq,N) preferredMediaChunkAlignment;
@property (Tq,N) preferredMediaChunkSize;
@property (T@"NSString",C,N) mediaDataLocation;
@property (T@"NSURL",C,N) sampleReferenceBaseURL;
@property (TB,N) maximizePowerEfficiency;
@property (T@"NSDictionary",C,N) sourcePixelBufferAttributes;
@property (T^{__CVPixelBufferPool=},R,N) pixelBufferPool;
```

## Instance methods

```
-[AVAssetWriterInputHelper setNaturalSize:];
-[AVAssetWriterInputHelper trackReferences];
-[AVAssetWriterInputHelper outputSettings];
-[AVAssetWriterInputHelper setExtendedLanguageTag:];
-[AVAssetWriterInputHelper setPreferredVolume:];
-[AVAssetWriterInputHelper layer];
-[AVAssetWriterInputHelper pixelBufferPool];
-[AVAssetWriterInputHelper isReadyForMoreMediaData];
-[AVAssetWriterInputHelper stopRequestingMediaData];
-[AVAssetWriterInputHelper trackID];
-[AVAssetWriterInputHelper naturalSize];
-[AVAssetWriterInputHelper dealloc];
-[AVAssetWriterInputHelper requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVAssetWriterInputHelper status];
-[AVAssetWriterInputHelper setTransform:];
-[AVAssetWriterInputHelper transform];
-[AVAssetWriterInputHelper metadata];
-[AVAssetWriterInputHelper preferredVolume];
-[AVAssetWriterInputHelper languageCode];
-[AVAssetWriterInputHelper provisionalAlternateGroupID];
-[AVAssetWriterInputHelper alternateGroupID];
-[AVAssetWriterInputHelper setMetadata:];
-[AVAssetWriterInputHelper description];
-[AVAssetWriterInputHelper setAlternateGroupID:];
-[AVAssetWriterInputHelper extendedLanguageTag];
-[AVAssetWriterInputHelper mediaType];
-[AVAssetWriterInputHelper setLanguageCode:];
-[AVAssetWriterInputHelper setLayer:];
-[AVAssetWriterInputHelper configurationState];
-[AVAssetWriterInputHelper appendPixelBuffer:withPresentationTime:];
-[AVAssetWriterInputHelper markAsFinished];
-[AVAssetWriterInputHelper sourcePixelBufferAttributes];
-[AVAssetWriterInputHelper setPreferredMediaChunkDuration:];
-[AVAssetWriterInputHelper weakReferenceToAssetWriterInput];
-[AVAssetWriterInputHelper setProvisionalAlternateGroupID:];
-[AVAssetWriterInputHelper setSourcePixelBufferAttributes:];
-[AVAssetWriterInputHelper addTrackAssociationWithTrackOfInput:type:];
-[AVAssetWriterInputHelper appendCaption:error:];
-[AVAssetWriterInputHelper appendCaptionGroup:error:];
-[AVAssetWriterInputHelper appendSampleBuffer:error:];
-[AVAssetWriterInputHelper appendTaggedPixelBufferGroup:withPresentationTime:];
-[AVAssetWriterInputHelper associatedInputsWithTrackAssociationType:];
-[AVAssetWriterInputHelper availableTrackAssociationTypes];
-[AVAssetWriterInputHelper canAddTrackAssociationWithTrackOfInput:type:];
-[AVAssetWriterInputHelper canBecomeReadyForMoreMediaDataAndReturnError:];
-[AVAssetWriterInputHelper canPerformMultiplePasses];
-[AVAssetWriterInputHelper canStartRespondingToEachPassDescriptionReturningReason:];
-[AVAssetWriterInputHelper currentPassDescription];
-[AVAssetWriterInputHelper didStartInitialSession];
-[AVAssetWriterInputHelper expectsMediaDataInRealTime];
-[AVAssetWriterInputHelper initWithConfigurationState:];
-[AVAssetWriterInputHelper markCurrentPassAsFinished];
-[AVAssetWriterInputHelper marksOutputTrackAsEnabled];
-[AVAssetWriterInputHelper maximizePowerEfficiency];
-[AVAssetWriterInputHelper mediaDataLocation];
-[AVAssetWriterInputHelper mediaTimeScale];
-[AVAssetWriterInputHelper performsMultiPassEncodingIfSupported];
-[AVAssetWriterInputHelper preferredMediaChunkAlignment];
-[AVAssetWriterInputHelper preferredMediaChunkDuration];
-[AVAssetWriterInputHelper preferredMediaChunkSize];
-[AVAssetWriterInputHelper prepareToEndSession];
-[AVAssetWriterInputHelper prepareToFinishWritingReturningError:];
-[AVAssetWriterInputHelper sampleReferenceBaseURL];
-[AVAssetWriterInputHelper setExpectsMediaDataInRealTime:];
-[AVAssetWriterInputHelper setMarksOutputTrackAsEnabled:];
-[AVAssetWriterInputHelper setMaximizePowerEfficiency:];
-[AVAssetWriterInputHelper setMediaDataLocation:];
-[AVAssetWriterInputHelper setMediaTimeScale:];
-[AVAssetWriterInputHelper setPerformsMultiPassEncodingIfSupported:];
-[AVAssetWriterInputHelper setPreferredMediaChunkAlignment:];
-[AVAssetWriterInputHelper setPreferredMediaChunkSize:];
-[AVAssetWriterInputHelper setSampleReferenceBaseURL:];
-[AVAssetWriterInputHelper setWeakReferenceToAssetWriterInput:];
-[AVAssetWriterInputHelper shouldRespondToInitialPassDescription];
-[AVAssetWriterInputHelper sourceFormatHint];
-[AVAssetWriterInputHelper transitionAssetWriterAndAllInputsToFailedStatusWithError:];
-[AVAssetWriterInputHelper transitionToAndReturnTerminalHelperWithTerminalStatus:];
```
