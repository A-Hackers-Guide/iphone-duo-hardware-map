# `UIAsyncTextInput` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIKeyInput`, `UITextSelectionDirectionNavigation`
- 0 instance variables, 18 properties, 53 instance methods, 0 class methods

## Properties

```
@property (T@"<UIAsyncTextInputDelegate>",?,W,N) asyncSystemInputDelegate;
@property (TB,?,R,N,GisReplaceAllowed) replacedAllowed;
@property (T@"NSString",?,R,N) markedText;
@property (T@"NSAttributedString",?,R,N) attributedMarkedText;
@property (TB,?,R,N) hasMarkedText;
@property (T@"NSString",?,R,N) selectedText;
@property (T@"NSArray",?,R,N) alternativesForSelectedText;
@property (TB,?,R,N) selectionAtDocumentStart;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) textFirstRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) textLastRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) unobscuredContentRect;
@property (T@"UIView",?,R,N) unscaledView;
@property (T@"UIView",?,R,N) textInputView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) selectionClipRect;
@property (T@"UITextRange",?,C) selectedTextRange;
@property (T@"UITextRange",?,R,N) markedTextRange;
@property (T@"<UITextInputTraits>",?,R,N) textInputTraits;
@property (T@"<UIExtendedTextInputTraits>",?,R,N) extendedTraitsDelegate;
```

## Instance methods

```
-[UIAsyncTextInput offsetFromPosition:toPosition:];
-[UIAsyncTextInput textInRange:];
-[UIAsyncTextInput textInputTraits];
-[UIAsyncTextInput selectionRectsForRange:];
-[UIAsyncTextInput insertTextSuggestion:];
-[UIAsyncTextInput caretRectForPosition:];
-[UIAsyncTextInput hasMarkedText];
-[UIAsyncTextInput setAttributedMarkedText:selectedRange:];
-[UIAsyncTextInput textInputView];
-[UIAsyncTextInput setBaseWritingDirection:forRange:];
-[UIAsyncTextInput selectedTextRange];
-[UIAsyncTextInput setSelectedTextRange:];
-[UIAsyncTextInput addTextAlternatives:];
-[UIAsyncTextInput insertDictationResult:];
-[UIAsyncTextInput markedTextRange];
-[UIAsyncTextInput unmarkText];
-[UIAsyncTextInput selectedText];
-[UIAsyncTextInput textFirstRect];
-[UIAsyncTextInput requestTextRectsForString:withCompletionHandler:];
-[UIAsyncTextInput attributedMarkedText];
-[UIAsyncTextInput selectionClipRect];
-[UIAsyncTextInput requestTextContextForAutocorrectionWithCompletionHandler:];
-[UIAsyncTextInput unobscuredContentRect];
-[UIAsyncTextInput markedText];
-[UIAsyncTextInput textLastRect];
-[UIAsyncTextInput transposeCharacters];
-[UIAsyncTextInput requestDocumentContext:completionHandler:];
-[UIAsyncTextInput shiftKeyStateChangedFrom:to:];
-[UIAsyncTextInput setMarkedText:selectedRange:];
-[UIAsyncTextInput canPerformAction:withSender:];
-[UIAsyncTextInput textStylingAtPosition:inDirection:];
-[UIAsyncTextInput alternativesForSelectedText];
-[UIAsyncTextInput asyncSystemInputDelegate];
-[UIAsyncTextInput deleteInDirection:toGranularity:];
-[UIAsyncTextInput didInsertFinalDictationResult];
-[UIAsyncTextInput extendedTraitsDelegate];
-[UIAsyncTextInput handleAsyncKeyEvent:withCompletionHandler:];
-[UIAsyncTextInput hasSelectablePositionAtPoint:];
-[UIAsyncTextInput insertTextPlaceholderWithSize:completionHandler:];
-[UIAsyncTextInput isReplaceAllowed];
-[UIAsyncTextInput pointIsNearMarkedText:];
-[UIAsyncTextInput removeTextPlaceholder:willInsertText:completionHandler:];
-[UIAsyncTextInput replaceDictatedText:withText:];
-[UIAsyncTextInput replaceSelectionOffset:length:withAnnotatedString:relativeReplacementRange:];
-[UIAsyncTextInput replaceText:withText:];
-[UIAsyncTextInput replaceText:withText:options:withCompletionHandler:];
-[UIAsyncTextInput requestDictationContext:];
-[UIAsyncTextInput selectionAtDocumentStart];
-[UIAsyncTextInput setAsyncSystemInputDelegate:];
-[UIAsyncTextInput unscaledView];
-[UIAsyncTextInput willDismissEditMenuWithAnimator:];
-[UIAsyncTextInput willInsertFinalDictationResult];
-[UIAsyncTextInput willPresentEditMenuWithAnimator:];
```
