# `_UIFluidSliderInteractionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _customDrivers;
d _stretchAmount;
d _velocityMultiplier;
Q _stepCount;
Q _preferredInputMethods;
d _neutralPosition;
d _minValue;
d _maxValue;
{CGSize="width"d"height"d} _trackSize;
```

## Properties

```
@property (T@"NSArray",&,N,S_setCustomDrivers:,V_customDrivers) _customDrivers;
@property (T{CGSize=dd},R,N,V_trackSize) trackSize;
@property (Td,N,V_stretchAmount) stretchAmount;
@property (Td,N,V_velocityMultiplier) velocityMultiplier;
@property (TQ,N,V_stepCount) stepCount;
@property (TQ,N,V_preferredInputMethods) preferredInputMethods;
@property (Td,N,V_neutralPosition) neutralPosition;
@property (Td,N,V_minValue) minValue;
@property (Td,N,V_maxValue) maxValue;
```

## Class methods

```
+[_UIFluidSliderInteractionConfiguration configurationWithTrackSize:];
```

## Instance methods

```
-[_UIFluidSliderInteractionConfiguration minValue];
-[_UIFluidSliderInteractionConfiguration _setCustomDrivers:];
-[_UIFluidSliderInteractionConfiguration maxValue];
-[_UIFluidSliderInteractionConfiguration stretchAmount];
-[_UIFluidSliderInteractionConfiguration velocityMultiplier];
-[_UIFluidSliderInteractionConfiguration setPreferredInputMethods:];
-[_UIFluidSliderInteractionConfiguration setStretchAmount:];
-[_UIFluidSliderInteractionConfiguration stepCount];
-[_UIFluidSliderInteractionConfiguration init];
-[_UIFluidSliderInteractionConfiguration copyWithTrackSize:];
-[_UIFluidSliderInteractionConfiguration setStepCount:];
-[_UIFluidSliderInteractionConfiguration trackSize];
-[_UIFluidSliderInteractionConfiguration copyWithVelocityMultiplier:];
-[_UIFluidSliderInteractionConfiguration _customDrivers];
-[_UIFluidSliderInteractionConfiguration preferredInputMethods];
-[_UIFluidSliderInteractionConfiguration description];
-[_UIFluidSliderInteractionConfiguration setMaxValue:];
-[_UIFluidSliderInteractionConfiguration setVelocityMultiplier:];
-[_UIFluidSliderInteractionConfiguration neutralPosition];
-[_UIFluidSliderInteractionConfiguration setNeutralPosition:];
-[_UIFluidSliderInteractionConfiguration copyWithZone:];
-[_UIFluidSliderInteractionConfiguration setMinValue:];
```
