# `MPSGraphOperation`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 11 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"MPSGraph" _graph;
@"NSArray" _inputTensors;
@"NSArray" _outputTensors;
@"NSMutableArray" _controlDependencies;
@"MPSGraphRegion" _region;
@"MPSGraphBlock" _parentBlock;
@"NSString" _name;
^v _mlirOperation;
B _stopGradient;
B _pruneOp;
@"NSMutableDictionary" _tensorNameDict;
```

## Properties

```
@property (TB,N,V_pruneOp) pruneOp;
@property (T@"NSMutableDictionary",&,N,V_tensorNameDict) tensorNameDict;
@property (TB,N,V_stopGradient) stopGradient;
@property (T@"NSArray",R,N,V_inputTensors) inputTensors;
@property (T@"NSArray",R,N,V_outputTensors) outputTensors;
@property (T@"NSArray",R,N) controlDependencies;
@property (T@"MPSGraph",R,W,N,V_graph) graph;
@property (T@"NSString",R,N,V_name) name;
```

## Instance methods

```
-[MPSGraphOperation graph];
-[MPSGraphOperation init];
-[MPSGraphOperation initInternal];
-[MPSGraphOperation controlDependencies];
-[MPSGraphOperation copyWithZone:];
-[MPSGraphOperation name];
-[MPSGraphOperation inputTensors];
-[MPSGraphOperation pruneOp];
-[MPSGraphOperation initWithGraph:inputTensors:controlDependencies:name:];
-[MPSGraphOperation initWithGraph:inputTensors:controlDependencies:region:name:];
-[MPSGraphOperation makeMLIROpWithBuilder:symbolTable:inputValues:opInitialization:name:];
-[MPSGraphOperation outputTensors];
-[MPSGraphOperation partialDerivateForCFOpWithAutodiff:];
-[MPSGraphOperation partialDerivativeForInputTensor:incomingGradient:inputIndex:name:];
-[MPSGraphOperation partialDerivativesForInputTensors:incomingGradients:name:];
-[MPSGraphOperation recurseFromBlock:onEscaped:withAutodiff:];
-[MPSGraphOperation recurseOnBlocksFromOutput:withAutodiff:];
-[MPSGraphOperation recurseOutFromBlockInput:withAutodiff:];
-[MPSGraphOperation setPruneOp:];
-[MPSGraphOperation setStopGradient:];
-[MPSGraphOperation setTensorNameDict:];
-[MPSGraphOperation stopGradient];
-[MPSGraphOperation tensorNameDict];
```
