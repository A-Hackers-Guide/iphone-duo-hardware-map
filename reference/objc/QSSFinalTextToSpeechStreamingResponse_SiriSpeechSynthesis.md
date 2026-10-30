# `QSSFinalTextToSpeechStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{FinalTextToSpeechStreamingResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSString",R,N) stream_id;
@property (Ti,R,N) total_pkt_number;
@property (T@"QSSTextToSpeechResponseDevData",R,N) dev_data;
```

## Instance methods

```
-[QSSFinalTextToSpeechStreamingResponse copyWithZone:];
-[QSSFinalTextToSpeechStreamingResponse addObjectToBuffer:];
-[QSSFinalTextToSpeechStreamingResponse error_code];
-[QSSFinalTextToSpeechStreamingResponse error_str];
-[QSSFinalTextToSpeechStreamingResponse flatbuffData];
-[QSSFinalTextToSpeechStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSFinalTextToSpeechStreamingResponse initWithFlatbuffData:];
-[QSSFinalTextToSpeechStreamingResponse initWithFlatbuffData:root:];
-[QSSFinalTextToSpeechStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSFinalTextToSpeechStreamingResponse session_id];
-[QSSFinalTextToSpeechStreamingResponse speech_id];
-[QSSFinalTextToSpeechStreamingResponse stream_id];
-[QSSFinalTextToSpeechStreamingResponse total_pkt_number];
-[QSSFinalTextToSpeechStreamingResponse dev_data];
```
