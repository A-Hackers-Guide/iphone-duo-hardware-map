# `AVAudioFormat`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 10 properties, 26 instance methods, 3 class methods

## Instance variables

```
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
@"AVAudioChannelLayout" _layout;
Q _commonFormat;
^v _reserved;
{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} _magicCookieMutex;
```

## Properties

```
@property (TB,R,N,GisStandard) standard;
@property (TQ,R,N) commonFormat;
@property (TI,R,N) channelCount;
@property (Td,R,N) sampleRate;
@property (TB,R,N,GisInterleaved) interleaved;
@property (Tr^{AudioStreamBasicDescription=dIIIIIIII},R,N) streamDescription;
@property (T@"AVAudioChannelLayout",R,N) channelLayout;
@property (T@"NSData",&,N) magicCookie;
@property (T@"NSDictionary",R,N) settings;
@property (T^{opaqueCMFormatDescription=},R,N) formatDescription;
```

## Class methods

```
+[AVAudioFormat supportsSecureCoding];
+[AVAudioFormat formatWithInvalidSampleRateAndChannelCount];
+[AVAudioFormat settingsFromASBD:channelLayout:];
```

## Instance methods

```
-[AVAudioFormat formatDescription];
-[AVAudioFormat sampleRate];
-[AVAudioFormat channelCount];
-[AVAudioFormat initWithCommonFormat:sampleRate:channels:interleaved:];
-[AVAudioFormat isInterleaved];
-[AVAudioFormat initWithFormatDescription:];
-[AVAudioFormat isStandard];
-[AVAudioFormat settings];
-[AVAudioFormat commonFormat];
-[AVAudioFormat dealloc];
-[AVAudioFormat initWithStreamDescription:channelLayout:];
-[AVAudioFormat streamDescription];
-[AVAudioFormat initWithCMAudioFormatDescription:];
-[AVAudioFormat initStandardFormatWithSampleRate:channelLayout:];
-[AVAudioFormat initWithCommonFormat:sampleRate:interleaved:channelLayout:];
-[AVAudioFormat magicCookie];
-[AVAudioFormat encodeWithCoder:];
-[AVAudioFormat hash];
-[AVAudioFormat description];
-[AVAudioFormat initWithStreamDescription:];
-[AVAudioFormat initWithCoder:];
-[AVAudioFormat channelLayout];
-[AVAudioFormat setMagicCookie:];
-[AVAudioFormat isEqual:];
-[AVAudioFormat initStandardFormatWithSampleRate:channels:];
-[AVAudioFormat initWithSettings:];
```
