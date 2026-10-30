# `QSSKeyword`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{Keyword=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) keyword_orthography;
@property (Td,R,N) posterior;
```

## Instance methods

```
-[QSSKeyword copyWithZone:];
-[QSSKeyword addObjectToBuffer:];
-[QSSKeyword flatbuffData];
-[QSSKeyword initAndVerifyWithFlatbuffData:];
-[QSSKeyword initWithFlatbuffData:];
-[QSSKeyword initWithFlatbuffData:root:];
-[QSSKeyword initWithFlatbuffData:root:verify:];
-[QSSKeyword keyword_orthography];
-[QSSKeyword posterior];
```
