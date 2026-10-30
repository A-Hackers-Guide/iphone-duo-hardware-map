# `UITextInput` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIKeyInput`
- 0 instance variables, 13 properties, 64 instance methods, 0 class methods

## Properties

```
@property (T@"UITextRange",C) selectedTextRange;
@property (T@"UITextRange",R,N) markedTextRange;
@property (T@"NSDictionary",C,N) markedTextStyle;
@property (T@"UITextPosition",R,N) beginningOfDocument;
@property (T@"UITextPosition",R,N) endOfDocument;
@property (T@"<UITextInputDelegate>",W,N) inputDelegate;
@property (T@"<UITextInputTokenizer>",R,N) tokenizer;
@property (T@"UIView",?,R,N) textInputView;
@property (Tq,?,N) selectionAffinity;
@property (T@,?,R,N) insertDictationResultPlaceholder;
@property (TB,?,N) supportsAdaptiveImageGlyph;
@property (TB,?,R,N,GisEditable) editable;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) unobscuredContentRect;
```

## Instance methods

```
-[UITextInput markedTextStyle];
-[UITextInput firstRectForRange:];
-[UITextInput offsetFromPosition:toPosition:];
-[UITextInput endOfDocument];
-[UITextInput tokenizer];
-[UITextInput textInRange:];
-[UITextInput comparePosition:toPosition:];
-[UITextInput selectionRectsForRange:];
-[UITextInput baseWritingDirectionForPosition:inDirection:];
-[UITextInput textRangeFromPosition:toPosition:];
-[UITextInput caretRectForPosition:];
-[UITextInput positionFromPosition:offset:];
-[UITextInput setBaseWritingDirection:forRange:];
-[UITextInput beginningOfDocument];
-[UITextInput selectedTextRange];
-[UITextInput setSelectedTextRange:];
-[UITextInput replaceRange:withText:];
-[UITextInput markedTextRange];
-[UITextInput setInputDelegate:];
-[UITextInput inputDelegate];
-[UITextInput unmarkText];
-[UITextInput setMarkedTextStyle:];
-[UITextInput closestPositionToPoint:withinRange:];
-[UITextInput characterRangeByExtendingPosition:inDirection:];
-[UITextInput positionFromPosition:inDirection:offset:];
-[UITextInput positionWithinRange:farthestInDirection:];
-[UITextInput closestPositionToPoint:];
-[UITextInput setMarkedText:selectedRange:];
-[UITextInput characterRangeAtPoint:];
-[UITextInput isEditable];
-[UITextInput setAttributedMarkedText:selectedRange:];
-[UITextInput textInputView];
-[UITextInput insertAttributedText:];
-[UITextInput insertDictationResult:];
-[UITextInput setSupportsAdaptiveImageGlyph:];
-[UITextInput insertTextPlaceholderWithSize:];
-[UITextInput frameForDictationResultPlaceholder:];
-[UITextInput supportsAdaptiveImageGlyph];
-[UITextInput selectionAffinity];
-[UITextInput updateFloatingCursorAtPoint:];
-[UITextInput insertAdaptiveImageGlyph:replacementRange:];
-[UITextInput removeDictationResultPlaceholder:willInsertResult:];
-[UITextInput replaceRange:withAttributedText:];
-[UITextInput unobscuredContentRect];
-[UITextInput attributedTextInRange:];
-[UITextInput endFloatingCursor];
-[UITextInput beginFloatingCursorAtPoint:];
-[UITextInput removeTextPlaceholder:];
-[UITextInput insertDictationResultPlaceholder];
-[UITextInput insertText:alternatives:style:];
-[UITextInput textStylingAtPosition:inDirection:];
-[UITextInput caretTransformForPosition:];
-[UITextInput characterOffsetOfPosition:withinRange:];
-[UITextInput dictationRecognitionFailed];
-[UITextInput dictationRecordingDidEnd];
-[UITextInput didDismissWritingTools];
-[UITextInput editMenuForTextRange:suggestedActions:];
-[UITextInput insertInputSuggestion:];
-[UITextInput positionWithinRange:atCharacterOffset:];
-[UITextInput setSelectionAffinity:];
-[UITextInput shouldChangeTextInRange:replacementText:];
-[UITextInput willDismissEditMenuWithAnimator:];
-[UITextInput willPresentEditMenuWithAnimator:];
-[UITextInput willPresentWritingTools];
```
