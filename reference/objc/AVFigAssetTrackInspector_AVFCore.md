# `AVFigAssetTrackInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetTrackInspector`
- 15 instance variables, 0 properties, 70 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAsset=} _figAsset;
^{OpaqueFigAssetTrack=} _figAssetTrack;
@"AVDispatchOnce" _copyFigFormatReaderOnce;
^{OpaqueFigFormatReader=} _figFormatReader;
@"AVDispatchOnce" _copyFigTrackReaderOnce;
^{OpaqueFigTrackReader=} _figTrackReader;
@"AVDispatchOnce" _copySampleCursorServiceOnce;
^{OpaqueFigSampleCursorService=} _figSampleCursorService;
B _sampleCursorTimeAccuracyIsExact;
^{OpaqueFigSimpleMutex=} _loadingMutex;
@"NSObject<OS_dispatch_queue>" _completionHandlerQueue;
@"NSMutableArray" _loadingBatches;
I _mediaType;
@"AVWeakReference" _weakReferenceToAsset;
B _prefersNominalDurations;
```

## Instance methods

```
-[AVFigAssetTrackInspector isPlayable];
-[AVFigAssetTrackInspector segments];
-[AVFigAssetTrackInspector commonMetadata];
-[AVFigAssetTrackInspector defaultAlternateGroupID];
-[AVFigAssetTrackInspector dimensions];
-[AVFigAssetTrackInspector formatDescriptions];
-[AVFigAssetTrackInspector asset];
-[AVFigAssetTrackInspector isSelfContained];
-[AVFigAssetTrackInspector loudnessInfo];
-[AVFigAssetTrackInspector _figAssetTrack];
-[AVFigAssetTrackInspector requiresFrameReordering];
-[AVFigAssetTrackInspector timeRange];
-[AVFigAssetTrackInspector isAudibleBooksContentAuthorized];
-[AVFigAssetTrackInspector nominalFrameRate];
-[AVFigAssetTrackInspector metadataForFormat:];
-[AVFigAssetTrackInspector playabilityValidationResult];
-[AVFigAssetTrackInspector layer];
-[AVFigAssetTrackInspector statusOfValueForKey:error:];
-[AVFigAssetTrackInspector hasProtectedContent];
-[AVFigAssetTrackInspector preferredTransform];
-[AVFigAssetTrackInspector _segmentsForProperty:];
-[AVFigAssetTrackInspector trackID];
-[AVFigAssetTrackInspector totalSampleDataLength];
-[AVFigAssetTrackInspector naturalSize];
-[AVFigAssetTrackInspector _addFigNotifications];
-[AVFigAssetTrackInspector decodabilityValidationResult];
-[AVFigAssetTrackInspector mediaPresentationTimeRange];
-[AVFigAssetTrackInspector _figFormatReader];
-[AVFigAssetTrackInspector _isDefunct];
-[AVFigAssetTrackInspector dealloc];
-[AVFigAssetTrackInspector hasSeamSamples];
-[AVFigAssetTrackInspector peakDataRate];
-[AVFigAssetTrackInspector _loadStatusForFigAssetTrackProperty:error:];
-[AVFigAssetTrackInspector _initWithAsset:trackID:trackIndex:];
-[AVFigAssetTrackInspector _invokeCompletionHandlerForLoadingBatches:];
-[AVFigAssetTrackInspector _valueAsCFTypeForProperty:propertyString:];
-[AVFigAssetTrackInspector _loadingBatches];
-[AVFigAssetTrackInspector segmentsExcludeAudioPrimingAndRemainderDurations];
-[AVFigAssetTrackInspector figAssetPropertyForSegments];
-[AVFigAssetTrackInspector _valueAsCFTypeForProperty:];
-[AVFigAssetTrackInspector isEnabled];
-[AVFigAssetTrackInspector preferredVolume];
-[AVFigAssetTrackInspector languageCode];
-[AVFigAssetTrackInspector availableMetadataFormats];
-[AVFigAssetTrackInspector minSampleDuration];
-[AVFigAssetTrackInspector segmentForTrackTime:];
-[AVFigAssetTrackInspector _figTrackReader];
-[AVFigAssetTrackInspector hasAudibleBooksContent];
-[AVFigAssetTrackInspector _removeFigNotifications];
-[AVFigAssetTrackInspector provisionalAlternateGroupID];
-[AVFigAssetTrackInspector _trackReferences];
-[AVFigAssetTrackInspector alternateGroupID];
-[AVFigAssetTrackInspector _loadingMutex];
-[AVFigAssetTrackInspector naturalTimeScale];
-[AVFigAssetTrackInspector hash];
-[AVFigAssetTrackInspector estimatedDataRate];
-[AVFigAssetTrackInspector gaplessSourceTimeRange];
-[AVFigAssetTrackInspector latentBaseDecodeTimeStampOfFirstTrackFragment];
-[AVFigAssetTrackInspector uneditedDuration];
-[AVFigAssetTrackInspector isExcludedFromAutoselectionInTrackGroup];
-[AVFigAssetTrackInspector extendedLanguageTag];
-[AVFigAssetTrackInspector _ensureAllDependenciesOfKeyAreLoaded:];
-[AVFigAssetTrackInspector segmentsAsPresented];
-[AVFigAssetTrackInspector mediaType];
-[AVFigAssetTrackInspector isEqual:];
-[AVFigAssetTrackInspector _figMediaType];
-[AVFigAssetTrackInspector _getFigSampleCursorServiceReportingTimeAccuracy:];
-[AVFigAssetTrackInspector isDecodable];
-[AVFigAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVFigAssetTrackInspector mediaDecodeTimeRange];
```
