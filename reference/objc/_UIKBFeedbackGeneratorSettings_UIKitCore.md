# `_UIKBFeedbackGeneratorSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 24 instance variables, 24 properties, 49 instance methods, 1 class methods

## Instance variables

```
d _typingFastInterval;
d _typingSlowInterval;
q _predictiveTextMinLength;
q _predictiveTextMaxLength;
@"_UIKBFeedbackGeneratorIntensitySettings" _indivisualKeyAudioVolume;
@"_UIKBFeedbackGeneratorIntensitySettings" _indivisualKeyAudioPitch;
@"_UIKBFeedbackGeneratorIntensitySettings" _indivisualKeyAudioPan;
@"_UIKBFeedbackGeneratorIntensitySettings" _indivisualKeyAudioBrightness;
@"_UIKBFeedbackGeneratorIntensitySettings" _indivisualKeyHaptic;
q _predictiveTextFeedbackOption;
@"_UIKBFeedbackGeneratorIntensitySettings" _predictiveTextAudioVolume;
@"_UIKBFeedbackGeneratorIntensitySettings" _predictiveTextAudioPan;
@"_UIKBFeedbackGeneratorIntensitySettings" _predictiveTextHaptic;
@"_UIKBFeedbackGeneratorIntensitySettings" _predictiveTextAudioPitch;
@"_UIKBFeedbackGeneratorIntensitySettings" _predictiveTextAudioBrightness;
d _predictiveTextEvenAudioPitch;
d _predictiveTextOddAudioPitch;
d _predictiveTextLongAudioBrightness;
d _predictiveTextShortAudioBrightness;
d _autoShutdownTimeout;
d _systemRingerVolumeMin;
d _systemRingerVolumeMax;
d _adjustedRingerVolumeMin;
d _adjustedRingerVolumeMax;
```

## Properties

```
@property (Td,N,V_typingFastInterval) typingFastInterval;
@property (Td,N,V_typingSlowInterval) typingSlowInterval;
@property (Tq,N,V_predictiveTextMinLength) predictiveTextMinLength;
@property (Tq,N,V_predictiveTextMaxLength) predictiveTextMaxLength;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_indivisualKeyAudioVolume) indivisualKeyAudioVolume;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_indivisualKeyAudioPitch) indivisualKeyAudioPitch;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_indivisualKeyAudioPan) indivisualKeyAudioPan;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_indivisualKeyAudioBrightness) indivisualKeyAudioBrightness;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_indivisualKeyHaptic) indivisualKeyHaptic;
@property (Tq,N,V_predictiveTextFeedbackOption) predictiveTextFeedbackOption;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_predictiveTextAudioVolume) predictiveTextAudioVolume;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_predictiveTextAudioPan) predictiveTextAudioPan;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_predictiveTextHaptic) predictiveTextHaptic;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_predictiveTextAudioPitch) predictiveTextAudioPitch;
@property (T@"_UIKBFeedbackGeneratorIntensitySettings",&,N,V_predictiveTextAudioBrightness) predictiveTextAudioBrightness;
@property (Td,N,V_predictiveTextEvenAudioPitch) predictiveTextEvenAudioPitch;
@property (Td,N,V_predictiveTextOddAudioPitch) predictiveTextOddAudioPitch;
@property (Td,N,V_predictiveTextLongAudioBrightness) predictiveTextLongAudioBrightness;
@property (Td,N,V_predictiveTextShortAudioBrightness) predictiveTextShortAudioBrightness;
@property (Td,N,V_autoShutdownTimeout) autoShutdownTimeout;
@property (Td,N,V_systemRingerVolumeMin) systemRingerVolumeMin;
@property (Td,N,V_systemRingerVolumeMax) systemRingerVolumeMax;
@property (Td,N,V_adjustedRingerVolumeMin) adjustedRingerVolumeMin;
@property (Td,N,V_adjustedRingerVolumeMax) adjustedRingerVolumeMax;
```

## Class methods

```
+[_UIKBFeedbackGeneratorSettings settingsControllerModule];
```

## Instance methods

```
-[_UIKBFeedbackGeneratorSettings setSystemRingerVolumeMin:];
-[_UIKBFeedbackGeneratorSettings predictiveTextAudioVolume];
-[_UIKBFeedbackGeneratorSettings indivisualKeyAudioBrightness];
-[_UIKBFeedbackGeneratorSettings setIndivisualKeyHaptic:];
-[_UIKBFeedbackGeneratorSettings setIndivisualKeyAudioVolume:];
-[_UIKBFeedbackGeneratorSettings setAutoShutdownTimeout:];
-[_UIKBFeedbackGeneratorSettings adjustedRingerVolumeMin];
-[_UIKBFeedbackGeneratorSettings setTypingFastInterval:];
-[_UIKBFeedbackGeneratorSettings predictiveTextOddAudioPitch];
-[_UIKBFeedbackGeneratorSettings predictiveTextAudioBrightness];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextMinLength:];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextHaptic:];
-[_UIKBFeedbackGeneratorSettings setAdjustedRingerVolumeMin:];
-[_UIKBFeedbackGeneratorSettings indivisualKeyAudioPan];
-[_UIKBFeedbackGeneratorSettings setTypingSlowInterval:];
-[_UIKBFeedbackGeneratorSettings predictiveTextAudioPitch];
-[_UIKBFeedbackGeneratorSettings setIndivisualKeyAudioPitch:];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextOddAudioPitch:];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextAudioPitch:];
-[_UIKBFeedbackGeneratorSettings setDefaultValues];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextAudioPan:];
-[_UIKBFeedbackGeneratorSettings predictiveTextShortAudioBrightness];
-[_UIKBFeedbackGeneratorSettings setSystemRingerVolumeMax:];
-[_UIKBFeedbackGeneratorSettings systemRingerVolumeMin];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextFeedbackOption:];
-[_UIKBFeedbackGeneratorSettings typingSlowInterval];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextAudioBrightness:];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextLongAudioBrightness:];
-[_UIKBFeedbackGeneratorSettings autoShutdownTimeout];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextMaxLength:];
-[_UIKBFeedbackGeneratorSettings indivisualKeyHaptic];
-[_UIKBFeedbackGeneratorSettings setIndivisualKeyAudioPan:];
-[_UIKBFeedbackGeneratorSettings systemRingerVolumeMax];
-[_UIKBFeedbackGeneratorSettings predictiveTextAudioPan];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextAudioVolume:];
-[_UIKBFeedbackGeneratorSettings predictiveTextFeedbackOption];
-[_UIKBFeedbackGeneratorSettings setAdjustedRingerVolumeMax:];
-[_UIKBFeedbackGeneratorSettings predictiveTextMinLength];
-[_UIKBFeedbackGeneratorSettings predictiveTextHaptic];
-[_UIKBFeedbackGeneratorSettings predictiveTextLongAudioBrightness];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextEvenAudioPitch:];
-[_UIKBFeedbackGeneratorSettings predictiveTextMaxLength];
-[_UIKBFeedbackGeneratorSettings indivisualKeyAudioPitch];
-[_UIKBFeedbackGeneratorSettings setPredictiveTextShortAudioBrightness:];
-[_UIKBFeedbackGeneratorSettings predictiveTextEvenAudioPitch];
-[_UIKBFeedbackGeneratorSettings indivisualKeyAudioVolume];
-[_UIKBFeedbackGeneratorSettings setIndivisualKeyAudioBrightness:];
-[_UIKBFeedbackGeneratorSettings typingFastInterval];
-[_UIKBFeedbackGeneratorSettings adjustedRingerVolumeMax];
```
