# `_UIFeedbackAudioFilePattern`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFeedback`
- Protocols: `_UIFeedbackFilePlayable_Internal`, `_UIFeedbackCoreHapticsPlayerReuse_Internal`, `_UIFeedbackCoreHapticsCustomAudio_Internal`, `_UIFeedbackDiscretePlayable`
- 4 instance variables, 8 properties, 12 instance methods, 3 class methods

## Instance variables

```
B _highPriority;
B _canReuseCoreHapticsPlayer;
B _disableEventUseVolumeEnvelope;
@"NSURL" _fileURL;
```

## Properties

```
@property (TB,N,V_canReuseCoreHapticsPlayer) canReuseCoreHapticsPlayer;
@property (TB,N,V_disableEventUseVolumeEnvelope) disableEventUseVolumeEnvelope;
@property (T@"NSURL",R,N,V_fileURL) fileURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisHighPriority,V_highPriority) highPriority;
```

## Class methods

```
+[_UIFeedbackAudioFilePattern supportsSecureCoding];
+[_UIFeedbackAudioFilePattern type];
+[_UIFeedbackAudioFilePattern feedbackPatternFromFile:];
```

## Instance methods

```
-[_UIFeedbackAudioFilePattern isHighPriority];
-[_UIFeedbackAudioFilePattern _effectivePlayableFeedbackTypes];
-[_UIFeedbackAudioFilePattern initWithDictionaryRepresentation:];
-[_UIFeedbackAudioFilePattern fileURL];
-[_UIFeedbackAudioFilePattern initWithFileURL:];
-[_UIFeedbackAudioFilePattern disableEventUseVolumeEnvelope];
-[_UIFeedbackAudioFilePattern setCanReuseCoreHapticsPlayer:];
-[_UIFeedbackAudioFilePattern canReuseCoreHapticsPlayer];
-[_UIFeedbackAudioFilePattern copyWithZone:];
-[_UIFeedbackAudioFilePattern isEqual:];
-[_UIFeedbackAudioFilePattern dictionaryRepresentation];
-[_UIFeedbackAudioFilePattern setDisableEventUseVolumeEnvelope:];
```
