# `SBSwitcherStrongPairIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 14 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSString" _backdropGroupName;
@"UIView" _maskViewContainerView;
@"UIView" _spineMaskView;
@"UIView" _leftMaskView;
@"UIView" _rightMaskView;
@"SBUIShapeView" _topMaskView;
@"SBUIShapeView" _bottomMaskView;
@"UIView" _backdropViewContainerView;
@"SBContinuousFoldBackdropView" _leftBackdropView;
@"SBContinuousFoldBackdropView" _rightBackdropView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftItemFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _leftItemCornerRadii;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightItemFrame;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _rightItemCornerRadii;
```

## Properties

```
@property (T@"UIView",&,N,V_maskViewContainerView) maskViewContainerView;
@property (T@"UIView",&,N,V_spineMaskView) spineMaskView;
@property (T@"UIView",&,N,V_leftMaskView) leftMaskView;
@property (T@"UIView",&,N,V_rightMaskView) rightMaskView;
@property (T@"SBUIShapeView",&,N,V_topMaskView) topMaskView;
@property (T@"SBUIShapeView",&,N,V_bottomMaskView) bottomMaskView;
@property (T@"UIView",&,N,V_backdropViewContainerView) backdropViewContainerView;
@property (T@"SBContinuousFoldBackdropView",&,N,V_leftBackdropView) leftBackdropView;
@property (T@"SBContinuousFoldBackdropView",&,N,V_rightBackdropView) rightBackdropView;
@property (T@"NSString",C,N,V_backdropGroupName) backdropGroupName;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_leftItemFrame) leftItemFrame;
@property (T{UIRectCornerRadii=dddd},N,V_leftItemCornerRadii) leftItemCornerRadii;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rightItemFrame) rightItemFrame;
@property (T{UIRectCornerRadii=dddd},N,V_rightItemCornerRadii) rightItemCornerRadii;
```

## Instance methods

```
-[SBSwitcherStrongPairIndicatorView leftBackdropView];
-[SBSwitcherStrongPairIndicatorView backdropGroupName];
-[SBSwitcherStrongPairIndicatorView layoutSubviews];
-[SBSwitcherStrongPairIndicatorView setBackdropGroupName:];
-[SBSwitcherStrongPairIndicatorView rightBackdropView];
-[SBSwitcherStrongPairIndicatorView initWithFrame:];
-[SBSwitcherStrongPairIndicatorView setTopMaskView:];
-[SBSwitcherStrongPairIndicatorView backdropViewContainerView];
-[SBSwitcherStrongPairIndicatorView bottomMaskView];
-[SBSwitcherStrongPairIndicatorView leftItemCornerRadii];
-[SBSwitcherStrongPairIndicatorView leftItemFrame];
-[SBSwitcherStrongPairIndicatorView leftMaskView];
-[SBSwitcherStrongPairIndicatorView maskViewContainerView];
-[SBSwitcherStrongPairIndicatorView rightItemCornerRadii];
-[SBSwitcherStrongPairIndicatorView rightItemFrame];
-[SBSwitcherStrongPairIndicatorView rightMaskView];
-[SBSwitcherStrongPairIndicatorView setBackdropViewContainerView:];
-[SBSwitcherStrongPairIndicatorView setBottomMaskView:];
-[SBSwitcherStrongPairIndicatorView setLeftBackdropView:];
-[SBSwitcherStrongPairIndicatorView setLeftItemCornerRadii:];
-[SBSwitcherStrongPairIndicatorView setLeftItemFrame:];
-[SBSwitcherStrongPairIndicatorView setLeftMaskView:];
-[SBSwitcherStrongPairIndicatorView setMaskViewContainerView:];
-[SBSwitcherStrongPairIndicatorView setRightBackdropView:];
-[SBSwitcherStrongPairIndicatorView setRightItemCornerRadii:];
-[SBSwitcherStrongPairIndicatorView setRightItemFrame:];
-[SBSwitcherStrongPairIndicatorView setRightMaskView:];
-[SBSwitcherStrongPairIndicatorView setSpineMaskView:];
-[SBSwitcherStrongPairIndicatorView spineMaskView];
-[SBSwitcherStrongPairIndicatorView topMaskView];
```
