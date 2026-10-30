# `AVAssetVariantAudioRenditionSpecificAttributes`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"FigAlternateObjC" _figAlternateObjC;
@"AVMediaSelectionOption" _mediaSelectionOption;
```

## Properties

```
@property (Tq,R,N) channelCount;
@property (TB,R,N,GisBinaural) binaural;
@property (TB,R,N,GisImmersive) immersive;
@property (TB,R,N,GisDownmix) downmix;
```

## Instance methods

```
-[AVAssetVariantAudioRenditionSpecificAttributes sampleRate];
-[AVAssetVariantAudioRenditionSpecificAttributes channelCount];
-[AVAssetVariantAudioRenditionSpecificAttributes dealloc];
-[AVAssetVariantAudioRenditionSpecificAttributes initWithFigAlternateObjC:mediaSelectionOption:];
-[AVAssetVariantAudioRenditionSpecificAttributes isBinaural];
-[AVAssetVariantAudioRenditionSpecificAttributes isDownmix];
-[AVAssetVariantAudioRenditionSpecificAttributes isImmersive];
```
