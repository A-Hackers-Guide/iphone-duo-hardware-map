# `PKUCBPaletteView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKPaletteView`
- Protocols: `PKPaletteButtonIntrinsicContentSizeObserver`
- 24 instance variables, 28 properties, 88 instance methods, 1 class methods

## Instance variables

```
B _returnKeyEnabled;
B _alwaysIncludeReturnKeyAndInputAssistantItems;
B _updatingUI;
q _returnKeyType;
@? _returnKeyHandler;
@"NSString" _localeIdentifier;
@"NSArray" _leadingBarButtons;
@"NSArray" _centeredBarButtons;
@"NSArray" _trailingBarButtons;
@"UIView" __contentView;
@"NSLayoutConstraint" __contentViewTopAnchor;
@"NSLayoutConstraint" __contentViewBottomAnchor;
@"NSLayoutConstraint" __contentViewLeadingAnchor;
@"NSLayoutConstraint" __contentViewTrailingAnchor;
@"UIStackView" __buttonStackView;
@"NSLayoutConstraint" __buttonStackViewHeightConstraint;
@"NSLayoutConstraint" __buttonStackViewBottomConstraint;
@"PKPaletteButtonGroupView" __leadingButtonGroupView;
@"PKPaletteButtonGroupView" __centeredButtonGroupView;
@"PKPaletteButtonGroupView" __trailingButtonGroupView;
@"PKPaletteButtonGroupView" __returnKeyButtonGroupView;
@"PKPaletteReturnKeyButton" __returnKeyButton;
@"NSArray" _nonCompactContentViewConstraints;
@"NSArray" _compactContentViewConstraints;
```

## Properties

```
@property (T@"UIView",&,N,V__contentView) _contentView;
@property (T@"NSLayoutConstraint",&,N,V__contentViewTopAnchor) _contentViewTopAnchor;
@property (T@"NSLayoutConstraint",&,N,V__contentViewBottomAnchor) _contentViewBottomAnchor;
@property (T@"NSLayoutConstraint",&,N,V__contentViewLeadingAnchor) _contentViewLeadingAnchor;
@property (T@"NSLayoutConstraint",&,N,V__contentViewTrailingAnchor) _contentViewTrailingAnchor;
@property (T@"UIStackView",&,N,V__buttonStackView) _buttonStackView;
@property (T@"NSLayoutConstraint",&,N,V__buttonStackViewHeightConstraint) _buttonStackViewHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V__buttonStackViewBottomConstraint) _buttonStackViewBottomConstraint;
@property (T@"PKPaletteButtonGroupView",&,N,V__leadingButtonGroupView) _leadingButtonGroupView;
@property (T@"PKPaletteButtonGroupView",&,N,V__centeredButtonGroupView) _centeredButtonGroupView;
@property (T@"PKPaletteButtonGroupView",&,N,V__trailingButtonGroupView) _trailingButtonGroupView;
@property (T@"PKPaletteButtonGroupView",&,N,V__returnKeyButtonGroupView) _returnKeyButtonGroupView;
@property (T@"PKPaletteReturnKeyButton",&,N,V__returnKeyButton) _returnKeyButton;
@property (TB,N,V_alwaysIncludeReturnKeyAndInputAssistantItems) alwaysIncludeReturnKeyAndInputAssistantItems;
@property (TB,N,GisUpdatingUI,V_updatingUI) updatingUI;
@property (T@"NSArray",C,N,V_nonCompactContentViewConstraints) nonCompactContentViewConstraints;
@property (T@"NSArray",C,N,V_compactContentViewConstraints) compactContentViewConstraints;
@property (Tq,N,V_returnKeyType) returnKeyType;
@property (TB,N,GisReturnKeyEnabled,V_returnKeyEnabled) returnKeyEnabled;
@property (T@?,C,N,V_returnKeyHandler) returnKeyHandler;
@property (T@"NSString",C,N,V_localeIdentifier) localeIdentifier;
@property (T@"NSArray",C,N,V_leadingBarButtons) leadingBarButtons;
@property (T@"NSArray",C,N,V_centeredBarButtons) centeredBarButtons;
@property (T@"NSArray",C,N,V_trailingBarButtons) trailingBarButtons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKUCBPaletteView makeBackgroundView];
```

## Instance methods

