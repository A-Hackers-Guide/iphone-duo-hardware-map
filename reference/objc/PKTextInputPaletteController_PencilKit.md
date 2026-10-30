# `PKTextInputPaletteController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKTextInputWindowFirstResponderControllerDelegate`, `PKPaletteControllerDelegate`, `PKPaletteTapToRadarCommandDelegate`, `PKPaletteFloatingKeyboardControllerDelegate`, `UIEditingOverlayInteractionWithView`
- 7 instance variables, 13 properties, 39 instance methods, 0 class methods

## Instance variables

```
B __writingStateActive;
@"PKPaletteFloatingKeyboardController" __floatingKeyboardController;
@"<PKTextInputPaletteControllerDelegate>" _delegate;
@"PKTextInputSettings" __textInputSettings;
@"PKTextInputWindowFirstResponderController" __windowFirstResponderController;
@"PKPaletteController" __paletteController;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _editingOverlayContainerSceneBounds;
```

## Properties

```
@property (T@"PKPaletteFloatingKeyboardController",&,N,V__floatingKeyboardController) _floatingKeyboardController;
@property (T@"PKTextInputSettings",&,N,V__textInputSettings) _textInputSettings;
@property (T@"PKTextInputWindowFirstResponderController",&,N,V__windowFirstResponderController) _windowFirstResponderController;
@property (T@"PKPaletteController",&,N,V__paletteController) _paletteController;
@property (T@"<PKTextInputPaletteControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisPaletteVisible) paletteVisible;
@property (TB,N,G_isWritingStateActive,S_setWritingStateActive:,V__writingStateActive) _writingStateActive;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_editingOverlayContainerSceneBounds) editingOverlayContainerSceneBounds;
@property (T@"UIWindowScene",R,N) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTextInputPaletteController init];
-[PKTextInputPaletteController dealloc];
-[PKTextInputPaletteController editingOverlayContainerDidChangeToSceneBounds:];
-[PKTextInputPaletteController setDelegate:];
-[PKTextInputPaletteController delegate];
-[PKTextInputPaletteController windowScene];
-[PKTextInputPaletteController _paletteControllerContainerView];
-[PKTextInputPaletteController set_floatingKeyboardController:];
-[PKTextInputPaletteController _windowFirstResponderController];
-[PKTextInputPaletteController _canShowPaletteUI];
-[PKTextInputPaletteController _floatingKeyboardController];
-[PKTextInputPaletteController _isFirstResponderEditableTextInputWithPencilTextInputSource];
-[PKTextInputPaletteController _isFirstResponderInputAssistantEnabled];
-[PKTextInputPaletteController _isFirstResponderVisible];
-[PKTextInputPaletteController _isWritingStateActive];
-[PKTextInputPaletteController _paletteController];
-[PKTextInputPaletteController _peformPaletteVisibilityUpdate];
-[PKTextInputPaletteController _recognitionLocaleIdentifierDidChange:];
-[PKTextInputPaletteController _setWritingStateActive:];
-[PKTextInputPaletteController _setupPaletteControllerIfNeededWithView:wantsPaletteVisible:];
-[PKTextInputPaletteController _shouldPaletteBeVisible];
-[PKTextInputPaletteController _textInputSettings];
-[PKTextInputPaletteController _updatePaletteVisibility];
-[PKTextInputPaletteController editingOverlayContainerSceneBounds];
-[PKTextInputPaletteController floatingKeyboardControllerWillHide:];
-[PKTextInputPaletteController floatingKeyboardControllerWillShow:];
-[PKTextInputPaletteController initWithTextInputSettings:];
-[PKTextInputPaletteController isPaletteVisible];
-[PKTextInputPaletteController paletteController:shouldOverridePaletteViewTraitCollectionTo:];
-[PKTextInputPaletteController paletteControllerFloatingKeyboardWillHide:];
-[PKTextInputPaletteController paletteControllerFloatingKeyboardWillShow:];
-[PKTextInputPaletteController paletteTapToRadarCommandConfiguration:];
-[PKTextInputPaletteController responderForFloatingKeyboardController:];
-[PKTextInputPaletteController setEditingOverlayContainerSceneBounds:];
-[PKTextInputPaletteController set_paletteController:];
-[PKTextInputPaletteController set_textInputSettings:];
-[PKTextInputPaletteController set_windowFirstResponderController:];
-[PKTextInputPaletteController updateFirstResponderVisibility];
-[PKTextInputPaletteController windowFirstResponderController:didChangeFirstResponder:];
```
