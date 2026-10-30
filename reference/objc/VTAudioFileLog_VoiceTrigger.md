# `VTAudioFileLog`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
^{OpaqueExtAudioFile=} _audioFile;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
@"NSURL" _url;
I _audioLength;
```

## Class methods

```
+[VTAudioFileLog sharedInstance];
```

## Instance methods

```
-[VTAudioFileLog startRecording];
-[VTAudioFileLog stopRecording];
-[VTAudioFileLog init];
-[VTAudioFileLog dealloc];
-[VTAudioFileLog appendAudioData:];
-[VTAudioFileLog _closeAudioFile];
```
