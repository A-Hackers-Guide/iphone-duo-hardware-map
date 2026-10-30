# `JFXComposition`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 24 properties, 98 instance methods, 1 class methods

## Instance variables

```
B _needsUpdate;
f _globalAudioVolume;
I _parentCode;
@"AVPlayerItem" _playerItem;
@"AVMutableComposition" _avComposition;
@"AVMutableVideoComposition" _videoComposition;
@"AVMutableAudioMix" _audioMix;
@"NSMapTable" _clipCustomRendererMap;
@"NSMapTable" _clipFaceTrackingPlaybackDelegates;
@"AVPlayerItem" _avPlayerItem;
@"JFXCompositionTrackGroup" _trackGroupA;
@"JFXCompositionTrackGroup" _trackGroupB;
@"NSMutableArray" _audioMixParameters;
@"<JFXCompositionPlayableElementsDataSource>" _clipsDataSource;
@"NSMutableArray" _videoCompositionInstructions;
q _backgroundAudioTrackCount;
q _foregroundAudioTrackCount;
@"<JFXPlayableElement>" _liveTransformClip;
@"NSMutableDictionary" _assetsUsed;
{CGSize="width"d"height"d} _viewSize;
{CGSize="width"d"height"d} _previousRenderSize;
{?="value"q"timescale"i"flags"I"epoch"q} _duration;
{PVTransformAnimationInfo="time"{?="value"q"timescale"i"flags"I"epoch"q}"translation"{CGPoint="x"d"y"d}"scale"d"rotation"d} _liveCompositionTransform;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_clipCustomRendererMap) clipCustomRendererMap;
@property (T@"NSMapTable",&,N,V_clipFaceTrackingPlaybackDelegates) clipFaceTrackingPlaybackDelegates;
@property (T@"AVPlayerItem",&,N,V_playerItem) playerItem;
@property (T@"AVMutableComposition",&,N,V_avComposition) avComposition;
@property (T@"AVMutableVideoComposition",&,N,V_videoComposition) videoComposition;
@property (T@"AVMutableAudioMix",&,N,V_audioMix) audioMix;
@property (T{?=qiIq},N,V_duration) duration;
@property (T@"AVPlayerItem",&,N,V_avPlayerItem) avPlayerItem;
@property (T@"JFXCompositionTrackGroup",&,N,V_trackGroupA) trackGroupA;
@property (T@"JFXCompositionTrackGroup",&,N,V_trackGroupB) trackGroupB;
@property (T@"NSMutableArray",&,N,V_audioMixParameters) audioMixParameters;
@property (T@"<JFXCompositionPlayableElementsDataSource>",&,N,V_clipsDataSource) clipsDataSource;
@property (T@"NSMutableArray",&,N,V_videoCompositionInstructions) videoCompositionInstructions;
@property (T{CGSize=dd},N,V_previousRenderSize) previousRenderSize;
@property (Tq,N,V_backgroundAudioTrackCount) backgroundAudioTrackCount;
@property (Tq,N,V_foregroundAudioTrackCount) foregroundAudioTrackCount;
@property (TB,N,V_needsUpdate) needsUpdate;
@property (T@"<JFXPlayableElement>",&,N,V_liveTransformClip) liveTransformClip;
@property (T{PVTransformAnimationInfo={?=qiIq}{CGPoint=dd}dd},N,V_liveCompositionTransform) liveCompositionTransform;
@property (T@"NSMutableDictionary",&,N,V_assetsUsed) assetsUsed;
@property (Tf,N,V_globalAudioVolume) globalAudioVolume;
@property (T{CGSize=dd},N,V_viewSize) viewSize;
@property (T@"PVColorSpace",R,N) compositionOutputColorSpace;
@property (TI,N,V_parentCode) parentCode;
```

## Class methods

```
+[JFXComposition instructionBuilderClass];
```

## Instance methods

