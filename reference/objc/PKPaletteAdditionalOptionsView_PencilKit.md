# `PKPaletteAdditionalOptionsView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteMoreOptionsViewControllerDelegate`, `UIPopoverPresentationControllerDelegate`, `PKPaletteEdgeLocating`, `PKPalettePopoverUpdating`, `PKPalettePopoverDismissing`, `PKPaletteViewSizeScaling`
- 43 instance variables, 43 properties, 107 instance methods, 0 class methods

## Instance variables

```
B _didTapOnPencilSettings;
@"PKUIPencilInteractionObserver" _pencilInteractionObserver;
@"PKAutoRefineSettingsObserver" _autoRefineSettingsObserver;
@"PKProofreadingSettingsObserver" _proofreadingSettingsObserver;
B _showsPlusButton;
B _showsTextButton;
B _showsShapeButton;
B _autoHideOn;
B _isFingerDrawsOn;
B _shouldAlwaysShowAutoRefineControls;
B _shouldShowFingerDrawsOption;
B _shouldShowTapToRadarOption;
B _shouldShowResetHandwritingEducationPane;
B _wantsEllipsisButtonVisible;
B _wantsInputAssistantViewVisible;
B _enableKeyboardButtons;
B _shouldHideHoverPreviewToggle;
Q _edgeLocation;
Q _cornerLocation;
d _scalingFactor;
@"<PKPalettePopoverPresenting>" _palettePopoverPresenting;
@"<PKPaletteAdditionalOptionsViewDelegate>" _delegate;
@"PKPaletteButton" _plusButton;
@"PKPaletteButton" _textButton;
@"PKPaletteButton" _shapeButton;
q _floatingKeyboardType;
@"UIStackView" _contentStackView;
@"UIStackView" _textShapeStackView;
@"UIStackView" _plusEllipsisStackView;
@"PKPaletteButton" _ellipsisButton;
@"PKPaletteButtonGroupView" _keyboardButtonGroupView;
@"PKPaletteKeyboardButton" _keyboardButton;
@"PKPaletteButton" _returnKeyButton;
@"PKPaletteMoreOptionsViewController" _moreOptionsViewController;
@"UIViewController" _presentedPopoverViewController;
@"NSLayoutConstraint" _plusButtonWidthConstraint;
@"NSLayoutConstraint" _plusButtonHeightConstraint;
@"NSLayoutConstraint" _ellipsisButtonWidthConstraint;
@"NSLayoutConstraint" _ellipsisButtonHeightConstraint;
@"NSLayoutConstraint" _textButtonWidthConstraint;
@"NSLayoutConstraint" _textButtonHeightConstraint;
@"NSLayoutConstraint" _shapeButtonWidthConstraint;
@"NSLayoutConstraint" _shapeButtonHeightConstraint;
```

## Properties

```
@property (T@"UIStackView",&,N,V_contentStackView) contentStackView;
@property (T@"UIStackView",&,N,V_textShapeStackView) textShapeStackView;
@property (T@"UIStackView",&,N,V_plusEllipsisStackView) plusEllipsisStackView;
@property (T@"PKPaletteButton",&,N,V_textButton) textButton;
@property (T@"PKPaletteButton",&,N,V_ellipsisButton) ellipsisButton;
@property (T@"PKPaletteButtonGroupView",&,N,V_keyboardButtonGroupView) keyboardButtonGroupView;
@property (T@"PKPaletteKeyboardButton",&,N,V_keyboardButton) keyboardButton;
@property (T@"PKPaletteButton",&,N,V_returnKeyButton) returnKeyButton;
@property (T@"PKPaletteMoreOptionsViewController",&,N,V_moreOptionsViewController) moreOptionsViewController;
@property (T@"UIViewController",&,N,V_presentedPopoverViewController) presentedPopoverViewController;
@property (T@"NSLayoutConstraint",&,N,V_plusButtonWidthConstraint) plusButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_plusButtonHeightConstraint) plusButtonHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_ellipsisButtonWidthConstraint) ellipsisButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_ellipsisButtonHeightConstraint) ellipsisButtonHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_textButtonWidthConstraint) textButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_textButtonHeightConstraint) textButtonHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_shapeButtonWidthConstraint) shapeButtonWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_shapeButtonHeightConstraint) shapeButtonHeightConstraint;
@property (T@"<PKPalettePopoverPresenting>",W,N,V_palettePopoverPresenting) palettePopoverPresenting;
@property (T@"<PKPaletteAdditionalOptionsViewDelegate>",W,N,V_delegate) delegate;
@property (T@"PKPaletteButton",&,N,V_plusButton) plusButton;
@property (T@"PKPaletteButton",R,N,V_shapeButton) shapeButton;
@property (TB,N,V_showsPlusButton) showsPlusButton;
@property (TB,N,V_showsTextButton) showsTextButton;
@property (TB,N,V_showsShapeButton) showsShapeButton;
@property (TB,N,GisAutoHideOn,V_autoHideOn) autoHideOn;
@property (TB,N,V_isFingerDrawsOn) isFingerDrawsOn;
@property (TB,N,V_shouldAlwaysShowAutoRefineControls) shouldAlwaysShowAutoRefineControls;
@property (TB,N,V_shouldShowFingerDrawsOption) shouldShowFingerDrawsOption;
@property (TB,N,V_shouldShowTapToRadarOption) shouldShowTapToRadarOption;
@property (TB,N,V_shouldShowResetHandwritingEducationPane) shouldShowResetHandwritingEducationPane;
@property (TB,N,V_wantsEllipsisButtonVisible) wantsEllipsisButtonVisible;
@property (TB,N,V_wantsInputAssistantViewVisible) wantsInputAssistantViewVisible;
@property (TB,N,V_enableKeyboardButtons) enableKeyboardButtons;
@property (Tq,N,V_floatingKeyboardType) floatingKeyboardType;
@property (TB,N,V_shouldHideHoverPreviewToggle) shouldHideHoverPreviewToggle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_edgeLocation) edgeLocation;
@property (TQ,N,V_cornerLocation) cornerLocation;
@property (Td,N,V_scalingFactor) scalingFactor;
```

