# `QSSTextToSpeechCacheMetaInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechCacheMetaInfo=[1C]} _root;
```

## Properties

```
@property (T@"QSSTextToSpeechMeta",R,N) meta_info;
@property (Tq,R,N) audio_type;
@property (TB,R,N) enable_word_timing_info;
@property (T@"QSSAudioDescription",R,N) decoder_description;
@property (T@"QSSAudioDescription",R,N) playback_description;
@property (Ti,R,N) audio_length;
@property (T@"NSString",R,N) text;
@property (T@"NSString",R,N) original_session_id;
```

## Instance methods

```
-[QSSTextToSpeechCacheMetaInfo text];
-[QSSTextToSpeechCacheMetaInfo copyWithZone:];
-[QSSTextToSpeechCacheMetaInfo addObjectToBuffer:];
-[QSSTextToSpeechCacheMetaInfo audio_type];
-[QSSTextToSpeechCacheMetaInfo decoder_description];
-[QSSTextToSpeechCacheMetaInfo enable_word_timing_info];
-[QSSTextToSpeechCacheMetaInfo flatbuffData];
-[QSSTextToSpeechCacheMetaInfo initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechCacheMetaInfo initWithFlatbuffData:];
-[QSSTextToSpeechCacheMetaInfo initWithFlatbuffData:root:];
-[QSSTextToSpeechCacheMetaInfo initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechCacheMetaInfo meta_info];
-[QSSTextToSpeechCacheMetaInfo playback_description];
-[QSSTextToSpeechCacheMetaInfo audio_length];
-[QSSTextToSpeechCacheMetaInfo original_session_id];
```
