# `QSSMutableStartSpeechTranslationLoggingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSStartSpeechTranslationLoggingRequest`
- 0 instance variables, 8 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) conversation_id;
@property (T@"NSString",C,N) request_id;
@property (T@"QSSTranslationLocalePair",C,N) translation_locale_pair;
@property (T@"QSSLanguageDetected",C,N) detected_locale;
@property (T@"NSString",C,N) user_selected_locale;
@property (T@"NSArray",C,N) senses;
@property (T@"NSString",C,N) user_selected_sense;
@property (T@"NSArray",C,N) user_interacted_senses;
```

## Instance methods

```
-[QSSMutableStartSpeechTranslationLoggingRequest init];
-[QSSMutableStartSpeechTranslationLoggingRequest copyWithZone:];
-[QSSMutableStartSpeechTranslationLoggingRequest conversation_id];
-[QSSMutableStartSpeechTranslationLoggingRequest detected_locale];
-[QSSMutableStartSpeechTranslationLoggingRequest request_id];
-[QSSMutableStartSpeechTranslationLoggingRequest senses];
-[QSSMutableStartSpeechTranslationLoggingRequest setConversation_id:];
-[QSSMutableStartSpeechTranslationLoggingRequest setDetected_locale:];
-[QSSMutableStartSpeechTranslationLoggingRequest setRequest_id:];
-[QSSMutableStartSpeechTranslationLoggingRequest setSenses:];
-[QSSMutableStartSpeechTranslationLoggingRequest setTranslation_locale_pair:];
-[QSSMutableStartSpeechTranslationLoggingRequest setUser_interacted_senses:];
-[QSSMutableStartSpeechTranslationLoggingRequest setUser_selected_locale:];
-[QSSMutableStartSpeechTranslationLoggingRequest setUser_selected_sense:];
-[QSSMutableStartSpeechTranslationLoggingRequest translation_locale_pair];
-[QSSMutableStartSpeechTranslationLoggingRequest user_interacted_senses];
-[QSSMutableStartSpeechTranslationLoggingRequest user_selected_locale];
-[QSSMutableStartSpeechTranslationLoggingRequest user_selected_sense];
```
