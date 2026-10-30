# `PKPaletteColorPickerContainerView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPopoverPresentationControllerDelegate`, `PKPalettePopoverDismissing`
- 9 instance variables, 13 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _shouldShowInputAssistantView;
@"<PKPaletteColorPickerContainerViewDelegate>" _delegate;
@"<PKDrawingPaletteViewStateSubject>" _paletteViewState;
@"PKPaletteColorPickerView" _colorPickerView;
@"<PKPalettePopoverPresenting>" _palettePopoverPresenting;
q _layoutAxis;
@"UIStackView" _stackView;
@"PKDrawingPaletteInputAssistantContainerView" _inputAssistantContainerView;
@"PKPaletteInputAssistantViewController" _inputAssistantViewController;
```

## Properties

```
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"PKDrawingPaletteInputAssistantContainerView",&,N,V_inputAssistantContainerView) inputAssistantContainerView;
@property (T@"PKPaletteInputAssistantViewController",&,N,V_inputAssistantViewController) inputAssistantViewController;
@property (T@"<PKPaletteColorPickerContainerViewDelegate>",W,N,V_delegate) delegate;
@property (T@"<PKDrawingPaletteViewStateSubject>",W,N,V_paletteViewState) paletteViewState;
@property (T@"PKPaletteColorPickerView",R,N,V_colorPickerView) colorPickerView;
@property (T@"<PKPalettePopoverPresenting>",W,N,V_palettePopoverPresenting) palettePopoverPresenting;
@property (TB,N,V_shouldShowInputAssistantView) shouldShowInputAssistantView;
@property (Tq,N,V_layoutAxis) layoutAxis;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteColorPickerContainerView adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPaletteColorPickerContainerView adaptivePresentationStyleForPresentationController:];
-[PKPaletteColorPickerContainerView layoutAxis];
-[PKPaletteColorPickerContainerView setDelegate:];
-[PKPaletteColorPickerContainerView setLayoutAxis:];
-[PKPaletteColorPickerContainerView delegate];
-[PKPaletteColorPickerContainerView stackView];
-[PKPaletteColorPickerContainerView setStackView:];
-[PKPaletteColorPickerContainerView traitCollectionDidChange:];
-[PKPaletteColorPickerContainerView _updateUI];
-[PKPaletteColorPickerContainerView initWithFrame:];
-[PKPaletteColorPickerContainerView inputAssistantViewController];
-[PKPaletteColorPickerContainerView dismissPalettePopoverWithCompletion:];
-[PKPaletteColorPickerContainerView setInputAssistantContainerView:];
-[PKPaletteColorPickerContainerView colorPickerView];
-[PKPaletteColorPickerContainerView _dismissViewController:withCompletion:];
-[PKPaletteColorPickerContainerView _handleUCBButtonPressed];
-[PKPaletteColorPickerContainerView _installInputAssistantViewContainer];
-[PKPaletteColorPickerContainerView _isInputAssistantViewControllerPresented];
-[PKPaletteColorPickerContainerView _showInputAssistantPopover];
-[PKPaletteColorPickerContainerView inputAssistantContainerView];
-[PKPaletteColorPickerContainerView palettePopoverPresenting];
-[PKPaletteColorPickerContainerView paletteViewState];
-[PKPaletteColorPickerContainerView setInputAssistantViewController:];
-[PKPaletteColorPickerContainerView setPalettePopoverPresenting:];
-[PKPaletteColorPickerContainerView setPaletteViewState:];
-[PKPaletteColorPickerContainerView setShouldShowInputAssistantView:];
-[PKPaletteColorPickerContainerView shouldShowInputAssistantView];
```
