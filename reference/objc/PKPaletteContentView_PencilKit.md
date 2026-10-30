# `PKPaletteContentView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteColorPickerContainerViewDelegate`, `PKPaletteButtonDelegate`, `PKPaletteEdgeLocating`, `PKPalettePopoverDismissing`, `PKPaletteViewStateObserving`
- 28 instance variables, 35 properties, 107 instance methods, 0 class methods

## Instance variables

```
@"PKPaletteButton" _closeButton;
B _usingSmallestSupportedWidth;
B _closeButtonVisible;
Q _edgeLocation;
Q _cornerLocation;
@"<PKPaletteContentViewDelegate>" _delegate;
@"PKPaletteUndoRedoView" _undoRedoView;
@"PKPaletteAdditionalOptionsView" _additionalOptionsView;
@"PKPaletteToolPickerAndColorPickerView" _toolAndColorPickerContainerView;
@"UIView" _contextualEditingView;
q _contextEditingMode;
d _colorMaximumLinearExposure;
@"<PKDrawingPaletteViewStateSubject>" _paletteViewState;
@"UIStackView" _stackView;
@"NSLayoutConstraint" _stackViewTopConstraint;
@"NSLayoutConstraint" _stackViewBottomConstraint;
@"NSLayoutConstraint" _stackViewLeftConstraint;
@"NSLayoutConstraint" _stackViewRightConstraint;
@"NSLayoutConstraint" _stackViewCenterXConstraint;
@"NSLayoutConstraint" _stackViewCompactLeftConstraint;
@"NSLayoutConstraint" _stackViewCompactRightConstraint;
@"NSLayoutConstraint" _toolAndColorPickerContainerViewHeightConstraint;
@"NSLayoutConstraint" _toolAndColorPickerContainerViewWidthConstraint;
@"NSLayoutConstraint" _toolPickerViewWidthConstraint;
@"NSLayoutConstraint" _toolPickerViewHeightConstraint;
@"UITapGestureRecognizer" _lassoToolTapGestureRecognizerInCompact;
@"NSLayoutConstraint" _additionalOptionsViewCompactWidthConstraint;
@"NSLayoutConstraint" _additionalOptionsViewCompactHeightConstraint;
```

## Properties

```
@property (T@"<PKDrawingPaletteViewStateSubject>",W,N,V_paletteViewState) paletteViewState;
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (T@"NSLayoutConstraint",&,N,V_stackViewTopConstraint) stackViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewBottomConstraint) stackViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewLeftConstraint) stackViewLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewRightConstraint) stackViewRightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewCenterXConstraint) stackViewCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewCompactLeftConstraint) stackViewCompactLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_stackViewCompactRightConstraint) stackViewCompactRightConstraint;
@property (T@"UIView",&,N,V_contextualEditingView) contextualEditingView;
@property (T@"NSLayoutConstraint",&,N,V_toolAndColorPickerContainerViewHeightConstraint) toolAndColorPickerContainerViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolAndColorPickerContainerViewWidthConstraint) toolAndColorPickerContainerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewWidthConstraint) toolPickerViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_toolPickerViewHeightConstraint) toolPickerViewHeightConstraint;
@property (T@"UITapGestureRecognizer",&,N,V_lassoToolTapGestureRecognizerInCompact) lassoToolTapGestureRecognizerInCompact;
@property (T@"NSLayoutConstraint",&,N,V_additionalOptionsViewCompactWidthConstraint) additionalOptionsViewCompactWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_additionalOptionsViewCompactHeightConstraint) additionalOptionsViewCompactHeightConstraint;
@property (T@"<PKPaletteContentViewDelegate>",W,N,V_delegate) delegate;
@property (T@"PKPaletteUndoRedoView",R,N,V_undoRedoView) undoRedoView;
@property (T@"PKPaletteToolPickerView",R,N) toolPickerView;
@property (T@"PKPaletteColorPickerView",R,N) colorPickerView;
@property (T@"PKDrawingPaletteInputAssistantView",R,N) paletteInputAssistantView;
@property (T@"PKPaletteAdditionalOptionsView",R,N,V_additionalOptionsView) additionalOptionsView;
@property (T@"PKPaletteToolPickerAndColorPickerView",R,N,V_toolAndColorPickerContainerView) toolAndColorPickerContainerView;
@property (Tq,N,V_contextEditingMode) contextEditingMode;
@property (T@"UIView",R,N) lassoToolEditingView;
@property (T@"NSString",C,N) lassoToolEditingViewIdentifier;
@property (TB,N,V_closeButtonVisible) closeButtonVisible;
@property (Td,N,V_colorMaximumLinearExposure) colorMaximumLinearExposure;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
```

