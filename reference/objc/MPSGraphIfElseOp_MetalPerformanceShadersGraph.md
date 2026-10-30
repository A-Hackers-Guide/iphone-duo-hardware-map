# `MPSGraphIfElseOp`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphOperation`
- 5 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@? _trueBlock;
@? _falseBlock;
@"NSArray" _falseResults;
@"NSArray" _trueResults;
{unique_ptr<AutodiffOpData, std::default_delete<AutodiffOpData>>=""{?="__ptr_"^{AutodiffOpData}}} _opData;
```

## Instance methods

```
-[MPSGraphIfElseOp initWithGraph:inputTensors:controlDependencies:trueBlock:falseBlock:name:];
-[MPSGraphIfElseOp makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphIfElseOp partialDerivateForCFOpWithAutodiff:];
-[MPSGraphIfElseOp recurseFromBlock:onEscaped:withAutodiff:];
-[MPSGraphIfElseOp recurseOnBlocksFromOutput:withAutodiff:];
```
