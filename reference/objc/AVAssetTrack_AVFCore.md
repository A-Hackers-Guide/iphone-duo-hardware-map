# `AVAssetTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`, `NSCopying`, `AVAsynchronousKeyValueLoading`
- 1 instance variables, 7 properties, 93 instance methods, 3 class methods

## Instance variables

```
@"AVAssetTrackInternal" _track;
```

## Properties

```
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"AVAsset",R,W,N) asset;
@property (Ti,R,N) trackID;
```

## Class methods

```
+[AVAssetTrack expectsPropertyRevisedNotifications];
+[AVAssetTrack keyPathsForValuesAffectingTimeRange];
+[AVAssetTrack mediaCharacteristicsForMediaTypes];
```

## Instance methods

```
-[AVAssetTrack isPlayable];
-[AVAssetTrack segments];
-[AVAssetTrack commonMetadata];
-[AVAssetTrack defaultAlternateGroupID];
-[AVAssetTrack dimensions];
-[AVAssetTrack formatDescriptions];
-[AVAssetTrack asset];
-[AVAssetTrack isSelfContained];
-[AVAssetTrack loudnessInfo];
-[AVAssetTrack _figAssetTrack];
-[AVAssetTrack requiresFrameReordering];
-[AVAssetTrack timeRange];
-[AVAssetTrack isAudibleBooksContentAuthorized];
-[AVAssetTrack nominalFrameRate];
-[AVAssetTrack metadataForFormat:];
-[AVAssetTrack playabilityValidationResult];
-[AVAssetTrack layer];
-[AVAssetTrack minFrameDuration];
-[AVAssetTrack statusOfValueForKey:error:];
-[AVAssetTrack hasProtectedContent];
-[AVAssetTrack init];
-[AVAssetTrack preferredTransform];
-[AVAssetTrack trackID];
-[AVAssetTrack totalSampleDataLength];
-[AVAssetTrack naturalSize];
-[AVAssetTrack mediaPresentationTimeRange];
-[AVAssetTrack _figFormatReader];
-[AVAssetTrack dealloc];
-[AVAssetTrack hasSeamSamples];
-[AVAssetTrack peakDataRate];
-[AVAssetTrack _initWithAsset:trackID:trackIndex:];
-[AVAssetTrack metadata];
-[AVAssetTrack segmentsExcludeAudioPrimingAndRemainderDurations];
-[AVAssetTrack isDefunct];
-[AVAssetTrack isEnabled];
-[AVAssetTrack preferredVolume];
-[AVAssetTrack languageCode];
-[AVAssetTrack availableMetadataFormats];
-[AVAssetTrack segmentForTrackTime:];
-[AVAssetTrack _figTrackReader];
-[AVAssetTrack hasAudibleBooksContent];
-[AVAssetTrack locale];
-[AVAssetTrack _weakReference];
-[AVAssetTrack provisionalAlternateGroupID];
-[AVAssetTrack _trackReferences];
-[AVAssetTrack alternateGroupID];
-[AVAssetTrack naturalTimeScale];
-[AVAssetTrack hash];
-[AVAssetTrack estimatedDataRate];
-[AVAssetTrack gaplessSourceTimeRange];
-[AVAssetTrack description];
-[AVAssetTrack latentBaseDecodeTimeStampOfFirstTrackFragment];
-[AVAssetTrack uneditedDuration];
-[AVAssetTrack isExcludedFromAutoselectionInTrackGroup];
-[AVAssetTrack extendedLanguageTag];
-[AVAssetTrack segmentsAsPresented];
-[AVAssetTrack copyWithZone:];
-[AVAssetTrack mediaType];
-[AVAssetTrack isEqual:];
-[AVAssetTrack isDecodable];
-[AVAssetTrack loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVAssetTrack mediaDecodeTimeRange];
-[AVAssetTrack _hasScaledEdits];
-[AVAssetTrack _pairedForcedOnlySubtitlesTrack];
-[AVAssetTrack _assetTrackInspector];
-[AVAssetTrack _fallbackTrack];
-[AVAssetTrack _firstAssociatedTrackWithAssociationType:];
-[AVAssetTrack _firstFormatDescriptionIsLPCM];
-[AVAssetTrack _hasEmptyEdits];
-[AVAssetTrack _hasMultipleDistinctFormatDescriptions];
-[AVAssetTrack _hasMultipleEdits];
-[AVAssetTrack _initWithAsset:trackID:];
-[AVAssetTrack _initWithAsset:trackIndex:];
-[AVAssetTrack _startListeningToFigAssetTrackNotifications];
-[AVAssetTrack _stopListeningToFigAssetTrackNotifications];
-[AVAssetTrack _subtitleFormatDescriptionMatchesTextDisplayFlags:flagsMask:];
-[AVAssetTrack associatedTracksOfType:];
-[AVAssetTrack availableTrackAssociationTypes];
-[AVAssetTrack canProvideSampleCursors];
-[AVAssetTrack hasAudioSampleDependencies];
-[AVAssetTrack hasMediaCharacteristic:];
-[AVAssetTrack hasMediaCharacteristics:];
-[AVAssetTrack loadAssociatedTracksOfType:completionHandler:];
-[AVAssetTrack loadMetadataForFormat:completionHandler:];
-[AVAssetTrack loadSamplePresentationTimeForTrackTime:completionHandler:];
-[AVAssetTrack loadSegmentForTrackTime:completionHandler:];
-[AVAssetTrack makeSampleCursorAtFirstSampleInDecodeOrder];
-[AVAssetTrack makeSampleCursorAtLastSampleInDecodeOrder];
-[AVAssetTrack makeSampleCursorWithPresentationTimeStamp:];
-[AVAssetTrack mediaCharacteristics];
-[AVAssetTrack samplePresentationTimeForTrackTime:];
-[AVAssetTrack statusOfValueForKey:];
-[AVAssetTrack transportStreamPID];
```
