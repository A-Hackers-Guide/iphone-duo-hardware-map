# `UITextReplacementGeneratorForCorrections`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextReplacementGenerator`
- 9 instance variables, 8 properties, 24 instance methods, 2 class methods

## Instance variables

```
B _showRevertingAutocorrectionInPredictionView;
B _forceHistoryReplacement;
B _forceAutocorrectionGuesses;
B _forceSpellingGuesses;
@"UITextChecker" _textChecker;
@"TIKeyboardCandidate" _autocorrectionRecord;
Q _maxEditDistance;
Q _maxCountAfterAutocorrectionGuesses;
Q _maxCountAfterSpellingGuesses;
```

## Properties

```
@property (T@"UITextChecker",&,N,V_textChecker) textChecker;
@property (T@"TIKeyboardCandidate",&,N,V_autocorrectionRecord) autocorrectionRecord;
@property (TB,N,V_forceHistoryReplacement) forceHistoryReplacement;
@property (TQ,N,V_maxEditDistance) maxEditDistance;
@property (TQ,N,V_maxCountAfterAutocorrectionGuesses) maxCountAfterAutocorrectionGuesses;
@property (TB,N,V_forceAutocorrectionGuesses) forceAutocorrectionGuesses;
@property (TQ,N,V_maxCountAfterSpellingGuesses) maxCountAfterSpellingGuesses;
@property (TB,N,V_forceSpellingGuesses) forceSpellingGuesses;
```

## Class methods

```
+[UITextReplacementGeneratorForCorrections generatorForTextInput:range:options:];
+[UITextReplacementGeneratorForCorrections rangeForTextReplacement:textInput:];
```

## Instance methods

```
-[UITextReplacementGeneratorForCorrections textChecker];
-[UITextReplacementGeneratorForCorrections init];
-[UITextReplacementGeneratorForCorrections replacements];
-[UITextReplacementGeneratorForCorrections maxEditDistance];
-[UITextReplacementGeneratorForCorrections setTextChecker:];
-[UITextReplacementGeneratorForCorrections addAutocorrectionGuessesToReplacements:];
-[UITextReplacementGeneratorForCorrections addPreviouslySuggestedAutocorrectionToReplacements:];
-[UITextReplacementGeneratorForCorrections addReplacementRevertingAutocorrectionToReplacements:];
-[UITextReplacementGeneratorForCorrections addSpellingGuessesForString:ToReplacements:];
-[UITextReplacementGeneratorForCorrections autocorrectionRecord];
-[UITextReplacementGeneratorForCorrections forceAutocorrectionGuesses];
-[UITextReplacementGeneratorForCorrections forceHistoryReplacement];
-[UITextReplacementGeneratorForCorrections forceSpellingGuesses];
-[UITextReplacementGeneratorForCorrections isStringMisspelled:];
-[UITextReplacementGeneratorForCorrections isStringToReplaceMisspelled];
-[UITextReplacementGeneratorForCorrections maxCountAfterAutocorrectionGuesses];
-[UITextReplacementGeneratorForCorrections maxCountAfterSpellingGuesses];
-[UITextReplacementGeneratorForCorrections setAutocorrectionRecord:];
-[UITextReplacementGeneratorForCorrections setForceAutocorrectionGuesses:];
-[UITextReplacementGeneratorForCorrections setForceHistoryReplacement:];
-[UITextReplacementGeneratorForCorrections setForceSpellingGuesses:];
-[UITextReplacementGeneratorForCorrections setMaxCountAfterAutocorrectionGuesses:];
-[UITextReplacementGeneratorForCorrections setMaxCountAfterSpellingGuesses:];
-[UITextReplacementGeneratorForCorrections setMaxEditDistance:];
```
