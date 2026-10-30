# `BiasEstimatorOutputs`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _outProbabilities;
d _rawRange;
d _correctedRange;
```

## Properties

```
@property (T@"NSArray",C,N,V_outProbabilities) outProbabilities;
@property (Td,N,V_rawRange) rawRange;
@property (Td,N,V_correctedRange) correctedRange;
```

## Class methods

```
+[BiasEstimatorOutputs supportsSecureCoding];
```

## Instance methods

```
-[BiasEstimatorOutputs encodeWithCoder:];
-[BiasEstimatorOutputs hash];
-[BiasEstimatorOutputs description];
-[BiasEstimatorOutputs initWithCoder:];
-[BiasEstimatorOutputs copyWithZone:];
-[BiasEstimatorOutputs isEqual:];
-[BiasEstimatorOutputs correctedRange];
-[BiasEstimatorOutputs initWithBiasEstimatorOutputs:];
-[BiasEstimatorOutputs initWithOuputProbabilities:rawRange:correctedRange:];
-[BiasEstimatorOutputs outProbabilities];
-[BiasEstimatorOutputs populateOrderedBiasEstimatorOutputs];
-[BiasEstimatorOutputs rawRange];
-[BiasEstimatorOutputs setCorrectedRange:];
-[BiasEstimatorOutputs setOutProbabilities:];
-[BiasEstimatorOutputs setRawRange:];
```
