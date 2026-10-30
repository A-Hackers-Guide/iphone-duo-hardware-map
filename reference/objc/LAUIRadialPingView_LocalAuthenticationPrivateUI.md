# `LAUIRadialPingView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 1 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _color;
@"UIView" _container;
@"UIView" _primary;
{array<(anonymous namespace)::blur_container, 2UL>="__elems_"[2{blur_container="view"@"UIImageView""pulse"{periodic_animation_state="enabled"B"_key"@"NSString""_layer"@"CALayer""_removal_timer"@"NSObject<OS_dispatch_source>"}}]} _blurs;
{periodic_animation_state="enabled"B"_key"@"NSString""_layer"@"CALayer""_removal_timer"@"NSObject<OS_dispatch_source>"} _pulse;
B _animating_dirty;
C _animating_counter;
B _animating;
```

## Properties

```
@property (TB,N,GisAnimating,V_animating) animating;
```

## Instance methods

```
-[LAUIRadialPingView didMoveToWindow];
-[LAUIRadialPingView dealloc];
-[LAUIRadialPingView layoutSubviews];
-[LAUIRadialPingView tintColorDidChange];
-[LAUIRadialPingView isAnimating];
-[LAUIRadialPingView setAnimating:];
-[LAUIRadialPingView initWithFrame:];
-[LAUIRadialPingView _attachPulseAnimationWithDelay:];
-[LAUIRadialPingView _attachExpandAnimationToContainer:withDelay:];
-[LAUIRadialPingView _endExpand];
-[LAUIRadialPingView _setExpand:forBlurAtIndex:withDelay:];
-[LAUIRadialPingView _setPulse:withDelay:];
-[LAUIRadialPingView _startExpandWithDelay:];
-[LAUIRadialPingView _updateAnimatingAnimated:];
-[LAUIRadialPingView _updateExpandForBlurAtIndex:withDelay:];
-[LAUIRadialPingView _updateViewsWithColor];
```
