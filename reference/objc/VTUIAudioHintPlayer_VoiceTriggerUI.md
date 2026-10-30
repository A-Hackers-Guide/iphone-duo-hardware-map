# `VTUIAudioHintPlayer`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _timer;
B _shouldSpeakAudioHint;
B _useCompactHints;
@"NSString" _language;
@"AFVoiceInfo" _outputVoice;
@"NSArray" _trainingPageAudioHintInstructions;
@"NSArray" _trainingPageAudioHintFiles;
@"NSArray" _trainingPageAudioHintPreviews;
@"VTUISpeechSynthesizer" _synth;
@"<VTUIAudioHintPlayerDelegate>" _delegate;
```

## Properties

```
@property (T@"VTUISpeechSynthesizer",&,N,V_synth) synth;
@property (TB,V_useCompactHints) useCompactHints;
@property (T@"<VTUIAudioHintPlayerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_shouldSpeakAudioHint) shouldSpeakAudioHint;
@property (T@"NSArray",&,N,V_trainingPageAudioHintInstructions) trainingPageAudioHintInstructions;
@property (T@"NSArray",&,N,V_trainingPageAudioHintFiles) trainingPageAudioHintFiles;
@property (T@"NSArray",&,N,V_trainingPageAudioHintPreviews) trainingPageAudioHintPreviews;
@property (T@"NSString",&,N,V_language) language;
@property (T@"AFVoiceInfo",&,N,V_outputVoice) outputVoice;
```

## Instance methods

```
-[VTUIAudioHintPlayer language];
-[VTUIAudioHintPlayer cleanup];
-[VTUIAudioHintPlayer _timerFired];
-[VTUIAudioHintPlayer setOutputVoice:];
-[VTUIAudioHintPlayer outputVoice];
-[VTUIAudioHintPlayer delegate];
-[VTUIAudioHintPlayer setLanguage:];
-[VTUIAudioHintPlayer useCompactHints];
-[VTUIAudioHintPlayer setUseCompactHints:];
-[VTUIAudioHintPlayer _audioHintPathForFileName:];
-[VTUIAudioHintPlayer _getTrainingPageAudioHintRequests];
-[VTUIAudioHintPlayer _hasValidHints];
-[VTUIAudioHintPlayer _setupHints];
-[VTUIAudioHintPlayer _systemLanguageMatchesSiriLanguage:siriLanguage:];
-[VTUIAudioHintPlayer _useCompactPhraseForInstruction:];
-[VTUIAudioHintPlayer initWithLanguage:delegate:];
-[VTUIAudioHintPlayer initWithLanguage:isCompact:delegate:];
-[VTUIAudioHintPlayer sendError:toMainForCompletion:];
-[VTUIAudioHintPlayer setShouldSpeakAudioHint:];
-[VTUIAudioHintPlayer setSynth:];
-[VTUIAudioHintPlayer setTrainingPageAudioHintFiles:];
-[VTUIAudioHintPlayer setTrainingPageAudioHintInstructions:];
-[VTUIAudioHintPlayer setTrainingPageAudioHintPreviews:];
-[VTUIAudioHintPlayer shouldSpeakAudioHint];
-[VTUIAudioHintPlayer speakAudioHint:completion:];
-[VTUIAudioHintPlayer speakConfirmationDialog:];
-[VTUIAudioHintPlayer synth];
-[VTUIAudioHintPlayer trainingPageAudioHintFiles];
-[VTUIAudioHintPlayer trainingPageAudioHintInstructions];
-[VTUIAudioHintPlayer trainingPageAudioHintPreviews];
-[VTUIAudioHintPlayer updateIfNeededForUsesMultipleTriggers:];
```
