# `MTL4ToolsMachineLearningPipelineState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4MachineLearningPipelineStateGGDSPI`
- 1 instance variables, 9 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _needsReflectionProperty;
```

## Properties

```
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"MTL4MachineLearningPipelineReflection",R) reflection;
@property (TQ,R) intermediatesHeapSize;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsMachineLearningPipelineState label];
-[MTL4ToolsMachineLearningPipelineState allocatedSize];
-[MTL4ToolsMachineLearningPipelineState reflection];
-[MTL4ToolsMachineLearningPipelineState initWithBaseObject:parent:];
-[MTL4ToolsMachineLearningPipelineState intermediatesHeapSize];
-[MTL4ToolsMachineLearningPipelineState optimizedBytecode];
-[MTL4ToolsMachineLearningPipelineState resourceBlobForByteCodeSignature:resourceName:error:];
-[MTL4ToolsMachineLearningPipelineState runWithInputsArray:resultsArray:intermediateOperations:];
-[MTL4ToolsMachineLearningPipelineState initWithBaseObject:parent:needsReflectionProperty:];
```
