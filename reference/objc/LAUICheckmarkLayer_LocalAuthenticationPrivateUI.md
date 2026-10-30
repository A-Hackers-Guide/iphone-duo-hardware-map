# `LAUICheckmarkLayer`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 11 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _shape_layer;
{vector<CAShapeLayer *, std::allocator<CAShapeLayer *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _transient_shape_layers;
B _animating;
I _animation_index;
d _line_width;
d _effective_line_width;
{vector<LAUI_CA_utilities::animation_completion_handler_container, std::allocator<LAUI_CA_utilities::animation_completion_handler_container>>="__begin_"^{animation_completion_handler_container}"__end_"^{animation_completion_handler_container}""{?="__cap_"^{animation_completion_handler_container}}} _completions;
B _revealed;
@"UIColor" _primary_color;
d _line_width_scale;
^{CGColor=} _color;
```

## Properties

```
@property (Td,N,V_line_width_scale) lineWidthScale;
@property (T@"UIColor",R,C,N,V_primary_color) primaryColor;
@property (T^{CGColor=},R,N,V_color) color;
@property (TB,R,N,GisRevealed,V_revealed) revealed;
@property (T{CGSize=dd},R,N) aspectSize;
```

## Instance methods

```
-[LAUICheckmarkLayer init];
-[LAUICheckmarkLayer dealloc];
-[LAUICheckmarkLayer color];
-[LAUICheckmarkLayer layoutSublayers];
-[LAUICheckmarkLayer primaryColor];
-[LAUICheckmarkLayer setRevealed:animated:];
-[LAUICheckmarkLayer aspectSize];
-[LAUICheckmarkLayer setColor:animated:];
-[LAUICheckmarkLayer setLineWidthScale:];
-[LAUICheckmarkLayer isRevealed];
-[LAUICheckmarkLayer setPrimaryColor:animated:];
-[LAUICheckmarkLayer setRevealed:animated:withCompletion:];
-[LAUICheckmarkLayer _animationsDidResolve];
-[LAUICheckmarkLayer _executeCompletions:];
-[LAUICheckmarkLayer _updateRevealedAnimated:];
-[LAUICheckmarkLayer defaultSizeForCircleWithDiameter:scale:];
-[LAUICheckmarkLayer lineWidthScale];
```
