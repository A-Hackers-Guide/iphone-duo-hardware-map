# `JFXCompositionTrackGroup`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 28 instance variables, 30 properties, 84 instance methods, 1 class methods

## Instance variables

```
B _isExporting;
B _seenSpeedClip;
B _seenMoreThanOneASBD;
B _isFlexMusic;
B _videoTrackInUse;
f _volumeAtLastVolumeChange;
f _volumeChangePending;
i _timeScale;
@"NSString" _label;
@"AVMutableCompositionTrack" _videoTrack;
@"AVMutableCompositionTrack" _audioTrack;
@"NSMutableArray" _audioSegments;
@"AVMutableAudioMixInputParameters" _audioParameters;
@"NSString" _preferredAudioTimePitchAlgorithm;
@"AVMutableComposition" _composition;
@"NSString" _timePitchAlgorithm;
@"NSMutableArray" _extraAudioTrackGroups;
^{opaqueCMFormatDescription=} _audioFormatDescription;
@"NSDictionary" _fmTrackInfoDict;
@"NSMutableArray" _videoSegments;
{?="value"q"timescale"i"flags"I"epoch"q} _cursor;
{?="value"q"timescale"i"flags"I"epoch"q} _cursorAtLastVideoInsertion;
{?="value"q"timescale"i"flags"I"epoch"q} _timeOfLastVolumeChange;
{?="value"q"timescale"i"flags"I"epoch"q} _timeOfLastRequest;
{?="value"q"timescale"i"flags"I"epoch"q} _fadeOutStart;
{?="value"q"timescale"i"flags"I"epoch"q} _fadeOutDuration;
{?="value"q"timescale"i"flags"I"epoch"q} _lastRampToZeroEnd;
{?="value"q"timescale"i"flags"I"epoch"q} _cursorForMovieAudio;
```

## Properties

```
@property (T@"NSString",N,V_timePitchAlgorithm) timePitchAlgorithm;
@property (T@"NSMutableArray",&,N,V_extraAudioTrackGroups) extraAudioTrackGroups;
@property (T^{opaqueCMFormatDescription=},&,N,V_audioFormatDescription) audioFormatDescription;
@property (TB,N,V_seenSpeedClip) seenSpeedClip;
@property (TB,N,V_seenMoreThanOneASBD) seenMoreThanOneASBD;
@property (T@"AVMutableAudioMixInputParameters",&,N,V_audioParameters) audioParameters;
@property (T@"NSDictionary",&,N,V_fmTrackInfoDict) fmTrackInfoDict;
@property (T{?=qiIq},N,V_lastRampToZeroEnd) lastRampToZeroEnd;
@property (TB,N,V_isFlexMusic) isFlexMusic;
@property (T{?=qiIq},R,N,V_cursorForMovieAudio) cursorForMovieAudio;
@property (Ti,N,V_timeScale) timeScale;
@property (TB,N,V_videoTrackInUse) videoTrackInUse;
@property (T@"NSMutableArray",&,N,V_videoSegments) videoSegments;
@property (T@"NSMutableArray",&,N,V_audioSegments) audioSegments;
@property (T@"NSString",C,N,V_label) label;
@property (T@"AVMutableCompositionTrack",&,N,V_videoTrack) videoTrack;
@property (T@"AVMutableCompositionTrack",&,N,V_audioTrack) audioTrack;
@property (T@"NSString",&,N,V_preferredAudioTimePitchAlgorithm) preferredAudioTimePitchAlgorithm;
@property (Ti,R,N) actualVideoTrackID;
@property (Ti,R,N) usableVideoTrackID;
@property (T{?=qiIq},R,N,V_cursor) cursor;
@property (T{?=qiIq},R,N,V_cursorAtLastVideoInsertion) cursorAtLastVideoInsertion;
@property (T{?=qiIq},N,V_timeOfLastVolumeChange) timeOfLastVolumeChange;
@property (T{?=qiIq},N,V_timeOfLastRequest) timeOfLastRequest;
@property (Tf,N,V_volumeAtLastVolumeChange) volumeAtLastVolumeChange;
@property (Tf,N,V_volumeChangePending) volumeChangePending;
@property (T{?=qiIq},N,V_fadeOutStart) fadeOutStart;
@property (T{?=qiIq},N,V_fadeOutDuration) fadeOutDuration;
@property (T@"AVMutableComposition",&,N,V_composition) composition;
@property (TB,N,V_isExporting) isExporting;
```

## Class methods

```
+[JFXCompositionTrackGroup visualDescriptionForSegments:];
```

## Instance methods

