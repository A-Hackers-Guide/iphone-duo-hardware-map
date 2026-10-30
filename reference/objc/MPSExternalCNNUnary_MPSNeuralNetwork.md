# `MPSExternalCNNUnary`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSExternalPluginBase`
- Protocols: `MPSExternalCNNUnary`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MPSExternalCNNUnary encodeBatchWithFilter:encoder:commandBuffer:callInfo:];
-[MPSExternalCNNUnary encodeToCommandBuffer:computeCommandEncoder:options:pluginOptions:sourceTexture:sourceInfo:destinationTexture:destinationInfo:];
-[MPSExternalCNNUnary encodeToCommandBuffer:computeCommandEncoder:options:sourceTexture:sourceInfo:destinationTexture:destinationInfo:];
-[MPSExternalCNNUnary encodeWithFilter:encoder:commandBuffer:callInfo:];
```
