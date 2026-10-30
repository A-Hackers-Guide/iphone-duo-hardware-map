# `AGXG19FamilyIndirectArgumentEncoder`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalIndirectArgumentEncoder`
- Protocols: `MTLArgumentEncoder`
- 1 instance variables, 8 properties, 31 instance methods, 0 class methods

## Instance variables

```
{IndirectArgumentEncoder="device"@"AGXG19FamilyDevice""layout"^{IndirectArgumentLayout}"arguments"*"current_argument_buffer"@"AGXG19FamilyBuffer"} _impl;
```

## Properties

```
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
-[AGXG19FamilyIndirectArgumentEncoder setBuffers:offsets:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyIndirectArgumentEncoder setBuffer:offset:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setIntersectionFunctionTable:atBufferIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setFunctionTable:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setTexture:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setSamplerState:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setFunctionTables:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder alignment];
-[AGXG19FamilyIndirectArgumentEncoder setSamplerStates:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setTextures:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setIntersectionFunctionTables:withBufferRange:];
-[AGXG19FamilyIndirectArgumentEncoder constantDataAtIndex:];
-[AGXG19FamilyIndirectArgumentEncoder encodedLength];
-[AGXG19FamilyIndirectArgumentEncoder setArgumentBuffer:offset:];
-[AGXG19FamilyIndirectArgumentEncoder setRenderPipelineState:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder initWithLayout:device:];
-[AGXG19FamilyIndirectArgumentEncoder newArgumentEncoderForBufferAtIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setAccelerationStructure:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setComputePipelineState:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setComputePipelineStates:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setDepthStencilState:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setDepthStencilStates:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setIndirectCommandBuffer:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setIndirectCommandBuffers:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setIntersectionFunctionTable:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setIntersectionFunctionTables:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setRenderPipelineStates:withRange:];
-[AGXG19FamilyIndirectArgumentEncoder setVisibleFunctionTable:atIndex:];
-[AGXG19FamilyIndirectArgumentEncoder setVisibleFunctionTables:withRange:];
```
