# `MPSGraphCallOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _outputTypes;
@"NSString" _symbolName;
Q _inliningOption;
```

## Instance methods

```
-[MPSGraphCallOp initWithGraph:inputTensors:controlDependencies:outputTypes:symbolName:inliningOption:name:];
-[MPSGraphCallOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphCallOp partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
```