```
-[PKUCBPaletteView setLocaleIdentifier:];
-[PKUCBPaletteView setReturnKeyType:];
-[PKUCBPaletteView localeIdentifier];
-[PKUCBPaletteView _contentView];
-[PKUCBPaletteView updateConstraints];
-[PKUCBPaletteView traitCollectionDidChange:];
-[PKUCBPaletteView shadowOpacity];
-[PKUCBPaletteView setReturnKeyEnabled:];
-[PKUCBPaletteView _updateUI];
-[PKUCBPaletteView initWithFrame:];
-[PKUCBPaletteView shadowRadius];
-[PKUCBPaletteView returnKeyType];
-[PKUCBPaletteView _contentMargin];
-[PKUCBPaletteView dismissPalettePopoverWithCompletion:];
-[PKUCBPaletteView _flashLanguageIndicatorIfNeeded];
-[PKUCBPaletteView paletteViewType];
-[PKUCBPaletteView _buttonGroupSpacing];
-[PKUCBPaletteView _buttonStackView];
-[PKUCBPaletteView _buttonStackViewBottomConstraint];
-[PKUCBPaletteView _buttonStackViewHeightConstraint];
-[PKUCBPaletteView _centeredBarButtons];
-[PKUCBPaletteView _centeredButtonGroupView];
-[PKUCBPaletteView _contentViewBottomAnchor];
-[PKUCBPaletteView _contentViewLeadingAnchor];
-[PKUCBPaletteView _contentViewTopAnchor];
-[PKUCBPaletteView _contentViewTrailingAnchor];
-[PKUCBPaletteView _handleReturnKey];
-[PKUCBPaletteView _leadingButtonGroupView];
-[PKUCBPaletteView _narrowLength];
-[PKUCBPaletteView _performUpdateUIBlock:];
-[PKUCBPaletteView _returnKeyButton];
-[PKUCBPaletteView _returnKeyButtonGroupView];
-[PKUCBPaletteView _shouldHideLeadingButtonGroupView];
-[PKUCBPaletteView _shouldHideReturnKeyButtonGroupView];
-[PKUCBPaletteView _shouldHideTrailingButtonGroupView];
-[PKUCBPaletteView _shouldShowCenterButtonGroupView];
-[PKUCBPaletteView _shouldShowInputAssistantItems];
-[PKUCBPaletteView _shouldShowReturnKey];
-[PKUCBPaletteView _trailingButtonGroupView];
-[PKUCBPaletteView _updateCenteredButtonGroup];
-[PKUCBPaletteView _updateLeadingButtonGroup];
-[PKUCBPaletteView _updateReturnKeyButton];
-[PKUCBPaletteView _updateSubviewLayoutAxis];
-[PKUCBPaletteView _updateTrailingButtonGroup];
-[PKUCBPaletteView alwaysIncludeReturnKeyAndInputAssistantItems];
-[PKUCBPaletteView borderColorForTraitCollection:];
-[PKUCBPaletteView borderWidthForTraitCollection:];
-[PKUCBPaletteView buttonDidChangeIntrinsicContentSize:];
-[PKUCBPaletteView centeredBarButtons];
-[PKUCBPaletteView compactContentViewConstraints];
-[PKUCBPaletteView compactPaletteHeight];
-[PKUCBPaletteView dampingRatioForThrowingFromPosition:toPosition:withVelocity:];
-[PKUCBPaletteView didChangePaletteScaleFactor];
-[PKUCBPaletteView isPalettePresentingPopover];
-[PKUCBPaletteView isReturnKeyEnabled];
-[PKUCBPaletteView isUpdatingUI];
-[PKUCBPaletteView leadingBarButtons];
-[PKUCBPaletteView nonCompactContentViewConstraints];
-[PKUCBPaletteView paletteSizeForEdge:];
-[PKUCBPaletteView responseForThrowingFromPosition:toPosition:withVelocity:];
-[PKUCBPaletteView returnKeyHandler];
-[PKUCBPaletteView setAlwaysIncludeReturnKeyAndInputAssistantItems:];
-[PKUCBPaletteView setCenteredBarButtons:];
-[PKUCBPaletteView setCompactContentViewConstraints:];
-[PKUCBPaletteView setLeadingBarButtons:];
-[PKUCBPaletteView setNonCompactContentViewConstraints:];
-[PKUCBPaletteView setReturnKeyHandler:];
-[PKUCBPaletteView setTrailingBarButtons:];
-[PKUCBPaletteView setUpdatingUI:];
-[PKUCBPaletteView set_buttonStackView:];
-[PKUCBPaletteView set_buttonStackViewBottomConstraint:];
-[PKUCBPaletteView set_buttonStackViewHeightConstraint:];
-[PKUCBPaletteView set_centeredButtonGroupView:];
-[PKUCBPaletteView set_contentView:];
-[PKUCBPaletteView set_contentViewBottomAnchor:];
-[PKUCBPaletteView set_contentViewLeadingAnchor:];
-[PKUCBPaletteView set_contentViewTopAnchor:];
-[PKUCBPaletteView set_contentViewTrailingAnchor:];
-[PKUCBPaletteView set_leadingButtonGroupView:];
-[PKUCBPaletteView set_returnKeyButton:];
-[PKUCBPaletteView set_returnKeyButtonGroupView:];
-[PKUCBPaletteView set_trailingButtonGroupView:];
-[PKUCBPaletteView shouldAdjustShadowRadiusForMinimized];
-[PKUCBPaletteView shouldExpandFromCorner];
-[PKUCBPaletteView shouldStartUpMinimized];
-[PKUCBPaletteView toolPreviewMatchesExpandedTool];
-[PKUCBPaletteView trailingBarButtons];
-[PKUCBPaletteView willStartAppearanceAnimation:];
```
