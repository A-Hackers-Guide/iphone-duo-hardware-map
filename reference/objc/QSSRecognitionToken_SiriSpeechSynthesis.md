# `QSSRecognitionToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) token_text;
@property (Ti,R,N) start_milli_seconds;
@property (Ti,R,N) end_milli_seconds;
@property (Ti,R,N) silence_start_milli_seconds;
@property (Ti,R,N) confidence;
@property (TB,R,N) add_space_after;
@property (T@"NSString",R,N) phone_seq;
@property (T@"NSString",R,N) ipa_phone_seq;
```

## Instance methods

```
-[QSSRecognitionToken copyWithZone:];
-[QSSRecognitionToken confidence];
-[QSSRecognitionToken addObjectToBuffer:];
-[QSSRecognitionToken flatbuffData];
-[QSSRecognitionToken initAndVerifyWithFlatbuffData:];
-[QSSRecognitionToken initWithFlatbuffData:];
-[QSSRecognitionToken initWithFlatbuffData:root:];
-[QSSRecognitionToken initWithFlatbuffData:root:verify:];
-[QSSRecognitionToken add_space_after];
-[QSSRecognitionToken end_milli_seconds];
-[QSSRecognitionToken ipa_phone_seq];
-[QSSRecognitionToken phone_seq];
-[QSSRecognitionToken silence_start_milli_seconds];
-[QSSRecognitionToken start_milli_seconds];
-[QSSRecognitionToken token_text];
```
