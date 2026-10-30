# `AudioDSPUplinkSpeechMixer`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](../userland/System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `RPBServerListener`, `UplinkSpeechMixer`
- 5 instance variables, 11 properties, 11 instance methods, 0 class methods

## Instance variables

```
{AudioDSPUplinkSpeechMixerSettings="streamDescription"{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I}"maximumFramesPerSlice"I} _settings;
{Reference<CA::DSP::Graph>="mRef"{ReferenceCounted<__CADSPGraph *>="mRef"^{__CADSPGraph}}} _graph;
@"RPBHost" _graphRemoteProcessingBlockHost;
{shared_ptr<caulk::deferred_logger>="__ptr_"^{deferred_logger}"__cntrl_"^{__shared_weak_count}} _graphErrorLogger;
d _graphInputSampleTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,D,N) streamDescription;
@property (TI,R,D,N) maximumFramesPerSlice;
@property (T@?,R,D,N) processBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AudioDSPUplinkSpeechMixer sampleRate];
-[AudioDSPUplinkSpeechMixer dealloc];
-[AudioDSPUplinkSpeechMixer processBlock];
-[AudioDSPUplinkSpeechMixer initWithSettings:];
-[AudioDSPUplinkSpeechMixer maximumFramesPerSlice];
-[AudioDSPUplinkSpeechMixer disconnectRemoteProcessingBlock];
-[AudioDSPUplinkSpeechMixer connectRemoteProcessingBlock];
-[AudioDSPUplinkSpeechMixer connectRemoteProcessingBlockServer:];
-[AudioDSPUplinkSpeechMixer diconnectRemoteProcessingBlockServer:];
-[AudioDSPUplinkSpeechMixer remoteProcessingBlockServerDidStartRunning:];
-[AudioDSPUplinkSpeechMixer remoteProcessingBlockServerDidStopRunning:];
```
