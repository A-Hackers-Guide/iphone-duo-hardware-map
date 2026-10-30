# `_UIDimmingKnockoutBackdropView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIInterfaceActionVisualBackgroundDisplaying`, `UIInterfaceActionVisualGroupBackgroundDisplaying`
- 6 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"UIView" dimmingKnockoutView;
@"UIVisualEffectView" backdropView;
d _alpha;
d _currentCornerRadius;
d _cornerRadius;
q _style;
```

## Properties

```
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Tq,N,V_style) style;
@property (T@"UIColor",?,&,N) fillColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDimmingKnockoutBackdropView _updateCornerRadius];
-[_UIDimmingKnockoutBackdropView initWithStyle:];
-[_UIDimmingKnockoutBackdropView style];
-[_UIDimmingKnockoutBackdropView setCornerRadius:];
-[_UIDimmingKnockoutBackdropView setBounds:];
-[_UIDimmingKnockoutBackdropView setStyle:];
-[_UIDimmingKnockoutBackdropView setAlpha:];
-[_UIDimmingKnockoutBackdropView setHighlighted:];
-[_UIDimmingKnockoutBackdropView _setContinuousCornerRadius:];
-[_UIDimmingKnockoutBackdropView cornerRadius];
-[_UIDimmingKnockoutBackdropView setRoundedCornerPosition:];
-[_UIDimmingKnockoutBackdropView setPressed:];
-[_UIDimmingKnockoutBackdropView _configureViewsWithStyle:];
-[_UIDimmingKnockoutBackdropView _dimmingKnockoutBackgroundColorForBackdropStyle:];
-[_UIDimmingKnockoutBackdropView _dimmingKnockoutFilterForBackdropStyle:];
-[_UIDimmingKnockoutBackdropView _updateBackdropViewWithStyle:alpha:];
-[_UIDimmingKnockoutBackdropView _vibrancyEffectForStyle:];
-[_UIDimmingKnockoutBackdropView _visualEffectForStyle:];
```
