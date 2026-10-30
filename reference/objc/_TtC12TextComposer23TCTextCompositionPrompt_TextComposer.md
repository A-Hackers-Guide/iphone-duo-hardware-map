# `_TtC12TextComposer23TCTextCompositionPrompt`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
_$sSSSg systemPrompt;
_$sSSSg _userPayload;
Swift.ArraySlice _$sySSGSg userPayloadArraySlice;
_$sSSSg fullPrompt;
Foundation.Locale ? locale;
TextComposer.TCTextCompositionSanitizationList ? sanitizationList;
TextComposer.TCTextCompositionTestingConfig ? testingConfig;
Swift.Bool needsAdditionalLanguageIdentification;
```

## Properties

```
@property (T@"NSString",N,C) systemPrompt;
@property (T@"NSString",N,C) userPayload;
@property (T@"NSLocale",N,C) locale;
```

## Instance methods

```
-[_TtC12TextComposer23TCTextCompositionPrompt init];
-[_TtC12TextComposer23TCTextCompositionPrompt setLocale:];
-[_TtC12TextComposer23TCTextCompositionPrompt locale];
-[_TtC12TextComposer23TCTextCompositionPrompt setUserPayload:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithFullPrompt:preferredLanguage:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithFullPrompt:preferredLanguage:sanitizationList:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithSystemPrompt:userPayload:preferredLanguage:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithSystemPrompt:userPayload:preferredLanguage:sanitizationList:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithSystemPrompt:userPayload:preferredLanguage:sanitizationList:needsAdditionalLanguageIdentification:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithSystemPrompt:userPayload:preferredLanguage:sanitizationList:needsAdditionalLanguageIdentification:testingConfig:];
-[_TtC12TextComposer23TCTextCompositionPrompt initWithSystemPrompt:userPayloadArray:preferredLanguage:sanitizationList:];
-[_TtC12TextComposer23TCTextCompositionPrompt promptStringAndReturnError:];
-[_TtC12TextComposer23TCTextCompositionPrompt setSystemPrompt:];
-[_TtC12TextComposer23TCTextCompositionPrompt shortenWithDropCount:error:];
-[_TtC12TextComposer23TCTextCompositionPrompt systemPrompt];
-[_TtC12TextComposer23TCTextCompositionPrompt userPayload];
```
