# `MTLToolsArgumentEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLArgumentEncoderSPI`
- 0 instance variables, 9 properties, 33 instance methods, 0 class methods

## Properties

```
@property (T@"_MTLIndirectArgumentBufferLayout",R,N) layout;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) encodedLength;
@property (TQ,R) alignment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsArgumentEncoder setBuffers:offsets:withRange:];
-[MTLToolsArgumentEncoder setVisibleFunctionTables:withBufferRange:];
-[MTLToolsArgumentEncoder setBuffer:offset:atIndex:];
-[MTLToolsArgumentEncoder setIntersectionFunctionTable:atBufferIndex:];
-[MTLToolsArgumentEncoder setVisibleFunctionTable:atBufferIndex:];
-[MTLToolsArgumentEncoder setTexture:atIndex:];
-[MTLToolsArgumentEncoder device];
-[MTLToolsArgumentEncoder setSamplerState:atIndex:];
-[MTLToolsArgumentEncoder label];
-[MTLToolsArgumentEncoder setLabel:];
-[MTLToolsArgumentEncoder alignment];
-[MTLToolsArgumentEncoder setSamplerStates:withRange:];
-[MTLToolsArgumentEncoder setTextures:withRange:];
-[MTLToolsArgumentEncoder layout];
-[MTLToolsArgumentEncoder setIntersectionFunctionTables:withBufferRange:];
-[MTLToolsArgumentEncoder constantDataAtIndex:];
-[MTLToolsArgumentEncoder encodedLength];
-[MTLToolsArgumentEncoder setArgumentBuffer:offset:];
-[MTLToolsArgumentEncoder setRenderPipelineState:atIndex:];
-[MTLToolsArgumentEncoder newArgumentEncoderForBufferAtIndex:];
-[MTLToolsArgumentEncoder setAccelerationStructure:atIndex:];
-[MTLToolsArgumentEncoder setArgumentBuffer:startOffset:arrayElement:];
-[MTLToolsArgumentEncoder setComputePipelineState:atIndex:];
-[MTLToolsArgumentEncoder setComputePipelineStates:withRange:];
-[MTLToolsArgumentEncoder setDepthStencilState:atIndex:];
-[MTLToolsArgumentEncoder setDepthStencilStates:withRange:];
-[MTLToolsArgumentEncoder setIndirectCommandBuffer:atIndex:];
-[MTLToolsArgumentEncoder setIndirectCommandBuffers:withRange:];
-[MTLToolsArgumentEncoder setIntersectionFunctionTable:atIndex:];
-[MTLToolsArgumentEncoder setIntersectionFunctionTables:withRange:];
-[MTLToolsArgumentEncoder setRenderPipelineStates:withRange:];
-[MTLToolsArgumentEncoder setVisibleFunctionTable:atIndex:];
-[MTLToolsArgumentEncoder setVisibleFunctionTables:withRange:];
```
