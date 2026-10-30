# `TPBadgeView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `TPView`
- 12 instance variables, 14 properties, 42 instance methods, 0 class methods

## Instance variables

```
Q _sizeCategory;
Q _theme;
@"UILabel" _titleLabel;
d _titleLabelFontSize;
d _layerCornerRadius;
@"NSLayoutConstraint" _heightAnchorLayoutConstraint;
@"NSLayoutConstraint" _widthAnchorLayoutConstraint;
@"NSLayoutConstraint" _titleLabelLeadingAnchorLayoutConstraint;
@"NSLayoutConstraint" _titleLabelTrailingAnchorLayoutConstraint;
d _heightAnchorLayoutConstraintConstantFontMultiplier;
d _titleLabelLeadingAnchorLayoutConstraintConstant;
d _titleLabelTrailingAnchorLayoutConstraintConstant;
```

## Properties

```
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (Td,N,V_titleLabelFontSize) titleLabelFontSize;
@property (Td,N,V_layerCornerRadius) layerCornerRadius;
@property (T@"NSLayoutConstraint",&,N,V_heightAnchorLayoutConstraint) heightAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_widthAnchorLayoutConstraint) widthAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_titleLabelLeadingAnchorLayoutConstraint) titleLabelLeadingAnchorLayoutConstraint;
@property (T@"NSLayoutConstraint",&,N,V_titleLabelTrailingAnchorLayoutConstraint) titleLabelTrailingAnchorLayoutConstraint;
@property (Td,N,V_heightAnchorLayoutConstraintConstantFontMultiplier) heightAnchorLayoutConstraintConstantFontMultiplier;
@property (Td,N,V_titleLabelLeadingAnchorLayoutConstraintConstant) titleLabelLeadingAnchorLayoutConstraintConstant;
@property (Td,N,V_titleLabelTrailingAnchorLayoutConstraintConstant) titleLabelTrailingAnchorLayoutConstraintConstant;
@property (TQ,N,V_sizeCategory) sizeCategory;
@property (TQ,N,V_theme) theme;
@property (T@"NSString",C,N) title;
@property (Td,R,N) suggestedHeight;
```

## Instance methods

```
-[TPBadgeView commonInit];
-[TPBadgeView theme];
-[TPBadgeView suggestedHeight];
-[TPBadgeView titleLabelTrailingAnchorLayoutConstraint];
-[TPBadgeView updateConstraintsConstants];
-[TPBadgeView heightAnchorLayoutConstraintConstantFontMultiplier];
-[TPBadgeView initWithTitle:];
-[TPBadgeView updateTheme];
-[TPBadgeView scaledLayoutValueForBaseValue:];
-[TPBadgeView titleLabel];
-[TPBadgeView titleLabelLeadingAnchorLayoutConstraintConstant];
-[TPBadgeView sizeCategory];
-[TPBadgeView setTitleLabelTrailingAnchorLayoutConstraintConstant:];
-[TPBadgeView setTitleLabelTrailingAnchorLayoutConstraint:];
-[TPBadgeView heightAnchorLayoutConstraint];
-[TPBadgeView updateSizeCategory];
-[TPBadgeView widthAnchorLayoutConstraint];
-[TPBadgeView setTitleLabelFontSize:];
-[TPBadgeView scaledLayoutValueForBaseValue:shouldLowerBound:];
-[TPBadgeView titleLabelLeadingAnchorLayoutConstraint];
-[TPBadgeView title];
-[TPBadgeView lastBaselineAnchor];
-[TPBadgeView loadConstraints];
-[TPBadgeView updateActiveHorizontalConstraints];
-[TPBadgeView titleLabelFontSize];
-[TPBadgeView setSizeCategory:];
-[TPBadgeView setTitleLabelLeadingAnchorLayoutConstraintConstant:];
-[TPBadgeView updateFonts];
-[TPBadgeView setTitle:];
-[TPBadgeView setTitleLabelLeadingAnchorLayoutConstraint:];
-[TPBadgeView setLayerCornerRadius:];
-[TPBadgeView firstBaselineAnchor];
-[TPBadgeView titleLabelTrailingAnchorLayoutConstraintConstant];
-[TPBadgeView setTheme:];
-[TPBadgeView setHeightAnchorLayoutConstraintConstantFontMultiplier:];
-[TPBadgeView initWithTitle:theme:];
-[TPBadgeView layerCornerRadius];
-[TPBadgeView setWidthAnchorLayoutConstraint:];
-[TPBadgeView _hasBaseline];
-[TPBadgeView setHeightAnchorLayoutConstraint:];
-[TPBadgeView _layoutSizeThatFits:fixedAxes:];
-[TPBadgeView unloadConstraints];
```
