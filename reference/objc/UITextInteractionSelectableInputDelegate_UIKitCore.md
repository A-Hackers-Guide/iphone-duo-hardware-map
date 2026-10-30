# `UITextInteractionSelectableInputDelegate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIResponder`
- Protocols: `UITextInput`
- 1 instance variables, 39 properties, 52 instance methods, 1 class methods

## Instance variables

```
@"UIResponder<UITextInput>" _textInput;
```

## Properties

```
@property (T@"UIResponder<UITextInput>",R,N) textInput;
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
@property (TB,R,N) hasText;
@property (Tq,?,N) autocapitalizationType;
@property (Tq,?,N) autocorrectionType;
@property (Tq,?,N) spellCheckingType;
@property (Tq,?,N) smartQuotesType;
@property (Tq,?,N) smartDashesType;
@property (Tq,?,N) smartInsertDeleteType;
@property (Tq,?,N) inlinePredictionType;
@property (Tq,?,N) mathExpressionCompletionType;
@property (Tq,?,N) grammarCheckingType;
@property (Tq,?,N) keyboardType;
@property (Tq,?,N) keyboardAppearance;
@property (Tq,?,N) returnKeyType;
@property (TB,?,N) enablesReturnKeyAutomatically;
@property (TB,?,N,GisSecureTextEntry) secureTextEntry;
@property (T@"NSString",?,C,N) textContentType;
@property (T@"UITextInputPasswordRules",?,C,N) passwordRules;
@property (Tq,?) writingToolsBehavior;
@property (TQ,?) allowedWritingToolsResultOptions;
@property (T@"UIConversationContext",?,&,N) conversationContext;
@property (TB,?,N) allowsNumberPadPopover;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextInteractionSelectableInputDelegate selectableInputDelegateWithTextInput:];
```

## Instance methods

```
-[UITextInteractionSelectableInputDelegate markedTextStyle];
-[UITextInteractionSelectableInputDelegate _moveToEndOfWord:withHistory:];
-[UITextInteractionSelectableInputDelegate firstRectForRange:];
-[UITextInteractionSelectableInputDelegate offsetFromPosition:toPosition:];
-[UITextInteractionSelectableInputDelegate endOfDocument];
-[UITextInteractionSelectableInputDelegate tokenizer];
-[UITextInteractionSelectableInputDelegate _moveUp:withHistory:];
-[UITextInteractionSelectableInputDelegate _moveLeft:withHistory:];
-[UITextInteractionSelectableInputDelegate textInRange:];
-[UITextInteractionSelectableInputDelegate comparePosition:toPosition:];
-[UITextInteractionSelectableInputDelegate selectionRectsForRange:];
-[UITextInteractionSelectableInputDelegate baseWritingDirectionForPosition:inDirection:];
-[UITextInteractionSelectableInputDelegate textRangeFromPosition:toPosition:];
-[UITextInteractionSelectableInputDelegate caretRectForPosition:];
-[UITextInteractionSelectableInputDelegate _moveRight:withHistory:];
-[UITextInteractionSelectableInputDelegate _moveToStartOfWord:withHistory:];
-[UITextInteractionSelectableInputDelegate positionFromPosition:offset:];
-[UITextInteractionSelectableInputDelegate hasText];
-[UITextInteractionSelectableInputDelegate setBaseWritingDirection:forRange:];
-[UITextInteractionSelectableInputDelegate beginningOfDocument];
-[UITextInteractionSelectableInputDelegate selectedTextRange];
-[UITextInteractionSelectableInputDelegate setSelectedTextRange:];
-[UITextInteractionSelectableInputDelegate replaceRange:withText:];
-[UITextInteractionSelectableInputDelegate _moveToEndOfDocument:withHistory:];
-[UITextInteractionSelectableInputDelegate _moveToStartOfParagraph:withHistory:];
-[UITextInteractionSelectableInputDelegate markedTextRange];
-[UITextInteractionSelectableInputDelegate setInputDelegate:];
-[UITextInteractionSelectableInputDelegate inputDelegate];
-[UITextInteractionSelectableInputDelegate insertText:];
-[UITextInteractionSelectableInputDelegate unmarkText];
-[UITextInteractionSelectableInputDelegate _deleteForwardAndNotify:];
-[UITextInteractionSelectableInputDelegate _moveCurrentSelection:];
-[UITextInteractionSelectableInputDelegate _moveDown:withHistory:];
-[UITextInteractionSelectableInputDelegate _moveToEndOfParagraph:withHistory:];
-[UITextInteractionSelectableInputDelegate _moveToStartOfLine:withHistory:];
-[UITextInteractionSelectableInputDelegate _unmarkText];
-[UITextInteractionSelectableInputDelegate _moveToStartOfDocument:withHistory:];
-[UITextInteractionSelectableInputDelegate _deleteBackwardAndNotify:];
-[UITextInteractionSelectableInputDelegate setMarkedTextStyle:];
-[UITextInteractionSelectableInputDelegate updateSelectionRects];
-[UITextInteractionSelectableInputDelegate closestPositionToPoint:withinRange:];
-[UITextInteractionSelectableInputDelegate characterRangeByExtendingPosition:inDirection:];
-[UITextInteractionSelectableInputDelegate positionFromPosition:inDirection:offset:];
-[UITextInteractionSelectableInputDelegate nextResponder];
-[UITextInteractionSelectableInputDelegate positionWithinRange:farthestInDirection:];
-[UITextInteractionSelectableInputDelegate _setMarkedText:selectedRange:];
-[UITextInteractionSelectableInputDelegate _moveToEndOfLine:withHistory:];
-[UITextInteractionSelectableInputDelegate closestPositionToPoint:];
-[UITextInteractionSelectableInputDelegate setMarkedText:selectedRange:];
-[UITextInteractionSelectableInputDelegate characterRangeAtPoint:];
-[UITextInteractionSelectableInputDelegate deleteBackward];
-[UITextInteractionSelectableInputDelegate textInput];
```
