# `MTL4DebugCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4ToolsCommandQueue`
- 0 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance methods

```
-[MTL4DebugCommandQueue removeInternalResidencySets:count:];
-[MTL4DebugCommandQueue removeResidencySet:];
-[MTL4DebugCommandQueue removeInternalResidencySet:];
-[MTL4DebugCommandQueue addInternalResidencySet:];
-[MTL4DebugCommandQueue addInternalResidencySets:count:];
-[MTL4DebugCommandQueue addResidencySets:count:];
-[MTL4DebugCommandQueue removeResidencySets:count:];
-[MTL4DebugCommandQueue addResidencySet:];
-[MTL4DebugCommandQueue dealloc];
-[MTL4DebugCommandQueue signalEvent:value:];
-[MTL4DebugCommandQueue waitForEvent:value:];
-[MTL4DebugCommandQueue signalDrawable:];
-[MTL4DebugCommandQueue commit:count:];
-[MTL4DebugCommandQueue commit:count:options:];
-[MTL4DebugCommandQueue copyBufferMappingsFromBuffer:toBuffer:operations:count:];
-[MTL4DebugCommandQueue copyTextureMappingsFromTexture:toTexture:operations:count:];
-[MTL4DebugCommandQueue updateBufferMappings:heap:operations:count:];
-[MTL4DebugCommandQueue updateTextureMappings:heap:operations:count:];
-[MTL4DebugCommandQueue waitForDrawable:];
-[MTL4DebugCommandQueue initWithBaseObject:parent:];
-[MTL4DebugCommandQueue waitForEvent:value:timeout:];
-[MTL4DebugCommandQueue validateBufferAccess:range:resourceSparsePageSize:context:];
-[MTL4DebugCommandQueue validateBufferAccess:region:resourceSparsePageSize:context:];
-[MTL4DebugCommandQueue validateCommitCommon:commandBuffers:count:];
-[MTL4DebugCommandQueue validateHeapAccess:rangeOffset:tileRegions:resourceSparsePageSize:context:];
-[MTL4DebugCommandQueue validateTextureAccess:region:mipLevel:slice:context:];
```
