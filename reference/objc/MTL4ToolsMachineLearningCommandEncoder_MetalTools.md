# `MTL4ToolsMachineLearningCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandEncoder`
- Protocols: `MTL4MachineLearningCommandEncoderGGDSPI`
- 1 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTL4ArgumentTable>" _currentArgumentTable;
```

## Properties

```
@property (T@"<MTL4ArgumentTable>",R,N,V_currentArgumentTable) currentArgumentTable;
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
```

## Instance methods

```
-[MTL4ToolsMachineLearningCommandEncoder endEncoding];
-[MTL4ToolsMachineLearningCommandEncoder dealloc];
-[MTL4ToolsMachineLearningCommandEncoder setPipelineState:];
-[MTL4ToolsMachineLearningCommandEncoder setArgumentTable:];
-[MTL4ToolsMachineLearningCommandEncoder startEventValue];
-[MTL4ToolsMachineLearningCommandEncoder currentArgumentTable];
-[MTL4ToolsMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:];
-[MTL4ToolsMachineLearningCommandEncoder endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:];
-[MTL4ToolsMachineLearningCommandEncoder endEventValue];
-[MTL4ToolsMachineLearningCommandEncoder initWithBaseObject:parent:];
-[MTL4ToolsMachineLearningCommandEncoder releaseArgumentTable];
```