```
-[JFXComposition validate];
-[JFXComposition needsUpdate];
-[JFXComposition setVideoComposition:];
-[JFXComposition update];
-[JFXComposition playerItem];
-[JFXComposition dealloc];
-[JFXComposition markDirty];
-[JFXComposition duration];
-[JFXComposition viewSize];
-[JFXComposition setDuration:];
-[JFXComposition setNeedsUpdate:];
-[JFXComposition videoComposition];
-[JFXComposition avPlayerItem];
-[JFXComposition setAvPlayerItem:];
-[JFXComposition setViewSize:];
-[JFXComposition audioMix];
-[JFXComposition setAudioMix:];
-[JFXComposition setPlayerItem:];
-[JFXComposition audioMixParameters];
-[JFXComposition setAudioMixParameters:];
-[JFXComposition playerItemDidReachEnd:];
-[JFXComposition CARenderingRequiredForClip:];
-[JFXComposition JFX_applyPropertiesForCustomVideoCompositor:];
-[JFXComposition JFX_finalizeVideoComposition];
-[JFXComposition JFX_setScrubbingModeForPlaybackDelegates:];
-[JFXComposition JFX_updateFaceTrackPropertiesForEffectsAtTime:];
-[JFXComposition JFX_updatePlaybackDelegatesForClip:];
-[JFXComposition outputFrameRate];
-[JFXComposition setTrackGroupA:];
-[JFXComposition AVComposition];
-[JFXComposition CFX_updateFaceTrackingPlaybackDelegateForClip:sharedMediaDataReaderManager:];
-[JFXComposition clipsDataSource];
-[JFXComposition JFX_hasEffectThatRequiresCustomRendering];
-[JFXComposition JFX_isContigousSplitClip:nextClip:];
-[JFXComposition JFX_preferredRenderScale];
-[JFXComposition setTrackGroupB:];
-[JFXComposition addBackTracksIfRemoved];
-[JFXComposition animojiCustomRendererPropsForClip:currentCustomProperties:sharedMediaDataReaderManager:];
-[JFXComposition applyExportProperties];
-[JFXComposition applyPlayerItemProperties];
-[JFXComposition applyPropertiesForCustomVideoCompositor:];
-[JFXComposition assetUsed:];
-[JFXComposition assetsUsed];
-[JFXComposition avComposition];
-[JFXComposition backgroundAudioTrackCount];
-[JFXComposition buildClipList];
-[JFXComposition burnInPlaybackSettings:];
-[JFXComposition clearPlayerItemProperties];
-[JFXComposition clipCustomRendererMap];
-[JFXComposition clipFaceTrackingPlaybackDelegates];
-[JFXComposition clipTransform:];
-[JFXComposition compositionItemsForState:compositionItem:backfillCompositionItem:];
-[JFXComposition compositionOutputColorSpace];
-[JFXComposition dissolveGraphNode:from:to:];
-[JFXComposition emptySegments:];
-[JFXComposition foregroundAudioTrackCount];
-[JFXComposition globalAudioVolume];
-[JFXComposition initWithClipsDataSource:];
-[JFXComposition instructionToHideTrackID:whileHidingTrackID:timeRange:requiresCARendering:];
-[JFXComposition instructionToShowClip:withTrackID:withTransform:timeRange:requiresCARendering:];
-[JFXComposition instructionToShowImageWithClip:withTransform:timeRange:requiresCARendering:];
-[JFXComposition liveCompositionTransform];
-[JFXComposition liveTransformClip];
-[JFXComposition logAddedTrack:trackID:];
-[JFXComposition logRemovedTrack:trackID:];
-[JFXComposition newInstructionGraphNodeForClip:clipTransform:compositionTrackID:requiresTweening:isContainedClip:];
-[JFXComposition noteEffectChangeForClip:];
-[JFXComposition notifyNeedsEffectPropertiesUpdatedForPlaybackTime:];
-[JFXComposition notifyPlaybackDidStopAtTime:];
-[JFXComposition notifyPlaybackWillBegin];
-[JFXComposition parentCode];
-[JFXComposition previousRenderSize];
-[JFXComposition rebuildCompositionInstructionsForVideoStillTitleCard:];
-[JFXComposition refreshAVComposition];
-[JFXComposition removeEmptyTracks];
-[JFXComposition removeTrackFromAudioMix:];
-[JFXComposition removeTrackIfEmpty:];
-[JFXComposition setAssetsUsed:];
-[JFXComposition setAvComposition:];
-[JFXComposition setBackgroundAudioTrackCount:];
-[JFXComposition setClipCustomRendererMap:];
-[JFXComposition setClipFaceTrackingPlaybackDelegates:];
-[JFXComposition setClipsDataSource:];
-[JFXComposition setForegroundAudioTrackCount:];
-[JFXComposition setGlobalAudioVolume:];
-[JFXComposition setLiveCompositionTransform:];
-[JFXComposition setLiveTransformClip:];
-[JFXComposition setParentCode:];
-[JFXComposition setPreviousRenderSize:];
-[JFXComposition setRenderScale];
-[JFXComposition setVideoCompositionInstructions:];
-[JFXComposition timeRangeForClip:];
-[JFXComposition trackGroupA];
-[JFXComposition trackGroupB];
-[JFXComposition updateRenderSizeIfNeeded];
-[JFXComposition updateVideoAndAudioInstructionForState:previousInstructions:waitingForResource:];
-[JFXComposition videoCompositionInstructions];
-[JFXComposition volumeForClip:];
```
