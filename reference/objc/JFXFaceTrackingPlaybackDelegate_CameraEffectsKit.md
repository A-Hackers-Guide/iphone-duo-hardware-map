# `JFXFaceTrackingPlaybackDelegate`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PVEffectTimedPropertiesDelegate`
- 10 instance variables, 14 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _isScrubbing;
@"JFXARMetadataMediaReader" _arMetadataReader;
@"NSObject<OS_dispatch_queue>" _mediaDataReaderUpdateQueue;
@"JFXSharedMediaDataReaderManager" _sharedMediaDataReaderManager;
@"<JFXPlayableElement>" _playableElement;
@"NSObject<OS_dispatch_queue>" _cachedFaceTrackingPropertiesQueue;
@"JFXFaceTrackingPlaybackProperties" _cachedFaceTrackingProperties;
{CGSize="width"d"height"d} _outputSize;
{?="value"q"timescale"i"flags"I"epoch"q} _playbackElementPlaybackPresentationOffset;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _playbackElementPlaybackMediaRange;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_mediaDataReaderUpdateQueue) mediaDataReaderUpdateQueue;
@property (T@"JFXARMetadataMediaReader",&,N,V_arMetadataReader) arMetadataReader;
@property (T@"JFXSharedMediaDataReaderManager",R,N,V_sharedMediaDataReaderManager) sharedMediaDataReaderManager;
@property (T@"<JFXPlayableElement>",R,N,V_playableElement) playableElement;
@property (T{CGSize=dd},R,N,V_outputSize) outputSize;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_cachedFaceTrackingPropertiesQueue) cachedFaceTrackingPropertiesQueue;
@property (T@"JFXFaceTrackingPlaybackProperties",&,N,V_cachedFaceTrackingProperties) cachedFaceTrackingProperties;
@property (T{?=qiIq},R,N,V_playbackElementPlaybackPresentationOffset) playbackElementPlaybackPresentationOffset;
@property (T{?={?=qiIq}{?=qiIq}},R,N,V_playbackElementPlaybackMediaRange) playbackElementPlaybackMediaRange;
@property (TB,N,V_isScrubbing) isScrubbing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXFaceTrackingPlaybackDelegate setIsScrubbing:];
-[JFXFaceTrackingPlaybackDelegate isScrubbing];
-[JFXFaceTrackingPlaybackDelegate outputSize];
-[JFXFaceTrackingPlaybackDelegate JFX_cachedFaceTrackingPropertiesForMediaTime:forDisplayingMediaAtInterfaceOrientation:];
-[JFXFaceTrackingPlaybackDelegate JFX_faceTrackingPlaybackPropertiesAtTime:forDisplayingMediaAtInterfaceOrientation:];
-[JFXFaceTrackingPlaybackDelegate JFX_initMetadataReadingProperties];
-[JFXFaceTrackingPlaybackDelegate JFX_unloadMediaDataReaders];
-[JFXFaceTrackingPlaybackDelegate JFX_arMetadataForMediaTime:foundTimeRange:];
-[JFXFaceTrackingPlaybackDelegate JFX_cacheFaceTrackingProperties:];
-[JFXFaceTrackingPlaybackDelegate JFX_initFaceTrackingCachingProperties];
-[JFXFaceTrackingPlaybackDelegate JFX_loadMediaDataReaders];
-[JFXFaceTrackingPlaybackDelegate JFX_setMediaDataReaderScrubbingMode:];
-[JFXFaceTrackingPlaybackDelegate playableElement];
-[JFXFaceTrackingPlaybackDelegate arDataAtTime:forDisplayingMediaAtInterfaceOrientation:];
-[JFXFaceTrackingPlaybackDelegate arMetadataReader];
-[JFXFaceTrackingPlaybackDelegate cachedFaceTrackingProperties];
-[JFXFaceTrackingPlaybackDelegate cachedFaceTrackingPropertiesQueue];
-[JFXFaceTrackingPlaybackDelegate effect:didStopRequestingTimedProperties:];
-[JFXFaceTrackingPlaybackDelegate effect:timedPropertiesForGroup:time:userContext:];
-[JFXFaceTrackingPlaybackDelegate effect:willStartRequestingTimedProperties:];
-[JFXFaceTrackingPlaybackDelegate faceTrackingTransformAtTime:forDisplayingMediaAtInterfaceOrientation:];
-[JFXFaceTrackingPlaybackDelegate initWithPlayableElement:sharedMediaDataReaderManager:outputSize:];
-[JFXFaceTrackingPlaybackDelegate jfx_mediaTimeFromPlaybackTime:];
-[JFXFaceTrackingPlaybackDelegate mediaDataReaderUpdateQueue];
-[JFXFaceTrackingPlaybackDelegate playbackElementPlaybackMediaRange];
-[JFXFaceTrackingPlaybackDelegate playbackElementPlaybackPresentationOffset];
-[JFXFaceTrackingPlaybackDelegate setArMetadataReader:];
-[JFXFaceTrackingPlaybackDelegate setCachedFaceTrackingProperties:];
-[JFXFaceTrackingPlaybackDelegate sharedMediaDataReaderManager];
-[JFXFaceTrackingPlaybackDelegate supportedTimedPropertyGroupsForEffect:];
```
