# `QSSStartSpeechTranslationLoggingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartSpeechTranslationLoggingRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (T@"QSSTranslationLocalePair",R,N) translation_locale_pair;
@property (T@"QSSLanguageDetected",R,N) detected_locale;
@property (T@"NSString",R,N) user_selected_locale;
@property (T@"NSArray",R,N) senses;
@property (T@"NSString",R,N) user_selected_sense;
@property (T@"NSArray",R,N) user_interacted_senses;
```

## Instance methods

```
-[QSSStartSpeechTranslationLoggingRequest copyWithZone:];
-[QSSStartSpeechTranslationLoggingRequest addObjectToBuffer:];
-[QSSStartSpeechTranslationLoggingRequest flatbuffData];
-[QSSStartSpeechTranslationLoggingRequest initAndVerifyWithFlatbuffData:];
-[QSSStartSpeechTranslationLoggingRequest initWithFlatbuffData:];
-[QSSStartSpeechTranslationLoggingRequest initWithFlatbuffData:root:];
-[QSSStartSpeechTranslationLoggingRequest initWithFlatbuffData:root:verify:];
-[QSSStartSpeechTranslationLoggingRequest conversation_id];
-[QSSStartSpeechTranslationLoggingRequest detected_locale];
-[QSSStartSpeechTranslationLoggingRequest request_id];
-[QSSStartSpeechTranslationLoggingRequest senses];
-[QSSStartSpeechTranslationLoggingRequest translation_locale_pair];
-[QSSStartSpeechTranslationLoggingRequest user_interacted_senses];
-[QSSStartSpeechTranslationLoggingRequest user_selected_locale];
-[QSSStartSpeechTranslationLoggingRequest user_selected_sense];
```
