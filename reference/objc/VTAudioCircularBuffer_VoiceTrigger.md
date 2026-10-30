# `VTAudioCircularBuffer`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<voicetrigger::VTAudioCircularBufferImpl<unsigned short>, std::default_delete<voicetrigger::VTAudioCircularBufferImpl<unsigned short>>>=""{?="__ptr_"^v}} _vtAudioCircularBufferImpl;
Q _bufferLength;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (TQ,N,V_bufferLength) bufferLength;
```

## Instance methods

```
-[VTAudioCircularBuffer saveRecordingBufferFrom:to:toURL:];
-[VTAudioCircularBuffer reset];
-[VTAudioCircularBuffer queue];
-[VTAudioCircularBuffer sampleCount];
-[VTAudioCircularBuffer setQueue:];
-[VTAudioCircularBuffer addSamples:numSamples:];
-[VTAudioCircularBuffer bufferLength];
-[VTAudioCircularBuffer copyBufferWithNumSamplesCopiedIn:];
-[VTAudioCircularBuffer initWithNumChannels:recordingDuration:samplingRate:];
-[VTAudioCircularBuffer setBufferLength:];
-[VTAudioCircularBuffer copySamplesFrom:to:withNumSamplesCopiedIn:];
```
