# `ICDocCamFilterButton`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 6 instance variables, 10 properties, 28 instance methods, 1 class methods

## Instance variables

```
s _filterType;
@"NSLayoutConstraint" _labelVerticalSpacingConstraint;
@"UILabel" _filterNameLabel;
@"UIImageView" _filterIconView;
@"UIView" _backgroundView;
@"NSLayoutConstraint" _iconSizeConstraint;
```

## Properties

```
@property (T@"UIView",W,N,V_backgroundView) backgroundView;
@property (T@"NSLayoutConstraint",W,N,V_iconSizeConstraint) iconSizeConstraint;
@property (T@"UIColor",R,N) inactiveBackgroundViewColor;
@property (T@"UIColor",R,N) inactiveTextColor;
@property (T@"UIColor",R,N) activeBackgroundViewColor;
@property (Ts,N,V_filterType) filterType;
@property (Td,D,N) iconSize;
@property (T@"NSLayoutConstraint",W,N,V_labelVerticalSpacingConstraint) labelVerticalSpacingConstraint;
@property (T@"UILabel",W,N,V_filterNameLabel) filterNameLabel;
@property (T@"UIImageView",W,N,V_filterIconView) filterIconView;
```

## Class methods

```
+[ICDocCamFilterButton filterButtonWithType:];
```

## Instance methods

```
-[ICDocCamFilterButton setIconSize:];
-[ICDocCamFilterButton iconSize];
-[ICDocCamFilterButton accessibilityFrame];
-[ICDocCamFilterButton setSelected:];
-[ICDocCamFilterButton accessibilityTraits];
-[ICDocCamFilterButton dealloc];
-[ICDocCamFilterButton filterType];
-[ICDocCamFilterButton hitTest:withEvent:];
-[ICDocCamFilterButton setHighlighted:];
-[ICDocCamFilterButton accessibilityLabel];
-[ICDocCamFilterButton isAccessibilityElement];
-[ICDocCamFilterButton backgroundView];
-[ICDocCamFilterButton setFilterType:];
-[ICDocCamFilterButton setBackgroundView:];
-[ICDocCamFilterButton awakeFromNib];
-[ICDocCamFilterButton inactiveTextColor];
-[ICDocCamFilterButton iconSizeConstraint];
-[ICDocCamFilterButton setIconSizeConstraint:];
-[ICDocCamFilterButton filterNameLabel];
-[ICDocCamFilterButton activeBackgroundViewColor];
-[ICDocCamFilterButton filterIconView];
-[ICDocCamFilterButton imageForFilterType:];
-[ICDocCamFilterButton inactiveBackgroundViewColor];
-[ICDocCamFilterButton labelVerticalSpacingConstraint];
-[ICDocCamFilterButton setFilterIconView:];
-[ICDocCamFilterButton setFilterNameLabel:];
-[ICDocCamFilterButton setLabelVerticalSpacingConstraint:];
-[ICDocCamFilterButton updateForAccessibilityDarkerSystemColors:];
```
