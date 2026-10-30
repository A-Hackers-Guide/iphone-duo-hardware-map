# `_UIStatusBarActivityView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIStatusBarDisplayable`
- 7 instance variables, 16 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _isSlow;
@"UIColor" _color;
@"CALayer" _mainLayer;
@"CAGradientLayer" _barLayer;
@"CALayer" _pointLayer;
d _thickness;
@"_UIStatusBarCycleAnimation" _cycleAnimation;
```

## Properties

```
@property (TB,?,R,N) wantsCrossfade;
@property (TB,?,R,N) prefersBaselineAlignment;
@property (TB,?,R,N) prefersCenterVerticalAlignment;
@property (Tq,?,R,N) overriddenVerticalAlignment;
@property (T@"UIAccessibilityHUDItem",?,R,N) accessibilityHUDRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CALayer",&,N,V_mainLayer) mainLayer;
@property (T@"CAGradientLayer",&,N,V_barLayer) barLayer;
@property (T@"CALayer",&,N,V_pointLayer) pointLayer;
@property (Td,N,V_thickness) thickness;
@property (T@"_UIStatusBarCycleAnimation",&,N,V_cycleAnimation) cycleAnimation;
@property (TB,N,V_isSlow) isSlow;
@property (T@"UIColor",C,N,V_color) color;
```

## Instance methods

```
-[_UIStatusBarActivityView _commonInit];
-[_UIStatusBarActivityView startAnimating];
-[_UIStatusBarActivityView setColor:];
-[_UIStatusBarActivityView applyStyleAttributes:];
-[_UIStatusBarActivityView intrinsicContentSize];
-[_UIStatusBarActivityView cycleAnimation];
-[_UIStatusBarActivityView color];
-[_UIStatusBarActivityView initWithCoder:];
-[_UIStatusBarActivityView traitCollectionDidChange:];
-[_UIStatusBarActivityView thickness];
-[_UIStatusBarActivityView setCycleAnimation:];
-[_UIStatusBarActivityView setThickness:];
-[_UIStatusBarActivityView initWithFrame:];
-[_UIStatusBarActivityView _stopAnimatingWithStoppingAnimations:completionHandler:];
-[_UIStatusBarActivityView _thicknessForTraitCollection:];
-[_UIStatusBarActivityView barLayer];
-[_UIStatusBarActivityView isSlow];
-[_UIStatusBarActivityView mainLayer];
-[_UIStatusBarActivityView pointLayer];
-[_UIStatusBarActivityView setBarLayer:];
-[_UIStatusBarActivityView setIsSlow:];
-[_UIStatusBarActivityView setMainLayer:];
-[_UIStatusBarActivityView setPointLayer:];
-[_UIStatusBarActivityView stopAnimatingWithCompletionHandler:];
```
