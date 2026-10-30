# `AVVideoOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVOutputSettings`
- 0 instance variables, 13 properties, 17 instance methods, 7 class methods

## Properties

```
@property (Ti,R,N) width;
@property (Ti,R,N) height;
@property (T@"NSDictionary",R,N) cleanApertureDictionary;
@property (T@"NSDictionary",R,N) pixelAspectRatioDictionary;
@property (T@"NSDictionary",R,N) pixelTransferProperties;
@property (T@"NSDictionary",R,N) videoScalingProperties;
@property (TB,R,N) dimensionsAreBoundingBox;
@property (T{?=qiIq},R,N) minimumFrameDuration;
@property (T@"NSString",R,N) frameRateConversionAlgorithm;
@property (TB,R,N) allowWideColor;
@property (TB,R,N) isProRes;
@property (TB,R,N) isProRes4KHighFPSSetting;
@property (T@"NSDictionary",R,N) videoSettingsDictionary;
```

## Class methods

```
+[AVVideoOutputSettings registeredOutputSettingsClasses];
+[AVVideoOutputSettings _outputSettingsWithOutputSettingsDictionary:mediaType:exceptionReason:];
+[AVVideoOutputSettings _validValuesForScalingMode];
+[AVVideoOutputSettings _videoOutputSettingsWithVideoSettingsDictionary:exceptionReason:];
+[AVVideoOutputSettings defaultVideoOutputSettings];
+[AVVideoOutputSettings videoOutputSettingsWithTrustedVideoSettingsDictionary:];
+[AVVideoOutputSettings videoOutputSettingsWithVideoSettingsDictionary:];
```

## Instance methods

```
-[AVVideoOutputSettings minimumFrameDuration];
-[AVVideoOutputSettings isProRes];
-[AVVideoOutputSettings width];
-[AVVideoOutputSettings height];
-[AVVideoOutputSettings allowWideColor];
-[AVVideoOutputSettings cleanApertureDictionary];
-[AVVideoOutputSettings colorPropertiesConsideringFormatDescriptions:colorPrimaries:transferFunction:ycbcrMatrix:];
-[AVVideoOutputSettings compatibleMediaTypes];
-[AVVideoOutputSettings dimensionsAreBoundingBox];
-[AVVideoOutputSettings frameRateConversionAlgorithm];
-[AVVideoOutputSettings initWithVideoSettingsDictionary:exceptionReason:];
-[AVVideoOutputSettings isProRes4KHighFPSSetting];
-[AVVideoOutputSettings pixelAspectRatioDictionary];
-[AVVideoOutputSettings pixelTransferProperties];
-[AVVideoOutputSettings validateUsingOutputSettingsValidator:reason:];
-[AVVideoOutputSettings videoScalingProperties];
-[AVVideoOutputSettings videoSettingsDictionary];
```
