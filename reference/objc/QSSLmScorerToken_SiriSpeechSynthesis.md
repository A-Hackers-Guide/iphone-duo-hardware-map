# `QSSLmScorerToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LmScorerToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) token_str;
@property (Td,R,N) log10_score;
@property (Ti,R,N) ngram_used;
```

## Instance methods

```
-[QSSLmScorerToken copyWithZone:];
-[QSSLmScorerToken addObjectToBuffer:];
-[QSSLmScorerToken flatbuffData];
-[QSSLmScorerToken initAndVerifyWithFlatbuffData:];
-[QSSLmScorerToken initWithFlatbuffData:];
-[QSSLmScorerToken initWithFlatbuffData:root:];
-[QSSLmScorerToken initWithFlatbuffData:root:verify:];
-[QSSLmScorerToken log10_score];
-[QSSLmScorerToken ngram_used];
-[QSSLmScorerToken token_str];
```
