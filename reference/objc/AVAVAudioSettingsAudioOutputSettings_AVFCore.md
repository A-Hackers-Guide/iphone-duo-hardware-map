# `AVAVAudioSettingsAudioOutputSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAudioOutputSettings`
- Protocols: `AVReencodedAudioSettingsForFig`, `AVDecodedAudioSettingsForFig`
- 0 instance variables, 0 properties, 8 instance methods, 2 class methods

## Class methods

```
+[AVAVAudioSettingsAudioOutputSettings _audioOutputSettingsWithAudioSettingsDictionary:exceptionReason:];
+[AVAVAudioSettingsAudioOutputSettings eligibleOutputSettingsDictionaryKeys];
```

## Instance methods

```
-[AVAVAudioSettingsAudioOutputSettings audioOptions];
-[AVAVAudioSettingsAudioOutputSettings canFullySpecifyOutputFormatReturningReason:];
-[AVAVAudioSettingsAudioOutputSettings copyAudioChannelLayoutForSourceFormatDescription:audioChannelLayoutSize:];
-[AVAVAudioSettingsAudioOutputSettings encoderIsAvailableOnCurrentSystemReturningError:];
-[AVAVAudioSettingsAudioOutputSettings getAudioStreamBasicDescription:forAudioFileTypeID:sourceFormatDescription:];
-[AVAVAudioSettingsAudioOutputSettings initWithAVAudioSettingsDictionary:exceptionReason:];
-[AVAVAudioSettingsAudioOutputSettings initWithTrustedAVAudioSettingsDictionary:];
-[AVAVAudioSettingsAudioOutputSettings willYieldCompressedSamples];
```
