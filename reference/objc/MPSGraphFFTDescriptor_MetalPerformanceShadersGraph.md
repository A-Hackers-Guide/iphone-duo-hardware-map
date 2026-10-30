# `MPSGraphFFTDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _inverse;
B _roundToOddHermitean;
Q _scalingMode;
```

## Properties

```
@property (TB,N,V_inverse) inverse;
@property (TQ,N,V_scalingMode) scalingMode;
@property (TB,N,V_roundToOddHermitean) roundToOddHermitean;
```

## Class methods

```
+[MPSGraphFFTDescriptor descriptor];
```

## Instance methods

```
-[MPSGraphFFTDescriptor setScalingMode:];
-[MPSGraphFFTDescriptor scalingMode];
-[MPSGraphFFTDescriptor copyWithZone:];
-[MPSGraphFFTDescriptor inverse];
-[MPSGraphFFTDescriptor setInverse:];
-[MPSGraphFFTDescriptor roundToOddHermitean];
-[MPSGraphFFTDescriptor setRoundToOddHermitean:];
```
