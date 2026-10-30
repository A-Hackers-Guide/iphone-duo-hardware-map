# `MTL4ComputePipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4PipelineDescriptor`
- 10 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _threadGroupSizeIsMultipleOfThreadExecutionWidth;
B _supportBinaryLinking;
B _optimizeForPersistentKernel;
@"MTL4StaticLinkingDescriptor" _staticLinkingDescriptor;
q _supportIndirectCommandBuffers;
@"MTL4FunctionDescriptor" _computeFunctionDescriptor;
Q _maxTotalThreadsPerThreadgroup;
q _forwardProgressUsage;
q _contentionRelief;
{?="width"Q"height"Q"depth"Q} _requiredThreadsPerThreadgroup;
```

## Properties

```
@property (T@"MTL4FunctionDescriptor",C,N,V_computeFunctionDescriptor) computeFunctionDescriptor;
@property (TB,N,V_threadGroupSizeIsMultipleOfThreadExecutionWidth) threadGroupSizeIsMultipleOfThreadExecutionWidth;
@property (TQ,N,V_maxTotalThreadsPerThreadgroup) maxTotalThreadsPerThreadgroup;
@property (T{?=QQQ},N,V_requiredThreadsPerThreadgroup) requiredThreadsPerThreadgroup;
@property (TB,N,V_supportBinaryLinking) supportBinaryLinking;
@property (T@"MTL4StaticLinkingDescriptor",C,N,V_staticLinkingDescriptor) staticLinkingDescriptor;
@property (Tq,N,V_supportIndirectCommandBuffers) supportIndirectCommandBuffers;
@property (Tq,N,V_forwardProgressUsage) forwardProgressUsage;
@property (Tq,N,V_contentionRelief) contentionRelief;
@property (TB,N,V_optimizeForPersistentKernel) optimizeForPersistentKernel;
```

## Instance methods

```
-[MTL4ComputePipelineDescriptor supportIndirectCommandBuffers];
-[MTL4ComputePipelineDescriptor setSupportIndirectCommandBuffers:];
-[MTL4ComputePipelineDescriptor setRequiredThreadsPerThreadgroup:];
-[MTL4ComputePipelineDescriptor staticLinkingDescriptor];
-[MTL4ComputePipelineDescriptor setComputeFunctionDescriptor:];
-[MTL4ComputePipelineDescriptor init];
-[MTL4ComputePipelineDescriptor dealloc];
-[MTL4ComputePipelineDescriptor reset];
-[MTL4ComputePipelineDescriptor setMaxTotalThreadsPerThreadgroup:];
-[MTL4ComputePipelineDescriptor setOptimizeForPersistentKernel:];
-[MTL4ComputePipelineDescriptor requiredThreadsPerThreadgroup];
-[MTL4ComputePipelineDescriptor maxTotalThreadsPerThreadgroup];
-[MTL4ComputePipelineDescriptor setStaticLinkingDescriptor:];
-[MTL4ComputePipelineDescriptor setContentionRelief:];
-[MTL4ComputePipelineDescriptor threadGroupSizeIsMultipleOfThreadExecutionWidth];
-[MTL4ComputePipelineDescriptor setForwardProgressUsage:];
-[MTL4ComputePipelineDescriptor hash];
-[MTL4ComputePipelineDescriptor contentionRelief];
-[MTL4ComputePipelineDescriptor forwardProgressUsage];
-[MTL4ComputePipelineDescriptor setThreadGroupSizeIsMultipleOfThreadExecutionWidth:];
-[MTL4ComputePipelineDescriptor copyWithZone:];
-[MTL4ComputePipelineDescriptor computeFunctionDescriptor];
-[MTL4ComputePipelineDescriptor isEqual:];
-[MTL4ComputePipelineDescriptor optimizeForPersistentKernel];
-[MTL4ComputePipelineDescriptor _staticLinkingDescriptorNoAlloc];
-[MTL4ComputePipelineDescriptor setSupportBinaryLinking:];
-[MTL4ComputePipelineDescriptor supportBinaryLinking];
```
