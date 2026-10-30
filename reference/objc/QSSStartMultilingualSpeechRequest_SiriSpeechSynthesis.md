# `QSSStartMultilingualSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartMultilingualSpeechRequest=[1C]} _root;
```

## Properties

```
@property (T@"QSSStartSpeechRequest",R,N) start_speech_request;
@property (T@"NSArray",R,N) language_parameters_by_id;
```

## Instance methods

```
-[QSSStartMultilingualSpeechRequest copyWithZone:];
-[QSSStartMultilingualSpeechRequest addObjectToBuffer:];
-[QSSStartMultilingualSpeechRequest flatbuffData];
-[QSSStartMultilingualSpeechRequest initAndVerifyWithFlatbuffData:];
-[QSSStartMultilingualSpeechRequest initWithFlatbuffData:];
-[QSSStartMultilingualSpeechRequest initWithFlatbuffData:root:];
-[QSSStartMultilingualSpeechRequest initWithFlatbuffData:root:verify:];
-[QSSStartMultilingualSpeechRequest language_parameters_by_id];
-[QSSStartMultilingualSpeechRequest start_speech_request];
```
