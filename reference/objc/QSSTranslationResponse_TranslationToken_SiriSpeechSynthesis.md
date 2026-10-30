# `QSSTranslationResponse_TranslationToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationToken=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) token;
@property (Tf,R,N) confidence;
@property (T@"QSSAlignment",R,N) mt_alignment;
@property (TB,R,N) add_space_after;
```

## Instance methods

```
-[QSSTranslationResponse_TranslationToken token];
-[QSSTranslationResponse_TranslationToken copyWithZone:];
-[QSSTranslationResponse_TranslationToken confidence];
-[QSSTranslationResponse_TranslationToken addObjectToBuffer:];
-[QSSTranslationResponse_TranslationToken flatbuffData];
-[QSSTranslationResponse_TranslationToken initAndVerifyWithFlatbuffData:];
-[QSSTranslationResponse_TranslationToken initWithFlatbuffData:];
-[QSSTranslationResponse_TranslationToken initWithFlatbuffData:root:];
-[QSSTranslationResponse_TranslationToken initWithFlatbuffData:root:verify:];
-[QSSTranslationResponse_TranslationToken add_space_after];
-[QSSTranslationResponse_TranslationToken mt_alignment];
```
