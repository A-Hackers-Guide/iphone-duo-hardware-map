# `MPSExternalCNNBinary`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSExternalPluginBase`
- Protocols: `MPSExternalCNNBinary`
- 0 instance variables, 4 properties, 3 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MPSExternalCNNBinary encodeBatchWithFilter:encoder:commandBuffer:callInfo:];
-[MPSExternalCNNBinary encodeToCommandBuffer:computeCommandEncoder:options:primaryTexture:primaryInfo:secondaryTexture:secondaryInfo:destinationTexture:destinationInfo:];
-[MPSExternalCNNBinary encodeWithFilter:encoder:commandBuffer:callInfo:];
```
