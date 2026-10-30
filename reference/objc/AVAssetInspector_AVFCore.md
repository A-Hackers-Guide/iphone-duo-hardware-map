# `AVAssetInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVFigObjectInspector`
- Protocols: `NSCopying`
- 0 instance variables, 46 properties, 51 instance methods, 0 class methods

## Properties

```
@property (T{?=qiIq},R,N) duration;
@property (Tf,R,N) preferredRate;
@property (Tf,R,N) preferredVolume;
@property (Tf,R,N) preferredSoundCheckVolumeNormalization;
@property (T{CGAffineTransform=dddddd},R,N) preferredTransform;
@property (T{?=qiIq},R,N) minimumTimeOffsetFromLive;
@property (T{CGSize=dd},R,N) naturalSize;
@property (Ti,R,N) naturalTimeScale;
@property (TB,R,N) providesPreciseDurationAndTiming;
@property (Tq,R,N) trackCount;
@property (T@"NSArray",R,N) trackIDs;
@property (T@"NSArray",R,N) alternateTrackGroups;
@property (T@"NSDictionary",R,N) trackReferences;
@property (T@"NSArray",R,N,G_mediaSelectionGroupDictionaries) mediaSelectionGroupDictionaries;
@property (T@"NSArray",R,N,G_authoredMediaSelectionGroupDictionaries) authoredMediaSelectionGroupDictionaries;
@property (T@"NSDictionary",R,N,G_localizedMediaSelectionOptionDisplayNames) localizedMediaSelectionOptionDisplayNames;
@property (T@"NSArray",R,N,G_customMediaSelectionScheme) customMediaSelectionScheme;
@property (T@"AVMetadataItem",R,N) creationDate;
@property (T@"NSString",R,N) lyrics;
@property (T@"NSArray",R,N) commonMetadata;
@property (T@"NSArray",R,N) availableMetadataFormats;
@property (TB,R,N,GisPlayable) playable;
@property (TB,R,N,GisExportable) exportable;
@property (TB,R,N,GisReadable) readable;
@property (TB,R,N,GisComposable) composable;
@property (TB,R,N,GisCompatibleWithSavedPhotosAlbum) compatibleWithSavedPhotosAlbum;
@property (TB,R,N,GisCompatibleWithAirPlayVideo) compatibleWithAirPlayVideo;
@property (T@"NSData",R,N) SHA1Digest;
@property (TB,R,N) canContainFragments;
@property (TB,R,N) containsFragments;
@property (T{?=qiIq},R,N) overallDurationHint;
@property (Tq,R,N) firstFragmentSequenceNumber;
@property (Tq,R,N) fragmentCount;
@property (T@,R,N) propertyListForProxy;
@property (T@"NSString",R,N) identifyingTagClass;
@property (T@"NSString",R,N) identifyingTag;
@property (T{CGSize=dd},R,N) maximumVideoResolution;
@property (T@"NSArray",R,N) availableVideoDynamicRanges;
@property (T@"AVDisplayCriteria",R,N) preferredDisplayCriteria;
@property (T@"NSUUID",R,N) httpSessionIdentifier;
@property (T@"NSUUID",R,N) uniqueIdentifier;
@property (TB,R,N) supportsAnalysisReporting;
@property (T@"NSArray",R,N,G_assetAnalysisMessages) assetAnalysisMessages;
@property (Tq,R,N,G_moovAtomSize) moovAtomSize;
@property (TB,R,N,G_isDefunct) defunct;
@property (TB,R,N) providesPreciseSampleTiming;
```

## Instance methods

```
-[AVAssetInspector lyrics];
-[AVAssetInspector isPlayable];
-[AVAssetInspector trackReferences];
-[AVAssetInspector commonMetadata];
-[AVAssetInspector _assetAnalysisMessages];
-[AVAssetInspector providesPreciseSampleTiming];
-[AVAssetInspector canContainFragments];
-[AVAssetInspector trackCount];
-[AVAssetInspector preferredDisplayCriteria];
-[AVAssetInspector maximumVideoResolution];
-[AVAssetInspector _customMediaSelectionScheme];
-[AVAssetInspector _mediaSelectionGroupDictionaries];
-[AVAssetInspector metadataForFormat:];
-[AVAssetInspector isCompatibleWithAirPlayVideo];
-[AVAssetInspector hasProtectedContent];
-[AVAssetInspector preferredTransform];
-[AVAssetInspector overallDurationHint];
-[AVAssetInspector naturalSize];
-[AVAssetInspector _isDefunct];
-[AVAssetInspector preferredRate];
-[AVAssetInspector makePropertyListForProxyWithOptions:];
-[AVAssetInspector isComposable];
-[AVAssetInspector propertyListForProxy];
-[AVAssetInspector httpSessionIdentifier];
-[AVAssetInspector creationDate];
-[AVAssetInspector alternateTrackGroups];
-[AVAssetInspector uniqueIdentifier];
-[AVAssetInspector supportsAnalysisReporting];
-[AVAssetInspector minimumTimeOffsetFromLive];
-[AVAssetInspector duration];
-[AVAssetInspector preferredSoundCheckVolumeNormalization];
-[AVAssetInspector preferredVolume];
-[AVAssetInspector isCompatibleWithSavedPhotosAlbum];
-[AVAssetInspector availableMetadataFormats];
-[AVAssetInspector _moovAtomSize];
-[AVAssetInspector identifyingTag];
-[AVAssetInspector fragmentCount];
-[AVAssetInspector containsFragments];
-[AVAssetInspector isExportable];
-[AVAssetInspector _authoredMediaSelectionGroupDictionaries];
-[AVAssetInspector identifyingTagClass];
-[AVAssetInspector naturalTimeScale];
-[AVAssetInspector availableVideoDynamicRanges];
-[AVAssetInspector _localizedMediaSelectionOptionDisplayNames];
-[AVAssetInspector providesPreciseDurationAndTiming];
-[AVAssetInspector copyWithZone:];
-[AVAssetInspector firstFragmentSequenceNumber];
-[AVAssetInspector isCompatibleWithPhotosTranscodingServiceWithOptions:];
-[AVAssetInspector SHA1Digest];
-[AVAssetInspector isReadable];
-[AVAssetInspector trackIDs];
```
