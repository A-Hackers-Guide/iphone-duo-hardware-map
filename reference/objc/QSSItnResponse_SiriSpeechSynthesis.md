# `QSSItnResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ItnResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSArray",R,N) formatted_words_list;
```

## Instance methods

```
-[QSSItnResponse language];
-[QSSItnResponse copyWithZone:];
-[QSSItnResponse addObjectToBuffer:];
-[QSSItnResponse flatbuffData];
-[QSSItnResponse initAndVerifyWithFlatbuffData:];
-[QSSItnResponse initWithFlatbuffData:];
-[QSSItnResponse initWithFlatbuffData:root:];
-[QSSItnResponse initWithFlatbuffData:root:verify:];
-[QSSItnResponse session_id];
-[QSSItnResponse speech_id];
-[QSSItnResponse formatted_words_list];
-[QSSItnResponse return_code];
-[QSSItnResponse return_str];
```
