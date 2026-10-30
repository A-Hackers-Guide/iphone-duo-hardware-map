# `AVOutputSettingsAssistant`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 16 instance methods, 7 class methods

## Instance variables

```
@"AVOutputSettingsAssistantInternal" _internal;
```

## Properties

```
@property (T@"NSDictionary",R,N) audioSettings;
@property (T@"NSDictionary",R,N) videoSettings;
@property (T@"NSString",R,N) outputFileType;
```

## Class methods

```
+[AVOutputSettingsAssistant videoSettingsAdjusterForPreset:];
+[AVOutputSettingsAssistant _allOutputSettingsPresets];
+[AVOutputSettingsAssistant availableOutputSettingsPresets];
+[AVOutputSettingsAssistant baseSettingsProviderForPreset:];
+[AVOutputSettingsAssistant outputSettingsAssistantWithPreset:];
+[AVOutputSettingsAssistant validatesSourceVideoMinFrameDuration];
+[AVOutputSettingsAssistant videoEncoderCapabilities];
```

## Instance methods

```
-[AVOutputSettingsAssistant videoSettings];
-[AVOutputSettingsAssistant init];
-[AVOutputSettingsAssistant initWithPreset:];
-[AVOutputSettingsAssistant dealloc];
-[AVOutputSettingsAssistant outputFileType];
-[AVOutputSettingsAssistant audioSettings];
-[AVOutputSettingsAssistant setSourceVideoMinFrameDuration:];
-[AVOutputSettingsAssistant sourceVideoAverageFrameDuration];
-[AVOutputSettingsAssistant setSourceAudioFormat:];
-[AVOutputSettingsAssistant setSourceVideoAverageFrameDuration:];
-[AVOutputSettingsAssistant setSourceVideoFormat:];
-[AVOutputSettingsAssistant setVideoEncoderSpecification:];
-[AVOutputSettingsAssistant sourceAudioFormat];
-[AVOutputSettingsAssistant sourceVideoFormat];
-[AVOutputSettingsAssistant sourceVideoMinFrameDuration];
-[AVOutputSettingsAssistant videoEncoderSpecification];
```
