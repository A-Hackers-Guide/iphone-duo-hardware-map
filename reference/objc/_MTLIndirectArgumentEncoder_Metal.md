# `_MTLIndirectArgumentEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLArgumentEncoder`
- 2 instance variables, 9 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"_MTLIndirectArgumentBufferLayout" _layout;
```

## Properties

```
@property (TQ,R,D) encodedLength;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C,D) label;
@property (T@"_MTLIndirectArgumentBufferLayout",R,N,V_layout) layout;
@property (TQ,R,D) alignment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLIndirectArgumentEncoder setBuffers:offsets:withRange:];
-[_MTLIndirectArgumentEncoder setVisibleFunctionTables:withBufferRange:];
-[_MTLIndirectArgumentEncoder setBuffer:offset:atIndex:];
-[_MTLIndirectArgumentEncoder setIntersectionFunctionTable:atBufferIndex:];
-[_MTLIndirectArgumentEncoder setVisibleFunctionTable:atBufferIndex:];
-[_MTLIndirectArgumentEncoder setTexture:atIndex:];
-[_MTLIndirectArgumentEncoder device];
-[_MTLIndirectArgumentEncoder setSamplerState:atIndex:];
-[_MTLIndirectArgumentEncoder dealloc];
-[_MTLIndirectArgumentEncoder setSamplerStates:withRange:];
-[_MTLIndirectArgumentEncoder setTextures:withRange:];
-[_MTLIndirectArgumentEncoder layout];
-[_MTLIndirectArgumentEncoder setIntersectionFunctionTables:withBufferRange:];
-[_MTLIndirectArgumentEncoder constantDataAtIndex:];
-[_MTLIndirectArgumentEncoder setArgumentBuffer:offset:];
-[_MTLIndirectArgumentEncoder setRenderPipelineState:atIndex:];
-[_MTLIndirectArgumentEncoder initWithLayout:device:];
-[_MTLIndirectArgumentEncoder newArgumentEncoderForBufferAtIndex:];
-[_MTLIndirectArgumentEncoder setAccelerationStructure:atIndex:];
-[_MTLIndirectArgumentEncoder setArgumentBuffer:startOffset:arrayElement:];
-[_MTLIndirectArgumentEncoder setComputePipelineState:atIndex:];
-[_MTLIndirectArgumentEncoder setComputePipelineStates:withRange:];
-[_MTLIndirectArgumentEncoder setDepthStencilState:atIndex:];
-[_MTLIndirectArgumentEncoder setDepthStencilStates:withRange:];
-[_MTLIndirectArgumentEncoder setIndirectArgumentBuffer:offset:];
-[_MTLIndirectArgumentEncoder setIndirectCommandBuffer:atIndex:];
-[_MTLIndirectArgumentEncoder setIndirectCommandBuffers:withRange:];
-[_MTLIndirectArgumentEncoder setIntersectionFunctionTable:atIndex:];
-[_MTLIndirectArgumentEncoder setIntersectionFunctionTables:withRange:];
-[_MTLIndirectArgumentEncoder setRenderPipelineStates:withRange:];
-[_MTLIndirectArgumentEncoder setVisibleFunctionTable:atIndex:];
-[_MTLIndirectArgumentEncoder setVisibleFunctionTables:withRange:];
```
