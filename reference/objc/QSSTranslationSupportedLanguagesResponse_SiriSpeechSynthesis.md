# `QSSTranslationSupportedLanguagesResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationSupportedLanguagesResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_string;
@property (T@"NSArray",R,N) language_pairs;
```

## Instance methods

```
-[QSSTranslationSupportedLanguagesResponse copyWithZone:];
-[QSSTranslationSupportedLanguagesResponse addObjectToBuffer:];
-[QSSTranslationSupportedLanguagesResponse flatbuffData];
-[QSSTranslationSupportedLanguagesResponse initAndVerifyWithFlatbuffData:];
-[QSSTranslationSupportedLanguagesResponse initWithFlatbuffData:];
-[QSSTranslationSupportedLanguagesResponse initWithFlatbuffData:root:];
-[QSSTranslationSupportedLanguagesResponse initWithFlatbuffData:root:verify:];
-[QSSTranslationSupportedLanguagesResponse language_pairs];
-[QSSTranslationSupportedLanguagesResponse request_id];
-[QSSTranslationSupportedLanguagesResponse return_code];
-[QSSTranslationSupportedLanguagesResponse return_string];
```
