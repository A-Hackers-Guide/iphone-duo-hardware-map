# `AVPixelBufferAttributesVideoOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVVideoOutputSettings`
- Protocols: `AVDecodedVideoSettingsForFig`
- 2 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _VTPixelAspectRatioDictionary;
@"NSDictionary" _VTCleanApertureDictionary;
```

## Properties

```
@property (T@"NSDictionary",R,N) pixelBufferAttributes;
@property (T@"NSString",R,N) fieldMode;
@property (T@"NSDictionary",R,N) decompressionProperties;
```

## Class methods

```
+[AVPixelBufferAttributesVideoOutputSettings _videoOutputSettingsWithVideoSettingsDictionary:exceptionReason:];
+[AVPixelBufferAttributesVideoOutputSettings eligibleOutputSettingsDictionaryKeys];
```

## Instance methods

```
-[AVPixelBufferAttributesVideoOutputSettings pixelBufferAttributes];
-[AVPixelBufferAttributesVideoOutputSettings dealloc];
-[AVPixelBufferAttributesVideoOutputSettings width];
-[AVPixelBufferAttributesVideoOutputSettings height];
-[AVPixelBufferAttributesVideoOutputSettings canFullySpecifyOutputFormatReturningReason:];
-[AVPixelBufferAttributesVideoOutputSettings cleanApertureDictionary];
-[AVPixelBufferAttributesVideoOutputSettings decompressionProperties];
-[AVPixelBufferAttributesVideoOutputSettings encoderIsAvailableOnCurrentSystemReturningError:];
-[AVPixelBufferAttributesVideoOutputSettings fieldMode];
-[AVPixelBufferAttributesVideoOutputSettings initWithPixelBufferAttributes:exceptionReason:];
-[AVPixelBufferAttributesVideoOutputSettings initWithTrustedPixelBufferAttributes:];
-[AVPixelBufferAttributesVideoOutputSettings pixelAspectRatioDictionary];
-[AVPixelBufferAttributesVideoOutputSettings willYieldCompressedSamples];
```
