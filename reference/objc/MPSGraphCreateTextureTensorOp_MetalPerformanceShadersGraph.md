# `MPSGraphCreateTextureTensorOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
B _compressed;
Q _mtlPixelFormat;
```

## Properties

```
@property (TQ,R,N,V_mtlPixelFormat) mtlPixelFormat;
@property (TB,R,N,V_compressed) compressed;
```

## Instance methods

```
-[MPSGraphCreateTextureTensorOp compressed];
-[MPSGraphCreateTextureTensorOp mtlPixelFormat];
-[MPSGraphCreateTextureTensorOp initWithGraph:inputTensors:controlDependencies:pixelFormat:isCompressed:name:];
-[MPSGraphCreateTextureTensorOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
```
