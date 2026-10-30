# `SFSSAudioPlaybackService`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
d _enqueuedSampleCount;
B _discontinuedDuringPlayback;
I _sessionID;
^{OpaqueAudioQueue=} _audioQueue;
@"NSString" _outputRoute;
@"NSCondition" _audioQueueStateCondition;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@"NSCondition",&,N,V_audioQueueStateCondition) audioQueueStateCondition;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,N,V_asbd) asbd;
@property (T^{OpaqueAudioQueue=},R,N,V_audioQueue) audioQueue;
@property (TI,N,V_sessionID) sessionID;
@property (T@"NSString",R,N,V_outputRoute) outputRoute;
@property (TB,R,N,V_discontinuedDuringPlayback) discontinuedDuringPlayback;
```

## Instance methods

```
-[SFSSAudioPlaybackService pause];
-[SFSSAudioPlaybackService sessionID];
-[SFSSAudioPlaybackService setSessionID:];
-[SFSSAudioPlaybackService stop];
-[SFSSAudioPlaybackService start];
-[SFSSAudioPlaybackService reset];
-[SFSSAudioPlaybackService audioQueue];
-[SFSSAudioPlaybackService asbd];
-[SFSSAudioPlaybackService handleMediaServerReset];
-[SFSSAudioPlaybackService enqueue:packetCount:packetDescriptions:];
-[SFSSAudioPlaybackService flushAndStop];
-[SFSSAudioPlaybackService isAudioQueueRunning];
-[SFSSAudioPlaybackService waitForAudioQueueStop];
-[SFSSAudioPlaybackService audioQueueStateCondition];
-[SFSSAudioPlaybackService discontinuedDuringPlayback];
-[SFSSAudioPlaybackService initWithAudioSessionID:asbd:];
-[SFSSAudioPlaybackService outputRoute];
-[SFSSAudioPlaybackService setAudioQueueStateCondition:];
-[SFSSAudioPlaybackService signalQueueRunningStateChange];
-[SFSSAudioPlaybackService waitForQueueRunningStateChange];
```
