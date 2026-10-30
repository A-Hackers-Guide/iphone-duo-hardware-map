# `AVPortraitEffectsMatte`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"AVPortraitEffectsMatteInternal" _internal;
```

## Properties

```
@property (TI,R) pixelFormatType;
@property (T^{__CVBuffer=},R) mattingImage;
```

## Class methods

```
+[AVPortraitEffectsMatte initialize];
+[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:];
+[AVPortraitEffectsMatte _allSupportedPortraitEffectsMattePixelFormatTypes];
```

## Instance methods

```
-[AVPortraitEffectsMatte auxiliaryImageType];
-[AVPortraitEffectsMatte debugDescription];
-[AVPortraitEffectsMatte dealloc];
-[AVPortraitEffectsMatte description];
-[AVPortraitEffectsMatte pixelFormatType];
-[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:];
-[AVPortraitEffectsMatte mattingImage];
-[AVPortraitEffectsMatte copyAuxiliaryMetadata];
-[AVPortraitEffectsMatte initWithPixelBuffer:auxiliaryMetadata:];
-[AVPortraitEffectsMatte initWithPixelBuffer:portraitEffectsMatteMetadataDictionary:];
-[AVPortraitEffectsMatte portraitEffectsMatteByApplyingExifOrientation:];
-[AVPortraitEffectsMatte portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:];
-[AVPortraitEffectsMatte versionMajor];
-[AVPortraitEffectsMatte versionMinor];
```
