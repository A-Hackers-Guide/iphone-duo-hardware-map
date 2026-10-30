# `_UIStatusBarEmergencySignalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`
- 7 instance variables, 16 properties, 19 instance methods, 2 class methods

## Instance variables

```
B _rounded;
@"UIImageView" _sosView;
@"_UIStatusBarCellularSignalView" _signalView;
q _iconSize;
@"NSLayoutConstraint" _topConstraint;
@"NSLayoutConstraint" _verticalInterspaceConstraint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
```

## Properties

```
@property (TB,N,V_rounded) rounded;
@property (Tq,N,V_iconSize) iconSize;
@property (T@"NSLayoutConstraint",&,N,V_topConstraint) topConstraint;
@property (T@"NSLayoutConstraint",&,N,V_verticalInterspaceConstraint) verticalInterspaceConstraint;
@property (T{UIEdgeInsets=dddd},N,V_alignmentRectInsets) alignmentRectInsets;
@property (T@"UIImageView",R,V_sosView) sosView;
@property (T@"_UIStatusBarCellularSignalView",R,V_signalView) signalView;
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

## Class methods

```
+[_UIStatusBarEmergencySignalView _interspaceForIconSize:];
+[_UIStatusBarEmergencySignalView _fontSizeForIconSize:];
```

## Instance methods

```
-[_UIStatusBarEmergencySignalView topConstraint];
-[_UIStatusBarEmergencySignalView _commonInit];
-[_UIStatusBarEmergencySignalView setTopConstraint:];
-[_UIStatusBarEmergencySignalView setIconSize:];
-[_UIStatusBarEmergencySignalView _iconSizeDidChange];
-[_UIStatusBarEmergencySignalView iconSize];
-[_UIStatusBarEmergencySignalView accessibilityHUDRepresentation];
-[_UIStatusBarEmergencySignalView applyStyleAttributes:];
-[_UIStatusBarEmergencySignalView intrinsicContentSize];
-[_UIStatusBarEmergencySignalView alignmentRectInsets];
-[_UIStatusBarEmergencySignalView signalView];
-[_UIStatusBarEmergencySignalView setVerticalInterspaceConstraint:];
-[_UIStatusBarEmergencySignalView verticalInterspaceConstraint];
-[_UIStatusBarEmergencySignalView setAlignmentRectInsets:];
-[_UIStatusBarEmergencySignalView initWithCoder:];
-[_UIStatusBarEmergencySignalView rounded];
-[_UIStatusBarEmergencySignalView setRounded:];
-[_UIStatusBarEmergencySignalView initWithFrame:];
-[_UIStatusBarEmergencySignalView sosView];
```
