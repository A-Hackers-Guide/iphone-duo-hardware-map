# `_UIFluidSliderDiscreteVolumeButtonDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFluidSliderDiscreteButtonDriver`
- Protocols: `_UIPhysicalButtonInteractionDelegate`, `_UIFluidSliderVolumeButtonDriving`
- 2 instance variables, 13 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"_UIPhysicalButtonInteraction" _physicalButtonInteraction;
Q __pressedButton;
```

## Properties

```
@property (TQ,N,V__pressedButton) _pressedButton;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UIPhysicalButtonInteraction",R,N,V_physicalButtonInteraction) physicalButtonInteraction;
@property (T@"<_UIFluidSliderDrivable>",W,N) drivable;
@property (T@"UIView",W,N) view;
@property (TB,N) enabled;
@property (TQ,N) trackAxis;
@property (Td,N) stretchAmount;
@property (Td,N) velocityMultiplier;
@property (T@"NSString",R,N) name;
```

## Instance methods

```
-[_UIFluidSliderDiscreteVolumeButtonDriver setView:];
-[_UIFluidSliderDiscreteVolumeButtonDriver setEnabled:];
-[_UIFluidSliderDiscreteVolumeButtonDriver cancel];
-[_UIFluidSliderDiscreteVolumeButtonDriver name];
-[_UIFluidSliderDiscreteVolumeButtonDriver _physicalButtonInteraction:handleAction:withActiveActions:];
-[_UIFluidSliderDiscreteVolumeButtonDriver _beginWithButton:];
-[_UIFluidSliderDiscreteVolumeButtonDriver _end];
-[_UIFluidSliderDiscreteVolumeButtonDriver _pressedButton];
-[_UIFluidSliderDiscreteVolumeButtonDriver physicalButtonInteraction];
-[_UIFluidSliderDiscreteVolumeButtonDriver set_pressedButton:];
```
