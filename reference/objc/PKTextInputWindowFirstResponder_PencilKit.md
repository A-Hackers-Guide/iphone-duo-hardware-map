# `PKTextInputWindowFirstResponder`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _isVisible;
B _editableTextInput;
B _hasScribbleInteraction;
B _disableInputAssistant;
B _notesHandwritingResponder;
q _textInputSource;
@"UITextInputAssistantItem" _inputAssistantItem;
```

## Properties

```
@property (TB,R,N,GisVisible,V_isVisible) isVisible;
@property (TB,R,N,GisPencilTextInputSource) pencilTextInputSource;
@property (Tq,R,N,V_textInputSource) textInputSource;
@property (TB,R,N,GisEditableTextInput,V_editableTextInput) editableTextInput;
@property (TB,R,N,V_hasScribbleInteraction) hasScribbleInteraction;
@property (TB,R,N,GisEditableTextInputWithPencilTextInputSource) editableTextInputWithPencilTextInputSource;
@property (T@"UITextInputAssistantItem",R,N,V_inputAssistantItem) inputAssistantItem;
@property (TB,N,V_disableInputAssistant) disableInputAssistant;
@property (TB,N,GisNotesHandwritingResponder,V_notesHandwritingResponder) notesHandwritingResponder;
```

## Instance methods

```
-[PKTextInputWindowFirstResponder textInputSource];
-[PKTextInputWindowFirstResponder isVisible];
-[PKTextInputWindowFirstResponder inputAssistantItem];
-[PKTextInputWindowFirstResponder disableInputAssistant];
-[PKTextInputWindowFirstResponder hasScribbleInteraction];
-[PKTextInputWindowFirstResponder initWithIsVisible:isEditableTextInput:hasScribbleInteraction:textInputSource:inputAssistantItem:];
-[PKTextInputWindowFirstResponder isEditableTextInput];
-[PKTextInputWindowFirstResponder isEditableTextInputWithPencilTextInputSource];
-[PKTextInputWindowFirstResponder isNotesHandwritingResponder];
-[PKTextInputWindowFirstResponder isPencilTextInputSource];
-[PKTextInputWindowFirstResponder setDisableInputAssistant:];
-[PKTextInputWindowFirstResponder setNotesHandwritingResponder:];
```
