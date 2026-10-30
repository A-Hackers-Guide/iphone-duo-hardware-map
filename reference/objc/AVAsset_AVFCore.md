# `AVAsset`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`, `NSCopying`, `AVAsynchronousKeyValueLoading`
- 2 instance variables, 18 properties, 135 instance methods, 13 class methods

## Instance variables

```
@"AVAssetInternal" _asset;
@"NSArray" _constituentFileURLs;
```

## Properties

```
@property (T@"NSArray",R) availableChapterLocales;
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,N) fragments;
@property (T@"<AVLoggingIdentifier>",R,&,N) loggingIdentifier;
@property (T@,R,N) propertyListForProxy;
@property (TB,R,N) isProxy;
@property (T{?=qiIq},R,N) duration;
@property (Tf,R,N) preferredRate;
@property (Tf,R,N) preferredVolume;
@property (T{CGAffineTransform=dddddd},R,N) preferredTransform;
@property (T{CGSize=dd},R,N) naturalSize;
@property (T@"AVDisplayCriteria",R,N) preferredDisplayCriteria;
@property (T{?=qiIq},R,N) minimumTimeOffsetFromLive;
@property (T@"NSArray",R,N,V_constituentFileURLs) constituentFileURLs;
```

## Class methods

```
+[AVAsset initialize];
+[AVAsset assetWithURL:];
+[AVAsset _assetCreationOptionsPrefersSandboxedOption:];
+[AVAsset _assetCreationOptionsRequiresInProcessOperation:];
+[AVAsset assetProxyWithPropertyList:];
+[AVAsset assetProxyWithPropertyList:options:];
+[AVAsset assetWithData:contentType:options:];
+[AVAsset assetWithURL:figPlaybackItem:trackIDs:dynamicBehavior:];
+[AVAsset expectsPropertyRevisedNotifications];
+[AVAsset inspectionOnlyAssetWithFigAsset:];
+[AVAsset inspectionOnlyAssetWithStreamDataParser:tracks:];
+[AVAsset makeAssetLoggingIdentifier];
+[AVAsset supportsPlayerItems];
```

## Instance methods

