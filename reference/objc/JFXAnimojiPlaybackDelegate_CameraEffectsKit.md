# `JFXAnimojiPlaybackDelegate`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PVCompositeDelegate`
- 16 instance variables, 20 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _isScrubbing;
B _useAnimojiBlendShapes;
@"JFXAnimojiEffectRenderer" _animojiRenderer;
@"JFXDepthDataMediaReader" _depthReader;
@"JFXARMetadataMediaReader" _arMetadataReader;
@"NSObject<OS_dispatch_queue>" _mediaDataReaderUpdateQueue;
@"JFXSharedMediaDataReaderManager" _sharedMediaDataReaderManager;
@"NSObject<OS_dispatch_queue>" _animojiRenderQueue;
@"JFXAnimojiEffect" _animojiEffect;
@"<JFXPlayableElement>" _playableElement;
@"NSObject<OS_dispatch_queue>" _delayedUnloadPlaybackQueue;
@? _delayedUnloadPlaybackResourcesBlock;
@"NSObject<OS_dispatch_queue>" _cachedAnimojiImageQueue;
@"JFXCachedAnimojiImage" _cachedAnimojiImage;
{?="value"q"timescale"i"flags"I"epoch"q} _playbackElementPlaybackPresentationOffset;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _playbackElementPlaybackMediaRange;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_mediaDataReaderUpdateQueue) mediaDataReaderUpdateQueue;
@property (T@"JFXARMetadataMediaReader",&,N,V_arMetadataReader) arMetadataReader;
@property (T@"JFXDepthDataMediaReader",&,N,V_depthReader) depthReader;
@property (T@"JFXSharedMediaDataReaderManager",&,N,V_sharedMediaDataReaderManager) sharedMediaDataReaderManager;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_animojiRenderQueue) animojiRenderQueue;
@property (T@"JFXAnimojiEffectRenderer",&,N,V_animojiRenderer) animojiRenderer;
@property (T@"JFXAnimojiEffect",&,N,V_animojiEffect) animojiEffect;
@property (TB,N,V_useAnimojiBlendShapes) useAnimojiBlendShapes;
@property (T@"<JFXPlayableElement>",R,N,V_playableElement) playableElement;
@property (T{?=qiIq},R,N,V_playbackElementPlaybackPresentationOffset) playbackElementPlaybackPresentationOffset;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_playbackElementPlaybackMediaRange) playbackElementPlaybackMediaRange;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_delayedUnloadPlaybackQueue) delayedUnloadPlaybackQueue;
@property (T@?,C,N,V_delayedUnloadPlaybackResourcesBlock) delayedUnloadPlaybackResourcesBlock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_cachedAnimojiImageQueue) cachedAnimojiImageQueue;
@property (T@"JFXCachedAnimojiImage",&,N,V_cachedAnimojiImage) cachedAnimojiImage;
@property (TB,N,V_isScrubbing) isScrubbing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXAnimojiPlaybackDelegate setIsScrubbing:];
-[JFXAnimojiPlaybackDelegate isScrubbing];
-[JFXAnimojiPlaybackDelegate JFX_arMetadataReaderItemForMediaTime:];
-[JFXAnimojiPlaybackDelegate JFX_avDepthDataFromDepthDataForMediaTime:];
-[JFXAnimojiPlaybackDelegate JFX_cacheAnimojiImage:];
-[JFXAnimojiPlaybackDelegate JFX_cachedAnimojiImageForMediaTime:forAnimojiRenderingAttributes:];
-[JFXAnimojiPlaybackDelegate JFX_initAnimojiImageBufferCachingProperties];
-[JFXAnimojiPlaybackDelegate JFX_loadAnimojiRenderer];
-[JFXAnimojiPlaybackDelegate JFX_unloadMediaDataReaders];
-[JFXAnimojiPlaybackDelegate setDepthReader:];
-[JFXAnimojiPlaybackDelegate JFX_clearCachedAnimojiImages];
-[JFXAnimojiPlaybackDelegate animojiRenderer];
-[JFXAnimojiPlaybackDelegate JFX_initAnimojiRenderingProperies];
-[JFXAnimojiPlaybackDelegate JFX_initMediaDataReaderProperties];
-[JFXAnimojiPlaybackDelegate JFX_initPlaybackLoadingProperies];
-[JFXAnimojiPlaybackDelegate JFX_loadMediaDataReaders];
-[JFXAnimojiPlaybackDelegate JFX_loadResourcesForPlayback];
-[JFXAnimojiPlaybackDelegate JFX_renderAnimojiEffect:forTime:withARFrame:depthData:inputBufferSize:captureOrientation:interfaceOrientation:preRecordedBlendShapes:backgroundColor:];
-[JFXAnimojiPlaybackDelegate JFX_requestUnloadResourcesForPlayback];
-[JFXAnimojiPlaybackDelegate JFX_setMediaDataReaderScrubbingMode:];
-[JFXAnimojiPlaybackDelegate JFX_unloadAnimojiRenderer];
-[JFXAnimojiPlaybackDelegate JFX_unloadResourcesForPlayback];
-[JFXAnimojiPlaybackDelegate playableElement];
-[JFXAnimojiPlaybackDelegate animojiEffect];
-[JFXAnimojiPlaybackDelegate animojiRenderQueue];
-[JFXAnimojiPlaybackDelegate arMetadataReader];
-[JFXAnimojiPlaybackDelegate cachedAnimojiImage];
-[JFXAnimojiPlaybackDelegate cachedAnimojiImageQueue];
-[JFXAnimojiPlaybackDelegate delayedUnloadPlaybackQueue];
-[JFXAnimojiPlaybackDelegate delayedUnloadPlaybackResourcesBlock];
-[JFXAnimojiPlaybackDelegate depthReader];
-[JFXAnimojiPlaybackDelegate initWithPlayableElement:sharedMediaDataReaderManager:];
-[JFXAnimojiPlaybackDelegate jfx_mediaTimeFromPlaybackTime:];
-[JFXAnimojiPlaybackDelegate loadWithUserContext:];
-[JFXAnimojiPlaybackDelegate mediaDataReaderUpdateQueue];
-[JFXAnimojiPlaybackDelegate playbackElementPlaybackMediaRange];
-[JFXAnimojiPlaybackDelegate playbackElementPlaybackPresentationOffset];
-[JFXAnimojiPlaybackDelegate preprocessWithInputs:time:userContext:compositeContext:];
-[JFXAnimojiPlaybackDelegate renderWithInputs:time:userContext:compositeContext:];
-[JFXAnimojiPlaybackDelegate setAnimojiEffect:];
-[JFXAnimojiPlaybackDelegate setAnimojiRenderer:];
-[JFXAnimojiPlaybackDelegate setArMetadataReader:];
-[JFXAnimojiPlaybackDelegate setCachedAnimojiImage:];
-[JFXAnimojiPlaybackDelegate setDelayedUnloadPlaybackResourcesBlock:];
-[JFXAnimojiPlaybackDelegate setSharedMediaDataReaderManager:];
-[JFXAnimojiPlaybackDelegate setUseAnimojiBlendShapes:];
-[JFXAnimojiPlaybackDelegate sharedMediaDataReaderManager];
-[JFXAnimojiPlaybackDelegate unloadWithUserContext:];
-[JFXAnimojiPlaybackDelegate useAnimojiBlendShapes];
```
