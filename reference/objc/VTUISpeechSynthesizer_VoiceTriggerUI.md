# `VTUISpeechSynthesizer`

- Image: [`/System/Library/PrivateFrameworks/VoiceTriggerUI.framework/VoiceTriggerUI`](../userland/System__Library__PrivateFrameworks__VoiceTriggerUI.framework__VoiceTriggerUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 19 instance methods, 0 class methods

## Instance variables

```
@? _speakAudioHintCompletion;
@? _speakStringCompletion;
@"SiriTTSDaemonSession" _ttsSession;
@"SiriTTSServiceSession" _serviceSession;
@"SiriTTSAudioRequest" _audioRequest;
@"SiriTTSSpeechRequest" _speechRequest;
@"SiriTTSAudioHintRequest" _audioHintRequest;
```

## Properties

```
@property (T@?,C,N,V_speakAudioHintCompletion) speakAudioHintCompletion;
@property (T@?,C,N,V_speakStringCompletion) speakStringCompletion;
@property (T@"SiriTTSDaemonSession",&,N,V_ttsSession) ttsSession;
@property (T@"SiriTTSServiceSession",&,N,V_serviceSession) serviceSession;
@property (T@"SiriTTSAudioRequest",&,N,V_audioRequest) audioRequest;
@property (T@"SiriTTSSpeechRequest",&,N,V_speechRequest) speechRequest;
@property (T@"SiriTTSAudioHintRequest",&,N,V_audioHintRequest) audioHintRequest;
```

## Instance methods

```
-[VTUISpeechSynthesizer init];
-[VTUISpeechSynthesizer serviceSession];
-[VTUISpeechSynthesizer isSpeaking];
-[VTUISpeechSynthesizer setSpeechRequest:];
-[VTUISpeechSynthesizer speechRequest];
-[VTUISpeechSynthesizer stopSpeaking];
-[VTUISpeechSynthesizer setServiceSession:];
-[VTUISpeechSynthesizer setTtsSession:];
-[VTUISpeechSynthesizer ttsSession];
-[VTUISpeechSynthesizer audioHintRequest];
-[VTUISpeechSynthesizer audioRequest];
-[VTUISpeechSynthesizer setAudioHintRequest:];
-[VTUISpeechSynthesizer setAudioRequest:];
-[VTUISpeechSynthesizer setSpeakAudioHintCompletion:];
-[VTUISpeechSynthesizer setSpeakStringCompletion:];
-[VTUISpeechSynthesizer speak:completion:];
-[VTUISpeechSynthesizer speak:language:completion:];
-[VTUISpeechSynthesizer speakAudioHintCompletion];
-[VTUISpeechSynthesizer speakStringCompletion];
```
