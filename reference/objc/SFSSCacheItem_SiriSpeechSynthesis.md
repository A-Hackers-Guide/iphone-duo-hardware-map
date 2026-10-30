# `SFSSCacheItem`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _key;
@"NSString" _text;
@"NSString" _voiceKey;
@"NSString" _resourceKey;
@"NSArray" _rawAudio;
{AudioStreamBasicDescription="mSampleRate"d"mFormatID"I"mFormatFlags"I"mBytesPerPacket"I"mFramesPerPacket"I"mBytesPerFrame"I"mChannelsPerFrame"I"mBitsPerChannel"I"mReserved"I} _asbd;
```

## Properties

```
@property (T@"NSString",R,N,V_key) key;
@property (T@"NSString",R,N,V_text) text;
@property (T@"NSString",R,N,V_voiceKey) voiceKey;
@property (T@"NSString",R,N,V_resourceKey) resourceKey;
@property (T{AudioStreamBasicDescription=dIIIIIIII},R,N,V_asbd) asbd;
@property (T@"NSArray",R,N,V_rawAudio) rawAudio;
```

## Class methods

```
+[SFSSCacheItem generateCacheKey:text:];
```

## Instance methods

```
-[SFSSCacheItem text];
-[SFSSCacheItem key];
-[SFSSCacheItem asbd];
-[SFSSCacheItem resourceKey];
-[SFSSCacheItem voiceKey];
-[SFSSCacheItem initWithText:voiceName:voiceKey:resourceKey:asbd:rawAudio:];
-[SFSSCacheItem rawAudio];
```
