# `CBJNDBasedContrastIndicatorPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBContrastIndicatorPolicy`
- 3 instance variables, 6 properties, 7 instance methods, 4 class methods

## Instance variables

```
{CBJNDBasedContrastIndicatorPolicyConfiguration="sdrParams"{CBJNDFormulaParams="luxFactor"f"nitsFactor"f"constant"f}"hdrParams"{CBJNDFormulaParams="luxFactor"f"nitsFactor"f"constant"f}"indicatorLuminanceFactor"f} _configuration;
B _boostingEnabled;
f _maxBoostBrightness;
```

## Properties

```
@property (TB,V_boostingEnabled) boostingEnabled;
@property (Tf,V_maxBoostBrightness) maxBoostBrightness;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBJNDBasedContrastIndicatorPolicy calculateContrastIndicatorForDisplayBrightness:andLux:usingFormulaParams:];
+[CBJNDBasedContrastIndicatorPolicy createConfigurationFromConfigurationProvider:withFallback:];
+[CBJNDBasedContrastIndicatorPolicy defaultRingConfiguration];
+[CBJNDBasedContrastIndicatorPolicy defaultSoftBoundaryConfiguration];
```

## Instance methods

```
-[CBJNDBasedContrastIndicatorPolicy description];
-[CBJNDBasedContrastIndicatorPolicy boostingEnabled];
-[CBJNDBasedContrastIndicatorPolicy calculateContrastIndicatorNitsForDisplayBrightness:isInHDR:andLux:];
-[CBJNDBasedContrastIndicatorPolicy initWithConfiguration:andMaxBoostBrightness:];
-[CBJNDBasedContrastIndicatorPolicy maxBoostBrightness];
-[CBJNDBasedContrastIndicatorPolicy setBoostingEnabled:];
-[CBJNDBasedContrastIndicatorPolicy setMaxBoostBrightness:];
```
