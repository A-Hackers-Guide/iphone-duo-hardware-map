# `QSSPartialTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PartialTextToSpeechStreamingResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSString",R,N) stream_id;
@property (Ti,R,N) current_pkt_number;
@property (T@"NSData",R,N) audio;
@property (T@"NSArray",R,N) word_timing_info;
@property (T@"QSSTextToSpeechFeature",R,N) feature;
```

## Instance methods

```
-[QSSPartialTextToSpeechStreamingResponse feature];
-[QSSPartialTextToSpeechStreamingResponse audio];
-[QSSPartialTextToSpeechStreamingResponse copyWithZone:];
-[QSSPartialTextToSpeechStreamingResponse addObjectToBuffer:];
-[QSSPartialTextToSpeechStreamingResponse audio:];
-[QSSPartialTextToSpeechStreamingResponse current_pkt_number];
-[QSSPartialTextToSpeechStreamingResponse error_code];
-[QSSPartialTextToSpeechStreamingResponse error_str];
-[QSSPartialTextToSpeechStreamingResponse flatbuffData];
-[QSSPartialTextToSpeechStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSPartialTextToSpeechStreamingResponse initWithFlatbuffData:];
-[QSSPartialTextToSpeechStreamingResponse initWithFlatbuffData:root:];
-[QSSPartialTextToSpeechStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSPartialTextToSpeechStreamingResponse session_id];
-[QSSPartialTextToSpeechStreamingResponse speech_id];
-[QSSPartialTextToSpeechStreamingResponse stream_id];
-[QSSPartialTextToSpeechStreamingResponse word_timing_info];
```
