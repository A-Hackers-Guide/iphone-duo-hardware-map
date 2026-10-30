# `QSSMultiUserStartSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{MultiUserStartSpeechRequest=[1C]} _root;
```

## Properties

```
@property (T@"QSSStartSpeechRequest",R,N) start_speech_request;
@property (T@"NSArray",R,N) user_parameters;
@property (T@"NSString",R,N) primary_speech_id;
```

## Instance methods

```
-[QSSMultiUserStartSpeechRequest copyWithZone:];
-[QSSMultiUserStartSpeechRequest addObjectToBuffer:];
-[QSSMultiUserStartSpeechRequest flatbuffData];
-[QSSMultiUserStartSpeechRequest initAndVerifyWithFlatbuffData:];
-[QSSMultiUserStartSpeechRequest initWithFlatbuffData:];
-[QSSMultiUserStartSpeechRequest initWithFlatbuffData:root:];
-[QSSMultiUserStartSpeechRequest initWithFlatbuffData:root:verify:];
-[QSSMultiUserStartSpeechRequest user_parameters];
-[QSSMultiUserStartSpeechRequest primary_speech_id];
-[QSSMultiUserStartSpeechRequest start_speech_request];
```
