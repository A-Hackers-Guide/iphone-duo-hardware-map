# `UITextInputAdditions` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 4 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"UITextInteractionAssistant",R,N) interactionAssistant;
@property (TB,R,N,GisEditable) editable;
@property (TB,R,N,GisEditing) editing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,G_caretRect) caretRect;
```

## Instance methods

```
-[UITextInputAdditions isEditable];
-[UITextInputAdditions textInputView];
-[UITextInputAdditions beginSelectionChange];
-[UITextInputAdditions interactionAssistant];
-[UITextInputAdditions endSelectionChange];
-[UITextInputAdditions _caretRect];
-[UITextInputAdditions isEditing];
-[UITextInputAdditions _selectionDisplayInteraction];
-[UITextInputAdditions _setSelectionDisplayInteraction:];
-[UITextInputAdditions selectionInteractionAssistant];
-[UITextInputAdditions _allowAnimatedUpdateSelectionRectViews];
-[UITextInputAdditions _textInputViewForAddingGestureRecognizers];
-[UITextInputAdditions _useGesturesForEditableContent];
```
