# `_UIAlertControllerTVBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIInterfaceActionVisualBackgroundDisplaying`, `UIInterfaceActionVisualGroupBackgroundDisplaying`
- 7 instance variables, 11 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _alphas;
B _shouldUseTintColorAsBackgroundColor;
B _isHighlighted;
B _isPressed;
B _shouldShowShadow;
@"_UIFloatingShadowView" _shadowView;
@"UIView" _backgroundView;
```

## Properties

```
@property (T@"_UIFloatingShadowView",&,N,V_shadowView) shadowView;
@property (TB,N,V_isHighlighted) isHighlighted;
@property (TB,N,V_isPressed) isPressed;
@property (T@"UIView",&,N,V_backgroundView) backgroundView;
@property (TB,N,V_shouldShowShadow) shouldShowShadow;
@property (TB,N,V_shouldUseTintColorAsBackgroundColor) shouldUseTintColorAsBackgroundColor;
@property (T@"UIColor",?,&,N) fillColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIAlertControllerTVBackgroundView backgroundInsetAmount];
+[_UIAlertControllerTVBackgroundView usesHighlightShadow];
```

## Instance methods

```
-[_UIAlertControllerTVBackgroundView _shadowRadius];
-[_UIAlertControllerTVBackgroundView _shadowOpacity];
-[_UIAlertControllerTVBackgroundView isHighlighted];
-[_UIAlertControllerTVBackgroundView layoutSubviews];
-[_UIAlertControllerTVBackgroundView setCornerRadius:];
-[_UIAlertControllerTVBackgroundView setIsHighlighted:];
-[_UIAlertControllerTVBackgroundView tintColorDidChange];
-[_UIAlertControllerTVBackgroundView setHighlighted:];
-[_UIAlertControllerTVBackgroundView _setContinuousCornerRadius:];
-[_UIAlertControllerTVBackgroundView shadowView];
-[_UIAlertControllerTVBackgroundView isPressed];
-[_UIAlertControllerTVBackgroundView backgroundView];
-[_UIAlertControllerTVBackgroundView setShadowView:];
-[_UIAlertControllerTVBackgroundView _updateBackgroundColor];
-[_UIAlertControllerTVBackgroundView initWithFrame:];
-[_UIAlertControllerTVBackgroundView setBackgroundView:];
-[_UIAlertControllerTVBackgroundView setRoundedCornerPosition:];
-[_UIAlertControllerTVBackgroundView setPressed:];
-[_UIAlertControllerTVBackgroundView _alphaForHighlighted:pressed:];
-[_UIAlertControllerTVBackgroundView _displayedBackgroundColor];
-[_UIAlertControllerTVBackgroundView _shadowOffset];
-[_UIAlertControllerTVBackgroundView alphaForState:];
-[_UIAlertControllerTVBackgroundView setAlpha:forState:];
-[_UIAlertControllerTVBackgroundView setIsPressed:];
-[_UIAlertControllerTVBackgroundView setShouldShowShadow:];
-[_UIAlertControllerTVBackgroundView setShouldUseTintColorAsBackgroundColor:];
-[_UIAlertControllerTVBackgroundView shouldShowShadow];
-[_UIAlertControllerTVBackgroundView shouldUseTintColorAsBackgroundColor];
```
