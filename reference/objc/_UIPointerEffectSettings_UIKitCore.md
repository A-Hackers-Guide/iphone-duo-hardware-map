# `_UIPointerEffectSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 17 instance variables, 17 properties, 35 instance methods, 2 class methods

## Instance variables

```
d _defaultPointerCornerRadius;
d _overrideSlipPoints;
d _slipFactorX;
d _slipFactorY;
d _parallaxAmount;
d _maxSlipPoints;
d _scaleUpPoints;
d _scaleUpAnimationResponse;
d _scaleUpAnimationDampingRatio;
d _dampedAnimationResponse;
d _dampedAnimationDampingRatio;
d _liftForceFloor;
d _liftForceExponent;
@"_UISpringAnimationPrototypeSettings" _liftProgress;
d _plasmaLensParallaxFactor;
d _plasmaParallaxFactor;
{CGPoint="x"d"y"d} _plasmaRubberbandFactor;
```

## Properties

```
@property (Td,N,V_defaultPointerCornerRadius) defaultPointerCornerRadius;
@property (Td,N,V_overrideSlipPoints) overrideSlipPoints;
@property (Td,N,V_slipFactorX) slipFactorX;
@property (Td,N,V_slipFactorY) slipFactorY;
@property (Td,N,V_parallaxAmount) parallaxAmount;
@property (Td,N,V_maxSlipPoints) maxSlipPoints;
@property (Td,N,V_scaleUpPoints) scaleUpPoints;
@property (Td,N,V_scaleUpAnimationResponse) scaleUpAnimationResponse;
@property (Td,N,V_scaleUpAnimationDampingRatio) scaleUpAnimationDampingRatio;
@property (Td,N,V_dampedAnimationResponse) dampedAnimationResponse;
@property (Td,N,V_dampedAnimationDampingRatio) dampedAnimationDampingRatio;
@property (Td,N,V_liftForceFloor) liftForceFloor;
@property (Td,N,V_liftForceExponent) liftForceExponent;
@property (T@"_UISpringAnimationPrototypeSettings",&,N,V_liftProgress) liftProgress;
@property (T{CGPoint=dd},N,V_plasmaRubberbandFactor) plasmaRubberbandFactor;
@property (Td,N,V_plasmaLensParallaxFactor) plasmaLensParallaxFactor;
@property (Td,N,V_plasmaParallaxFactor) plasmaParallaxFactor;
```

## Class methods

```
+[_UIPointerEffectSettings settingsControllerModule];
+[_UIPointerEffectSettings pointerSlipMatchesContentSlip];
```

## Instance methods

```
-[_UIPointerEffectSettings parallaxAmount];
-[_UIPointerEffectSettings liftProgress];
-[_UIPointerEffectSettings setDefaultValues];
-[_UIPointerEffectSettings setLiftProgress:];
-[_UIPointerEffectSettings setSlipFactorX:];
-[_UIPointerEffectSettings setDampedAnimationDampingRatio:];
-[_UIPointerEffectSettings setSlipFactorY:];
-[_UIPointerEffectSettings dampedAnimationDampingRatio];
-[_UIPointerEffectSettings dampedAnimationResponse];
-[_UIPointerEffectSettings defaultPointerCornerRadius];
-[_UIPointerEffectSettings liftForceExponent];
-[_UIPointerEffectSettings liftForceFloor];
-[_UIPointerEffectSettings maxSlipPoints];
-[_UIPointerEffectSettings overrideSlipPoints];
-[_UIPointerEffectSettings plasmaLensParallaxFactor];
-[_UIPointerEffectSettings plasmaParallaxFactor];
-[_UIPointerEffectSettings plasmaRubberbandFactor];
-[_UIPointerEffectSettings scaleUpAnimationDampingRatio];
-[_UIPointerEffectSettings scaleUpAnimationResponse];
-[_UIPointerEffectSettings scaleUpPoints];
-[_UIPointerEffectSettings setDampedAnimationResponse:];
-[_UIPointerEffectSettings setDefaultPointerCornerRadius:];
-[_UIPointerEffectSettings setLiftForceExponent:];
-[_UIPointerEffectSettings setLiftForceFloor:];
-[_UIPointerEffectSettings setMaxSlipPoints:];
-[_UIPointerEffectSettings setOverrideSlipPoints:];
-[_UIPointerEffectSettings setParallaxAmount:];
-[_UIPointerEffectSettings setPlasmaLensParallaxFactor:];
-[_UIPointerEffectSettings setPlasmaParallaxFactor:];
-[_UIPointerEffectSettings setPlasmaRubberbandFactor:];
-[_UIPointerEffectSettings setScaleUpAnimationDampingRatio:];
-[_UIPointerEffectSettings setScaleUpAnimationResponse:];
-[_UIPointerEffectSettings setScaleUpPoints:];
-[_UIPointerEffectSettings slipFactorX];
-[_UIPointerEffectSettings slipFactorY];
```
