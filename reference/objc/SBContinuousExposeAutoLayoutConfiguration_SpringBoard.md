# `SBContinuousExposeAutoLayoutConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
d _screenScale;
d _dockHeightWithBottomEdgePadding;
@"SBSwitcherWindowingConfiguration" _windowingConfiguration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containerBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftStatusBarPartIntersectionRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightStatusBarPartIntersectionRegion;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_containerBounds) containerBounds;
@property (Td,R,N,V_screenScale) screenScale;
@property (Td,R,N,V_dockHeightWithBottomEdgePadding) dockHeightWithBottomEdgePadding;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_leftStatusBarPartIntersectionRegion) leftStatusBarPartIntersectionRegion;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_rightStatusBarPartIntersectionRegion) rightStatusBarPartIntersectionRegion;
@property (T@"SBSwitcherWindowingConfiguration",R,N,V_windowingConfiguration) windowingConfiguration;
```

## Instance methods

```
-[SBContinuousExposeAutoLayoutConfiguration screenScale];
-[SBContinuousExposeAutoLayoutConfiguration containerBounds];
-[SBContinuousExposeAutoLayoutConfiguration dockHeightWithBottomEdgePadding];
-[SBContinuousExposeAutoLayoutConfiguration initWithContainerBounds:screenScale:dockHeightWithBottomEdgePadding:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:windowingConfiguration:];
-[SBContinuousExposeAutoLayoutConfiguration leftStatusBarPartIntersectionRegion];
-[SBContinuousExposeAutoLayoutConfiguration rightStatusBarPartIntersectionRegion];
-[SBContinuousExposeAutoLayoutConfiguration windowingConfiguration];
```
