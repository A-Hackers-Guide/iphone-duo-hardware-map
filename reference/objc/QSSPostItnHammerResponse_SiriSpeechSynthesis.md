# `QSSPostItnHammerResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PostItnHammerResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSArray",R,N) tokens;
```

## Instance methods

```
-[QSSPostItnHammerResponse language];
-[QSSPostItnHammerResponse tokens];
-[QSSPostItnHammerResponse copyWithZone:];
-[QSSPostItnHammerResponse addObjectToBuffer:];
-[QSSPostItnHammerResponse flatbuffData];
-[QSSPostItnHammerResponse initAndVerifyWithFlatbuffData:];
-[QSSPostItnHammerResponse initWithFlatbuffData:];
-[QSSPostItnHammerResponse initWithFlatbuffData:root:];
-[QSSPostItnHammerResponse initWithFlatbuffData:root:verify:];
-[QSSPostItnHammerResponse session_id];
-[QSSPostItnHammerResponse speech_id];
-[QSSPostItnHammerResponse return_code];
-[QSSPostItnHammerResponse return_str];
```
