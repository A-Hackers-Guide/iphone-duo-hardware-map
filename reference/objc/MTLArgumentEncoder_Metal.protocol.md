# `MTLArgumentEncoder` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 28 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) encodedLength;
@property (TQ,R) alignment;
```

## Instance methods

```
-[MTLArgumentEncoder setBuffers:offsets:withRange:];
-[MTLArgumentEncoder setBuffer:offset:atIndex:];
-[MTLArgumentEncoder setTexture:atIndex:];
-[MTLArgumentEncoder device];
-[MTLArgumentEncoder setSamplerState:atIndex:];
-[MTLArgumentEncoder label];
-[MTLArgumentEncoder setLabel:];
-[MTLArgumentEncoder alignment];
-[MTLArgumentEncoder setSamplerStates:withRange:];
-[MTLArgumentEncoder setTextures:withRange:];
-[MTLArgumentEncoder constantDataAtIndex:];
-[MTLArgumentEncoder encodedLength];
-[MTLArgumentEncoder setArgumentBuffer:offset:];
-[MTLArgumentEncoder setRenderPipelineState:atIndex:];
-[MTLArgumentEncoder newArgumentEncoderForBufferAtIndex:];
-[MTLArgumentEncoder setAccelerationStructure:atIndex:];
-[MTLArgumentEncoder setArgumentBuffer:startOffset:arrayElement:];
-[MTLArgumentEncoder setComputePipelineState:atIndex:];
-[MTLArgumentEncoder setComputePipelineStates:withRange:];
-[MTLArgumentEncoder setDepthStencilState:atIndex:];
-[MTLArgumentEncoder setDepthStencilStates:withRange:];
-[MTLArgumentEncoder setIndirectCommandBuffer:atIndex:];
-[MTLArgumentEncoder setIndirectCommandBuffers:withRange:];
-[MTLArgumentEncoder setIntersectionFunctionTable:atIndex:];
-[MTLArgumentEncoder setIntersectionFunctionTables:withRange:];
-[MTLArgumentEncoder setRenderPipelineStates:withRange:];
-[MTLArgumentEncoder setVisibleFunctionTable:atIndex:];
-[MTLArgumentEncoder setVisibleFunctionTables:withRange:];
```
