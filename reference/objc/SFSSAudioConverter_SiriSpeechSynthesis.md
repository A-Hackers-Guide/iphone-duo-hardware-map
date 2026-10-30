# `SFSSAudioConverter`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 2 class methods

## Instance variables

```
^{OpaqueAudioConverter=} _decoder;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _srcAsbd;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _dstAsbd;
```

## Class methods

```
+[SFSSAudioConverter sharedInstance];
+[SFSSAudioConverter isAsbdSameAs:dstAsbd:];
```

## Instance methods

```
-[SFSSAudioConverter dealloc];
-[SFSSAudioConverter reset];
-[SFSSAudioConverter convertChunks:srcAsbd:dstAsbd:outError:];
-[SFSSAudioConverter createAudioConverter:dstAsbd:];
```
