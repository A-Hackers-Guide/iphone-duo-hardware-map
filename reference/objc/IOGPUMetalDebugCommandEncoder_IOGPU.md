# `IOGPUMetalDebugCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDebugCommandEncoder`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _kernelCommandBufferCurrent;
^v _kernelCommandBufferEnd;
^{IOGPUResourceList=[114I]^I^Q^(?)IIIIIIII^{IOGPUSegmentResourceDescriptorGroup}QQIIIIIII^?^v} _resourceList;
@"MTLResourceList" _api_resourceList;
```

## Instance methods

```
-[IOGPUMetalDebugCommandEncoder endEncoding];
-[IOGPUMetalDebugCommandEncoder dealloc];
-[IOGPUMetalDebugCommandEncoder kprintfBytes:length:];
-[IOGPUMetalDebugCommandEncoder addAPIResource:];
-[IOGPUMetalDebugCommandEncoder IOLogBytes:length:];
-[IOGPUMetalDebugCommandEncoder addDebugResourceListInfo:flag:];
-[IOGPUMetalDebugCommandEncoder debugBytes:length:output_type:];
-[IOGPUMetalDebugCommandEncoder initWithCommandBuffer:];
-[IOGPUMetalDebugCommandEncoder reserveKernelCommandBufferSpace:];
-[IOGPUMetalDebugCommandEncoder restartDebugPass];
```
