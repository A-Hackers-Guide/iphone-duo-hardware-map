# `TPRevealingRingView`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 10 properties, 34 instance methods, 1 class methods

## Instance variables

```
{?="size"{CGSize="width"d"height"d}"outerPath"{?="rect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"cornerRadius"d}"innerPath"{?="rect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"cornerRadius"d}"isCircle"B"drawsOutsideOuterPath"B} _outerViewDrawingProperties;
@"_TPTemplatedColoredImageView" _outerView;
{?="size"{CGSize="width"d"height"d}"outerPath"{?="rect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"cornerRadius"d}"innerPath"{?="rect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}"cornerRadius"d}"isCircle"B"drawsOutsideOuterPath"B} _innerViewDrawingProperties;
@"_TPTemplatedColoredImageView" _innerView;
@"UIColor" _colorOutsideRing;
@"UIColor" _colorInsideRing;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _paddingOutsideRing;
d _defaultRingStrokeWidth;
d _revealAnimationDuration;
d _unrevealAnimationDuration;
d _cornerRadius;
B _isCircularRing;
B _revealed;
d _alphaInsideRing;
d _alphaOutsideRing;
@"UIColor" _colorInsidegamRing;
```

## Properties

```
@property (T{CGSize=dd},R,D,N) ringSize;
@property (T{UIEdgeInsets=dddd},R,N,V_paddingOutsideRing) paddingOutsideRing;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Td,N,V_defaultRingStrokeWidth) defaultRingStrokeWidth;
@property (T@"UIColor",&,N,V_colorOutsideRing) colorOutsideRing;
@property (T@"UIColor",&,N,V_colorInsidegamRing) colorInsideRing;
@property (Td,N,V_revealAnimationDuration) revealAnimationDuration;
@property (Td,N,V_unrevealAnimationDuration) unrevealAnimationDuration;
@property (Td,N,V_alphaOutsideRing) alphaOutsideRing;
@property (Td,N,V_alphaInsideRing) alphaInsideRing;
```

## Class methods

```
+[TPRevealingRingView classIdentifier];
```

## Instance methods

```
-[TPRevealingRingView intrinsicContentSize];
-[TPRevealingRingView layoutSubviews];
-[TPRevealingRingView setCornerRadius:];
-[TPRevealingRingView cornerRadius];
-[TPRevealingRingView setFrame:];
-[TPRevealingRingView description];
-[TPRevealingRingView initWithFrame:];
-[TPRevealingRingView ringSize];
-[TPRevealingRingView initWithFrame:paddingOutsideRing:];
-[TPRevealingRingView paddingOutsideRing];
-[TPRevealingRingView setAlphaInsideRing:];
-[TPRevealingRingView setAlphaOutsideRing:];
-[TPRevealingRingView setColorInsideRing:];
-[TPRevealingRingView setColorOutsideRing:];
-[TPRevealingRingView setDefaultRingStrokeWidth:];
-[TPRevealingRingView setPaddingOutsideRing:];
-[TPRevealingRingView setRevealAnimationDuration:];
-[TPRevealingRingView setRevealed:animated:];
-[TPRevealingRingView setRevealed:animated:delay:];
-[TPRevealingRingView setUnrevealAnimationDuration:];
-[TPRevealingRingView colorInsideRing];
-[TPRevealingRingView alphaInsideRing];
-[TPRevealingRingView _animateForReveal:withDuration:delay:];
-[TPRevealingRingView _calculateOuter:inner:newXOffset:newYOffset:withScale:];
-[TPRevealingRingView _computeInnerViewDrawingPropertiesWithScale:];
-[TPRevealingRingView _computeOuterViewDrawingPropertiesWithScale:];
-[TPRevealingRingView _evaluateCircularness];
-[TPRevealingRingView _isSquare:];
-[TPRevealingRingView _shouldDrawAsCircle:cornerRadius:];
-[TPRevealingRingView alphaOutsideRing];
-[TPRevealingRingView colorOutsideRing];
-[TPRevealingRingView defaultRingStrokeWidth];
-[TPRevealingRingView revealAnimationDuration];
-[TPRevealingRingView unrevealAnimationDuration];
```
