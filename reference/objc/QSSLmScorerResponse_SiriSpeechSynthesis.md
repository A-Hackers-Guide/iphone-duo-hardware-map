# `QSSLmScorerResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LmScorerResponse=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSArray",R,N) tokens;
@property (Td,R,N) ppl;
```

## Instance methods

```
-[QSSLmScorerResponse tokens];
-[QSSLmScorerResponse copyWithZone:];
-[QSSLmScorerResponse addObjectToBuffer:];
-[QSSLmScorerResponse flatbuffData];
-[QSSLmScorerResponse initAndVerifyWithFlatbuffData:];
-[QSSLmScorerResponse initWithFlatbuffData:];
-[QSSLmScorerResponse initWithFlatbuffData:root:];
-[QSSLmScorerResponse initWithFlatbuffData:root:verify:];
-[QSSLmScorerResponse ppl];
-[QSSLmScorerResponse return_code];
-[QSSLmScorerResponse return_str];
```
