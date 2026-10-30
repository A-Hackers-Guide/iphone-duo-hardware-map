# `QSSWord`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{Word=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) orthography;
@property (T@"NSData",R,N) pronunciations;
@property (Ti,R,N) frequency;
@property (T@"NSString",R,N) tag;
```

## Instance methods

```
-[QSSWord frequency];
-[QSSWord tag];
-[QSSWord copyWithZone:];
-[QSSWord orthography];
-[QSSWord addObjectToBuffer:];
-[QSSWord flatbuffData];
-[QSSWord initAndVerifyWithFlatbuffData:];
-[QSSWord initWithFlatbuffData:];
-[QSSWord initWithFlatbuffData:root:];
-[QSSWord initWithFlatbuffData:root:verify:];
-[QSSWord pronunciations];
-[QSSWord pronunciations:];
```
