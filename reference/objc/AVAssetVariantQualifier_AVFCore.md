# `AVAssetVariantQualifier`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 1 properties, 9 instance methods, 17 class methods

## Instance variables

```
@"AVAssetVariant" _variant;
@"FigAssetVariantQualifierObjC" _figAssetVariantQualifier;
q _environmentalConditions;
```

## Properties

```
@property (Tq,N) environmentalConditions;
```

## Class methods

```
+[AVAssetVariantQualifier supportsSecureCoding];
+[AVAssetVariantQualifier assetVariantQualifierForMaximumValueInKeyPath:];
+[AVAssetVariantQualifier assetVariantQualifierForMinimumValueInKeyPath:];
+[AVAssetVariantQualifier assetVariantQualifierWithPredicate:];
+[AVAssetVariantQualifier assetVariantQualifierWithVariant:];
+[AVAssetVariantQualifier predicateForAudioSampleRate:mediaSelectionOption:operatorType:];
+[AVAssetVariantQualifier predicateForAudioSampleRate:operatorType:];
+[AVAssetVariantQualifier predicateForBinauralAudio:];
+[AVAssetVariantQualifier predicateForBinauralAudio:mediaSelectionOption:];
+[AVAssetVariantQualifier predicateForChannelCount:mediaSelectionOption:operatorType:];
+[AVAssetVariantQualifier predicateForChannelCount:operatorType:];
+[AVAssetVariantQualifier predicateForDownmixAudio:];
+[AVAssetVariantQualifier predicateForDownmixAudio:mediaSelectionOption:];
+[AVAssetVariantQualifier predicateForImmersiveAudio:];
+[AVAssetVariantQualifier predicateForImmersiveAudio:mediaSelectionOption:];
+[AVAssetVariantQualifier predicateForPresentationHeight:operatorType:];
+[AVAssetVariantQualifier predicateForPresentationWidth:operatorType:];
```

## Instance methods

```
-[AVAssetVariantQualifier initWithVariant:];
-[AVAssetVariantQualifier dealloc];
-[AVAssetVariantQualifier encodeWithCoder:];
-[AVAssetVariantQualifier initWithCoder:];
-[AVAssetVariantQualifier copyWithZone:];
-[AVAssetVariantQualifier _figAssetVariantQualifier];
-[AVAssetVariantQualifier _variant];
-[AVAssetVariantQualifier environmentalConditions];
-[AVAssetVariantQualifier setEnvironmentalConditions:];
```
