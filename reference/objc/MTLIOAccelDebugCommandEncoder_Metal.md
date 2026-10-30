# `MTLIOAccelDebugCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDebugCommandEncoder`
- 4 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
^v _kernelCommandBufferCurrent;
^v _kernelCommandBufferEnd;
^{IOAccelResourceList=[256S]^{IOAccelSegmentResourceDescriptorGroup}QQIIIIIII^?^v} _resourceList;
@"MTLResourceList" _api_resourceList;
```

## Instance methods

```
-[MTLIOAccelDebugCommandEncoder endEncoding];
-[MTLIOAccelDebugCommandEncoder dealloc];
-[MTLIOAccelDebugCommandEncoder kprintfBytes:length:];
-[MTLIOAccelDebugCommandEncoder IOLogResource:length:];
-[MTLIOAccelDebugCommandEncoder addAPIResource:];
-[MTLIOAccelDebugCommandEncoder IOLogBytes:length:];
-[MTLIOAccelDebugCommandEncoder addDebugResourceListInfo:flag:];
-[MTLIOAccelDebugCommandEncoder debugBytes:length:output_type:];
-[MTLIOAccelDebugCommandEncoder debugResourceBytes:length:output_type:];
-[MTLIOAccelDebugCommandEncoder initWithCommandBuffer:];
-[MTLIOAccelDebugCommandEncoder kprintfResource:length:];
-[MTLIOAccelDebugCommandEncoder reserveKernelCommandBufferSpace:];
-[MTLIOAccelDebugCommandEncoder restartDebugPass];
```
