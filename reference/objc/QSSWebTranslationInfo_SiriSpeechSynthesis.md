# `QSSWebTranslationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{WebTranslationInfo=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) text;
@property (T@"NSArray",R,N) spans;
```

## Instance methods

```
-[QSSWebTranslationInfo text];
-[QSSWebTranslationInfo copyWithZone:];
-[QSSWebTranslationInfo spans];
-[QSSWebTranslationInfo addObjectToBuffer:];
-[QSSWebTranslationInfo flatbuffData];
-[QSSWebTranslationInfo initAndVerifyWithFlatbuffData:];
-[QSSWebTranslationInfo initWithFlatbuffData:];
-[QSSWebTranslationInfo initWithFlatbuffData:root:];
-[QSSWebTranslationInfo initWithFlatbuffData:root:verify:];
```
