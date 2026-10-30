# `_UIPointerEffectTintView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffectView`
- Protocols: `_UILumaTrackingBackdropViewDelegate`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _luminance;
@? _tintColorMatrixProvider;
B _disabled;
B _pressed;
```

## Properties

```
@property (TB,N,GisDisabled,V_disabled) disabled;
@property (TB,N,GisPressed,V_pressed) pressed;
```

## Instance methods

```
-[_UIPointerEffectTintView backgroundLumaView:didTransitionToLevel:];
-[_UIPointerEffectTintView isDisabled];
-[_UIPointerEffectTintView isPressed];
-[_UIPointerEffectTintView setDisabled:];
-[_UIPointerEffectTintView setPressed:];
-[_UIPointerEffectTintView _updateAlpha];
-[_UIPointerEffectTintView _updateBackgroundEffects];
-[_UIPointerEffectTintView initWithTintColorMatrixProvider:];
```
