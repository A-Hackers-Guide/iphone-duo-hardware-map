# `AVMediaSelectionTrackOption`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMediaSelectionOption`
- 7 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
@ _groupID;
@"AVAssetTrack" _track;
@"NSDictionary" _dictionary;
@"AVWeakReference" _weakReferenceToGroup;
B _displaysNonForcedSubtitles;
@"NSNumber" _audioCompositionPresetIndex;
@"NSArray" _audioCompositionPresetIndexesForFallbackIDs;
```

## Instance methods

```
-[AVMediaSelectionTrackOption isPlayable];
-[AVMediaSelectionTrackOption commonMetadata];
-[AVMediaSelectionTrackOption _groupID];
-[AVMediaSelectionTrackOption metadataForFormat:];
-[AVMediaSelectionTrackOption trackID];
-[AVMediaSelectionTrackOption dealloc];
-[AVMediaSelectionTrackOption group];
-[AVMediaSelectionTrackOption dictionary];
-[AVMediaSelectionTrackOption availableMetadataFormats];
-[AVMediaSelectionTrackOption locale];
-[AVMediaSelectionTrackOption track];
-[AVMediaSelectionTrackOption initWithAsset:group:dictionary:];
-[AVMediaSelectionTrackOption hash];
-[AVMediaSelectionTrackOption mediaType];
-[AVMediaSelectionTrackOption isEqual:];
-[AVMediaSelectionTrackOption _audioCompositionPresetIndex];
-[AVMediaSelectionTrackOption _audioCompositionPresetIndexesForFallbackIDs];
-[AVMediaSelectionTrackOption _track];
-[AVMediaSelectionTrackOption associatedMediaSelectionOptionInMediaSelectionGroup:];
-[AVMediaSelectionTrackOption displaysNonForcedSubtitles];
-[AVMediaSelectionTrackOption mediaSubTypes];
```
