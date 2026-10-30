# `QSSTranslationLocalePair`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationLocalePair=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) source_locale;
@property (T@"NSString",R,N) target_locale;
```

## Instance methods

```
-[QSSTranslationLocalePair copyWithZone:];
-[QSSTranslationLocalePair addObjectToBuffer:];
-[QSSTranslationLocalePair flatbuffData];
-[QSSTranslationLocalePair initAndVerifyWithFlatbuffData:];
-[QSSTranslationLocalePair initWithFlatbuffData:];
-[QSSTranslationLocalePair initWithFlatbuffData:root:];
-[QSSTranslationLocalePair initWithFlatbuffData:root:verify:];
-[QSSTranslationLocalePair source_locale];
-[QSSTranslationLocalePair target_locale];
```
