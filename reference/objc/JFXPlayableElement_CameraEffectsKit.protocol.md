# `JFXPlayableElement` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `JFXDepthDataReaderCreationAttributesProvider`, `JFXARMetadataReaderCreationAttributesProvider`
- 0 instance variables, 18 properties, 25 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) uuid;
@property (Tq,R,N) playableAspectRatio;
@property (Tq,R,N) playableAspectRatioPreservationMode;
@property (T@"JFXMediaItem",R,N) mediaItem;
@property (TB,R,N) isAssetUnavailable;
@property (TB,R,N) isAssetLoaded;
@property (Tq,R,N) mediaType;
@property (TB,R,N) isStill;
@property (TB,R,N) isVideo;
@property (TB,R,N) shouldRenderVideoAsBlack;
@property (T{CGSize=dd},R,N) playableMediaSizeWithTransform;
@property (Ti,R,N) playableMediaContentMode;
@property (T@"NSData",R,N) originalAnimojiDataRepresentation;
@property (TQ,R,N) originalAnimojiVersionNumber;
@property (Ti,R,N) presentationTime;
@property (Ti,R,N) duration;
@property (Ti,R,N) mediaStartOffset;
@property (T@"PVTransformAnimation",R,N) transformAnimation;
```

## Instance methods

```
-[JFXPlayableElement mediaItem];
-[JFXPlayableElement uuid];
-[JFXPlayableElement isAssetLoaded];
-[JFXPlayableElement duration];
-[JFXPlayableElement mediaType];
-[JFXPlayableElement isVideo];
-[JFXPlayableElement presentationTime];
-[JFXPlayableElement transformAnimation];
-[JFXPlayableElement isStill];
-[JFXPlayableElement hasPlayableEffectOfType:];
-[JFXPlayableElement isAssetUnavailable];
-[JFXPlayableElement mediaStartOffset];
-[JFXPlayableElement originalAnimojiDataRepresentation];
-[JFXPlayableElement originalAnimojiVersionNumber];
-[JFXPlayableElement playableAspectRatio];
-[JFXPlayableElement playableAspectRatioPreservationMode];
-[JFXPlayableElement playableEffectStack];
-[JFXPlayableElement playableEffectStackExcludingType:];
-[JFXPlayableElement playableEffectsOfType:];
-[JFXPlayableElement playableMediaContentMode];
-[JFXPlayableElement playableMediaSizeWithTransform];
-[JFXPlayableElement playableRectInOutputSize:];
-[JFXPlayableElement playableScaleInOutputSize:];
-[JFXPlayableElement rectFromNormalizedPlayableRect:inOutputSize:];
-[JFXPlayableElement shouldRenderVideoAsBlack];
```