## Instance methods

```
-[PKPaletteAdditionalOptionsView adaptivePresentationStyleForPresentationController:traitCollection:];
-[PKPaletteAdditionalOptionsView adaptivePresentationStyleForPresentationController:];
-[PKPaletteAdditionalOptionsView didMoveToWindow];
-[PKPaletteAdditionalOptionsView intrinsicContentSize];
-[PKPaletteAdditionalOptionsView willMoveToSuperview:];
-[PKPaletteAdditionalOptionsView textButton];
-[PKPaletteAdditionalOptionsView scalingFactor];
-[PKPaletteAdditionalOptionsView setDelegate:];
-[PKPaletteAdditionalOptionsView delegate];
-[PKPaletteAdditionalOptionsView setScalingFactor:];
-[PKPaletteAdditionalOptionsView traitCollectionDidChange:];
-[PKPaletteAdditionalOptionsView _updateUI];
-[PKPaletteAdditionalOptionsView initWithFrame:];
-[PKPaletteAdditionalOptionsView contentStackView];
-[PKPaletteAdditionalOptionsView dismissPalettePopoverWithCompletion:];
-[PKPaletteAdditionalOptionsView keyboardButton];
-[PKPaletteAdditionalOptionsView plusButton];
-[PKPaletteAdditionalOptionsView setContentStackView:];
-[PKPaletteAdditionalOptionsView setKeyboardButton:];
-[PKPaletteAdditionalOptionsView setPlusButton:];
-[PKPaletteAdditionalOptionsView _keyboardButtonGroupViewButtons];
-[PKPaletteAdditionalOptionsView _setPlusButton:];
-[PKPaletteAdditionalOptionsView returnKeyButton];
-[PKPaletteAdditionalOptionsView showsPlusButton];
-[PKPaletteAdditionalOptionsView isFingerDrawsOn];
-[PKPaletteAdditionalOptionsView plusButtonFrame];
-[PKPaletteAdditionalOptionsView setShapeButtonHeightConstraint:];
-[PKPaletteAdditionalOptionsView setShouldShowFingerDrawsOption:];
-[PKPaletteAdditionalOptionsView showsTextButton];
-[PKPaletteAdditionalOptionsView updatePopoverUI];
-[PKPaletteAdditionalOptionsView _didSelectEllipsisButton:];
-[PKPaletteAdditionalOptionsView _handleAutoRefineSettingsDidChange];
-[PKPaletteAdditionalOptionsView _handleKeyboardButton];
-[PKPaletteAdditionalOptionsView _handleProofreadingSettingsDidChange];
-[PKPaletteAdditionalOptionsView _handleReturnKeyButton];
-[PKPaletteAdditionalOptionsView _handleSceneWillDeactivateNotification:];
-[PKPaletteAdditionalOptionsView _hasPlusButtonView];
-[PKPaletteAdditionalOptionsView _pencilInteractionPrefersPencilOnlyDrawsDidChange];
-[PKPaletteAdditionalOptionsView _updateMoreOptionsViewControllerAutoRefineState];
-[PKPaletteAdditionalOptionsView _updateMoreOptionsViewControllerProofreadingState];
-[PKPaletteAdditionalOptionsView cornerLocation];
-[PKPaletteAdditionalOptionsView edgeLocation];
-[PKPaletteAdditionalOptionsView ellipsisButton];
-[PKPaletteAdditionalOptionsView ellipsisButtonHeightConstraint];
-[PKPaletteAdditionalOptionsView ellipsisButtonWidthConstraint];
-[PKPaletteAdditionalOptionsView enableKeyboardButtons];
-[PKPaletteAdditionalOptionsView floatingKeyboardType];
-[PKPaletteAdditionalOptionsView isAutoHideOn];
-[PKPaletteAdditionalOptionsView keyboardButtonGroupView];
-[PKPaletteAdditionalOptionsView moreOptionsViewController];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidSelectOpenPencilSettings:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidSelectResetHandwritingEducationPane:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidSelectTapToRadar:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidToggleAutoHide:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidToggleAutoRefine:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidToggleFingerDraws:];
-[PKPaletteAdditionalOptionsView moreOptionsViewControllerDidToggleProofreading:];
-[PKPaletteAdditionalOptionsView palettePopoverPresenting];
-[PKPaletteAdditionalOptionsView plusButtonHeightConstraint];
-[PKPaletteAdditionalOptionsView plusButtonWidthConstraint];
-[PKPaletteAdditionalOptionsView plusEllipsisStackView];
-[PKPaletteAdditionalOptionsView presentedPopoverViewController];
-[PKPaletteAdditionalOptionsView setAutoHideOn:];
-[PKPaletteAdditionalOptionsView setCornerLocation:];
-[PKPaletteAdditionalOptionsView setEdgeLocation:];
-[PKPaletteAdditionalOptionsView setEllipsisButton:];
-[PKPaletteAdditionalOptionsView setEllipsisButtonHeightConstraint:];
-[PKPaletteAdditionalOptionsView setEllipsisButtonWidthConstraint:];
-[PKPaletteAdditionalOptionsView setEnableKeyboardButtons:];
-[PKPaletteAdditionalOptionsView setFloatingKeyboardType:];
-[PKPaletteAdditionalOptionsView setIsFingerDrawsOn:];
-[PKPaletteAdditionalOptionsView setKeyboardButtonGroupView:];
-[PKPaletteAdditionalOptionsView setMoreOptionsViewController:];
-[PKPaletteAdditionalOptionsView setPalettePopoverPresenting:];
-[PKPaletteAdditionalOptionsView setPlusButtonHeightConstraint:];
-[PKPaletteAdditionalOptionsView setPlusButtonWidthConstraint:];
-[PKPaletteAdditionalOptionsView setPlusEllipsisStackView:];
-[PKPaletteAdditionalOptionsView setPresentedPopoverViewController:];
-[PKPaletteAdditionalOptionsView setReturnKeyButton:];
-[PKPaletteAdditionalOptionsView setShapeButtonWidthConstraint:];
-[PKPaletteAdditionalOptionsView setShouldAlwaysShowAutoRefineControls:];
-[PKPaletteAdditionalOptionsView setShouldHideHoverPreviewToggle:];
-[PKPaletteAdditionalOptionsView setShouldShowResetHandwritingEducationPane:];
-[PKPaletteAdditionalOptionsView setShouldShowTapToRadarOption:];
-[PKPaletteAdditionalOptionsView setShowsPlusButton:];
-[PKPaletteAdditionalOptionsView setShowsShapeButton:];
-[PKPaletteAdditionalOptionsView setShowsTextButton:];
-[PKPaletteAdditionalOptionsView setTextButton:];
-[PKPaletteAdditionalOptionsView setTextButtonHeightConstraint:];
-[PKPaletteAdditionalOptionsView setTextButtonWidthConstraint:];
-[PKPaletteAdditionalOptionsView setTextShapeStackView:];
-[PKPaletteAdditionalOptionsView setWantsEllipsisButtonVisible:];
-[PKPaletteAdditionalOptionsView setWantsInputAssistantViewVisible:];
-[PKPaletteAdditionalOptionsView shapeButton];
-[PKPaletteAdditionalOptionsView shapeButtonHeightConstraint];
-[PKPaletteAdditionalOptionsView shapeButtonWidthConstraint];
-[PKPaletteAdditionalOptionsView shouldAlwaysShowAutoRefineControls];
-[PKPaletteAdditionalOptionsView shouldHideHoverPreviewToggle];
-[PKPaletteAdditionalOptionsView shouldShowFingerDrawsOption];
-[PKPaletteAdditionalOptionsView shouldShowResetHandwritingEducationPane];
-[PKPaletteAdditionalOptionsView shouldShowTapToRadarOption];
-[PKPaletteAdditionalOptionsView showsShapeButton];
-[PKPaletteAdditionalOptionsView textButtonHeightConstraint];
-[PKPaletteAdditionalOptionsView textButtonWidthConstraint];
-[PKPaletteAdditionalOptionsView textShapeStackView];
-[PKPaletteAdditionalOptionsView wantsEllipsisButtonVisible];
-[PKPaletteAdditionalOptionsView wantsInputAssistantViewVisible];
```
