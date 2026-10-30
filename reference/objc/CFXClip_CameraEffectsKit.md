# `CFXClip`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `JFXPlayableElement`
- 13 instance variables, 31 properties, 71 instance methods, 6 class methods

## Instance variables

```
i _presentationTime;
i _duration;
i _mediaStartOffset;
i _transformInitialStartOffset;
@"NSString" _uuid;
@"JFXMediaItem" _mediaItem;
@"NSURL" _metadataURL;
@"NSData" _originalAnimojiDataRepresentation;
Q _originalAnimojiVersionNumber;
@"PVTransformAnimation" _transformAnimation;
@"NSMutableArray" _filters;
@"NSMutableArray" _overlays;
@"NSMutableArray" _animojis;
```

## Properties

```
@property (T@"NSString",&,N,V_uuid) uuid;
@property (T@"JFXMediaItem",&,N,V_mediaItem) mediaItem;
@property (T@"NSMutableArray",&,N,V_filters) filters;
@property (T@"NSMutableArray",&,N,V_overlays) overlays;
@property (T@"NSMutableArray",&,N,V_animojis) animojis;
@property (Ti,R,N,V_presentationTime) presentationTime;
@property (Ti,N,V_duration) duration;
@property (Ti,R,N,V_mediaStartOffset) mediaStartOffset;
@property (Tq,R,N) mediaType;
@property (Tq,N) mediaInterfaceOrientationForDisplay;
@property (T{CGSize=dd},R,N) mediaSize;
@property (T@"NSURL",&,N,V_metadataURL) metadataURL;
@property (T@"NSData",&,N,V_originalAnimojiDataRepresentation) originalAnimojiDataRepresentation;
@property (TQ,N,V_originalAnimojiVersionNumber) originalAnimojiVersionNumber;
@property (T@"PVTransformAnimation",&,N,V_transformAnimation) transformAnimation;
@property (Ti,N,V_transformInitialStartOffset) transformInitialStartOffset;
@property (Tq,R,N) playableAspectRatio;
@property (Tq,R,N) playableAspectRatioPreservationMode;
@property (TB,R,N) isAssetUnavailable;
@property (TB,R,N) isAssetLoaded;
@property (TB,R,N) isStill;
@property (TB,R,N) isVideo;
@property (TB,R,N) shouldRenderVideoAsBlack;
@property (T{CGSize=dd},R,N) playableMediaSizeWithTransform;
@property (Ti,R,N) playableMediaContentMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"JFXMediaReaderCreationAVAssetTrackAttributes",R,N) depthDataReaderAssetTrackAttributes;
@property (T@"JFXMediaReaderCreationAVAssetTrackAttributes",R,N) arMetadataReaderAssetTrackAttributes;
```

## Class methods

```
+[CFXClip cfx_createStillClipPreviewWithLocalURL:maximumImageDimension:effectStack:completionHandler:];
+[CFXClip cfx_createVideoClipWithLocalURL:effectStack:completionHandler:];
+[CFXClip cfx_writeProxyImageToURL:fromImageAtURL:maximumImageDimension:outColorSpace:];
+[CFXClip createCaptureClip];
+[CFXClip createClipWithLocalURL:effectStack:isVideo:maximumImageDimension:completionHandler:];
+[CFXClip defaultClip];
```

## Instance methods

```
-[CFXClip mediaItem];
-[CFXClip addEffect:];
-[CFXClip uuid];
-[CFXClip init];
-[CFXClip metadataURL];
-[CFXClip dealloc];
-[CFXClip setUuid:];
-[CFXClip removeAllEffects];
-[CFXClip setFilters:];
-[CFXClip isAssetLoaded];
-[CFXClip filters];
-[CFXClip duration];
-[CFXClip overlays];
-[CFXClip removeEffect:];
-[CFXClip hash];
-[CFXClip description];
-[CFXClip setDuration:];
-[CFXClip setOverlays:];
-[CFXClip copyWithZone:];
-[CFXClip mediaType];
-[CFXClip isEqual:];
-[CFXClip isVideo];
-[CFXClip presentationTime];
-[CFXClip setMetadataURL:];
-[CFXClip initWithMediaItem:];
-[CFXClip setMediaItem:];
-[CFXClip transformAnimation];
-[CFXClip mediaSize];
-[CFXClip setPresentationTime:];
-[CFXClip addEffectStack:];
-[CFXClip isStill];
-[CFXClip setTransformInitialStartOffset:];
-[CFXClip animojis];
-[CFXClip arMetadataReaderAssetTrackAttributes];
-[CFXClip cfx_addEffect:];
-[CFXClip cfx_clipType];
-[CFXClip cfx_effectsOfType:];
-[CFXClip cfx_isAssetInTrash];
-[CFXClip cfx_isAssetMissing];
-[CFXClip cfx_removeAllEffectsOfType:];
-[CFXClip depthDataReaderAssetTrackAttributes];
-[CFXClip effectStack];
-[CFXClip effectStackExcludingType:];
-[CFXClip effectsOfType:];
-[CFXClip hasMetadataAsset];
-[CFXClip hasPlayableEffectOfType:];
-[CFXClip isAssetUnavailable];
-[CFXClip mediaInterfaceOrientationForDisplay];
-[CFXClip mediaStartOffset];
-[CFXClip originalAnimojiDataRepresentation];
-[CFXClip originalAnimojiVersionNumber];
-[CFXClip playableAspectRatio];
-[CFXClip playableAspectRatioPreservationMode];
-[CFXClip playableEffectStack];
-[CFXClip playableEffectStackExcludingType:];
-[CFXClip playableEffectsOfType:];
-[CFXClip playableMediaContentMode];
-[CFXClip playableMediaSizeWithTransform];
-[CFXClip playableRectInOutputSize:];
-[CFXClip playableScaleInOutputSize:];
-[CFXClip rectFromNormalizedPlayableRect:inOutputSize:];
-[CFXClip removeAllEffectsOfType:];
-[CFXClip setAnimojis:];
-[CFXClip setMediaInterfaceOrientationForDisplay:];
-[CFXClip setOriginalAnimojiDataRepresentation:];
-[CFXClip setOriginalAnimojiVersionNumber:];
-[CFXClip setTransformAnimation:];
-[CFXClip shouldRenderVideoAsBlack];
-[CFXClip stringForMediaType:];
-[CFXClip transformInitialStartOffset];
-[CFXClip updateTransformPresentationTimeRange];
```
