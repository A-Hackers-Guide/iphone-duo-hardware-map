# `_UIFluidSliderSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 9 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"_UISpringAnimationPrototypeSettings" _programmaticUpdate;
@"_UISpringAnimationPrototypeSettings" _pressScale;
d _sliderDriftFactor;
d _sliderStepCount;
d _defaultStretchAmount;
d _squishFactor;
d _minSquishPoints;
@"_UIFluidSliderElasticPanDriverSettings" _elasticPanDriverSettings;
@"_UIFluidSliderDiscreteButtonDriverSettings" _discreteButtonDriverSettings;
```

## Properties

```
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_programmaticUpdate) programmaticUpdate;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_pressScale) pressScale;
@property (Td,N,V_sliderDriftFactor) sliderDriftFactor;
@property (Td,N,V_sliderStepCount) sliderStepCount;
@property (Td,N,V_defaultStretchAmount) defaultStretchAmount;
@property (Td,N,V_squishFactor) squishFactor;
@property (Td,N,V_minSquishPoints) minSquishPoints;
@property (T@"_UIFluidSliderElasticPanDriverSettings",&,N,V_elasticPanDriverSettings) elasticPanDriverSettings;
@property (T@"_UIFluidSliderDiscreteButtonDriverSettings",&,N,V_discreteButtonDriverSettings) discreteButtonDriverSettings;
```

## Class methods

```
+[_UIFluidSliderSettings settingsControllerModule];
```

## Instance methods

```
-[_UIFluidSliderSettings setSquishFactor:];
-[_UIFluidSliderSettings elasticPanDriverSettings];
-[_UIFluidSliderSettings setPressScale:];
-[_UIFluidSliderSettings setElasticPanDriverSettings:];
-[_UIFluidSliderSettings minSquishPoints];
-[_UIFluidSliderSettings pressScale];
-[_UIFluidSliderSettings programmaticUpdate];
-[_UIFluidSliderSettings setSliderStepCount:];
-[_UIFluidSliderSettings squishFactor];
-[_UIFluidSliderSettings setDefaultValues];
-[_UIFluidSliderSettings setSliderDriftFactor:];
-[_UIFluidSliderSettings sliderDriftFactor];
-[_UIFluidSliderSettings setDefaultStretchAmount:];
-[_UIFluidSliderSettings setMinSquishPoints:];
-[_UIFluidSliderSettings setProgrammaticUpdate:];
-[_UIFluidSliderSettings setDiscreteButtonDriverSettings:];
-[_UIFluidSliderSettings discreteButtonDriverSettings];
-[_UIFluidSliderSettings defaultStretchAmount];
-[_UIFluidSliderSettings sliderStepCount];
```
