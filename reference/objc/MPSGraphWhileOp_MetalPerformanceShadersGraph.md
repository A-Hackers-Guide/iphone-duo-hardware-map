# `MPSGraphWhileOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 10 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@? _beforeBlock;
@? _afterBlock;
@"NSArray" _initInputTensors;
@"NSArray" _beforeResult;
@"NSArray" _afterResult;
@"NSArray" _beforeBlockArguments;
@"NSArray" _afterBlockArguments;
@"MPSGraphTensor" _predicateTensor;
@"MPSGraphTensor" _itersCountTensor;
{unique_ptr<AutodiffOpData, std::default_delete<AutodiffOpData>>=""{?="__ptr_"^{AutodiffOpData}}} _opData;
```

## Instance methods

```
-[MPSGraphWhileOp initWithGraph:inputTensors:controlDependencies:beforeBlock:afterBlock:name:];
-[MPSGraphWhileOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphWhileOp partialDerivateForCFOpWithAutodiff:];
-[MPSGraphWhileOp recurseFromBlock:onEscaped:withAutodiff:];
-[MPSGraphWhileOp recurseOnBlocksFromOutput:withAutodiff:];
-[MPSGraphWhileOp recurseOutFromBlockInput:withAutodiff:];
```
