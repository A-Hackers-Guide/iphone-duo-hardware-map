# `AVFigAssetInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetInspector`
- 7 instance variables, 11 properties, 69 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigAsset=} _figAsset;
@"AVDispatchOnce" _checkIsStreamingOnce;
@"AVDispatchOnce" _makeDisplayCriteriaOnce;
@"AVDisplayCriteria" _displayCriteria;
B _isStreaming;
B didCheckForSaveRestriction;
B hasSaveRestriction;
```

## Properties

```
@property (T^{OpaqueFigAsset=},R,N,G_figAsset) figAsset;
@property (T@"NSURL",R,N) URL;
@property (T@"NSArray",R,N) figChapterGroupInfo;
@property (T@"NSArray",R,N) figChapters;
@property (T@"NSURL",R,N) resolvedURL;
@property (T@"NSURL",R,N) originalNetworkContentURL;
@property (TB,R,N) hasProtectedContent;
@property (TB,R,N,G_isStreaming) streaming;
@property (TQ,R,N) downloadToken;
@property (T@"NSArray",R,N) variants;
@property (T@"NSArray",R,N) contentKeySpecifiersEligibleForPreloading;
```

## Instance methods

```
-[AVFigAssetInspector lyrics];
-[AVFigAssetInspector isPlayable];
-[AVFigAssetInspector trackReferences];
-[AVFigAssetInspector commonMetadata];
-[AVFigAssetInspector _assetAnalysisMessages];
-[AVFigAssetInspector providesPreciseSampleTiming];
-[AVFigAssetInspector canContainFragments];
-[AVFigAssetInspector trackCount];
-[AVFigAssetInspector preferredDisplayCriteria];
-[AVFigAssetInspector maximumVideoResolution];
-[AVFigAssetInspector _customMediaSelectionScheme];
-[AVFigAssetInspector _mediaSelectionGroupDictionaries];
-[AVFigAssetInspector metadataForFormat:];
-[AVFigAssetInspector isCompatibleWithAirPlayVideo];
-[AVFigAssetInspector hasProtectedContent];
-[AVFigAssetInspector preferredTransform];
-[AVFigAssetInspector overallDurationHint];
-[AVFigAssetInspector naturalSize];
-[AVFigAssetInspector _isDefunct];
-[AVFigAssetInspector preferredRate];
-[AVFigAssetInspector makePropertyListForProxyWithOptions:];
-[AVFigAssetInspector dealloc];
-[AVFigAssetInspector isComposable];
-[AVFigAssetInspector _nameForProxy];
-[AVFigAssetInspector propertyListForProxy];
-[AVFigAssetInspector httpSessionIdentifier];
-[AVFigAssetInspector creationDate];
-[AVFigAssetInspector alternateTrackGroups];
-[AVFigAssetInspector uniqueIdentifier];
-[AVFigAssetInspector supportsAnalysisReporting];
-[AVFigAssetInspector hasProtectedContentWithoutPropertyString];
-[AVFigAssetInspector variants];
-[AVFigAssetInspector minimumTimeOffsetFromLive];
-[AVFigAssetInspector _isStreaming];
-[AVFigAssetInspector _valueAsCFTypeForProperty:propertyString:];
-[AVFigAssetInspector duration];
-[AVFigAssetInspector preferredSoundCheckVolumeNormalization];
-[AVFigAssetInspector _valueAsCFTypeForProperty:];
-[AVFigAssetInspector preferredVolume];
-[AVFigAssetInspector isCompatibleWithSavedPhotosAlbum];
-[AVFigAssetInspector availableMetadataFormats];
-[AVFigAssetInspector _moovAtomSize];
-[AVFigAssetInspector figChapters];
-[AVFigAssetInspector identifyingTag];
-[AVFigAssetInspector fragmentCount];
-[AVFigAssetInspector containsFragments];
-[AVFigAssetInspector downloadToken];
-[AVFigAssetInspector resolvedURL];
-[AVFigAssetInspector isExportable];
-[AVFigAssetInspector _authoredMediaSelectionGroupDictionaries];
-[AVFigAssetInspector identifyingTagClass];
-[AVFigAssetInspector naturalTimeScale];
-[AVFigAssetInspector hash];
-[AVFigAssetInspector _figAsset];
-[AVFigAssetInspector originalNetworkContentURL];
-[AVFigAssetInspector initWithFigAsset:];
-[AVFigAssetInspector availableVideoDynamicRanges];
-[AVFigAssetInspector _localizedMediaSelectionOptionDisplayNames];
-[AVFigAssetInspector providesPreciseDurationAndTiming];
-[AVFigAssetInspector firstFragmentSequenceNumber];
-[AVFigAssetInspector isEqual:];
-[AVFigAssetInspector contentKeySpecifiersEligibleForPreloading];
-[AVFigAssetInspector _copyFormatReader];
-[AVFigAssetInspector figChapterGroupInfo];
-[AVFigAssetInspector URL];
-[AVFigAssetInspector _hasQTSaveRestriction];
-[AVFigAssetInspector isCompatibleWithPhotosTranscodingServiceWithOptions:];
-[AVFigAssetInspector SHA1Digest];
-[AVFigAssetInspector isReadable];
```
