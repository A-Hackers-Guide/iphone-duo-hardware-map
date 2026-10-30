# `AVVoiceControllerRecordDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance methods

```
-[AVVoiceControllerRecordDelegate voiceControllerAudioCallback:forStream:buffer:];
-[AVVoiceControllerRecordDelegate voiceControllerBeginRecordInterruption:];
-[AVVoiceControllerRecordDelegate voiceControllerBeginRecordInterruption:withContext:];
-[AVVoiceControllerRecordDelegate voiceControllerDidDetectEndpoint:ofType:];
-[AVVoiceControllerRecordDelegate voiceControllerDidDetectEndpoint:ofType:atTime:];
-[AVVoiceControllerRecordDelegate voiceControllerDidDetectStartpoint:];
-[AVVoiceControllerRecordDelegate voiceControllerDidFinishAlertPlayback:ofType:error:];
-[AVVoiceControllerRecordDelegate voiceControllerDidFinishAlertPlayback:withSettings:error:];
-[AVVoiceControllerRecordDelegate voiceControllerDidSetAudioSessionActive:isActivated:];
-[AVVoiceControllerRecordDelegate voiceControllerDidStartRecording:forStream:successfully:error:];
-[AVVoiceControllerRecordDelegate voiceControllerDidStartRecording:successfully:];
-[AVVoiceControllerRecordDelegate voiceControllerDidStartRecording:successfully:error:];
-[AVVoiceControllerRecordDelegate voiceControllerDidStopRecording:forReason:];
-[AVVoiceControllerRecordDelegate voiceControllerDidStopRecording:forStream:forReason:];
-[AVVoiceControllerRecordDelegate voiceControllerEncoderErrorDidOccur:error:];
-[AVVoiceControllerRecordDelegate voiceControllerEndRecordInterruption:];
-[AVVoiceControllerRecordDelegate voiceControllerEventOccurred:forStream:error:];
-[AVVoiceControllerRecordDelegate voiceControllerLPCMAudioCallback:forStream:buffer:];
-[AVVoiceControllerRecordDelegate voiceControllerLPCMRecordBufferAvailable:buffer:];
-[AVVoiceControllerRecordDelegate voiceControllerMediaServicesWereLost:];
-[AVVoiceControllerRecordDelegate voiceControllerMediaServicesWereReset:];
-[AVVoiceControllerRecordDelegate voiceControllerRecordBufferAvailable:buffer:];
-[AVVoiceControllerRecordDelegate voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:];
-[AVVoiceControllerRecordDelegate voiceControllerStreamInvalidated:forStream:];
-[AVVoiceControllerRecordDelegate voiceControllerWillSetAudioSessionActive:willActivate:];
-[AVVoiceControllerRecordDelegate voiceControllerWirelessSplitterRouteAvailable:devices:];
```
