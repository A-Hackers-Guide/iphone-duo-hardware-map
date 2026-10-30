# `UIStatusBarBackgroundView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIStatusBarStyleAttributes" _style;
@"UIImageView" _glowView;
B _glowEnabled;
B _suppressGlow;
```

## Instance methods

```
-[UIStatusBarBackgroundView style];
-[UIStatusBarBackgroundView _backgroundImageName];
-[UIStatusBarBackgroundView _baseImage];
-[UIStatusBarBackgroundView _glowImage];
-[UIStatusBarBackgroundView _setGlowAnimationEnabled:waitForNextCycle:];
-[UIStatusBarBackgroundView _startGlowAnimationWaitForNextCycle:];
-[UIStatusBarBackgroundView _stopGlowAnimation];
-[UIStatusBarBackgroundView _styleCanGlow];
-[UIStatusBarBackgroundView initWithFrame:style:backgroundColor:];
-[UIStatusBarBackgroundView setGlowAnimationEnabled:];
-[UIStatusBarBackgroundView setSuppressesGlow:];
```
