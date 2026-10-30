# `MPSGraphGRUDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 12 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _hasMask;
B _hasInitState;
B _hasBias2;
B _reverse;
B _training;
B _bidirectional;
B _resetAfter;
B _resetGateFirst;
B _flipZ;
Q _resetGateActivation;
Q _updateGateActivation;
Q _outputGateActivation;
```

## Properties

```
@property (TB,N,V_reverse) reverse;
@property (TB,N,V_bidirectional) bidirectional;
@property (TB,N,V_training) training;
@property (TB,N,V_resetGateFirst) resetGateFirst;
@property (TB,N,V_resetAfter) resetAfter;
@property (TB,N,V_flipZ) flipZ;
@property (TQ,N,V_updateGateActivation) updateGateActivation;
@property (TQ,N,V_resetGateActivation) resetGateActivation;
@property (TQ,N,V_outputGateActivation) outputGateActivation;
```

## Class methods

```
+[MPSGraphGRUDescriptor descriptor];
```

## Instance methods

```
-[MPSGraphGRUDescriptor reverse];
-[MPSGraphGRUDescriptor training];
-[MPSGraphGRUDescriptor setTraining:];
-[MPSGraphGRUDescriptor copyWithZone:];
-[MPSGraphGRUDescriptor setReverse:];
-[MPSGraphGRUDescriptor bidirectional];
-[MPSGraphGRUDescriptor outputGateActivation];
-[MPSGraphGRUDescriptor setOutputGateActivation:];
-[MPSGraphGRUDescriptor setBidirectional:];
-[MPSGraphGRUDescriptor flipZ];
-[MPSGraphGRUDescriptor resetAfter];
-[MPSGraphGRUDescriptor resetGateActivation];
-[MPSGraphGRUDescriptor resetGateFirst];
-[MPSGraphGRUDescriptor setFlipZ:];
-[MPSGraphGRUDescriptor setResetAfter:];
-[MPSGraphGRUDescriptor setResetGateActivation:];
-[MPSGraphGRUDescriptor setResetGateFirst:];
-[MPSGraphGRUDescriptor setUpdateGateActivation:];
-[MPSGraphGRUDescriptor updateGateActivation];
```
