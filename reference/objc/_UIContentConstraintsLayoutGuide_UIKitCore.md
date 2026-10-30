# `_UIContentConstraintsLayoutGuide`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UILayoutGuide`
- 13 instance variables, 13 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _wantsMaximumSizeConstraintsActive;
B _wantsMinimumSizeConstraintsActive;
@"NSLayoutConstraint" _leadingConstraint;
@"NSLayoutConstraint" _trailingConstraint;
@"NSLayoutConstraint" _topConstraint;
@"NSLayoutConstraint" _bottomConstraint;
@"NSLayoutConstraint" _maximumWidthConstraint;
@"NSLayoutConstraint" _maximumHeightConstraint;
@"NSLayoutConstraint" _minimumWidthConstraint;
@"NSLayoutConstraint" _minimumHeightConstraint;
{CGSize="width"d"height"d} _maximumSize;
{CGSize="width"d"height"d} _minimumSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _edgeInsets;
```

## Properties

```
@property (T@"NSLayoutConstraint",R,N,V_leadingConstraint) leadingConstraint;
@property (T@"NSLayoutConstraint",R,N,V_trailingConstraint) trailingConstraint;
@property (T@"NSLayoutConstraint",R,N,V_topConstraint) topConstraint;
@property (T@"NSLayoutConstraint",R,N,V_bottomConstraint) bottomConstraint;
@property (TB,R,N,V_wantsMaximumSizeConstraintsActive) wantsMaximumSizeConstraintsActive;
@property (T@"NSLayoutConstraint",R,N,V_maximumWidthConstraint) maximumWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_maximumHeightConstraint) maximumHeightConstraint;
@property (TB,R,N,V_wantsMinimumSizeConstraintsActive) wantsMinimumSizeConstraintsActive;
@property (T@"NSLayoutConstraint",R,N,V_minimumWidthConstraint) minimumWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_minimumHeightConstraint) minimumHeightConstraint;
@property (T{UIEdgeInsets=dddd},N,V_edgeInsets) edgeInsets;
@property (T{CGSize=dd},N,V_maximumSize) maximumSize;
@property (T{CGSize=dd},N,V_minimumSize) minimumSize;
```

## Instance methods

```
-[_UIContentConstraintsLayoutGuide topConstraint];
-[_UIContentConstraintsLayoutGuide setMaximumSize:];
-[_UIContentConstraintsLayoutGuide maximumSize];
-[_UIContentConstraintsLayoutGuide setMinimumSize:];
-[_UIContentConstraintsLayoutGuide minimumSize];
-[_UIContentConstraintsLayoutGuide _allSizeConstraints];
-[_UIContentConstraintsLayoutGuide maximumHeightConstraint];
-[_UIContentConstraintsLayoutGuide init];
-[_UIContentConstraintsLayoutGuide setEdgeInsets:];
-[_UIContentConstraintsLayoutGuide minimumWidthConstraint];
-[_UIContentConstraintsLayoutGuide trailingConstraint];
-[_UIContentConstraintsLayoutGuide _clearConstraints];
-[_UIContentConstraintsLayoutGuide leadingConstraint];
-[_UIContentConstraintsLayoutGuide _updateAllSizeConstraints];
-[_UIContentConstraintsLayoutGuide edgeInsets];
-[_UIContentConstraintsLayoutGuide setOwningView:];
-[_UIContentConstraintsLayoutGuide _setAllSizeConstraintsActive:];
-[_UIContentConstraintsLayoutGuide wantsMaximumSizeConstraintsActive];
-[_UIContentConstraintsLayoutGuide _setAllMarginConstraintsActive:];
-[_UIContentConstraintsLayoutGuide wantsMinimumSizeConstraintsActive];
-[_UIContentConstraintsLayoutGuide _updateAllMarginConstraintConstants];
-[_UIContentConstraintsLayoutGuide maximumWidthConstraint];
-[_UIContentConstraintsLayoutGuide _allMarginConstraints];
-[_UIContentConstraintsLayoutGuide minimumHeightConstraint];
-[_UIContentConstraintsLayoutGuide bottomConstraint];
```
