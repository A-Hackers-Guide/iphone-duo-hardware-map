# `UIKeyboardImplStateProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `UITextInputDelegate`
- 0 instance variables, 2 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"TIKeyboardState",R,N) keyboardState;
@property (TB,N) shouldIgnoreTextInputChanges;
```

## Instance methods

```
-[UIKeyboardImplStateProtocol updateTextInputKeyboardSource];
-[UIKeyboardImplStateProtocol setDocumentState:];
-[UIKeyboardImplStateProtocol textSuggestionDidChange:];
-[UIKeyboardImplStateProtocol isMinimized];
-[UIKeyboardImplStateProtocol updateKeyboardStateForDeletion];
-[UIKeyboardImplStateProtocol documentState];
-[UIKeyboardImplStateProtocol shouldIgnoreTextInputChanges];
-[UIKeyboardImplStateProtocol syncDocumentStateToInputDelegate];
-[UIKeyboardImplStateProtocol updateKeyboardStateForInsertion:];
-[UIKeyboardImplStateProtocol keyboardState];
-[UIKeyboardImplStateProtocol didChangeForwardingInputDelegate:];
-[UIKeyboardImplStateProtocol clearInputForMarkedText];
-[UIKeyboardImplStateProtocol subtractKeyboardFrameFromRect:inView:];
-[UIKeyboardImplStateProtocol updateKeyboardStateForReplacingText:withText:];
-[UIKeyboardImplStateProtocol setShouldIgnoreTextInputChanges:];
```
