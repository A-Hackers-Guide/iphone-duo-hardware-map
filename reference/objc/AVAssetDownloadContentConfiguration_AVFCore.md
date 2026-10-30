# `AVAssetDownloadContentConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _variantQualifiers;
@"NSArray" _mediaSelections;
```

## Properties

```
@property (T@"NSArray",C,N,V_variantQualifiers) variantQualifiers;
@property (T@"NSArray",C,N,V_mediaSelections) mediaSelections;
```

## Class methods

```
+[AVAssetDownloadContentConfiguration supportsSecureCoding];
```

## Instance methods

```
-[AVAssetDownloadContentConfiguration init];
-[AVAssetDownloadContentConfiguration dealloc];
-[AVAssetDownloadContentConfiguration encodeWithCoder:];
-[AVAssetDownloadContentConfiguration initWithCoder:];
-[AVAssetDownloadContentConfiguration copyWithZone:];
-[AVAssetDownloadContentConfiguration mediaSelections];
-[AVAssetDownloadContentConfiguration _createFigContentConfigForEnvironmentalCondition:];
-[AVAssetDownloadContentConfiguration _serializeIntoDownloadConfig:asset:];
-[AVAssetDownloadContentConfiguration _serializeIntoDownloadConfig:environmentalCondition:];
-[AVAssetDownloadContentConfiguration setMediaSelections:];
-[AVAssetDownloadContentConfiguration setVariantQualifiers:];
-[AVAssetDownloadContentConfiguration variantQualifiers];
```
