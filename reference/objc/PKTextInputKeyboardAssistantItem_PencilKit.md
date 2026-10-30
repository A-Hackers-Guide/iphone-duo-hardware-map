# `PKTextInputKeyboardAssistantItem`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIBarButtonItem`
- Protocols: `PKPaletteFloatingKeyboardControllerDelegate`
- 5 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _floatingKeyboardType;
@"UIImage" _indicatorImage;
@"PKTextInputLanguageSelectionToken" _observerToken;
@"<PKTextInputKeyboardAssistantItemDelegate>" _delegate;
@"PKPaletteFloatingKeyboardController" _floatingKeyboardController;
```

## Properties

```
@property (T@"PKPaletteFloatingKeyboardController",&,N,V_floatingKeyboardController) floatingKeyboardController;
@property (T@"<PKTextInputKeyboardAssistantItemDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputKeyboardAssistantItem init];
-[PKTextInputKeyboardAssistantItem dealloc];
-[PKTextInputKeyboardAssistantItem setDelegate:];
-[PKTextInputKeyboardAssistantItem delegate];
-[PKTextInputKeyboardAssistantItem initWithCoder:];
-[PKTextInputKeyboardAssistantItem didAction:];
-[PKTextInputKeyboardAssistantItem _currentInteraction];
-[PKTextInputKeyboardAssistantItem _updateImageAndNotify];
-[PKTextInputKeyboardAssistantItem didDisplayAssistantItem];
-[PKTextInputKeyboardAssistantItem floatingKeyboardController];
-[PKTextInputKeyboardAssistantItem floatingKeyboardController:didChangeKeyboardType:];
-[PKTextInputKeyboardAssistantItem floatingKeyboardControllerWillHide:];
-[PKTextInputKeyboardAssistantItem floatingKeyboardControllerWillShow:];
-[PKTextInputKeyboardAssistantItem responderForFloatingKeyboardController:];
-[PKTextInputKeyboardAssistantItem setFloatingKeyboardController:];
```
