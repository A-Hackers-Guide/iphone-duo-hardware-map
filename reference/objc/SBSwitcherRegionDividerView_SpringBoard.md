# `SBSwitcherRegionDividerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _obscuresLeftRegion;
B _obscuresRightRegion;
d _punchoutCornerRadius;
d _dividerWidth;
@"UIView" _leftPunchoutView;
@"UIView" _rightPunchoutView;
{CGPoint="x"d"y"d} _dividerCenter;
```

## Properties

```
@property (T@"UIView",W,N,V_leftPunchoutView) leftPunchoutView;
@property (T@"UIView",W,N,V_rightPunchoutView) rightPunchoutView;
@property (TB,N,V_obscuresLeftRegion) obscuresLeftRegion;
@property (TB,N,V_obscuresRightRegion) obscuresRightRegion;
@property (Td,N,V_punchoutCornerRadius) punchoutCornerRadius;
@property (Td,N,V_dividerWidth) dividerWidth;
@property (T{CGPoint=dd},N,V_dividerCenter) dividerCenter;
```

## Instance methods

```
-[SBSwitcherRegionDividerView layoutSubviews];
-[SBSwitcherRegionDividerView updateProperties];
-[SBSwitcherRegionDividerView initWithFrame:];
-[SBSwitcherRegionDividerView dividerWidth];
-[SBSwitcherRegionDividerView setDividerWidth:];
-[SBSwitcherRegionDividerView _leftPunchoutViewFrame];
-[SBSwitcherRegionDividerView _makePunchoutViewWithCornerMask:];
-[SBSwitcherRegionDividerView _rightPunchoutViewFrame];
-[SBSwitcherRegionDividerView dividerCenter];
-[SBSwitcherRegionDividerView leftPunchoutView];
-[SBSwitcherRegionDividerView obscuresLeftRegion];
-[SBSwitcherRegionDividerView obscuresRightRegion];
-[SBSwitcherRegionDividerView punchoutCornerRadius];
-[SBSwitcherRegionDividerView rightPunchoutView];
-[SBSwitcherRegionDividerView setDividerCenter:];
-[SBSwitcherRegionDividerView setLeftPunchoutView:];
-[SBSwitcherRegionDividerView setObscuresLeftRegion:];
-[SBSwitcherRegionDividerView setObscuresRightRegion:];
-[SBSwitcherRegionDividerView setPunchoutCornerRadius:];
-[SBSwitcherRegionDividerView setRightPunchoutView:];
```
