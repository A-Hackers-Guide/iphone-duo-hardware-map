# `SFSSTTSEngineCallbackResult`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
{vector<unsigned char, std::allocator<unsigned char>>="__begin_"*"__end_"*""{?="__cap_"*}} _pcmDataBuffer;
{vector<TTSSynthesizer::Marker, std::allocator<TTSSynthesizer::Marker>>="__begin_"^{Marker}"__end_"^{Marker}""{?="__cap_"^{Marker}}} _marker;
@"NSError" _error;
@? _beginCallback;
@? _chunkCallback;
@? _endCallback;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@?,C,N,V_beginCallback) beginCallback;
@property (T@?,C,N,V_chunkCallback) chunkCallback;
@property (T@?,C,N,V_endCallback) endCallback;
@property (T{AudioStreamBasicDescription=dIIIIIIII},N,V_asbd) asbd;
@property (T@"NSError",R,N,V_error) error;
```

## Instance methods

```
-[SFSSTTSEngineCallbackResult error];
-[SFSSTTSEngineCallbackResult marker];
-[SFSSTTSEngineCallbackResult asbd];
-[SFSSTTSEngineCallbackResult setAsbd:];
-[SFSSTTSEngineCallbackResult pcmData];
-[SFSSTTSEngineCallbackResult setEndCallback:];
-[SFSSTTSEngineCallbackResult beginCallback];
-[SFSSTTSEngineCallbackResult chunkCallback];
-[SFSSTTSEngineCallbackResult endCallback];
-[SFSSTTSEngineCallbackResult initWithBeginCallback:chunkCallback:endCallback:];
-[SFSSTTSEngineCallbackResult pcmDataBuffer];
-[SFSSTTSEngineCallbackResult setBeginCallback:];
-[SFSSTTSEngineCallbackResult setChunkCallback:];
-[SFSSTTSEngineCallbackResult synthesisCallback:];
```
