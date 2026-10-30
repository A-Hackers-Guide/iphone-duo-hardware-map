# `PKPaletteButtonGroupView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PKPaletteViewSizeScaling`
- 9 instance variables, 14 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _useEqualInterItemSpacing;
d _scalingFactor;
@"NSArray" _buttons;
@"UIStackView" _buttonStackView;
@"NSLayoutConstraint" _buttonStackViewTopConstraint;
@"NSLayoutConstraint" _buttonStackViewLeadingConstraint;
@"NSLayoutConstraint" _buttonStackViewBottomConstraint;
@"NSLayoutConstraint" _buttonStackViewTrailingConstraint;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _additionalContentMargins;
```

## Properties

```
@property (T@"UIStackView",&,N,V_buttonStackView) buttonStackView;
@property (T@"NSArray",C,N,V_buttons) buttons;
@property (T@"NSLayoutConstraint",&,N,V_buttonStackViewTopConstraint) buttonStackViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_buttonStackViewLeadingConstraint) buttonStackViewLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_buttonStackViewBottomConstraint) buttonStackViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_buttonStackViewTrailingConstraint) buttonStackViewTrailingConstraint;
@property (Tq,N) axis;
@property (TB,N,V_useEqualInterItemSpacing) useEqualInterItemSpacing;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_additionalContentMargins) additionalContentMargins;
@property (Td,N,V_scalingFactor) scalingFactor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKPaletteButtonGroupView buttons];
-[PKPaletteButtonGroupView axis];
-[PKPaletteButtonGroupView setAxis:];
-[PKPaletteButtonGroupView scalingFactor];
-[PKPaletteButtonGroupView setButtons:];
-[PKPaletteButtonGroupView setScalingFactor:];
-[PKPaletteButtonGroupView _updateUI];
-[PKPaletteButtonGroupView addButton:];
-[PKPaletteButtonGroupView initWithFrame:];
-[PKPaletteButtonGroupView additionalContentMargins];
-[PKPaletteButtonGroupView removeAllButtons];
-[PKPaletteButtonGroupView buttonStackView];
-[PKPaletteButtonGroupView buttonStackViewBottomConstraint];
-[PKPaletteButtonGroupView addButtonsFromArray:];
-[PKPaletteButtonGroupView buttonStackViewLeadingConstraint];
-[PKPaletteButtonGroupView buttonStackViewTopConstraint];
-[PKPaletteButtonGroupView buttonStackViewTrailingConstraint];
-[PKPaletteButtonGroupView setAdditionalContentMargins:];
-[PKPaletteButtonGroupView setButtonStackView:];
-[PKPaletteButtonGroupView setButtonStackViewBottomConstraint:];
-[PKPaletteButtonGroupView setButtonStackViewLeadingConstraint:];
-[PKPaletteButtonGroupView setButtonStackViewTopConstraint:];
-[PKPaletteButtonGroupView setButtonStackViewTrailingConstraint:];
-[PKPaletteButtonGroupView setUseEqualInterItemSpacing:];
-[PKPaletteButtonGroupView useEqualInterItemSpacing];
```
