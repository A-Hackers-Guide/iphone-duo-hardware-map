# `MLOptimizationHints`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
q _reshapeFrequency;
q _specializationStrategy;
d _hotHandDuration;
```

## Properties

```
@property (Td,N,V_hotHandDuration) hotHandDuration;
@property (Tq,N,V_reshapeFrequency) reshapeFrequency;
@property (Tq,N,V_specializationStrategy) specializationStrategy;
```

## Class methods

```
+[MLOptimizationHints supportsSecureCoding];
```

## Instance methods

```
-[MLOptimizationHints setReshapeFrequency:];
-[MLOptimizationHints specializationStrategy];
-[MLOptimizationHints init];
-[MLOptimizationHints setSpecializationStrategy:];
-[MLOptimizationHints reshapeFrequency];
-[MLOptimizationHints setHotHandDuration:];
-[MLOptimizationHints encodeWithCoder:];
-[MLOptimizationHints hash];
-[MLOptimizationHints hotHandDuration];
-[MLOptimizationHints description];
-[MLOptimizationHints initWithCoder:];
-[MLOptimizationHints copyWithZone:];
-[MLOptimizationHints specializationStrategyToString:];
-[MLOptimizationHints reshapeFrequencyToString:];
-[MLOptimizationHints isEqual:];
```
