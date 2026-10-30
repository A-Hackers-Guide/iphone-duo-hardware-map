# `_UIFluidSliderInteractionUpdate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _tracking;
B _atTarget;
d _value;
q _interactionState;
q _type;
d __unclampedValue;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trackBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _barFrame;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _trackTransform;
```

## Properties

```
@property (Td,N,V_value) value;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_trackBounds) trackBounds;
@property (T{CGAffineTransform=dddddd},N,V_trackTransform) trackTransform;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_barFrame) barFrame;
@property (Tq,N,V_interactionState) interactionState;
@property (TB,N,GisTracking,V_tracking) tracking;
@property (Tq,N,V_type) type;
@property (TB,N,GisAtTarget,V_atTarget) atTarget;
@property (Td,N,V__unclampedValue) _unclampedValue;
```

## Instance methods

```
-[_UIFluidSliderInteractionUpdate setInteractionState:];
-[_UIFluidSliderInteractionUpdate trackBounds];
-[_UIFluidSliderInteractionUpdate setTracking:];
-[_UIFluidSliderInteractionUpdate value];
-[_UIFluidSliderInteractionUpdate setAtTarget:];
-[_UIFluidSliderInteractionUpdate set_unclampedValue:];
-[_UIFluidSliderInteractionUpdate isTracking];
-[_UIFluidSliderInteractionUpdate setValue:];
-[_UIFluidSliderInteractionUpdate setType:];
-[_UIFluidSliderInteractionUpdate setTrackBounds:];
-[_UIFluidSliderInteractionUpdate type];
-[_UIFluidSliderInteractionUpdate barFrame];
-[_UIFluidSliderInteractionUpdate trackTransform];
-[_UIFluidSliderInteractionUpdate interactionState];
-[_UIFluidSliderInteractionUpdate _unclampedValue];
-[_UIFluidSliderInteractionUpdate setBarFrame:];
-[_UIFluidSliderInteractionUpdate setTrackTransform:];
-[_UIFluidSliderInteractionUpdate isAtTarget];
```
