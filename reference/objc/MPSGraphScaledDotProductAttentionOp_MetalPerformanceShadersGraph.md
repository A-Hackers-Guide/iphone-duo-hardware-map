# `MPSGraphScaledDotProductAttentionOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _hasSinks;
B _hasCausalMask;
```

## Properties

```
@property (TB,N,V_hasSinks) hasSinks;
@property (TB,N,V_hasCausalMask) hasCausalMask;
```

## Instance methods

```
-[MPSGraphScaledDotProductAttentionOp hasSinks];
-[MPSGraphScaledDotProductAttentionOp setHasSinks:];
-[MPSGraphScaledDotProductAttentionOp hasCausalMask];
-[MPSGraphScaledDotProductAttentionOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphScaledDotProductAttentionOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
-[MPSGraphScaledDotProductAttentionOp setHasCausalMask:];
```
