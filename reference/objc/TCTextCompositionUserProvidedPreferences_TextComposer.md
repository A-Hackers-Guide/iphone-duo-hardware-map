# `TCTextCompositionUserProvidedPreferences`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _preferenceStrings;
@"TCSmartReplyUserQuestionnaire" _multipleChoicePreferences;
@"NSArray" _gradedPreferences;
```

## Properties

```
@property (T@"NSArray",R,C,V_preferenceStrings) preferenceStrings;
@property (T@"TCSmartReplyUserQuestionnaire",R,C,V_multipleChoicePreferences) multipleChoicePreferences;
@property (T@"NSArray",R,C,V_gradedPreferences) gradedPreferences;
```

## Class methods

```
+[TCTextCompositionUserProvidedPreferences supportsSecureCoding];
```

## Instance methods

```
-[TCTextCompositionUserProvidedPreferences encodeWithCoder:];
-[TCTextCompositionUserProvidedPreferences hash];
-[TCTextCompositionUserProvidedPreferences initWithCoder:];
-[TCTextCompositionUserProvidedPreferences copyWithZone:];
-[TCTextCompositionUserProvidedPreferences isEqual:];
-[TCTextCompositionUserProvidedPreferences gradedPreferences];
-[TCTextCompositionUserProvidedPreferences initWithPreferenceStrings:gradedPreferences:multipleChoicePreferences:];
-[TCTextCompositionUserProvidedPreferences multipleChoicePreferences];
-[TCTextCompositionUserProvidedPreferences preferenceStrings];
```
