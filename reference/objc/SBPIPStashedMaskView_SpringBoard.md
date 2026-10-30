# `SBPIPStashedMaskView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 12 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _tabHidden;
B _tabShownLeft;
@"UIView" _mainBody;
@"UIView" _tab;
@"UIView" _tabTopCornerFill;
@"UIView" _tabBottomCornerFill;
@"UIView" _tabLeftTopCornerDestOut;
@"UIView" _tabLeftBottomCornerDestOut;
@"UIView" _tabRightTopCornerDestOut;
@"UIView" _tabRightBottomCornerDestOut;
@"UIView" _tabShadowView;
{CGSize="width"d"height"d} _minimumStashTabSize;
```

## Properties

```
@property (T@"UIView",W,N,V_tabShadowView) tabShadowView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) tabViewBounds;
@property (T{CGSize=dd},N,V_minimumStashTabSize) minimumStashTabSize;
```

## Instance methods

```
-[SBPIPStashedMaskView layoutSubviews];
-[SBPIPStashedMaskView _continuousCornerRadius];
-[SBPIPStashedMaskView _setContinuousCornerRadius:];
-[SBPIPStashedMaskView pointInside:withEvent:];
-[SBPIPStashedMaskView initWithFrame:];
-[SBPIPStashedMaskView _mainBodyBounds];
-[SBPIPStashedMaskView initWithFrame:minimumStashTabSize:];
-[SBPIPStashedMaskView minimumStashTabSize];
-[SBPIPStashedMaskView setMinimumStashTabSize:];
-[SBPIPStashedMaskView setTabHidden:left:];
-[SBPIPStashedMaskView setTabShadowView:];
-[SBPIPStashedMaskView tabShadowView];
-[SBPIPStashedMaskView tabViewBounds];
```
