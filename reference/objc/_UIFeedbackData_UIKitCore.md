# `_UIFeedbackData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFeedbackData`
- 16 instance variables, 20 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _isTransientHaptic;
B _canReuseCoreHapticsPlayer;
B _disableEventUseVolumeEnvelope;
I _effectiveSystemSoundID;
f _intensity;
f _sharpness;
Q _effectiveEventType;
d _effectiveDuration;
d _effectiveDelay;
@"_UIFeedbackParameters" _hapticParameters;
@"_UIFeedbackParameters" _audioParameters;
Q _effectiveEnabledFeedbackTypes;
@"NSURL" _fileURL;
Q _fileFeedbackType;
@"CHHapticPattern" _pattern;
@"BKSHIDHapticFeedbackRequest" _hidRequest;
```

## Properties

```
@property (TQ,N,S_setEffectiveEventType:,V_effectiveEventType) effectiveEventType;
@property (Td,N,S_setEffectiveDuration:,V_effectiveDuration) effectiveDuration;
@property (Td,N,S_setEffectiveDelay:,V_effectiveDelay) effectiveDelay;
@property (T@"_UIFeedbackParameters",&,N,S_setHapticParameters:,V_hapticParameters) hapticParameters;
@property (T@"_UIFeedbackParameters",&,N,S_setAudioParameters:,V_audioParameters) audioParameters;
@property (TQ,N,S_setEffectiveEnabledFeedbackTypes:,V_effectiveEnabledFeedbackTypes) effectiveEnabledFeedbackTypes;
@property (TI,N,S_setEffectiveSystemSoundID:,V_effectiveSystemSoundID) effectiveSystemSoundID;
@property (T@"NSURL",&,N,S_setFileURL:,V_fileURL) fileURL;
@property (TQ,N,S_setFileFeedbackType:,V_fileFeedbackType) fileFeedbackType;
@property (T@"CHHapticPattern",&,N,S_setPattern:,V_pattern) pattern;
@property (T@"BKSHIDHapticFeedbackRequest",&,N,S_setHIDRequest:,V_hidRequest) hidRequest;
@property (TB,N,S_setIsTransientHaptic:,V_isTransientHaptic) isTransientHaptic;
@property (Tf,N,S_setIntensity:,V_intensity) intensity;
@property (Tf,N,S_setSharpness:,V_sharpness) sharpness;
@property (TB,N,S_setCanReuseCoreHapticsPlayer:,V_canReuseCoreHapticsPlayer) canReuseCoreHapticsPlayer;
@property (TB,N,S_setDisableEventUseVolumeEnvelope:,V_disableEventUseVolumeEnvelope) disableEventUseVolumeEnvelope;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFeedbackData _setIntensity:];
-[_UIFeedbackData intensity];
-[_UIFeedbackData pattern];
-[_UIFeedbackData hapticParameters];
-[_UIFeedbackData _setIsTransientHaptic:];
-[_UIFeedbackData effectiveSystemSoundID];
-[_UIFeedbackData fileURL];
-[_UIFeedbackData _setAudioParameters:];
-[_UIFeedbackData audioParameters];
-[_UIFeedbackData _setFileFeedbackType:];
-[_UIFeedbackData _setEffectiveDelay:];
-[_UIFeedbackData disableEventUseVolumeEnvelope];
-[_UIFeedbackData effectiveDuration];
-[_UIFeedbackData sharpness];
-[_UIFeedbackData _setPattern:];
-[_UIFeedbackData _setHapticParameters:];
-[_UIFeedbackData _setHIDRequest:];
-[_UIFeedbackData _setEffectiveEnabledFeedbackTypes:];
-[_UIFeedbackData _setSharpness:];
-[_UIFeedbackData effectiveEnabledFeedbackTypes];
-[_UIFeedbackData fileFeedbackType];
-[_UIFeedbackData effectiveEventType];
-[_UIFeedbackData effectiveDelay];
-[_UIFeedbackData isTransientHaptic];
-[_UIFeedbackData _setDisableEventUseVolumeEnvelope:];
-[_UIFeedbackData _setEffectiveEventType:];
-[_UIFeedbackData _setEffectiveDuration:];
-[_UIFeedbackData _setEffectiveSystemSoundID:];
-[_UIFeedbackData canReuseCoreHapticsPlayer];
-[_UIFeedbackData _setFileURL:];
-[_UIFeedbackData hidRequest];
-[_UIFeedbackData _setCanReuseCoreHapticsPlayer:];
```
