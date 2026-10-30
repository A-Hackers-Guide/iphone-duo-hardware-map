# `PKPaletteController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKPaletteHostingWindowScene`, `PKPaletteFloatingKeyboardControllerDelegate`, `UIPopoverPresentationControllerDelegate`, `PKPaletteMoreOptionsViewControllerDelegate`
- 16 instance variables, 23 properties, 69 instance methods, 0 class methods

## Instance variables

```
@"<PKPaletteControllerDelegate>" _delegate;
@"PKTextInputWindowFirstResponder" _firstResponder;
@"PKPaletteTapToRadarCommand" _tapToRadarCommand;
@"PKPaletteHostView" __hostView;
@"PKUCBPaletteView" __paletteView;
@"NSLayoutConstraint" _paletteHostViewWidthConstraint;
@"NSLayoutConstraint" _paletteHostViewHeightConstraint;
@"PKPaletteButton" _undoButton;
@"PKPaletteButton" _redoButton;
@"PKPaletteButton" _returnKeyButton;
@"PKPaletteKeyboardButton" _keyboardButton;
@"NSArray" _trailingButtonsWithReturnKey;
@"NSArray" _trailingButtonsWithoutReturnKey;
@"PKPaletteFloatingKeyboardController" _floatingKeyboardController;
@"PKPaletteInputAssistantButtonProvider" _inputAssistantButtonProvider;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _adjustedWindowSceneBounds;
```

## Properties

```
@property (T@"PKPaletteHostView",&,N,V__hostView) _hostView;
@property (T@"PKUCBPaletteView",&,N,V__paletteView) _paletteView;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewWidthConstraint) paletteHostViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteHostViewHeightConstraint) paletteHostViewHeightConstraint;
@property (T@"PKPaletteButton",&,N,V_undoButton) undoButton;
@property (T@"PKPaletteButton",&,N,V_redoButton) redoButton;
@property (T@"PKPaletteButton",&,N,V_returnKeyButton) returnKeyButton;
@property (T@"PKPaletteKeyboardButton",&,N,V_keyboardButton) keyboardButton;
@property (T@"NSArray",R,C,N,V_trailingButtonsWithReturnKey) trailingButtonsWithReturnKey;
@property (T@"NSArray",R,C,N,V_trailingButtonsWithoutReturnKey) trailingButtonsWithoutReturnKey;
@property (T@"PKPaletteFloatingKeyboardController",&,N,V_floatingKeyboardController) floatingKeyboardController;
@property (T@"PKPaletteInputAssistantButtonProvider",&,N,V_inputAssistantButtonProvider) inputAssistantButtonProvider;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_adjustedWindowSceneBounds) adjustedWindowSceneBounds;
@property (T@"<PKPaletteControllerDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N) palettePosition;
@property (TB,R,N,GisPaletteVisible) paletteVisible;
@property (T@"PKTextInputWindowFirstResponder",&,N,V_firstResponder) firstResponder;
@property (T@"PKPaletteTapToRadarCommand",&,N,V_tapToRadarCommand) tapToRadarCommand;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) paletteHostingWindowSceneBounds;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteController tearDown];
-[PKPaletteController adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPaletteController adaptivePresentationStyleForPresentationController:];
-[PKPaletteController setUndoButton:];
-[PKPaletteController redoButton];
-[PKPaletteController setRedoButton:];
-[PKPaletteController undoButton];
-[PKPaletteController init];
-[PKPaletteController dealloc];
-[PKPaletteController setDelegate:];
-[PKPaletteController delegate];
-[PKPaletteController _hostView];
-[PKPaletteController _handleReturn];
-[PKPaletteController firstResponder];
-[PKPaletteController setFirstResponder:];
-[PKPaletteController keyboardButton];
-[PKPaletteController setKeyboardButton:];
-[PKPaletteController _adjustedUserInterfaceSizeClass];
-[PKPaletteController paletteHostingWindowSceneBounds];
-[PKPaletteController returnKeyButton];
-[PKPaletteController _handleKeyboard];
-[PKPaletteController paletteHostViewHeightConstraint];
-[PKPaletteController palettePosition];
-[PKPaletteController trailingButtonsWithoutReturnKey];
-[PKPaletteController _adjustedHorizontalSizeClassTraitCollection];
-[PKPaletteController _handleMoreButton:];
-[PKPaletteController _handleRedo];
-[PKPaletteController _handleTextInputResponderCapabilitiesChanged:];
-[PKPaletteController _handleTextInputReturnKeyStateChanged:];
-[PKPaletteController _handleUndo];
-[PKPaletteController _openPencilSettings];
-[PKPaletteController _paletteView];
-[PKPaletteController _presentMoreOptionsPopoverFromButton:];
-[PKPaletteController _recognitionLocaleIdentifierDidChange:];
-[PKPaletteController _shouldOverridePaletteViewTraitCollectionTo:];
-[PKPaletteController _shouldPaletteUseCompactHorizontalSizeClass];
-[PKPaletteController _updatePaletteUI];
-[PKPaletteController _updatePaletteViewTraitCollection];
-[PKPaletteController _updatePaletteWithApplicationSpecificItems];
-[PKPaletteController _updatePaletteWithDefaultItems];
-[PKPaletteController _updateReturnKey];
-[PKPaletteController _updateTrailingBarButtons];
-[PKPaletteController _updateUndoRedoEnabledState];
-[PKPaletteController adjustedWindowSceneBounds];
-[PKPaletteController floatingKeyboardController];
-[PKPaletteController floatingKeyboardController:didChangeKeyboardType:];
-[PKPaletteController floatingKeyboardControllerWillHide:];
-[PKPaletteController floatingKeyboardControllerWillShow:];
-[PKPaletteController inputAssistantButtonProvider];
-[PKPaletteController installInView:];
-[PKPaletteController isPaletteVisible];
-[PKPaletteController moreOptionsViewControllerDidSelectOpenPencilSettings:];
-[PKPaletteController moreOptionsViewControllerDidSelectTapToRadar:];
-[PKPaletteController moreOptionsViewControllerDidToggleAutoHide:];
-[PKPaletteController moreOptionsViewControllerDidToggleFingerDraws:];
-[PKPaletteController paletteHostViewWidthConstraint];
-[PKPaletteController responderForFloatingKeyboardController:];
-[PKPaletteController setAdjustedWindowSceneBounds:];
-[PKPaletteController setFloatingKeyboardController:];
-[PKPaletteController setInputAssistantButtonProvider:];
-[PKPaletteController setPaletteHostViewHeightConstraint:];
-[PKPaletteController setPaletteHostViewWidthConstraint:];
-[PKPaletteController setPaletteVisible:animated:completion:];
-[PKPaletteController setReturnKeyButton:];
-[PKPaletteController setTapToRadarCommand:];
-[PKPaletteController set_hostView:];
-[PKPaletteController set_paletteView:];
-[PKPaletteController tapToRadarCommand];
-[PKPaletteController trailingButtonsWithReturnKey];
```
