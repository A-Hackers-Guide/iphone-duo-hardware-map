# `MPSGraphBufferToTensorOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _shape;
@"NSArray" _interleave;
I _type;
B _isTensorBufferOp;
B _isChannelAndInterleaveSame;
```

## Instance methods

```
-[MPSGraphBufferToTensorOp initWithGraph:inputTensors:controlDependencies:shape:type:interleave:isTensorBufferOp:isChannelAndInterleaveSame:name:];
-[MPSGraphBufferToTensorOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphBufferToTensorOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
