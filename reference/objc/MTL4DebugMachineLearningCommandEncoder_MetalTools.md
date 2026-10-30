# `MTL4DebugMachineLearningCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsMachineLearningCommandEncoder`
- 3 instance variables, 1 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MTL4DebugCommandEncoder" _debugCommandEncoder;
@"MTL4ToolsMachineLearningPipelineState" _currentPipelineState;
@"<MTL4MachineLearningPipelineState>" _mlPipelineState;
```

## Properties

```
@property (T@"<MTL4MachineLearningPipelineState>",R,N,V_mlPipelineState) mlPipelineState;
```

## Instance methods

```
-[MTL4DebugMachineLearningCommandEncoder endEncoding];
-[MTL4DebugMachineLearningCommandEncoder dealloc];
-[MTL4DebugMachineLearningCommandEncoder commandBuffer];
-[MTL4DebugMachineLearningCommandEncoder setPipelineState:];
-[MTL4DebugMachineLearningCommandEncoder setArgumentTable:];
-[MTL4DebugMachineLearningCommandEncoder updateFence:afterEncoderStages:];
-[MTL4DebugMachineLearningCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4DebugMachineLearningCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4DebugMachineLearningCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4DebugMachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:];
-[MTL4DebugMachineLearningCommandEncoder waitForFence:beforeEncoderStages:];
-[MTL4DebugMachineLearningCommandEncoder mlPipelineState];
-[MTL4DebugMachineLearningCommandEncoder initWithMLCommandEncoder:commandBuffer:];
```
