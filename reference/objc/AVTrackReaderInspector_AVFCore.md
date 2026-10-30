# `AVTrackReaderInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetTrackInspector`
- 9 instance variables, 0 properties, 51 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigFormatReader=} _formatReader;
^{OpaqueFigTrackReader=} _trackReader;
@"AVDispatchOnce" _copySampleCursorServiceOnce;
^{OpaqueFigSampleCursorService=} _figSampleCursorService;
B _sampleCursorTimeAccuracyIsExact;
i _trackID;
I _mediaType;
@"AVWeakReference" _weakReferenceToAsset;
B _prefersNominalDurations;
```

## Instance methods

```
-[AVTrackReaderInspector isPlayable];
-[AVTrackReaderInspector segments];
-[AVTrackReaderInspector commonMetadata];
-[AVTrackReaderInspector defaultAlternateGroupID];
-[AVTrackReaderInspector dimensions];
-[AVTrackReaderInspector formatDescriptions];
-[AVTrackReaderInspector asset];
-[AVTrackReaderInspector isSelfContained];
-[AVTrackReaderInspector loudnessInfo];
-[AVTrackReaderInspector requiresFrameReordering];
-[AVTrackReaderInspector timeRange];
-[AVTrackReaderInspector nominalFrameRate];
-[AVTrackReaderInspector metadataForFormat:];
-[AVTrackReaderInspector playabilityValidationResult];
-[AVTrackReaderInspector layer];
-[AVTrackReaderInspector preferredTransform];
-[AVTrackReaderInspector trackID];
-[AVTrackReaderInspector totalSampleDataLength];
-[AVTrackReaderInspector naturalSize];
-[AVTrackReaderInspector decodabilityValidationResult];
-[AVTrackReaderInspector _figFormatReader];
-[AVTrackReaderInspector dealloc];
-[AVTrackReaderInspector hasSeamSamples];
-[AVTrackReaderInspector peakDataRate];
-[AVTrackReaderInspector _initWithAsset:trackID:trackIndex:];
-[AVTrackReaderInspector _valueAsCFTypeForProperty:];
-[AVTrackReaderInspector isEnabled];
-[AVTrackReaderInspector preferredVolume];
-[AVTrackReaderInspector languageCode];
-[AVTrackReaderInspector availableMetadataFormats];
-[AVTrackReaderInspector minSampleDuration];
-[AVTrackReaderInspector _figTrackReader];
-[AVTrackReaderInspector provisionalAlternateGroupID];
-[AVTrackReaderInspector _trackReferences];
-[AVTrackReaderInspector alternateGroupID];
-[AVTrackReaderInspector naturalTimeScale];
-[AVTrackReaderInspector hash];
-[AVTrackReaderInspector estimatedDataRate];
-[AVTrackReaderInspector latentBaseDecodeTimeStampOfFirstTrackFragment];
-[AVTrackReaderInspector uneditedDuration];
-[AVTrackReaderInspector isExcludedFromAutoselectionInTrackGroup];
-[AVTrackReaderInspector extendedLanguageTag];
-[AVTrackReaderInspector segmentsAsPresented];
-[AVTrackReaderInspector mediaType];
-[AVTrackReaderInspector isEqual:];
-[AVTrackReaderInspector _figMediaType];
-[AVTrackReaderInspector _getFigSampleCursorServiceReportingTimeAccuracy:];
-[AVTrackReaderInspector isDecodable];
-[AVTrackReaderInspector _segmentsPreferringNominalDurations:];
-[AVTrackReaderInspector hasAudioSampleDependencies];
-[AVTrackReaderInspector mediaCharacteristics];
```
