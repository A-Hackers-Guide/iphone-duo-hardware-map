# `SFSpeechSynthesisTask`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFSpeechSynthesisTaskProtocol`
- 20 instance variables, 24 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _isSpeaking;
B _isFinished;
B _isCancelled;
@"NSError" _error;
@"NSCondition" _synthesisStateCondition;
d _audioPlaybackBufferDuration;
@"SFSpeechSynthesisRequest" _request;
@"SFSSAudioPlaybackService" _playbackService;
@"SFSSVoiceAsset" _voiceAsset;
@"SFSSResourceAsset" _resourceAsset;
@"SFSSInstrumentMetrics" _instrumentMetrics;
@"NSString" _taskIdentifer;
d _bufferedDuration;
@"NSMutableArray" _bufferedAudios;
@"NSMutableArray" _bufferedAudioData;
@"NSMutableArray" _phonemeSequence;
q _speakState;
q _synthesisState;
@"<SFSpeechSynthesisTaskPrivateDelegate>" _delegate;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@"NSCondition",&,N,V_synthesisStateCondition) synthesisStateCondition;
@property (Td,N,V_audioPlaybackBufferDuration) audioPlaybackBufferDuration;
@property (T{AudioStreamBasicDescription=dIIIIIIII},N,V_asbd) asbd;
@property (T@"SFSpeechSynthesisRequest",&,N,V_request) request;
@property (T@"SFSSAudioPlaybackService",&,N,V_playbackService) playbackService;
@property (T@"SFSSVoiceAsset",&,N,V_voiceAsset) voiceAsset;
@property (T@"SFSSResourceAsset",&,N,V_resourceAsset) resourceAsset;
@property (T@"SFSSInstrumentMetrics",&,N,V_instrumentMetrics) instrumentMetrics;
@property (T@"NSString",C,N,V_taskIdentifer) taskIdentifer;
@property (Td,N,V_bufferedDuration) bufferedDuration;
@property (T@"NSMutableArray",&,N,V_bufferedAudios) bufferedAudios;
@property (T@"NSMutableArray",&,N,V_bufferedAudioData) bufferedAudioData;
@property (T@"NSMutableArray",&,N,V_phonemeSequence) phonemeSequence;
@property (Tq,N,V_speakState) speakState;
@property (Tq,N,V_synthesisState) synthesisState;
@property (T@"<SFSpeechSynthesisTaskPrivateDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_isSpeaking) isSpeaking;
@property (TB,N,V_isFinished) isFinished;
@property (TB,N,V_isCancelled) isCancelled;
@property (T@"NSError",C,N,V_error) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SFSpeechSynthesisTask start:];
-[SFSpeechSynthesisTask pause];
-[SFSpeechSynthesisTask setError:];
-[SFSpeechSynthesisTask isFinished];
-[SFSpeechSynthesisTask initWithRequest:];
-[SFSpeechSynthesisTask isCancelled];
-[SFSpeechSynthesisTask error];
-[SFSpeechSynthesisTask request];
-[SFSpeechSynthesisTask setDelegate:];
-[SFSpeechSynthesisTask startTask:];
-[SFSpeechSynthesisTask delegate];
-[SFSpeechSynthesisTask setRequest:];
-[SFSpeechSynthesisTask cancel];
-[SFSpeechSynthesisTask resume];
-[SFSpeechSynthesisTask setIsCancelled:];
-[SFSpeechSynthesisTask setIsFinished:];
-[SFSpeechSynthesisTask isSpeaking];
-[SFSpeechSynthesisTask setIsSpeaking:];
-[SFSpeechSynthesisTask cancelTask];
-[SFSpeechSynthesisTask asbd];
-[SFSpeechSynthesisTask setAsbd:];
-[SFSpeechSynthesisTask initSpeak:asbd:];
-[SFSpeechSynthesisTask phonemeSequence];
-[SFSpeechSynthesisTask playbackService];
-[SFSpeechSynthesisTask setAudioPlaybackBufferDuration:];
-[SFSpeechSynthesisTask audioPlaybackBufferDuration];
-[SFSpeechSynthesisTask bufferedAudioData];
-[SFSpeechSynthesisTask bufferedAudios];
-[SFSpeechSynthesisTask bufferedDuration];
-[SFSpeechSynthesisTask handleSynthesisBegin:asbd:audioPlaybackBufferDuration:voiceAsset:resourceAsset:];
-[SFSpeechSynthesisTask handleSynthesisChunks:];
-[SFSpeechSynthesisTask handleSynthesisEnd:];
-[SFSpeechSynthesisTask handleSynthesisEndCallback];
-[SFSpeechSynthesisTask handleSynthesisFrontendFeaturePhoneme:];
-[SFSpeechSynthesisTask handleSynthesisInit];
-[SFSpeechSynthesisTask instrumentMetrics];
-[SFSpeechSynthesisTask isSpeakRequest];
-[SFSpeechSynthesisTask resourceAsset];
-[SFSpeechSynthesisTask setBufferedAudioData:];
-[SFSpeechSynthesisTask setBufferedAudios:];
-[SFSpeechSynthesisTask setBufferedDuration:];
-[SFSpeechSynthesisTask setErrorIfNotNull:];
-[SFSpeechSynthesisTask setInstrumentMetrics:];
-[SFSpeechSynthesisTask setPhonemeSequence:];
-[SFSpeechSynthesisTask setPlaybackService:];
-[SFSpeechSynthesisTask setResourceAsset:];
-[SFSpeechSynthesisTask setSpeakState:];
-[SFSpeechSynthesisTask setSynthesisState:];
-[SFSpeechSynthesisTask setSynthesisStateCondition:];
-[SFSpeechSynthesisTask setTaskIdentifer:];
-[SFSpeechSynthesisTask setVoiceAsset:];
-[SFSpeechSynthesisTask speakState];
-[SFSpeechSynthesisTask startSpeakIfValid];
-[SFSpeechSynthesisTask synthesisState];
-[SFSpeechSynthesisTask synthesisStateCondition];
-[SFSpeechSynthesisTask taskIdentifer];
-[SFSpeechSynthesisTask voiceAsset];
-[SFSpeechSynthesisTask waitForSpeakFinish];
```
