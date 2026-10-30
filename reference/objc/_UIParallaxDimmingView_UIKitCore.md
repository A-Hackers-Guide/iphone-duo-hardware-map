# `_UIParallaxDimmingView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" leftEdgeFade;
d _backgroundDimmingAmount;
@"UIColor" _dimmingColor;
@"UIView" _addingSubview;
```

## Properties

```
@property (Td,N,V_backgroundDimmingAmount) backgroundDimmingAmount;
@property (T@"UIColor",&,N,V_dimmingColor) dimmingColor;
@property (T@"UIView",&,N,V_addingSubview) addingSubview;
@property (Td,R,N) presentationDimmingAmount;
```

## Instance methods

```
-[_UIParallaxDimmingView dimmingColor];
-[_UIParallaxDimmingView didMoveToWindow];
-[_UIParallaxDimmingView _basicAnimationWithKeyPath:];
-[_UIParallaxDimmingView backgroundDimmingAmount];
-[_UIParallaxDimmingView addingSubview];
-[_UIParallaxDimmingView setAddingSubview:];
-[_UIParallaxDimmingView crossFade];
-[_UIParallaxDimmingView _updateLeftEdgeFade:];
-[_UIParallaxDimmingView setDimmingColor:];
-[_UIParallaxDimmingView setBackgroundDimmingAmount:];
-[_UIParallaxDimmingView initViewWrappingView:withLeftBorder:shouldReverseLayoutDirection:];
-[_UIParallaxDimmingView initWithFrame:];
-[_UIParallaxDimmingView presentationDimmingAmount];
-[_UIParallaxDimmingView initWithFrame:overrideDimmingColor:];
-[_UIParallaxDimmingView defaultBorderColor];
```
