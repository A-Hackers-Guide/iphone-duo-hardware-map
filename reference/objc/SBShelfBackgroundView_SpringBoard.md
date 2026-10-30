# `SBShelfBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"MTMaterialView" _backgroundView;
@"UIView" _backgroundMaskView;
@"UIView" _backgroundMaskInnerRectangleView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _extendedBlurRect;
```

## Properties

```
@property (Td,N) weighting;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_extendedBlurRect) extendedBlurRect;
```

## Instance methods

```
-[SBShelfBackgroundView layoutSubviews];
-[SBShelfBackgroundView weighting];
-[SBShelfBackgroundView setWeighting:];
-[SBShelfBackgroundView initWithFrame:];
-[SBShelfBackgroundView extendedBlurRect];
-[SBShelfBackgroundView setExtendedBlurRect:];
```
