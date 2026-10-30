# `_UICubicPolyTangent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISettingsKeyObserver`
- 8 instance variables, 13 properties, 28 instance methods, 1 class methods

## Instance variables

```
d _initialLinearGain;
d _parabolicGain;
d _cubicGain;
d _quarticGain;
d _tangentLineSpeed;
d _tangentSqrtSpeed;
d _tangentCbrtSpeed;
d _tangentHyperCbrtSpeed;
```

## Properties

```
@property (Td,N,V_initialLinearGain) initialLinearGain;
@property (Td,N,V_parabolicGain) parabolicGain;
@property (Td,N,V_cubicGain) cubicGain;
@property (Td,N,V_quarticGain) quarticGain;
@property (Td,N,V_tangentLineSpeed) tangentLineSpeed;
@property (Td,N,V_tangentSqrtSpeed) tangentSqrtSpeed;
@property (Td,N,V_tangentCbrtSpeed) tangentCbrtSpeed;
@property (Td,N,V_tangentHyperCbrtSpeed) tangentHyperCbrtSpeed;
@property (TB,R,N) isEmpty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UICubicPolyTangent keyboardTrackpadCurve];
```

## Instance methods

```
-[_UICubicPolyTangent init];
-[_UICubicPolyTangent settings:changedValueForKey:];
-[_UICubicPolyTangent isEmpty];
-[_UICubicPolyTangent RootPowerOfEarliestTangent:];
-[_UICubicPolyTangent piecewiseCubicAcceleratedSpeed:];
-[_UICubicPolyTangent setQuarticGain:];
-[_UICubicPolyTangent clipForIOFixedMath:polynomialPower:tangencyStartingAt:];
-[_UICubicPolyTangent clipGainsForIOFixedMathWithTangency];
-[_UICubicPolyTangent cubicGain];
-[_UICubicPolyTangent gainForPower:];
-[_UICubicPolyTangent initialLinearGain];
-[_UICubicPolyTangent parabolicGain];
-[_UICubicPolyTangent quarticDerivative:];
-[_UICubicPolyTangent quarticFunction:];
-[_UICubicPolyTangent quarticGain];
-[_UICubicPolyTangent quarticTangentFunction:powerOfEarliestTangent:];
-[_UICubicPolyTangent setCubicGain:];
-[_UICubicPolyTangent setInitialLinearGain:];
-[_UICubicPolyTangent setParabolicGain:];
-[_UICubicPolyTangent setTangentCbrtSpeed:];
-[_UICubicPolyTangent setTangentHyperCbrtSpeed:];
-[_UICubicPolyTangent setTangentLineSpeed:];
-[_UICubicPolyTangent setTangentSqrtSpeed:];
-[_UICubicPolyTangent tangentCbrtSpeed];
-[_UICubicPolyTangent tangentHyperCbrtSpeed];
-[_UICubicPolyTangent tangentLineSpeed];
-[_UICubicPolyTangent tangentSpeedForPower:];
-[_UICubicPolyTangent tangentSqrtSpeed];
```
