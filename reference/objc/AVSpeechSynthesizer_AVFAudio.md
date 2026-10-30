# `AVSpeechSynthesizer`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 16 instance methods, 3 class methods

## Instance variables

```
B _speaking;
B _paused;
B _usesApplicationAudioSession;
B _mixToTelephonyUplink;
@"<AVSpeechSynthesizerDelegate>" _delegate;
@"NSArray" _outputChannels;
```

## Properties

```
@property (T@"<AVSpeechSynthesizerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisSpeaking,V_speaking) speaking;
@property (TB,R,N,GisPaused,V_paused) paused;
@property (T@"NSArray",&,N,V_outputChannels) outputChannels;
@property (TB,N,V_usesApplicationAudioSession) usesApplicationAudioSession;
@property (TB,N,V_mixToTelephonyUplink) mixToTelephonyUplink;
```

## Class methods

```
+[AVSpeechSynthesizer initialize];
+[AVSpeechSynthesizer personalVoiceAuthorizationStatus];
+[AVSpeechSynthesizer requestPersonalVoiceAuthorizationWithCompletionHandler:];
```

## Instance methods

```
-[AVSpeechSynthesizer isPaused];
-[AVSpeechSynthesizer outputChannels];
-[AVSpeechSynthesizer setDelegate:];
-[AVSpeechSynthesizer delegate];
-[AVSpeechSynthesizer setUsesApplicationAudioSession:];
-[AVSpeechSynthesizer speakUtterance:];
-[AVSpeechSynthesizer continueSpeaking];
-[AVSpeechSynthesizer isSpeaking];
-[AVSpeechSynthesizer pauseSpeakingAtBoundary:];
-[AVSpeechSynthesizer stopSpeakingAtBoundary:];
-[AVSpeechSynthesizer setOutputChannels:];
-[AVSpeechSynthesizer mixToTelephonyUplink];
-[AVSpeechSynthesizer setMixToTelephonyUplink:];
-[AVSpeechSynthesizer usesApplicationAudioSession];
-[AVSpeechSynthesizer writeUtterance:toBufferCallback:];
-[AVSpeechSynthesizer writeUtterance:toBufferCallback:toMarkerCallback:];
```
