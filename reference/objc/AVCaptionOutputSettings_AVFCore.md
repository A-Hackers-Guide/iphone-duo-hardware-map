# `AVCaptionOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVOutputSettings`
- 1 instance variables, 2 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _captionSettingsDictionary;
```

## Properties

```
@property (T{?=qiIq},R,N) captionTimeCodeFrameDuration;
@property (TB,R,N) useDropFrameTimeCode;
```

## Class methods

```
+[AVCaptionOutputSettings _outputSettingsWithOutputSettingsDictionary:mediaType:exceptionReason:];
+[AVCaptionOutputSettings eligibleOutputSettingsDictionaryKeys];
+[AVCaptionOutputSettings supportsEmptyOutputSettingsDictionary];
```

## Instance methods

```
-[AVCaptionOutputSettings canFullySpecifyOutputFormatReturningReason:];
-[AVCaptionOutputSettings captionTimeCodeFrameDuration];
-[AVCaptionOutputSettings compatibleMediaTypes];
-[AVCaptionOutputSettings encoderIsAvailableOnCurrentSystemReturningError:];
-[AVCaptionOutputSettings initWithCaptionSettingsDictionary:exceptionReason:];
-[AVCaptionOutputSettings useDropFrameTimeCode];
-[AVCaptionOutputSettings validateUsingOutputSettingsValidator:reason:];
-[AVCaptionOutputSettings willYieldCompressedSamples];
```
