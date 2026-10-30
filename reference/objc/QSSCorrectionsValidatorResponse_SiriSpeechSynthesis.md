# `QSSCorrectionsValidatorResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CorrectionsValidatorResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSArray",R,N) corrections;
```

## Instance methods

```
-[QSSCorrectionsValidatorResponse language];
-[QSSCorrectionsValidatorResponse corrections];
-[QSSCorrectionsValidatorResponse copyWithZone:];
-[QSSCorrectionsValidatorResponse addObjectToBuffer:];
-[QSSCorrectionsValidatorResponse flatbuffData];
-[QSSCorrectionsValidatorResponse initAndVerifyWithFlatbuffData:];
-[QSSCorrectionsValidatorResponse initWithFlatbuffData:];
-[QSSCorrectionsValidatorResponse initWithFlatbuffData:root:];
-[QSSCorrectionsValidatorResponse initWithFlatbuffData:root:verify:];
-[QSSCorrectionsValidatorResponse session_id];
-[QSSCorrectionsValidatorResponse speech_id];
-[QSSCorrectionsValidatorResponse return_code];
-[QSSCorrectionsValidatorResponse return_str];
```
