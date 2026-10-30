# `QSSStreamingTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StreamingTranslationRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) task;
@property (T@"NSString",R,N) source_language;
@property (T@"NSString",R,N) target_language;
@property (T@"NSString",R,N) translation_text;
@property (T@"NSString",R,N) sequence_id;
@property (TB,R,N) disable_log;
@property (Tq,R,N) opt_in_status;
@property (T@"NSString",R,N) app_id;
@property (TB,R,N) final_message;
```

## Instance methods

```
-[QSSStreamingTranslationRequest task];
-[QSSStreamingTranslationRequest copyWithZone:];
-[QSSStreamingTranslationRequest addObjectToBuffer:];
-[QSSStreamingTranslationRequest app_id];
-[QSSStreamingTranslationRequest flatbuffData];
-[QSSStreamingTranslationRequest initAndVerifyWithFlatbuffData:];
-[QSSStreamingTranslationRequest initWithFlatbuffData:];
-[QSSStreamingTranslationRequest initWithFlatbuffData:root:];
-[QSSStreamingTranslationRequest initWithFlatbuffData:root:verify:];
-[QSSStreamingTranslationRequest speech_id];
-[QSSStreamingTranslationRequest source_language];
-[QSSStreamingTranslationRequest target_language];
-[QSSStreamingTranslationRequest disable_log];
-[QSSStreamingTranslationRequest final_message];
-[QSSStreamingTranslationRequest opt_in_status];
-[QSSStreamingTranslationRequest request_id];
-[QSSStreamingTranslationRequest sequence_id];
-[QSSStreamingTranslationRequest translation_text];
```
