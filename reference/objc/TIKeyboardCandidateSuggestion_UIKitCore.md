# `TIKeyboardCandidateSuggestion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TIKeyboardCandidate`
- 2 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
Q _customInfoType;
@"UITextSuggestion" _textSuggestion;
```

## Properties

```
@property (T@"UITextSuggestion",R,N,V_textSuggestion) textSuggestion;
```

## Class methods

```
+[TIKeyboardCandidateSuggestion candidateWithSuggestion:];
+[TIKeyboardCandidateSuggestion candidateWithSuggestion:customInfoType:];
```

## Instance methods

```
-[TIKeyboardCandidateSuggestion input];
-[TIKeyboardCandidateSuggestion label];
-[TIKeyboardCandidateSuggestion candidate];
-[TIKeyboardCandidateSuggestion customInfoType];
-[TIKeyboardCandidateSuggestion copyWithZone:];
-[TIKeyboardCandidateSuggestion isEqual:];
-[TIKeyboardCandidateSuggestion initWithSuggestion:customInfoType:];
-[TIKeyboardCandidateSuggestion textSuggestion];
```
