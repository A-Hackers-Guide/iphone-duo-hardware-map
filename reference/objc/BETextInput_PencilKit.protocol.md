# `BETextInput` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIKeyInput`, `BETextSelectionDirectionNavigation`, `BEResponderEditActions`
- 0 instance variables, 20 properties, 71 instance methods, 0 class methods

## Properties

```
@property (T@"<BETextInputDelegate>",W,N) asyncInputDelegate;
@property (TB,R,N,GisEditable) editable;
@property (TB,R,N) automaticallyPresentEditMenu;
@property (T@"<BEExtendedTextInputTraits>",R,N) extendedTextInputTraits;
@property (TB,R,N,GisReplaceAllowed) replaceAllowed;
@property (T@"UIView",?,R,N) selectionContainerViewBelowText;
@property (T@"UIView",?,R,N) selectionContainerViewAboveText;
@property (T@"NSString",R) selectedText;
@property (T@"UITextRange",C) selectedTextRange;
@property (TB,R,N,GisSelectionAtDocumentStart) selectionAtDocumentStart;
@property (T@"NSString",R,N) markedText;
@property (T@"NSAttributedString",R,N) attributedMarkedText;
@property (T@"UITextRange",R,N) markedTextRange;
@property (TB,R,N) hasMarkedText;
@property (T@"UIView",R,N) textInputView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) textFirstRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) textLastRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) unobscuredContentRect;
@property (T@"UIView",R,N) unscaledView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) selectionClipRect;
```

## Instance methods

```
-[BETextInput offsetFromPosition:toPosition:];
-[BETextInput textInRange:];
-[BETextInput selectionRectsForRange:];
-[BETextInput isEditable];
-[BETextInput asyncInputDelegate];
-[BETextInput insertTextSuggestion:];
-[BETextInput caretRectForPosition:];
-[BETextInput hasMarkedText];
-[BETextInput setAttributedMarkedText:selectedRange:];
-[BETextInput textInputView];
-[BETextInput setBaseWritingDirection:forRange:];
-[BETextInput selectedTextRange];
-[BETextInput setSelectedTextRange:];
-[BETextInput addTextAlternatives:];
-[BETextInput markedTextRange];
-[BETextInput unmarkText];
-[BETextInput setAsyncInputDelegate:];
-[BETextInput selectedText];
-[BETextInput textFirstRect];
-[BETextInput requestTextRectsForString:withCompletionHandler:];
-[BETextInput cancelAutoscroll];
-[BETextInput attributedMarkedText];
-[BETextInput selectionClipRect];
-[BETextInput requestTextContextForAutocorrectionWithCompletionHandler:];
-[BETextInput unobscuredContentRect];
-[BETextInput markedText];
-[BETextInput selectPositionAtPoint:completionHandler:];
-[BETextInput textLastRect];
-[BETextInput requestDocumentContext:completionHandler:];
-[BETextInput setMarkedText:selectedRange:];
-[BETextInput canPerformAction:withSender:];
-[BETextInput textStylingAtPosition:inDirection:];
-[BETextInput requestPreferredArrowDirectionForEditMenuWithCompletionHandler:];
-[BETextInput adjustSelectionBoundaryToPoint:touchPhase:baseIsStart:flags:];
-[BETextInput adjustSelectionByRange:completionHandler:];
-[BETextInput alternativesForSelectedText];
-[BETextInput automaticallyPresentEditMenu];
-[BETextInput autoscrollToPoint:];
-[BETextInput deleteInDirection:toGranularity:];
-[BETextInput didInsertFinalDictationResult];
-[BETextInput extendedTextInputTraits];
-[BETextInput handleKeyEntry:withCompletionHandler:];
-[BETextInput insertTextAlternatives:];
-[BETextInput insertTextPlaceholderWithSize:completionHandler:];
-[BETextInput isPointNearMarkedText:];
-[BETextInput isReplaceAllowed];
-[BETextInput isSelectionAtDocumentStart];
-[BETextInput moveByOffset:];
-[BETextInput moveSelectionAtBoundary:inStorageDirection:completionHandler:];
-[BETextInput removeTextPlaceholder:willInsertText:completionHandler:];
-[BETextInput replaceDictatedText:withText:];
-[BETextInput replaceSelectedText:withText:];
-[BETextInput replaceText:withText:options:completionHandler:];
-[BETextInput selectPositionAtPoint:withContextRequest:completionHandler:];
-[BETextInput selectTextForEditMenuWithLocationInView:completionHandler:];
-[BETextInput selectTextInGranularity:atPoint:completionHandler:];
-[BETextInput selectWordForReplacement];
-[BETextInput setSelectionFromPoint:toPoint:gesture:state:];
-[BETextInput shiftKeyStateChangedFromState:toState:];
-[BETextInput systemWillDismissEditMenuWithAnimator:];
-[BETextInput systemWillPresentEditMenuWithAnimator:];
-[BETextInput textInteractionGesture:shouldBeginAtPoint:];
-[BETextInput transposeCharactersAroundSelection];
-[BETextInput unscaledView];
-[BETextInput updateCurrentSelectionTo:fromGesture:inState:];
-[BETextInput updateSelectionWithExtentPoint:boundary:completionHandler:];
-[BETextInput willInsertFinalDictationResult];
-[BETextInput selectionContainerViewAboveText];
-[BETextInput selectionContainerViewBelowText];
-[BETextInput keyboardWillDismiss];
-[BETextInput removeTextAlternatives];
```
