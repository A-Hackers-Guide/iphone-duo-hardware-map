# `SFSSTTSEngine`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<TTSSynthesizer, std::default_delete<TTSSynthesizer>>=""{?="__ptr_"^{TTSSynthesizer}}} _synthesizer;
@"NSString" _voicePath;
@"SFSSTTSEngineCallbackResult" _callbackResult;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@"NSString",&,N,V_voicePath) voicePath;
@property (T@"SFSSTTSEngineCallbackResult",&,N,V_callbackResult) callbackResult;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,N,V_asbd) asbd;
```

## Instance methods

```
-[SFSSTTSEngine preheat];
-[SFSSTTSEngine dealloc];
-[SFSSTTSEngine asbd];
-[SFSSTTSEngine stopSynthesis];
-[SFSSTTSEngine voicePath];
-[SFSSTTSEngine setVoicePath:];
-[SFSSTTSEngine constructPcmAsbdWithSampleRate:];
-[SFSSTTSEngine initWithVoicePath:resourcePath:];
-[SFSSTTSEngine callbackResult];
-[SFSSTTSEngine loadResourceAtPath:mimeType:];
-[SFSSTTSEngine setCallbackResult:];
-[SFSSTTSEngine synthesizeText:loggable:synthesisBegin:synthesisChunk:synthesisEnd:];
```
