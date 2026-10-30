# `QSSItnRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ItnRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSArray",R,N) words_list;
```

## Instance methods

```
-[QSSItnRequest language];
-[QSSItnRequest copyWithZone:];
-[QSSItnRequest addObjectToBuffer:];
-[QSSItnRequest flatbuffData];
-[QSSItnRequest initAndVerifyWithFlatbuffData:];
-[QSSItnRequest initWithFlatbuffData:];
-[QSSItnRequest initWithFlatbuffData:root:];
-[QSSItnRequest initWithFlatbuffData:root:verify:];
-[QSSItnRequest session_id];
-[QSSItnRequest speech_id];
-[QSSItnRequest words_list];
```
