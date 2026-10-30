# `AVAVVideoSettingsVideoOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVVideoOutputSettings`
- Protocols: `AVReencodedVideoSettingsForFig`
- 4 instance variables, 4 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _adaptedVideoCompressionProperties;
@"NSDictionary" _VTPixelAspectRatioDictionary;
@"NSDictionary" _VTCleanApertureDictionary;
B _shouldPrepareEncodedSampleBuffersForPaddedWrites;
```

## Properties

```
@property (TI,R,N) videoCodecType;
@property (T@"NSDictionary",R,N) videoEncoderSpecification;
@property (T@"NSDictionary",R,N) videoCompressionProperties;
@property (TB,N) shouldPrepareEncodedSampleBuffersForPaddedWrites;
```

## Class methods

```
+[AVAVVideoSettingsVideoOutputSettings _validateVideoCompressionProperties:againstSupportedPropertyDictionary:forCodecType:exceptionReason:];
+[AVAVVideoSettingsVideoOutputSettings _videoOutputSettingsWithVideoSettingsDictionary:exceptionReason:];
+[AVAVVideoSettingsVideoOutputSettings eligibleOutputSettingsDictionaryKeys];
```

## Instance methods

```
-[AVAVVideoSettingsVideoOutputSettings dealloc];
-[AVAVVideoSettingsVideoOutputSettings width];
-[AVAVVideoSettingsVideoOutputSettings height];
-[AVAVVideoSettingsVideoOutputSettings canFullySpecifyOutputFormatReturningReason:];
-[AVAVVideoSettingsVideoOutputSettings cleanApertureDictionary];
-[AVAVVideoSettingsVideoOutputSettings encoderIsAvailableOnCurrentSystemReturningError:];
-[AVAVVideoSettingsVideoOutputSettings initWithAVVideoSettingsDictionary:exceptionReason:];
-[AVAVVideoSettingsVideoOutputSettings initWithTrustedAVVideoSettingsDictionary:];
-[AVAVVideoSettingsVideoOutputSettings pixelAspectRatioDictionary];
-[AVAVVideoSettingsVideoOutputSettings setShouldPrepareEncodedSampleBuffersForPaddedWrites:];
-[AVAVVideoSettingsVideoOutputSettings shouldPrepareEncodedSampleBuffersForPaddedWrites];
-[AVAVVideoSettingsVideoOutputSettings videoCodecType];
-[AVAVVideoSettingsVideoOutputSettings videoCompressionProperties];
-[AVAVVideoSettingsVideoOutputSettings videoEncoderSpecification];
-[AVAVVideoSettingsVideoOutputSettings willYieldCompressedSamples];
```
