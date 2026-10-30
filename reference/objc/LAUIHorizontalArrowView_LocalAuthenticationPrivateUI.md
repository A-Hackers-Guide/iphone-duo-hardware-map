# `LAUIHorizontalArrowView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 20 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _color;
B _effective_animating;
S _dismissal_animation_count;
B _animated;
d _resting_height;
@"UIView" _container;
@"UIView" _arrow_container;
@"UIImageView" _head;
@"UIView" _tail_container;
@"UIImageView" _tail;
@"UILabel" _label;
B _pulsing;
{periodic_animation_state="enabled"B"_key"@"NSString""_layer"@"CALayer""_removal_timer"@"NSObject<OS_dispatch_source>"} _head_pulse;
{periodic_animation_state="enabled"B"_key"@"NSString""_layer"@"CALayer""_removal_timer"@"NSObject<OS_dispatch_source>"} _tail_container_pulse;
{periodic_animation_state="enabled"B"_key"@"NSString""_layer"@"CALayer""_removal_timer"@"NSObject<OS_dispatch_source>"} _tail_counter_pulse;
B _animating;
q _direction;
d _displacement;
@"NSString" _text;
{CGSize="width"d"height"d} _maximum_line_size;
```

## Properties

```
@property (TB,N,GisAnimating,V_animating) animating;
@property (Tq,N,V_direction) direction;
@property (Td,N,V_displacement) displacement;
@property (T@"NSString",C,N,V_text) text;
@property (T{CGSize=dd},N,V_maximum_line_size) maximumLineSize;
```

## Instance methods

```
-[LAUIHorizontalArrowView didMoveToWindow];
-[LAUIHorizontalArrowView text];
-[LAUIHorizontalArrowView _updateFont];
-[LAUIHorizontalArrowView dealloc];
-[LAUIHorizontalArrowView setDirection:];
-[LAUIHorizontalArrowView layoutSubviews];
-[LAUIHorizontalArrowView direction];
-[LAUIHorizontalArrowView sizeThatFits:];
-[LAUIHorizontalArrowView tintColorDidChange];
-[LAUIHorizontalArrowView displacement];
-[LAUIHorizontalArrowView contentSizeCategoryDidChange:];
-[LAUIHorizontalArrowView setText:];
-[LAUIHorizontalArrowView isAnimating];
-[LAUIHorizontalArrowView setAnimating:];
-[LAUIHorizontalArrowView initWithFrame:];
-[LAUIHorizontalArrowView setDisplacement:];
-[LAUIHorizontalArrowView maximumLineSize];
-[LAUIHorizontalArrowView _layoutIfNeededAnimated:];
-[LAUIHorizontalArrowView _updateAnimatingAnimated:];
-[LAUIHorizontalArrowView _updateDirectionTransform];
-[LAUIHorizontalArrowView _updateLabelSize];
-[LAUIHorizontalArrowView _updatePulsingWithDelay:];
-[LAUIHorizontalArrowView _updateViewsWithColor];
-[LAUIHorizontalArrowView boldTextStatusDidChange:];
-[LAUIHorizontalArrowView setMaximumLineSize:];
```
