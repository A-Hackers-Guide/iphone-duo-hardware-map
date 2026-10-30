# `MPSGraphColToImOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 2 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"MPSGraphImToColOpDescriptor" _colToImDesc;
@"NSArray" _shape;
```

## Instance methods

```
-[MPSGraphColToImOp initWithGraph:inputTensors:controlDependencies:descriptor:outputShape:name:];
-[MPSGraphColToImOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
```
