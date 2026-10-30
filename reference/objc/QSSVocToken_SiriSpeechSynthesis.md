# `QSSVocToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{VocToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) orthography;
@property (T@"NSData",R,N) blob;
```

## Instance methods

```
-[QSSVocToken copyWithZone:];
-[QSSVocToken orthography];
-[QSSVocToken blob];
-[QSSVocToken addObjectToBuffer:];
-[QSSVocToken flatbuffData];
-[QSSVocToken initAndVerifyWithFlatbuffData:];
-[QSSVocToken initWithFlatbuffData:];
-[QSSVocToken initWithFlatbuffData:root:];
-[QSSVocToken initWithFlatbuffData:root:verify:];
-[QSSVocToken blob:];
```
