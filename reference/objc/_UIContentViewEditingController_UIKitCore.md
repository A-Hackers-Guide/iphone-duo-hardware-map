# `_UIContentViewEditingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextFieldDelegate`, `UIGestureRecognizerDelegate`, `_UIPassthroughScrollInteractionDelegate`
- 8 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UILongPressGestureRecognizer" _longPressRecognizer;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
B _hasEdits;
@"UIView" _contentView;
@"UILabel" _editableLabel;
@"UITextField" _textInputView;
@"_UIContentViewEditingConfiguration" _editingConfiguration;
@"<_UIListContentTextPropertiesInternal>" _labelProperties;
```

## Properties

```
@property (T@"UITextField",&,N,V_textInputView) textInputView;
@property (T@"UIView",R,W,N,V_contentView) contentView;
@property (T@"UILabel",R,N,V_editableLabel) editableLabel;
@property (T@"_UIContentViewEditingConfiguration",R,N,V_editingConfiguration) editingConfiguration;
@property (T@"<_UIListContentTextPropertiesInternal>",R,N,V_labelProperties) labelProperties;
@property (TB,R,N,GisDisplayingEditedText) displayingEditedText;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContentViewEditingController textInputView];
-[_UIContentViewEditingController dealloc];
-[_UIContentViewEditingController textFieldShouldEndEditing:];
-[_UIContentViewEditingController textFieldDidBeginEditing:];
-[_UIContentViewEditingController passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIContentViewEditingController textFieldDidEndEditing:];
-[_UIContentViewEditingController textFieldShouldBeginEditing:];
-[_UIContentViewEditingController textFieldShouldReturn:];
-[_UIContentViewEditingController passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIContentViewEditingController textField:shouldChangeCharactersInRange:replacementString:];
-[_UIContentViewEditingController contentView];
-[_UIContentViewEditingController description];
-[_UIContentViewEditingController labelProperties];
-[_UIContentViewEditingController editableLabel];
-[_UIContentViewEditingController editingConfiguration];
-[_UIContentViewEditingController initWithContentView:editableLabel:];
-[_UIContentViewEditingController isDisplayingEditedText];
-[_UIContentViewEditingController longPressRecognizerChanged:];
-[_UIContentViewEditingController makeTextInputFirstResponderWithInitialLayoutBlock:];
-[_UIContentViewEditingController setTextInputView:];
-[_UIContentViewEditingController updateLabelProperties:editingConfiguration:];
```
