# `MTLCountersDevice`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsDevice`
- 1 instance variables, 1 properties, 69 instance methods, 0 class methods

## Instance variables

```
B _APITimingEnabled;
```

## Properties

```
@property (TB,R,N,V_APITimingEnabled) APITimingEnabled;
```

## Instance methods

```
-[MTLCountersDevice newDynamicLibrary:computeDescriptor:error:];
-[MTLCountersDevice newRenderPipelineStateWithTileDescriptor:options:completionHandler:];
-[MTLCountersDevice newLibraryWithFile:error:];
-[MTLCountersDevice setWritableHeapsEnabled:];
-[MTLCountersDevice newDynamicLibraryFromURL:error:];
-[MTLCountersDevice newFunctionWithGLCoreIR:inputsDescription:functionType:];
-[MTLCountersDevice newFunctionWithGLESIR:functionType:];
-[MTLCountersDevice newFunctionWithGLESIR:inputsDescription:functionType:];
-[MTLCountersDevice newComputePipelineStateWithFunction:completionHandler:];
-[MTLCountersDevice newRenderPipelineStateWithDescriptor:options:completionHandler:];
-[MTLCountersDevice newLibraryWithDescriptor:completionHandler:];
-[MTLCountersDevice newCommandQueueWithDescriptor:];
-[MTLCountersDevice newLibraryWithStitchedDescriptor:error:];
-[MTLCountersDevice newComputePipelineStateWithFunction:options:completionHandler:];
-[MTLCountersDevice newLibraryWithSource:options:completionHandler:];
-[MTLCountersDevice newRenderPipelineStateWithDescriptor:completionHandler:];
-[MTLCountersDevice newLibraryWithURL:error:];
-[MTLCountersDevice newFunctionWithGLIR:inputsDescription:functionType:];
-[MTLCountersDevice newDynamicLibrary:error:];
-[MTLCountersDevice newDefaultLibraryWithBundle:error:];
-[MTLCountersDevice areWritableHeapsEnabled];
-[MTLCountersDevice newComputePipelineStateWithImageFilterFunctionsSPI:imageFilterFunctionInfo:error:];
-[MTLCountersDevice newLibraryWithStitchedDescriptorSPI:error:];
-[MTLCountersDevice newDagStringWithGraphs:];
-[MTLCountersDevice newComputePipelineStateWithDescriptor:completionHandler:];
-[MTLCountersDevice newComputePipelineStateWithDescriptor:options:completionHandler:];
-[MTLCountersDevice newLibraryWithData:error:];
-[MTLCountersDevice newComputePipelineStateWithDescriptor:error:];
-[MTLCountersDevice newComputePipelineStateWithFunction:options:reflection:error:];
-[MTLCountersDevice newLibraryWithStitchedDescriptor:completionHandler:];
-[MTLCountersDevice newFunctionWithGLIR:functionType:];
-[MTLCountersDevice newCommandQueueWithMaxCommandBufferCount:];
-[MTLCountersDevice newLibraryWithDAG:functions:error:];
-[MTLCountersDevice newLibraryWithImageFilterFunctionsSPI:imageFilterFunctionInfo:error:];
-[MTLCountersDevice newLibraryWithDescriptor:error:];
-[MTLCountersDevice newDefaultLibrary];
-[MTLCountersDevice newFunctionWithGLCoreIR:functionType:];
-[MTLCountersDevice newLibraryWithSource:options:error:];
-[MTLCountersDevice newDynamicLibraryWithURL:error:];
-[MTLCountersDevice newRenderPipelineStateWithDescriptor:options:reflection:error:];
-[MTLCountersDevice newRenderPipelineStateWithDescriptor:error:];
-[MTLCountersDevice newLibraryWithDescriptorSPI:error:];
-[MTLCountersDevice newComputePipelineStateWithFunction:error:];
-[MTLCountersDevice newComputePipelineStateWithDescriptor:options:reflection:error:];
-[MTLCountersDevice newCommandQueue];
-[MTLCountersDevice newBufferWithDescriptor:];
-[MTLCountersDevice dealloc];
-[MTLCountersDevice newTextureWithDescriptor:];
-[MTLCountersDevice newFence];
-[MTLCountersDevice newRenderPipelineStateWithTileDescriptor:options:reflection:error:];
-[MTLCountersDevice newLibraryWithCIFilters:imageFilterFunctionInfo:error:];
-[MTLCountersDevice newBufferWithBytesNoCopy:length:options:deallocator:];
-[MTLCountersDevice newBufferWithLength:options:];
-[MTLCountersDevice newDepthStencilStateWithDescriptor:];
-[MTLCountersDevice newHeapWithDescriptor:];
-[MTLCountersDevice newSamplerStateWithDescriptor:];
-[MTLCountersDevice newTextureWithBytesNoCopy:length:descriptor:deallocator:];
-[MTLCountersDevice newTextureWithDescriptor:iosurface:plane:];
-[MTLCountersDevice newBufferWithBytes:length:options:];
-[MTLCountersDevice newBufferWithIOSurface:];
-[MTLCountersDevice newLibraryWithCIFiltersForComputePipeline:imageFilterFunctionInfo:error:];
-[MTLCountersDevice newLibraryWithGraphs:functions:error:];
-[MTLCountersDevice newLibraryWithGraphsSPI:functions:error:];
-[MTLCountersDevice newRenderPipelineStateWithTileDescriptor:completionHandler:];
-[MTLCountersDevice newRenderPipelineStateWithTileDescriptor:error:];
-[MTLCountersDevice initWithBaseObject:parent:];
-[MTLCountersDevice APITimingEnabled];
-[MTLCountersDevice _newRenderPipelineStateWithTileDescriptor:options:completionHandler:];
-[MTLCountersDevice _newRenderPipelineStateWithTileDescriptor:options:reflection:error:];
```
