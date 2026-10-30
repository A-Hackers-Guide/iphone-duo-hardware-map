# `_UISlideriOSFluidVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISlideriOSVisualElement`
- Protocols: `_UIFluidSliderDirectDrivingDelegate`, `_UISliderFluidStyleVisualElement`
- 6 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"_UIFluidSliderInteraction" _fluidInteraction;
d _thumbPosition;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trackBounds;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _trackTransform;
Q _fluidUpdateSource;
B _changeWithVolumeButtons;
```

## Properties

```
@property (TB,N,V_changeWithVolumeButtons) changeWithVolumeButtons;
@property (TQ,R,N) fluidUpdateSource;
@property (T@"UISlider",W,N) slider;
@property (T@"UISliderDataModel",&,N) data;
@property (T@"NSArray",?,R,N) additionalTrackingViews;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISlideriOSFluidVisualElement cancelTouchTracking];
-[_UISlideriOSFluidVisualElement setValue:animated:];
-[_UISlideriOSFluidVisualElement didSetValues];
-[_UISlideriOSFluidVisualElement didSetEnabled];
-[_UISlideriOSFluidVisualElement endTrackingWithTouch:withEvent:];
-[_UISlideriOSFluidVisualElement continueTrackingWithTouch:withEvent:];
-[_UISlideriOSFluidVisualElement didSetUserInteractionEnabled];
-[_UISlideriOSFluidVisualElement setSlider:];
-[_UISlideriOSFluidVisualElement didSetFluidTrackHidden];
-[_UISlideriOSFluidVisualElement beginTrackingWithTouch:withEvent:];
-[_UISlideriOSFluidVisualElement changeWithVolumeButtons];
-[_UISlideriOSFluidVisualElement setBounds:];
-[_UISlideriOSFluidVisualElement driver:shouldBeginAtPoint:];
-[_UISlideriOSFluidVisualElement didSetSpeedMultiplier];
-[_UISlideriOSFluidVisualElement setFrame:];
-[_UISlideriOSFluidVisualElement setChangeWithVolumeButtons:];
-[_UISlideriOSFluidVisualElement driver:shouldAdjustValueForProposedValue:adjustedValue:startValue:endValue:];
-[_UISlideriOSFluidVisualElement _controlTouchBegan:withEvent:];
-[_UISlideriOSFluidVisualElement fluidUpdateSource];
-[_UISlideriOSFluidVisualElement _controlTouchMoved:withEvent:];
-[_UISlideriOSFluidVisualElement initWithFrame:];
-[_UISlideriOSFluidVisualElement cancelMouseTracking];
-[_UISlideriOSFluidVisualElement _controlTouchEnded:withEvent:];
-[_UISlideriOSFluidVisualElement _modifiedTrackRect:];
-[_UISlideriOSFluidVisualElement _setValue:minimum:maximum:animated:];
-[_UISlideriOSFluidVisualElement _setupFeedback];
-[_UISlideriOSFluidVisualElement _setupInteraction];
-[_UISlideriOSFluidVisualElement _updateConfigurationForFrameChange:];
-[_UISlideriOSFluidVisualElement _updateModelValue:sendAction:];
-[_UISlideriOSFluidVisualElement _updatedConfigurationForTrackSize:];
```
