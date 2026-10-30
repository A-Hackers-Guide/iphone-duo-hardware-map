# `_UIStatusBarDualCellularSignalView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`
- 7 instance variables, 16 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _rounded;
@"_UIStatusBarCellularSignalView" _topSignalView;
@"_UIStatusBarCellularSignalView" _bottomSignalView;
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
@property (T@"_UIStatusBarCellularSignalView",R,V_topSignalView) topSignalView;
@property (T@"_UIStatusBarCellularSignalView",R,V_bottomSignalView) bottomSignalView;
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
+[_UIStatusBarDualCellularSignalView _interspaceForIconSize:];
```

## Instance methods

```
-[_UIStatusBarDualCellularSignalView topConstraint];
-[_UIStatusBarDualCellularSignalView _commonInit];
-[_UIStatusBarDualCellularSignalView setTopConstraint:];
-[_UIStatusBarDualCellularSignalView setIconSize:];
-[_UIStatusBarDualCellularSignalView _iconSizeDidChange];
-[_UIStatusBarDualCellularSignalView iconSize];
-[_UIStatusBarDualCellularSignalView accessibilityHUDRepresentation];
-[_UIStatusBarDualCellularSignalView applyStyleAttributes:];
-[_UIStatusBarDualCellularSignalView intrinsicContentSize];
-[_UIStatusBarDualCellularSignalView alignmentRectInsets];
-[_UIStatusBarDualCellularSignalView viewForLastBaselineLayout];
-[_UIStatusBarDualCellularSignalView setVerticalInterspaceConstraint:];
-[_UIStatusBarDualCellularSignalView verticalInterspaceConstraint];
-[_UIStatusBarDualCellularSignalView setAlignmentRectInsets:];
-[_UIStatusBarDualCellularSignalView initWithCoder:];
-[_UIStatusBarDualCellularSignalView rounded];
-[_UIStatusBarDualCellularSignalView setRounded:];
-[_UIStatusBarDualCellularSignalView initWithFrame:];
-[_UIStatusBarDualCellularSignalView topSignalView];
-[_UIStatusBarDualCellularSignalView bottomSignalView];
```
