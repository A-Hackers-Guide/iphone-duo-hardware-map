# `AVAudioOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVOutputSettings`
- 0 instance variables, 1 properties, 4 instance methods, 7 class methods

## Properties

```
@property (T@"NSDictionary",R,N) audioSettingsDictionary;
```

## Class methods

```
+[AVAudioOutputSettings registeredOutputSettingsClasses];
+[AVAudioOutputSettings _audioOutputSettingsWithAudioSettingsDictionary:exceptionReason:];
+[AVAudioOutputSettings _outputSettingsWithOutputSettingsDictionary:mediaType:exceptionReason:];
+[AVAudioOutputSettings audioConverterPropertiesForAudioSettingsDictionary:];
+[AVAudioOutputSettings audioOutputSettingsWithAudioSettingsDictionary:];
+[AVAudioOutputSettings audioOutputSettingsWithTrustedAudioSettingsDictionary:];
+[AVAudioOutputSettings defaultAudioOutputSettings];
```

## Instance methods

```
-[AVAudioOutputSettings audioSettingsDictionary];
-[AVAudioOutputSettings compatibleMediaTypes];
-[AVAudioOutputSettings initWithAudioSettingsDictionary:exceptionReason:];
-[AVAudioOutputSettings validateUsingOutputSettingsValidator:reason:];
```
