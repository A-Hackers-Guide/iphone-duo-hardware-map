# `CASDFGeneratorRequest`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _includeGradient;
q _outputBitDepth;
d _padding;
d _maximumDistance;
d _gradientSmoothing;
d _zeroValueDistance;
d _oneValueDistance;
```

## Properties

```
@property (Tq,N,V_outputBitDepth) outputBitDepth;
@property (Td,N,V_padding) padding;
@property (Td,N,V_maximumDistance) maximumDistance;
@property (TB,N,V_includeGradient) includeGradient;
@property (Td,N,V_gradientSmoothing) gradientSmoothing;
@property (Td,N,V_zeroValueDistance) zeroValueDistance;
@property (Td,N,V_oneValueDistance) oneValueDistance;
```

## Class methods

```
+[CASDFGeneratorRequest request];
+[CASDFGeneratorRequest requestForEffect:];
+[CASDFGeneratorRequest requestForEffects:];
```

## Instance methods

```
-[CASDFGeneratorRequest padding];
-[CASDFGeneratorRequest init];
-[CASDFGeneratorRequest setPadding:];
-[CASDFGeneratorRequest includeGradient];
-[CASDFGeneratorRequest maximumDistance];
-[CASDFGeneratorRequest _resetConfiguration];
-[CASDFGeneratorRequest _unionConfigurationForEffect:];
-[CASDFGeneratorRequest gradientSmoothing];
-[CASDFGeneratorRequest oneValueDistance];
-[CASDFGeneratorRequest outputBitDepth];
-[CASDFGeneratorRequest setGradientSmoothing:];
-[CASDFGeneratorRequest setIncludeGradient:];
-[CASDFGeneratorRequest setMaximumDistance:];
-[CASDFGeneratorRequest setOneValueDistance:];
-[CASDFGeneratorRequest setOutputBitDepth:];
-[CASDFGeneratorRequest setZeroValueDistance:];
-[CASDFGeneratorRequest zeroValueDistance];
```
