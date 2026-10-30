# `MPSGraphSingleGateRNNDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 6 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _hasMask;
B _hasInitState;
B _reverse;
B _training;
B _bidirectional;
Q _activation;
```

## Properties

```
@property (TB,N,V_reverse) reverse;
@property (TB,N,V_bidirectional) bidirectional;
@property (TB,N,V_training) training;
@property (TQ,N,V_activation) activation;
```

## Class methods

```
+[MPSGraphSingleGateRNNDescriptor descriptor];
```

## Instance methods

```
-[MPSGraphSingleGateRNNDescriptor reverse];
-[MPSGraphSingleGateRNNDescriptor training];
-[MPSGraphSingleGateRNNDescriptor setTraining:];
-[MPSGraphSingleGateRNNDescriptor copyWithZone:];
-[MPSGraphSingleGateRNNDescriptor setReverse:];
-[MPSGraphSingleGateRNNDescriptor bidirectional];
-[MPSGraphSingleGateRNNDescriptor activation];
-[MPSGraphSingleGateRNNDescriptor setActivation:];
-[MPSGraphSingleGateRNNDescriptor setBidirectional:];
```
