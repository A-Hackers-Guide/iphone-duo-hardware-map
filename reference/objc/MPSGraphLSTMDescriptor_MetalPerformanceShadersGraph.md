# `MPSGraphLSTMDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 15 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _hasMask;
B _hasInitState;
B _hasInitCell;
B _hasPeephole;
B _hasCellGradient;
B _reverse;
B _training;
B _bidirectional;
B _produceCell;
B _forgetGateLast;
Q _activation;
Q _inputGateActivation;
Q _forgetGateActivation;
Q _cellGateActivation;
Q _outputGateActivation;
```

## Properties

```
@property (TB,N,V_reverse) reverse;
@property (TB,N,V_bidirectional) bidirectional;
@property (TB,N,V_produceCell) produceCell;
@property (TB,N,V_training) training;
@property (TB,N,V_forgetGateLast) forgetGateLast;
@property (TQ,N,V_inputGateActivation) inputGateActivation;
@property (TQ,N,V_forgetGateActivation) forgetGateActivation;
@property (TQ,N,V_cellGateActivation) cellGateActivation;
@property (TQ,N,V_outputGateActivation) outputGateActivation;
@property (TQ,N,V_activation) activation;
```

## Class methods

```
+[MPSGraphLSTMDescriptor descriptor];
```

## Instance methods

```
-[MPSGraphLSTMDescriptor reverse];
-[MPSGraphLSTMDescriptor training];
-[MPSGraphLSTMDescriptor setTraining:];
-[MPSGraphLSTMDescriptor copyWithZone:];
-[MPSGraphLSTMDescriptor setReverse:];
-[MPSGraphLSTMDescriptor bidirectional];
-[MPSGraphLSTMDescriptor activation];
-[MPSGraphLSTMDescriptor setActivation:];
-[MPSGraphLSTMDescriptor cellGateActivation];
-[MPSGraphLSTMDescriptor forgetGateActivation];
-[MPSGraphLSTMDescriptor inputGateActivation];
-[MPSGraphLSTMDescriptor outputGateActivation];
-[MPSGraphLSTMDescriptor setCellGateActivation:];
-[MPSGraphLSTMDescriptor setForgetGateActivation:];
-[MPSGraphLSTMDescriptor setInputGateActivation:];
-[MPSGraphLSTMDescriptor setOutputGateActivation:];
-[MPSGraphLSTMDescriptor setProduceCell:];
-[MPSGraphLSTMDescriptor setBidirectional:];
-[MPSGraphLSTMDescriptor setForgetGateLast:];
-[MPSGraphLSTMDescriptor forgetGateLast];
-[MPSGraphLSTMDescriptor produceCell];
```
