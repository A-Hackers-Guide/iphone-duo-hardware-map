# `UIInlineTextCompletionControllerDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 12 properties, 23 instance methods, 0 class methods

## Properties

```
@property (T@"UIKBInputDelegateManager",R,N) inputDelegateManager;
@property (T@"<UIInlineTextCompletionLearning>",R,N) inlineTextCompletionLearner;
@property (T@"UITextInputTraits",R,N) textInputTraits;
@property (T@"TIDocumentState",R,N) documentState;
@property (T@"TIKeyboardState",R,N) keyboardState;
@property (T@"TIKeyboardInputManagerState",R,N) inputManagerState;
@property (T@"UIKeyboardTaskQueue",R,N) taskQueue;
@property (T@"UIView",R,N) inputOverlayContainer;
@property (TB,R,N) delegateSupportsCorrectionUI;
@property (TB,R,N) inlineTextCompletionAllowedForAutocorrectionType;
@property (TB,R,N) isSelecting;
@property (TB,R,N) showingEmojiSearch;
```

## Instance methods

```
-[UIInlineTextCompletionControllerDelegate taskQueue];
-[UIInlineTextCompletionControllerDelegate generateCandidates];
-[UIInlineTextCompletionControllerDelegate showingEmojiSearch];
-[UIInlineTextCompletionControllerDelegate documentState];
-[UIInlineTextCompletionControllerDelegate inputDelegateManager];
-[UIInlineTextCompletionControllerDelegate rangeForTextCompletionInput:];
-[UIInlineTextCompletionControllerDelegate removeAutocorrectPrompt];
-[UIInlineTextCompletionControllerDelegate isSelecting];
-[UIInlineTextCompletionControllerDelegate updateKeyboardConfigurations];
-[UIInlineTextCompletionControllerDelegate textInputTraits];
-[UIInlineTextCompletionControllerDelegate refreshKeyboardState];
-[UIInlineTextCompletionControllerDelegate inputManagerState];
-[UIInlineTextCompletionControllerDelegate inputOverlayContainer];
-[UIInlineTextCompletionControllerDelegate presentTextCompletionAsMarkedText:];
-[UIInlineTextCompletionControllerDelegate acceptPredictiveInput:appendSeparator:executionContext:];
-[UIInlineTextCompletionControllerDelegate inlineTextCompletionLearner];
-[UIInlineTextCompletionControllerDelegate keyboardState];
-[UIInlineTextCompletionControllerDelegate textCompletionInputRectsFromFirstRect:lastRect:];
-[UIInlineTextCompletionControllerDelegate acceptPredictiveInput:];
-[UIInlineTextCompletionControllerDelegate inlineTextCompletionAllowedForAutocorrectionType];
-[UIInlineTextCompletionControllerDelegate delegateSupportsCorrectionUI];
-[UIInlineTextCompletionControllerDelegate removeTextCompletionFromMarkedText:];
-[UIInlineTextCompletionControllerDelegate autocorrectionController];
```
