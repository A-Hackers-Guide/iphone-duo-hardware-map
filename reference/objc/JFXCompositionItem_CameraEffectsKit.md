# `JFXCompositionItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 13 properties, 32 instance methods, 3 class methods

## Instance variables

```
B _isFinalClip;
B _isFreezeFrame;
B _isWaitingForResource;
f _speed;
i _timeScale;
@"<JFXPlayableElement>" _clip;
{?="value"q"timescale"i"flags"I"epoch"q} _destinationDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _audioStartOffset;
{?="value"q"timescale"i"flags"I"epoch"q} _audioEndOffset;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _sourceTimeRange;
```

## Properties

```
@property (T@"<JFXPlayableElement>",&,N,V_clip) clip;
@property (TB,N,V_isFinalClip) isFinalClip;
@property (T{?={?=qiIq}{?=qiIq}},N,V_sourceTimeRange) sourceTimeRange;
@property (T{?=qiIq},N,V_destinationDuration) destinationDuration;
@property (T{?=qiIq},N,V_audioStartOffset) audioStartOffset;
@property (T{?=qiIq},N,V_audioEndOffset) audioEndOffset;
@property (TB,R,N) hasVideoContent;
@property (TB,R,N,V_isFreezeFrame) isFreezeFrame;
@property (Tf,N,V_speed) speed;
@property (TB,R,N,V_isWaitingForResource) isWaitingForResource;
@property (TB,R,N) needSilenceAtEnd;
@property (TB,R,N) needAudioLoop;
@property (Ti,N,V_timeScale) timeScale;
```

## Class methods

```
+[JFXCompositionItem compositionItemWithClip:timeScale:];
+[JFXCompositionItem mediaserverdCrashed];
+[JFXCompositionItem silenceAsset];
```

## Instance methods

```
-[JFXCompositionItem timeScale];
-[JFXCompositionItem setClip:];
-[JFXCompositionItem setSpeed:];
-[JFXCompositionItem debugDescription];
-[JFXCompositionItem speed];
-[JFXCompositionItem setTimeScale:];
-[JFXCompositionItem dealloc];
-[JFXCompositionItem description];
-[JFXCompositionItem clip];
-[JFXCompositionItem sourceTimeRange];
-[JFXCompositionItem hasVideoContent];
-[JFXCompositionItem setIsFinalClip:];
-[JFXCompositionItem audioEndOffset];
-[JFXCompositionItem audioStartOffset];
-[JFXCompositionItem audioTrackSegmentsLoopedForDestinationTimeRange:];
-[JFXCompositionItem audioTrackSegmentsLoopedWithDestinationTime:];
-[JFXCompositionItem audioTrackSegmentsWithDestinationTime:];
-[JFXCompositionItem audioTrackSegmentsWithDestinationTime:paddedFromTime:];
-[JFXCompositionItem destinationDuration];
-[JFXCompositionItem emptyTrackSegmentWithDestinationRange:];
-[JFXCompositionItem emptyTrackSegmentWithDestinationTime:];
-[JFXCompositionItem initWithClip:timeScale:];
-[JFXCompositionItem isFinalClip];
-[JFXCompositionItem isFreezeFrame];
-[JFXCompositionItem isWaitingForResource];
-[JFXCompositionItem needAudioLoop];
-[JFXCompositionItem needSilenceAtEnd];
-[JFXCompositionItem setAudioEndOffset:];
-[JFXCompositionItem setAudioStartOffset:];
-[JFXCompositionItem setDestinationDuration:];
-[JFXCompositionItem setSourceTimeRange:];
-[JFXCompositionItem videoTrackSegmentsWithDestinationRange:];
```
