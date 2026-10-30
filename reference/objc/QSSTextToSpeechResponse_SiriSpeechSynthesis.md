# `QSSTextToSpeechResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 13 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (Tq,R,N) audio_type;
@property (Ti,R,N) sample_rate;
@property (T@"NSData",R,N) audio;
@property (T@"QSSAudioDescription",R,N) decoder_description;
@property (T@"QSSAudioDescription",R,N) playback_description;
@property (T@"NSArray",R,N) word_timing_info;
@property (T@"QSSTextToSpeechMeta",R,N) meta_info;
@property (T@"QSSTextToSpeechFeature",R,N) feature;
@property (T@"QSSTextToSpeechResponseDevData",R,N) dev_data;
```

## Instance methods

```
-[QSSTextToSpeechResponse feature];
-[QSSTextToSpeechResponse audio];
-[QSSTextToSpeechResponse copyWithZone:];
-[QSSTextToSpeechResponse addObjectToBuffer:];
-[QSSTextToSpeechResponse audio:];
-[QSSTextToSpeechResponse audio_type];
-[QSSTextToSpeechResponse decoder_description];
-[QSSTextToSpeechResponse error_code];
-[QSSTextToSpeechResponse error_str];
-[QSSTextToSpeechResponse flatbuffData];
-[QSSTextToSpeechResponse initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechResponse initWithFlatbuffData:];
-[QSSTextToSpeechResponse initWithFlatbuffData:root:];
-[QSSTextToSpeechResponse initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechResponse meta_info];
-[QSSTextToSpeechResponse playback_description];
-[QSSTextToSpeechResponse sample_rate];
-[QSSTextToSpeechResponse session_id];
-[QSSTextToSpeechResponse speech_id];
-[QSSTextToSpeechResponse word_timing_info];
-[QSSTextToSpeechResponse dev_data];
```