```
-[AVAsset lyrics];
-[AVAsset isPlayable];
-[AVAsset isProxy];
-[AVAsset trackReferences];
-[AVAsset commonMetadata];
-[AVAsset _assetAnalysisMessages];
-[AVAsset providesPreciseSampleTiming];
-[AVAsset canContainFragments];
-[AVAsset preferredDisplayCriteria];
-[AVAsset tracksWithMediaCharacteristic:];
-[AVAsset fragments];
-[AVAsset tracksWithMediaType:];
-[AVAsset maximumVideoResolution];
-[AVAsset _customMediaSelectionScheme];
-[AVAsset _mediaSelectionGroupDictionaries];
-[AVAsset metadataForFormat:];
-[AVAsset isCompatibleWithAirPlayVideo];
-[AVAsset loggingIdentifier];
-[AVAsset valueForUndefinedKey:];
-[AVAsset statusOfValueForKey:error:];
-[AVAsset hasProtectedContent];
-[AVAsset init];
-[AVAsset preferredTransform];
-[AVAsset overallDurationHint];
-[AVAsset naturalSize];
-[AVAsset initWithURL:options:];
-[AVAsset preferredRate];
-[AVAsset makePropertyListForProxyWithOptions:];
-[AVAsset dealloc];
-[AVAsset isComposable];
-[AVAsset _prefersNominalDurations];
-[AVAsset propertyListForProxy];
-[AVAsset _classForTrackInspectors];
-[AVAsset mediaSelectionGroupForMediaCharacteristic:];
-[AVAsset creationDate];
-[AVAsset alternateTrackGroups];
-[AVAsset supportsAnalysisReporting];
-[AVAsset minimumTimeOffsetFromLive];
-[AVAsset _isStreaming];
-[AVAsset metadata];
-[AVAsset duration];
-[AVAsset isDefunct];
-[AVAsset preferredSoundCheckVolumeNormalization];
-[AVAsset trackWithTrackID:];
-[AVAsset preferredVolume];
-[AVAsset isCompatibleWithSavedPhotosAlbum];
-[AVAsset availableMetadataFormats];
-[AVAsset _commonLoggingIdentifier];
-[AVAsset loadValuesAsynchronouslyForKeys:keysForCollectionKeys:completionHandler:];
-[AVAsset containsFragments];
-[AVAsset _weakReference];
-[AVAsset _nameForLogging];
-[AVAsset isExportable];
-[AVAsset _setFragmentMindingInterval:];
-[AVAsset _authoredMediaSelectionGroupDictionaries];
-[AVAsset naturalTimeScale];
-[AVAsset hash];
-[AVAsset _figAsset];
-[AVAsset availableVideoDynamicRanges];
-[AVAsset _localizedMediaSelectionOptionDisplayNames];
-[AVAsset _fragmentMindingInterval];
-[AVAsset _setIsAssociatedWithFragmentMinder:];
-[AVAsset providesPreciseDurationAndTiming];
-[AVAsset copyWithZone:];
-[AVAsset tracks];
-[AVAsset isEqual:];
-[AVAsset _copyFormatReader];
-[AVAsset cancelLoading];
-[AVAsset isCompatibleWithPhotosTranscodingServiceWithOptions:];
-[AVAsset loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVAsset isReadable];
-[AVAsset _firstTrackGroupWithMediaTypes:];
-[AVAsset tracksWithMediaCharacteristics:];
-[AVAsset _assetInspector];
-[AVAsset _mindsFragments];
-[AVAsset _needsLegacyChangeNotifications];
-[AVAsset _ID3Metadata];
-[AVAsset _absoluteURL];
-[AVAsset _addChapterMetadataItem:timeRange:toChapters:fromIndex:];
-[AVAsset _assetInspectorLoader];
-[AVAsset _availableCanonicalizedChapterLanguages];
-[AVAsset _availableMediaCharacteristicsFromMediaSelectionGroupDictionaries:];
-[AVAsset _availableMediaCharacteristicsWithMediaSelectionOptionsIncludingExtendedOptions:];
-[AVAsset _chapterDataTypeForMediaSubType:];
-[AVAsset _chapterMetadataGroupsBestMatchingPreferredLanguages:containingItemsWithCommonKeys:];
-[AVAsset _chapterMetadataGroupsWithFigChapterGroups:titleLanguage:containingItemsWithCommonKeys:];
-[AVAsset _chapterMetadataGroupsWithTitleLanguage:containingItemsWithCommonKeys:];
-[AVAsset _chapterTracks];
-[AVAsset _comparisonToken];
-[AVAsset _doNotLogURLs];
-[AVAsset _handleURLRequest:];
-[AVAsset _hasResourceLoaderDelegate];
-[AVAsset _loadChapterInfo];
-[AVAsset _loadValuesSynchronouslyForKeys:trackKeys:];
-[AVAsset _mediaSelectionGroupDictionariesIncludingExtendedOptions:];
-[AVAsset _mediaSelectionGroupForMediaCharacteristic:extended:];
-[AVAsset _mediaSelectionGroupForMediaCharacteristic:inMediaSelectionGroupDictionaries:];
-[AVAsset _mediaSelectionGroupForPropertyList:extended:mediaSelectionOption:];
-[AVAsset _mutableComposition];
-[AVAsset _playbackItem];
-[AVAsset _requiresInProcessOperation];
-[AVAsset _serverHasDied];
-[AVAsset _setLoggingIdentifier:];
-[AVAsset _tracksDidChange];
-[AVAsset _tracksWithClass:];
-[AVAsset allMediaSelections];
-[AVAsset audioAlternatesTrackGroup];
-[AVAsset authoredMediaSelectionGroupForMediaCharacteristic:];
-[AVAsset availableChapterLanguages];
-[AVAsset availableChapterLocales];
-[AVAsset availableMediaCharacteristicsWithAuthoredMediaSelectionOptions];
-[AVAsset availableMediaCharacteristicsWithMediaSelectionOptions];
-[AVAsset chapterMetadataGroupsBestMatchingPreferredLanguages:];
-[AVAsset chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:];
-[AVAsset compatibleTrackForCompositionTrack:];
-[AVAsset constituentFileURLs];
-[AVAsset findCompatibleTrackForCompositionTrack:completionHandler:];
-[AVAsset findUnusedTrackIDWithCompletionHandler:];
-[AVAsset initWithData:contentType:options:];
-[AVAsset loadChapterMetadataGroupsBestMatchingPreferredLanguages:completionHandler:];
-[AVAsset loadChapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:completionHandler:];
-[AVAsset loadMediaSelectionGroupForMediaCharacteristic:completionHandler:];
-[AVAsset loadMetadataForFormat:completionHandler:];
-[AVAsset loadTrackWithTrackID:completionHandler:];
-[AVAsset loadTracksWithMediaCharacteristic:completionHandler:];
-[AVAsset loadTracksWithMediaType:completionHandler:];
-[AVAsset mediaSelectionGroupForPropertyList:extended:mediaSelectionOption:];
-[AVAsset mediaSelectionGroupForPropertyList:mediaSelectionOption:];
-[AVAsset moovAtomSize];
-[AVAsset preferredMediaSelection];
-[AVAsset referenceRestrictions];
-[AVAsset statusOfValueForKey:];
-[AVAsset subtitleAlternatesTrackGroup];
-[AVAsset trackGroups];
-[AVAsset unusedTrackID];
```
