# `AVPlaybackItemTrackInspector`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetTrackInspector`
- 4 instance variables, 0 properties, 19 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigPlaybackItem=} _playbackItem;
i _trackID;
I _mediaType;
@"AVWeakReference" _weakReferenceToAsset;
```

## Instance methods

```
-[AVPlaybackItemTrackInspector dimensions];
-[AVPlaybackItemTrackInspector formatDescriptions];
-[AVPlaybackItemTrackInspector asset];
-[AVPlaybackItemTrackInspector timeRange];
-[AVPlaybackItemTrackInspector preferredTransform];
-[AVPlaybackItemTrackInspector trackID];
-[AVPlaybackItemTrackInspector naturalSize];
-[AVPlaybackItemTrackInspector dealloc];
-[AVPlaybackItemTrackInspector peakDataRate];
-[AVPlaybackItemTrackInspector _initWithAsset:trackID:trackIndex:];
-[AVPlaybackItemTrackInspector _valueAsCFTypeForProperty:];
-[AVPlaybackItemTrackInspector isEnabled];
-[AVPlaybackItemTrackInspector hash];
-[AVPlaybackItemTrackInspector estimatedDataRate];
-[AVPlaybackItemTrackInspector mediaType];
-[AVPlaybackItemTrackInspector isEqual:];
-[AVPlaybackItemTrackInspector _figMediaType];
-[AVPlaybackItemTrackInspector _playbackItem];
-[AVPlaybackItemTrackInspector samplePresentationTimeForTrackTime:];
```
