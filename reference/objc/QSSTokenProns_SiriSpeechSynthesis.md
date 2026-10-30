# `QSSTokenProns`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TokenProns=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) orthography;
@property (T@"NSArray",R,N) sanitized_sequences;
@property (T@"NSArray",R,N) prons;
@property (T@"NSArray",R,N) normalized_prons;
```

## Instance methods

```
-[QSSTokenProns copyWithZone:];
-[QSSTokenProns orthography];
-[QSSTokenProns addObjectToBuffer:];
-[QSSTokenProns flatbuffData];
-[QSSTokenProns initAndVerifyWithFlatbuffData:];
-[QSSTokenProns initWithFlatbuffData:];
-[QSSTokenProns initWithFlatbuffData:root:];
-[QSSTokenProns initWithFlatbuffData:root:verify:];
-[QSSTokenProns prons];
-[QSSTokenProns normalized_prons];
-[QSSTokenProns sanitized_sequences];
```
