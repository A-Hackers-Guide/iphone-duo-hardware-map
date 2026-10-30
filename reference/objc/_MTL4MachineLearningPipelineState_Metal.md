# `_MTL4MachineLearningPipelineState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLAllocation`
- Protocols: `MTL4MachineLearningPipelineStateGGDSPI`
- 9 instance variables, 14 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"MTL4MachineLearningPipelineReflection" _reflection;
q _deviceSelection;
Q _allocatedSize;
@"<MTLDevice>" _device;
Q _intermediatesHeapSize;
@"<MPSGraphExecutableProxy>" _executable;
@"NSArray" _inputShapes;
@"NSArray" _outputShapes;
@"NSString" _functionName;
```

## Properties

```
@property (TQ,N) allocatedSize;
@property (T@"MTL4MachineLearningPipelineReflection",R,V_reflection) reflection;
@property (TQ,R,V_intermediatesHeapSize) intermediatesHeapSize;
@property (Tq,V_deviceSelection) deviceSelection;
@property (T@"<MPSGraphExecutableProxy>",R,V_executable) executable;
@property (T@"NSArray",&,V_inputShapes) inputShapes;
@property (T@"NSArray",&,V_outputShapes) outputShapes;
@property (T@"NSString",R,V_functionName) functionName;
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4MachineLearningPipelineState functionName];
-[_MTL4MachineLearningPipelineState device];
-[_MTL4MachineLearningPipelineState allocatedSize];
-[_MTL4MachineLearningPipelineState dealloc];
-[_MTL4MachineLearningPipelineState executable];
-[_MTL4MachineLearningPipelineState reflection];
-[_MTL4MachineLearningPipelineState inputShapes];
-[_MTL4MachineLearningPipelineState outputShapes];
-[_MTL4MachineLearningPipelineState deviceSelection];
-[_MTL4MachineLearningPipelineState setInputShapes:];
-[_MTL4MachineLearningPipelineState initWithDevice:descriptor:executable:functionName:deviceSelection:];
-[_MTL4MachineLearningPipelineState intermediatesHeapSize];
-[_MTL4MachineLearningPipelineState optimizedBytecode];
-[_MTL4MachineLearningPipelineState resourceBlobForByteCodeSignature:resourceName:error:];
-[_MTL4MachineLearningPipelineState runWithInputsArray:resultsArray:intermediateOperations:];
-[_MTL4MachineLearningPipelineState setAllocatedSize:];
-[_MTL4MachineLearningPipelineState setDeviceSelection:];
-[_MTL4MachineLearningPipelineState setOutputShapes:];
-[_MTL4MachineLearningPipelineState setReflection:];
```