```
-[JFXCompositionTrackGroup validate];
-[JFXCompositionTrackGroup setComposition:];
-[JFXCompositionTrackGroup timeScale];
-[JFXCompositionTrackGroup cursor];
-[JFXCompositionTrackGroup isExporting];
-[JFXCompositionTrackGroup setTimeScale:];
-[JFXCompositionTrackGroup audioParameters];
-[JFXCompositionTrackGroup label];
-[JFXCompositionTrackGroup setLabel:];
-[JFXCompositionTrackGroup preferredAudioTimePitchAlgorithm];
-[JFXCompositionTrackGroup dealloc];
-[JFXCompositionTrackGroup audioFormatDescription];
-[JFXCompositionTrackGroup markDirty];
-[JFXCompositionTrackGroup composition];
-[JFXCompositionTrackGroup apply:];
-[JFXCompositionTrackGroup description];
-[JFXCompositionTrackGroup fadeOutDuration];
-[JFXCompositionTrackGroup setFadeOutDuration:];
-[JFXCompositionTrackGroup videoSegments];
-[JFXCompositionTrackGroup setVideoTrack:];
-[JFXCompositionTrackGroup videoTrack];
-[JFXCompositionTrackGroup setIsExporting:];
-[JFXCompositionTrackGroup audioTrack];
-[JFXCompositionTrackGroup asbd:isEqualTo:];
-[JFXCompositionTrackGroup fmTrackInfoDict];
-[JFXCompositionTrackGroup videoTrackInUse];
-[JFXCompositionTrackGroup applyCompositionItem:skipAudio:];
-[JFXCompositionTrackGroup setIsFlexMusic:];
-[JFXCompositionTrackGroup actualVideoTrackID];
-[JFXCompositionTrackGroup addExtraAudioTrackGroup:];
-[JFXCompositionTrackGroup applyAudioMixParameters:];
-[JFXCompositionTrackGroup applyCompositionItem:];
-[JFXCompositionTrackGroup applyCompositionItem:atTime:];
-[JFXCompositionTrackGroup applyCompositionItem:atTime:skipAudio:];
-[JFXCompositionTrackGroup applyCompositionItemAsLoopedAudio:forTimeRange:];
-[JFXCompositionTrackGroup applyPaddingToTime:];
-[JFXCompositionTrackGroup applyToTrack:withSegments:assets:];
-[JFXCompositionTrackGroup audioSegments];
-[JFXCompositionTrackGroup commitPendingVolumeToTime:];
-[JFXCompositionTrackGroup commitVolumeRampFromStartVolume:toEndVolume:timeRange:];
-[JFXCompositionTrackGroup containsAudioSegments];
-[JFXCompositionTrackGroup containsSegments];
-[JFXCompositionTrackGroup containsVideoSegments];
-[JFXCompositionTrackGroup cursorAtLastVideoInsertion];
-[JFXCompositionTrackGroup cursorForMovieAudio];
-[JFXCompositionTrackGroup extraAudioTrackGroups];
-[JFXCompositionTrackGroup fadeOutStart];
-[JFXCompositionTrackGroup initWithLabel:timeScale:];
-[JFXCompositionTrackGroup isFlexMusic];
-[JFXCompositionTrackGroup lastRampToZeroEnd];
-[JFXCompositionTrackGroup linearFadeOutValueForTime:];
-[JFXCompositionTrackGroup removeExtraAudioTrackGroups];
-[JFXCompositionTrackGroup requestVolume:atTime:];
-[JFXCompositionTrackGroup requestVolumeRampFromStartVolume:toEndVolume:timeRange:];
-[JFXCompositionTrackGroup requestVolumeRampFromStartVolume:toEndVolume:timeRange:fillEmptySegment:];
-[JFXCompositionTrackGroup resetVolumeState];
-[JFXCompositionTrackGroup seenMoreThanOneASBD];
-[JFXCompositionTrackGroup seenSpeedClip];
-[JFXCompositionTrackGroup setAudioFormatDescription:];
-[JFXCompositionTrackGroup setAudioParameters:];
-[JFXCompositionTrackGroup setAudioSegments:];
-[JFXCompositionTrackGroup setAudioTrack:];
-[JFXCompositionTrackGroup setExtraAudioTrackGroups:];
-[JFXCompositionTrackGroup setFadeOutStart:];
-[JFXCompositionTrackGroup setFadedVolumeRampFromStartVolume:toEndVolume:timeRange:];
-[JFXCompositionTrackGroup setFmTrackInfoDict:];
-[JFXCompositionTrackGroup setLastRampToZeroEnd:];
-[JFXCompositionTrackGroup setPreferredAudioTimePitchAlgorithm:];
-[JFXCompositionTrackGroup setSeenMoreThanOneASBD:];
-[JFXCompositionTrackGroup setSeenSpeedClip:];
-[JFXCompositionTrackGroup setTimeOfLastRequest:];
-[JFXCompositionTrackGroup setTimeOfLastVolumeChange:];
-[JFXCompositionTrackGroup setTimePitchAlgorithm:];
-[JFXCompositionTrackGroup setVideoSegments:];
-[JFXCompositionTrackGroup setVideoTrackInUse:];
-[JFXCompositionTrackGroup setVolumeAtLastVolumeChange:];
-[JFXCompositionTrackGroup setVolumeChangePending:];
-[JFXCompositionTrackGroup shouldCommitVolume:];
-[JFXCompositionTrackGroup timeOfLastRequest];
-[JFXCompositionTrackGroup timeOfLastVolumeChange];
-[JFXCompositionTrackGroup timePitchAlgorithm];
-[JFXCompositionTrackGroup usableVideoTrackID];
-[JFXCompositionTrackGroup volumeAtLastVolumeChange];
-[JFXCompositionTrackGroup volumeChangePending];
```