## Instance methods

```
-[PKPaletteContentView layoutSubviews];
-[PKPaletteContentView hitTest:withEvent:];
-[PKPaletteContentView setDelegate:];
-[PKPaletteContentView safeAreaInsetsDidChange];
-[PKPaletteContentView delegate];
-[PKPaletteContentView stackView];
-[PKPaletteContentView setStackView:];
-[PKPaletteContentView traitCollectionDidChange:];
-[PKPaletteContentView _updateUI];
-[PKPaletteContentView _closeButtonTapped:];
-[PKPaletteContentView dismissPalettePopoverWithCompletion:];
-[PKPaletteContentView toolAndColorPickerContainerView];
-[PKPaletteContentView colorPickerView];
-[PKPaletteContentView plusButtonFrame];
-[PKPaletteContentView stackViewCompactRightConstraint];
-[PKPaletteContentView _configureMenuForKeyboardButton:];
-[PKPaletteContentView _configureReturnKeyButton:];
-[PKPaletteContentView _contextEditingModeWantsContextualEditingViewVisible];
-[PKPaletteContentView _didTapLassoToolInCompact];
-[PKPaletteContentView _dismissPalettePopoverUsingConfirmationBlock:completion:];
-[PKPaletteContentView _handleKeyboardButtonPressed];
-[PKPaletteContentView _handleReturnKeyButtonPressed];
-[PKPaletteContentView _installAdditionalOptionsView];
-[PKPaletteContentView _installStackView];
-[PKPaletteContentView _installUndoRedoButtonsView];
-[PKPaletteContentView _interItemToolsSpacing];
-[PKPaletteContentView _isHandwritingToolSelected];
-[PKPaletteContentView _stackViewDistribution];
-[PKPaletteContentView _stackViewSpacing];
-[PKPaletteContentView _undoRedoButtonsInterItemSpacing];
-[PKPaletteContentView _updateAdditionalOptionsViewVisibility];
-[PKPaletteContentView _updateCloseButtonVisibility];
-[PKPaletteContentView _updateColorPickerContainerViewLocationInHierarchy];
-[PKPaletteContentView _updateUIResetUnselectedToolsVisible:];
-[PKPaletteContentView _useEqualSpacingStackViewDistribution];
-[PKPaletteContentView _wantsAdditionalOptionsViewVisible];
-[PKPaletteContentView _wantsUndoRedoButtonsShadow];
-[PKPaletteContentView _wantsUndoRedoButtonsVisible];
-[PKPaletteContentView additionalOptionsView];
-[PKPaletteContentView additionalOptionsViewCompactHeightConstraint];
-[PKPaletteContentView additionalOptionsViewCompactWidthConstraint];
-[PKPaletteContentView closeButtonVisible];
-[PKPaletteContentView colorMaximumLinearExposure];
-[PKPaletteContentView colorPickerContainerView:willDismissInputAssistantView:];
-[PKPaletteContentView colorPickerContainerView:willPresentInputAssistantView:];
-[PKPaletteContentView contextEditingMode];
-[PKPaletteContentView contextualEditingView];
-[PKPaletteContentView cornerLocation];
-[PKPaletteContentView dismissEyeDropper];
-[PKPaletteContentView edgeLocation];
-[PKPaletteContentView initWithPaletteViewStateObservable:];
-[PKPaletteContentView isEllipsisButtonVisible];
-[PKPaletteContentView lassoToolEditingView];
-[PKPaletteContentView lassoToolEditingViewIdentifier];
-[PKPaletteContentView lassoToolTapGestureRecognizerInCompact];
-[PKPaletteContentView paletteButton:backgroundColorForState:];
-[PKPaletteContentView paletteButton:tintColorForState:];
-[PKPaletteContentView paletteButton:wantsCustomBackgroundColorForState:];
-[PKPaletteContentView paletteButton:wantsCustomTintColorForState:];
-[PKPaletteContentView paletteInputAssistantView];
-[PKPaletteContentView paletteViewState];
-[PKPaletteContentView paletteViewStateDidChange:];
-[PKPaletteContentView paletteViewStateDidChange:updatePaletteAppearance:];
-[PKPaletteContentView paletteViewStateDidChangeAutoHide:];
-[PKPaletteContentView paletteViewStateDidChangeEnableKeyboardButtons:];
-[PKPaletteContentView paletteViewStateDidChangeFloatingKeyboardType:];
-[PKPaletteContentView paletteViewStateDidChangeInputAssistantItems:];
-[PKPaletteContentView paletteViewStateDidChangeIsVisible:];
-[PKPaletteContentView paletteViewStateDidChangeScaleFactor:];
-[PKPaletteContentView paletteViewStateDidChangeSelectedTool:];
-[PKPaletteContentView paletteViewStateDidChangeShowsHandwritingTool:];
-[PKPaletteContentView setAdditionalOptionsViewCompactHeightConstraint:];
-[PKPaletteContentView setAdditionalOptionsViewCompactWidthConstraint:];
-[PKPaletteContentView setCloseButtonVisible:];
-[PKPaletteContentView setColorMaximumLinearExposure:];
-[PKPaletteContentView setContextEditingMode:];
-[PKPaletteContentView setContextualEditingView:];
-[PKPaletteContentView setCornerLocation:];
-[PKPaletteContentView setEdgeLocation:];
-[PKPaletteContentView setLassoToolEditingViewIdentifier:];
-[PKPaletteContentView setLassoToolTapGestureRecognizerInCompact:];
-[PKPaletteContentView setPaletteViewState:];
-[PKPaletteContentView setStackViewBottomConstraint:];
-[PKPaletteContentView setStackViewCenterXConstraint:];
-[PKPaletteContentView setStackViewCompactLeftConstraint:];
-[PKPaletteContentView setStackViewCompactRightConstraint:];
-[PKPaletteContentView setStackViewLeftConstraint:];
-[PKPaletteContentView setStackViewRightConstraint:];
-[PKPaletteContentView setStackViewTopConstraint:];
-[PKPaletteContentView setToolAndColorPickerContainerViewHeightConstraint:];
-[PKPaletteContentView setToolAndColorPickerContainerViewWidthConstraint:];
-[PKPaletteContentView setToolPickerViewHeightConstraint:];
-[PKPaletteContentView setToolPickerViewWidthConstraint:];
-[PKPaletteContentView stackViewBottomConstraint];
-[PKPaletteContentView stackViewCenterXConstraint];
-[PKPaletteContentView stackViewCompactLeftConstraint];
-[PKPaletteContentView stackViewLeftConstraint];
-[PKPaletteContentView stackViewRightConstraint];
-[PKPaletteContentView stackViewTopConstraint];
-[PKPaletteContentView toggleColorSelectionPopover];
-[PKPaletteContentView toolAndColorPickerContainerViewHeightConstraint];
-[PKPaletteContentView toolAndColorPickerContainerViewWidthConstraint];
-[PKPaletteContentView toolPickerView];
-[PKPaletteContentView toolPickerView:widthForToolAtIndex:isCompactSize:];
-[PKPaletteContentView toolPickerViewHeightConstraint];
-[PKPaletteContentView toolPickerViewWidthConstraint];
-[PKPaletteContentView undoRedoView];
```
