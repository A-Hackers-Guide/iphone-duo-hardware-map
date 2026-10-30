# `EditListCompositionState`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _isLastClip;
B _clipRequiresCA;
i _overlapLeft;
i _overlapRight;
i _audioStartOffset;
i _audioEndOffset;
@"JFXCompositionTrackGroup" _currentTrackGroup;
@"JFXCompositionTrackGroup" _alternateTrackGroup;
@"<JFXPlayableElement>" _clip;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _videoCompTimeRange;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _audioCompTimeRange;
```

## Properties

```
@property (T@"JFXCompositionTrackGroup",&,N,V_currentTrackGroup) currentTrackGroup;
@property (T@"JFXCompositionTrackGroup",&,N,V_alternateTrackGroup) alternateTrackGroup;
@property (T@"<JFXPlayableElement>",W,N,V_clip) clip;
@property (Ti,N,V_overlapLeft) overlapLeft;
@property (Ti,N,V_overlapRight) overlapRight;
@property (TB,N,V_isLastClip) isLastClip;
@property (TB,N,V_clipRequiresCA) clipRequiresCA;
@property (T{?={?=qiIq}{?=qiIq}},N,V_videoCompTimeRange) videoCompTimeRange;
@property (T{?={?=qiIq}{?=qiIq}},N,V_audioCompTimeRange) audioCompTimeRange;
@property (Ti,N,V_audioStartOffset) audioStartOffset;
@property (Ti,N,V_audioEndOffset) audioEndOffset;
```

## Instance methods

```
-[EditListCompositionState setClip:];
-[EditListCompositionState description];
-[EditListCompositionState clip];
-[EditListCompositionState setOverlapLeft:];
-[EditListCompositionState alternateTrackGroup];
-[EditListCompositionState audioCompTimeRange];
-[EditListCompositionState audioEndOffset];
-[EditListCompositionState audioStartOffset];
-[EditListCompositionState clipRequiresCA];
-[EditListCompositionState currentTrackGroup];
-[EditListCompositionState isLastClip];
-[EditListCompositionState overlapLeft];
-[EditListCompositionState overlapRight];
-[EditListCompositionState setAlternateTrackGroup:];
-[EditListCompositionState setAudioCompTimeRange:];
-[EditListCompositionState setAudioEndOffset:];
-[EditListCompositionState setAudioStartOffset:];
-[EditListCompositionState setClipRequiresCA:];
-[EditListCompositionState setCurrentTrackGroup:];
-[EditListCompositionState setIsLastClip:];
-[EditListCompositionState setOverlapRight:];
-[EditListCompositionState setVideoCompTimeRange:];
-[EditListCompositionState swapTrackGroup];
-[EditListCompositionState videoCompTimeRange];
```
