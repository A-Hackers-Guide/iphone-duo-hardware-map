# `MPSGraphForLoopOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@? _bodyBlock;
@"NSArray" _bodyResult;
@"NSArray" _iterArgs;
@"NSArray" _forBlockArguments;
{unique_ptr<AutodiffOpData, std::default_delete<AutodiffOpData>>=""{?="__ptr_"^{AutodiffOpData}}} _opData;
```

## Instance methods

```
-[MPSGraphForLoopOp initWithGraph:inputTensors:controlDependencies:bodyBlock:iterArgs:name:];
-[MPSGraphForLoopOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphForLoopOp partialDerivateForCFOpWithAutodiff:];
-[MPSGraphForLoopOp recurseFromBlock:onEscaped:withAutodiff:];
-[MPSGraphForLoopOp recurseOnBlocksFromOutput:withAutodiff:];
-[MPSGraphForLoopOp recurseOutFromBlockInput:withAutodiff:];
```
