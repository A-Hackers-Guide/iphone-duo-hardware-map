# `QSSCorrectionsAlignment`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CorrectionsAlignment=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) original_words;
@property (T@"NSString",R,N) corrected_words;
```

## Instance methods

```
-[QSSCorrectionsAlignment copyWithZone:];
-[QSSCorrectionsAlignment addObjectToBuffer:];
-[QSSCorrectionsAlignment flatbuffData];
-[QSSCorrectionsAlignment initAndVerifyWithFlatbuffData:];
-[QSSCorrectionsAlignment initWithFlatbuffData:];
-[QSSCorrectionsAlignment initWithFlatbuffData:root:];
-[QSSCorrectionsAlignment initWithFlatbuffData:root:verify:];
-[QSSCorrectionsAlignment corrected_words];
-[QSSCorrectionsAlignment original_words];
```
