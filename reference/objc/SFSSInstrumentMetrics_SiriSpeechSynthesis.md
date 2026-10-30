# `SFSSInstrumentMetrics`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _isSpeechRequest;
@"NSString" _text;
@"NSString" _voiceAssetKey;
@"NSString" _resourceAssetKey;
@"NSString" _audioOutputRoute;
@"NSString" _clientBundleIdentifier;
q _requestCreatedTimestamp;
q _synthesisBeginTimestamp;
q _synthesisEndTimestamp;
q _speakBeginTimestamp;
q _speakEndTimestamp;
d _audioDuration;
q _errorCode;
q _sourceOfTTS;
```

## Properties

```
@property (T@"NSString",C,V_text) text;
@property (T@"NSString",C,V_voiceAssetKey) voiceAssetKey;
@property (T@"NSString",C,V_resourceAssetKey) resourceAssetKey;
@property (T@"NSString",C,V_audioOutputRoute) audioOutputRoute;
@property (T@"NSString",C,V_clientBundleIdentifier) clientBundleIdentifier;
@property (Tq,V_requestCreatedTimestamp) requestCreatedTimestamp;
@property (Tq,V_synthesisBeginTimestamp) synthesisBeginTimestamp;
@property (Tq,V_synthesisEndTimestamp) synthesisEndTimestamp;
@property (Tq,V_speakBeginTimestamp) speakBeginTimestamp;
@property (Tq,V_speakEndTimestamp) speakEndTimestamp;
@property (Td,V_audioDuration) audioDuration;
@property (Tq,V_errorCode) errorCode;
@property (Tq,V_sourceOfTTS) sourceOfTTS;
@property (TB,V_isSpeechRequest) isSpeechRequest;
```

## Instance methods

```
-[SFSSInstrumentMetrics setErrorCode:];
-[SFSSInstrumentMetrics errorCode];
-[SFSSInstrumentMetrics text];
-[SFSSInstrumentMetrics setAudioOutputRoute:];
-[SFSSInstrumentMetrics setClientBundleIdentifier:];
-[SFSSInstrumentMetrics clientBundleIdentifier];
-[SFSSInstrumentMetrics description];
-[SFSSInstrumentMetrics audioOutputRoute];
-[SFSSInstrumentMetrics setText:];
-[SFSSInstrumentMetrics playbackDuration];
-[SFSSInstrumentMetrics isSpeechRequest];
-[SFSSInstrumentMetrics setSourceOfTTS:];
-[SFSSInstrumentMetrics audioDuration];
-[SFSSInstrumentMetrics setAudioDuration:];
-[SFSSInstrumentMetrics sourceOfTTS];
-[SFSSInstrumentMetrics voiceAssetKey];
-[SFSSInstrumentMetrics setVoiceAssetKey:];
-[SFSSInstrumentMetrics dictionaryMetrics];
-[SFSSInstrumentMetrics clockFactor];
-[SFSSInstrumentMetrics requestCreatedTimestamp];
-[SFSSInstrumentMetrics resourceAssetKey];
-[SFSSInstrumentMetrics setIsSpeechRequest:];
-[SFSSInstrumentMetrics setRequestCreatedTimestamp:];
-[SFSSInstrumentMetrics setResourceAssetKey:];
-[SFSSInstrumentMetrics setSpeakBeginTimestamp:];
-[SFSSInstrumentMetrics setSpeakEndTimestamp:];
-[SFSSInstrumentMetrics setSynthesisBeginTimestamp:];
-[SFSSInstrumentMetrics setSynthesisEndTimestamp:];
-[SFSSInstrumentMetrics speakBeginTimestamp];
-[SFSSInstrumentMetrics speakEndTimestamp];
-[SFSSInstrumentMetrics speakLatency];
-[SFSSInstrumentMetrics synthesisBeginTimestamp];
-[SFSSInstrumentMetrics synthesisEndTimestamp];
-[SFSSInstrumentMetrics synthesisLatency];
```
