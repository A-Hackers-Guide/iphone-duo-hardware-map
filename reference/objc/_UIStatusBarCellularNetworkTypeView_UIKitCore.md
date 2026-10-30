# `_UIStatusBarCellularNetworkTypeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`
- 6 instance variables, 14 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _animatingUpdate;
q _type;
@"_UIStatusBarStringView" _stringView;
@"UIVectorLabel" _prefixLabel;
@"UIVectorLabel" _accessoryLabel;
@"NSLayoutConstraint" _widthConstraint;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"_UIStatusBarStringView",&,N,V_stringView) stringView;
@property (T@"UIVectorLabel",&,N,V_prefixLabel) prefixLabel;
@property (T@"UIVectorLabel",&,N,V_accessoryLabel) accessoryLabel;
@property (T@"NSLayoutConstraint",&,N,V_widthConstraint) widthConstraint;
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarCellularNetworkTypeView accessibilityHUDRepresentation];
-[_UIStatusBarCellularNetworkTypeView applyStyleAttributes:];
-[_UIStatusBarCellularNetworkTypeView viewForLastBaselineLayout];
-[_UIStatusBarCellularNetworkTypeView setType:];
-[_UIStatusBarCellularNetworkTypeView type];
-[_UIStatusBarCellularNetworkTypeView widthConstraint];
-[_UIStatusBarCellularNetworkTypeView setWidthConstraint:];
-[_UIStatusBarCellularNetworkTypeView initWithFrame:];
-[_UIStatusBarCellularNetworkTypeView setPrefixLabel:];
-[_UIStatusBarCellularNetworkTypeView _animateUpdateToText:prefixLength:styleAttributes:attributedText:type:];
-[_UIStatusBarCellularNetworkTypeView accessoryLabel];
-[_UIStatusBarCellularNetworkTypeView prefixLabel];
-[_UIStatusBarCellularNetworkTypeView setAccessoryLabel:];
-[_UIStatusBarCellularNetworkTypeView setAttributedText:prefixLength:forType:animated:];
-[_UIStatusBarCellularNetworkTypeView setFixedWidth:];
-[_UIStatusBarCellularNetworkTypeView setStringView:];
-[_UIStatusBarCellularNetworkTypeView setText:prefixLength:withStyleAttributes:forType:animated:];
-[_UIStatusBarCellularNetworkTypeView stringView];
```
