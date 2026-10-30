# `QSSRecoverPronsResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecoverPronsResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSArray",R,N) recovery_return_codes;
@property (T@"NSArray",R,N) voc_tokens;
```

## Instance methods

```
-[QSSRecoverPronsResponse copyWithZone:];
-[QSSRecoverPronsResponse addObjectToBuffer:];
-[QSSRecoverPronsResponse error_code];
-[QSSRecoverPronsResponse error_str];
-[QSSRecoverPronsResponse flatbuffData];
-[QSSRecoverPronsResponse initAndVerifyWithFlatbuffData:];
-[QSSRecoverPronsResponse initWithFlatbuffData:];
-[QSSRecoverPronsResponse initWithFlatbuffData:root:];
-[QSSRecoverPronsResponse initWithFlatbuffData:root:verify:];
-[QSSRecoverPronsResponse session_id];
-[QSSRecoverPronsResponse speech_id];
-[QSSRecoverPronsResponse recovery_return_codes];
-[QSSRecoverPronsResponse voc_tokens];
```
