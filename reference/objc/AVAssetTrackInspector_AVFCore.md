# `AVAssetTrackInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVFigObjectInspector`
- Protocols: `AVAsynchronousKeyValueLoading`
- 3 instance variables, 53 properties, 70 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _weakReference;
@"AVDispatchOnce" _synthesizeMediaCharacteristicsOnce;
@"NSArray" _cachedMediaCharacteristics;
```

## Properties

```
@property (Ti,R,N) trackID;
@property (TI,R,N,G_figMediaType) figMediaType;
@property (T^{OpaqueFigTrackReader=},R,N,G_figTrackReader) figTrackReader;
@property (T^{OpaqueFigAssetTrack=},R,N,G_figAssetTrack) figAssetTrack;
@property (T^{OpaqueFigFormatReader=},R,N,G_figFormatReader) figFormatReader;
@property (T@"NSString",R,N) mediaType;
@property (T@"NSArray",R,N) formatDescriptions;
@property (TB,R,N,GisPlayable) playable;
@property (TB,R,N,GisDecodable) decodable;
@property (TB,R,N,GisEnabled) enabled;
@property (TB,R,N,GisSelfContained) selfContained;
@property (Tq,R,N) totalSampleDataLength;
@property (T{?={?=qiIq}{?=qiIq}},R,N) timeRange;
@property (T{?=qiIq},R,N) uneditedDuration;
@property (T{?={?=qiIq}{?=qiIq}},R,N) mediaPresentationTimeRange;
@property (T{?={?=qiIq}{?=qiIq}},R,N) mediaDecodeTimeRange;
@property (T{?=qiIq},R,N) latentBaseDecodeTimeStampOfFirstTrackFragment;
@property (TB,R,N) requiresFrameReordering;
@property (Ti,R,N) naturalTimeScale;
@property (Tf,R,N) estimatedDataRate;
@property (Tf,R,N) peakDataRate;
@property (T@"NSString",R,N) languageCode;
@property (Ti,R,N) transportStreamPID;
@property (T@"NSArray",R,N) mediaCharacteristics;
@property (T@"NSString",R,N) extendedLanguageTag;
@property (T@"NSLocale",R,N) locale;
@property (T{CGSize=dd},R,N) naturalSize;
@property (T{CGAffineTransform=dddddd},R,N) preferredTransform;
@property (Tq,R,N) layer;
@property (Tf,R,N) preferredVolume;
@property (TB,R,N) hasAudioSampleDependencies;
@property (T@"NSDictionary",R,N) loudnessInfo;
@property (Tf,R,N) nominalFrameRate;
@property (T{?=qiIq},R,N) minSampleDuration;
@property (T@"NSArray",R,C,N) segments;
@property (T@"NSArray",R,N) commonMetadata;
@property (T@"NSArray",R,N) availableMetadataFormats;
@property (Tq,R,N) alternateGroupID;
@property (Tq,R,N) defaultAlternateGroupID;
@property (Tq,R,N) provisionalAlternateGroupID;
@property (TB,R,N,GisExcludedFromAutoselectionInTrackGroup) excludedFromAutoselectionInTrackGroup;
@property (T{CGSize=dd},R,N) dimensions;
@property (T@"NSDictionary",R,N,G_trackReferences) trackReferences;
@property (TB,R,N) hasProtectedContent;
@property (TB,R,N) hasAudibleBooksContent;
@property (TB,R,N) isAudibleBooksContentAuthorized;
@property (TB,R,N) hasSeamSamples;
@property (Ti,R,N) playabilityValidationResult;
@property (TB,R,N) segmentsExcludeAudioPrimingAndRemainderDurations;
@property (T{?={?=qiIq}{?=qiIq}},R,N) gaplessSourceTimeRange;
@property (T@"NSArray",R,C,N) segmentsAsPresented;
@property (TB,R,N) canProvideSampleCursors;
@property (TB,R,N,G_isDefunct) defunct;
```

## Class methods

```
+[AVAssetTrackInspector assetTrackInspectorWithAsset:trackID:trackIndex:];
```

## Instance methods

```
-[AVAssetTrackInspector isPlayable];
-[AVAssetTrackInspector segments];
-[AVAssetTrackInspector commonMetadata];
-[AVAssetTrackInspector defaultAlternateGroupID];
-[AVAssetTrackInspector dimensions];
-[AVAssetTrackInspector formatDescriptions];
-[AVAssetTrackInspector isSelfContained];
-[AVAssetTrackInspector loudnessInfo];
-[AVAssetTrackInspector _figAssetTrack];
-[AVAssetTrackInspector requiresFrameReordering];
-[AVAssetTrackInspector timeRange];
-[AVAssetTrackInspector isAudibleBooksContentAuthorized];
-[AVAssetTrackInspector nominalFrameRate];
-[AVAssetTrackInspector metadataForFormat:];
-[AVAssetTrackInspector playabilityValidationResult];
-[AVAssetTrackInspector layer];
-[AVAssetTrackInspector statusOfValueForKey:error:];
-[AVAssetTrackInspector hasProtectedContent];
-[AVAssetTrackInspector init];
-[AVAssetTrackInspector preferredTransform];
-[AVAssetTrackInspector trackID];
-[AVAssetTrackInspector totalSampleDataLength];
-[AVAssetTrackInspector naturalSize];
-[AVAssetTrackInspector mediaPresentationTimeRange];
-[AVAssetTrackInspector _figFormatReader];
-[AVAssetTrackInspector _isDefunct];
-[AVAssetTrackInspector dealloc];
-[AVAssetTrackInspector hasSeamSamples];
-[AVAssetTrackInspector peakDataRate];
-[AVAssetTrackInspector _initWithAsset:trackID:trackIndex:];
-[AVAssetTrackInspector segmentsExcludeAudioPrimingAndRemainderDurations];
-[AVAssetTrackInspector isEnabled];
-[AVAssetTrackInspector preferredVolume];
-[AVAssetTrackInspector languageCode];
-[AVAssetTrackInspector availableMetadataFormats];
-[AVAssetTrackInspector minSampleDuration];
-[AVAssetTrackInspector segmentForTrackTime:];
-[AVAssetTrackInspector _figTrackReader];
-[AVAssetTrackInspector hasAudibleBooksContent];
-[AVAssetTrackInspector locale];
-[AVAssetTrackInspector _weakReference];
-[AVAssetTrackInspector provisionalAlternateGroupID];
-[AVAssetTrackInspector _trackReferences];
-[AVAssetTrackInspector alternateGroupID];
-[AVAssetTrackInspector naturalTimeScale];
-[AVAssetTrackInspector estimatedDataRate];
-[AVAssetTrackInspector gaplessSourceTimeRange];
-[AVAssetTrackInspector latentBaseDecodeTimeStampOfFirstTrackFragment];
-[AVAssetTrackInspector uneditedDuration];
-[AVAssetTrackInspector isExcludedFromAutoselectionInTrackGroup];
-[AVAssetTrackInspector extendedLanguageTag];
-[AVAssetTrackInspector segmentsAsPresented];
-[AVAssetTrackInspector copyWithZone:];
-[AVAssetTrackInspector mediaType];
-[AVAssetTrackInspector _figMediaType];
-[AVAssetTrackInspector _getFigSampleCursorServiceReportingTimeAccuracy:];
-[AVAssetTrackInspector isDecodable];
-[AVAssetTrackInspector loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVAssetTrackInspector mediaDecodeTimeRange];
-[AVAssetTrackInspector _initWithAsset:trackID:];
-[AVAssetTrackInspector _initWithAsset:trackIndex:];
-[AVAssetTrackInspector _segmentsForSegmentData:];
-[AVAssetTrackInspector canProvideSampleCursors];
-[AVAssetTrackInspector hasAudioSampleDependencies];
-[AVAssetTrackInspector makeSampleCursorAtFirstSampleInDecodeOrder];
-[AVAssetTrackInspector makeSampleCursorAtLastSampleInDecodeOrder];
-[AVAssetTrackInspector makeSampleCursorWithPresentationTimeStamp:];
-[AVAssetTrackInspector mediaCharacteristics];
-[AVAssetTrackInspector samplePresentationTimeForTrackTime:];
-[AVAssetTrackInspector transportStreamPID];
```
