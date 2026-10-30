# `_UITextInputSessionAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 39 properties, 65 instance methods, 0 class methods

## Instance variables

```
q _source;
q _textInputActionsSource;
q _textInputActionsType;
Q _insertedTextLength;
Q _insertedEmojiCount;
Q _insertedPunctuationCount;
Q _removedTextLength;
Q _removedEmojiCount;
Q _removedPunctuationCount;
q _inputActionCountFromMergedActions;
Q _largestSingleInsertionLength;
Q _largestSingleDeletionLength;
@"NSString" _language;
@"NSString" _region;
@"NSString" _keyboardVariant;
@"NSString" _keyboardLayout;
@"NSString" _keyboardType;
@"NSString" _appBundleId;
q _flagOptions;
{_NSRange="location"Q"length"Q} _relativeRangeBefore;
```

## Properties

```
@property (Tq,N,V_source) source;
@property (T{_NSRange=QQ},N,V_relativeRangeBefore) relativeRangeBefore;
@property (TB,R,N) changedContent;
@property (TB,R,N) isCapableOfTextInsertion;
@property (Tq,N,V_textInputActionsSource) textInputActionsSource;
@property (Tq,N,V_textInputActionsType) textInputActionsType;
@property (Tq,R,N) inputActionCount;
@property (TQ,N,V_insertedTextLength) insertedTextLength;
@property (TQ,N,V_insertedEmojiCount) insertedEmojiCount;
@property (TQ,N,V_insertedPunctuationCount) insertedPunctuationCount;
@property (TQ,N,V_removedTextLength) removedTextLength;
@property (TQ,N,V_removedEmojiCount) removedEmojiCount;
@property (TQ,N,V_removedPunctuationCount) removedPunctuationCount;
@property (Tq,R,N) netCharacterCount;
@property (Tq,N,V_inputActionCountFromMergedActions) inputActionCountFromMergedActions;
@property (TQ,N,V_largestSingleInsertionLength) largestSingleInsertionLength;
@property (TQ,N,V_largestSingleDeletionLength) largestSingleDeletionLength;
@property (T@"NSString",C,N,V_language) language;
@property (T@"NSString",C,N,V_region) region;
@property (T@"NSString",C,N,V_keyboardVariant) keyboardVariant;
@property (T@"NSString",C,N,V_keyboardLayout) keyboardLayout;
@property (T@"NSString",C,N,V_keyboardType) keyboardType;
@property (T@"NSString",C,N,V_appBundleId) appBundleId;
@property (Tq,N,V_flagOptions) flagOptions;
@property (T@"_UITextInputSessionBeganAction",R,N) asBegan;
@property (T@"_UITextInputSessionEndAction",R,N) asEnd;
@property (T@"_UITextInputSessionInsertionAction",R,N) asInsertion;
@property (T@"_UITextInputSessionDeletionAction",R,N) asDeletion;
@property (T@"_UITextInputSessionSelectionAction",R,N) asSelection;
@property (T@"_UITextInputSessionCopyAction",R,N) asCopy;
@property (T@"_UITextInputSessionCutAction",R,N) asCut;
@property (T@"_UITextInputSessionPasteAction",R,N) asPaste;
@property (T@"_UITextInputSessionUndoAction",R,N) asUndo;
@property (T@"_UITextInputSessionRedoAction",R,N) asRedo;
@property (T@"_UITextInputSessionKeyboardDockItemButtonPressAction",R,N) asKeyboardDockItemButtonPress;
@property (T@"_UITextInputSessionDictationBeganAction",R,N) asDictationBegan;
@property (T@"_UITextInputSessionDictationEndedAction",R,N) asDictationEnded;
@property (T@"_UITextInputSessionReplaceTextAction",R,N) asReplaceText;
@property (T@"_UITextInputSessionReplaceWithCandidateAction",R,N) asReplaceWithCandidate;
```

## Instance methods

```
-[_UITextInputSessionAction setRegion:];
-[_UITextInputSessionAction language];
-[_UITextInputSessionAction appBundleId];
-[_UITextInputSessionAction setKeyboardType:];
-[_UITextInputSessionAction region];
-[_UITextInputSessionAction inputActionCount];
-[_UITextInputSessionAction setAppBundleId:];
-[_UITextInputSessionAction inputModeUniqueString];
-[_UITextInputSessionAction keyboardType];
-[_UITextInputSessionAction setSource:];
-[_UITextInputSessionAction setKeyboardLayout:];
-[_UITextInputSessionAction isCapableOfTextInsertion];
-[_UITextInputSessionAction setKeyboardVariant:];
-[_UITextInputSessionAction description];
-[_UITextInputSessionAction mergeActionIfPossible:];
-[_UITextInputSessionAction keyboardVariant];
-[_UITextInputSessionAction changedContent];
-[_UITextInputSessionAction source];
-[_UITextInputSessionAction setLanguage:];
-[_UITextInputSessionAction keyboardLayout];
-[_UITextInputSessionAction asBegan];
-[_UITextInputSessionAction asPaste];
-[_UITextInputSessionAction setFlagOptions:];
-[_UITextInputSessionAction setLargestSingleDeletionLength:];
-[_UITextInputSessionAction asCopy];
-[_UITextInputSessionAction asCut];
-[_UITextInputSessionAction asDeletion];
-[_UITextInputSessionAction asDictationBegan];
-[_UITextInputSessionAction asDictationEnded];
-[_UITextInputSessionAction asEnd];
-[_UITextInputSessionAction asInsertion];
-[_UITextInputSessionAction asKeyboardDockItemButtonPress];
-[_UITextInputSessionAction asRedo];
-[_UITextInputSessionAction asReplaceText];
-[_UITextInputSessionAction asReplaceWithCandidate];
-[_UITextInputSessionAction asSelection];
-[_UITextInputSessionAction asUndo];
-[_UITextInputSessionAction flagOptions];
-[_UITextInputSessionAction inputActionCountFromMergedActions];
-[_UITextInputSessionAction insertedEmojiCount];
-[_UITextInputSessionAction insertedPunctuationCount];
-[_UITextInputSessionAction insertedTextLength];
-[_UITextInputSessionAction isMergeableWith:];
-[_UITextInputSessionAction largestSingleDeletionLength];
-[_UITextInputSessionAction largestSingleInsertionLength];
-[_UITextInputSessionAction netCharacterCount];
-[_UITextInputSessionAction relativeRangeBefore];
-[_UITextInputSessionAction removedEmojiCount];
-[_UITextInputSessionAction removedPunctuationCount];
-[_UITextInputSessionAction removedTextLength];
-[_UITextInputSessionAction setInputActionCountFromMergedActions:];
-[_UITextInputSessionAction setInsertedEmojiCount:];
-[_UITextInputSessionAction setInsertedPunctuationCount:];
-[_UITextInputSessionAction setInsertedTextLength:];
-[_UITextInputSessionAction setInsertedTextLengthWithoutTracking:];
-[_UITextInputSessionAction setLargestSingleInsertionLength:];
-[_UITextInputSessionAction setRelativeRangeBefore:];
-[_UITextInputSessionAction setRemovedEmojiCount:];
-[_UITextInputSessionAction setRemovedPunctuationCount:];
-[_UITextInputSessionAction setRemovedTextLength:];
-[_UITextInputSessionAction setRemovedTextLengthWithoutTracking:];
-[_UITextInputSessionAction setTextInputActionsSource:];
-[_UITextInputSessionAction setTextInputActionsType:];
-[_UITextInputSessionAction textInputActionsSource];
-[_UITextInputSessionAction textInputActionsType];
```
