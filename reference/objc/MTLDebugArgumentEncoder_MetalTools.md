# `MTLDebugArgumentEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsArgumentEncoder`
- 3 instance variables, 0 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<MTLBuffer>" _currentBuffer;
Q _currentOffset;
^v _reflectionParser;
```

## Instance methods

```
-[MTLDebugArgumentEncoder setBuffers:offsets:withRange:];
-[MTLDebugArgumentEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLDebugArgumentEncoder setBuffer:offset:atIndex:];
-[MTLDebugArgumentEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLDebugArgumentEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLDebugArgumentEncoder setTexture:atIndex:];
-[MTLDebugArgumentEncoder setSamplerState:atIndex:];
-[MTLDebugArgumentEncoder dealloc];
-[MTLDebugArgumentEncoder setSamplerStates:withRange:];
-[MTLDebugArgumentEncoder setTextures:withRange:];
-[MTLDebugArgumentEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLDebugArgumentEncoder constantDataAtIndex:];
-[MTLDebugArgumentEncoder setArgumentBuffer:offset:];
-[MTLDebugArgumentEncoder setRenderPipelineState:atIndex:];
-[MTLDebugArgumentEncoder newArgumentEncoderForBufferAtIndex:];
-[MTLDebugArgumentEncoder setAccelerationStructure:atIndex:];
-[MTLDebugArgumentEncoder setArgumentBuffer:startOffset:arrayElement:];
-[MTLDebugArgumentEncoder setComputePipelineState:atIndex:];
-[MTLDebugArgumentEncoder setComputePipelineStates:withRange:];
-[MTLDebugArgumentEncoder setDepthStencilState:atIndex:];
-[MTLDebugArgumentEncoder setDepthStencilStates:withRange:];
-[MTLDebugArgumentEncoder setIndirectCommandBuffer:atIndex:];
-[MTLDebugArgumentEncoder setIndirectCommandBuffers:withRange:];
-[MTLDebugArgumentEncoder setIntersectionFunctionTable:atIndex:];
-[MTLDebugArgumentEncoder setIntersectionFunctionTables:withRange:];
-[MTLDebugArgumentEncoder setRenderPipelineStates:withRange:];
-[MTLDebugArgumentEncoder setVisibleFunctionTable:atIndex:];
-[MTLDebugArgumentEncoder setVisibleFunctionTables:withRange:];
-[MTLDebugArgumentEncoder initWithBaseObject:structType:parent:];
-[MTLDebugArgumentEncoder setArgumentBuffer:startOffset:elementIndex:];
```
