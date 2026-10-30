# `MTL4ComputeCommandEncoderSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4ComputeCommandEncoder`, `MTL4CommandEncoderSPI`
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[MTL4ComputeCommandEncoderSPI fillTexture:level:slice:region:color:];
-[MTL4ComputeCommandEncoderSPI fillBuffer:range:pattern4:];
-[MTL4ComputeCommandEncoderSPI fillTexture:level:slice:region:bytes:length:];
-[MTL4ComputeCommandEncoderSPI fillTexture:level:slice:region:color:pixelFormat:];
-[MTL4ComputeCommandEncoderSPI deserializeInstanceAccelerationStructure:referencedAccelerationStructures:fromBuffer:];
-[MTL4ComputeCommandEncoderSPI deserializePrimitiveAccelerationStructure:fromBuffer:];
-[MTL4ComputeCommandEncoderSPI serializeInstanceAccelerationStructure:referencedAccelerationStructures:toBuffer:];
-[MTL4ComputeCommandEncoderSPI serializePrimitiveAccelerationStructure:toBuffer:];
-[MTL4ComputeCommandEncoderSPI setToolsDispatchBufferSPI:atIndex:];
-[MTL4ComputeCommandEncoderSPI writeAccelerationStructureSerializationData:toBuffer:];
-[MTL4ComputeCommandEncoderSPI writeAccelerationStructureTraversalDepth:toBuffer:];
-[MTL4ComputeCommandEncoderSPI writeDeserializedAccelerationStructureSize:toBuffer:];
-[MTL4ComputeCommandEncoderSPI writeGenericBVHStructureOfAccelerationStructure:into:];
-[MTL4ComputeCommandEncoderSPI writeGenericBVHStructureSizesOfAccelerationStructure:into:];
-[MTL4ComputeCommandEncoderSPI writeGenericBVHStructureSizesOfAccelerationStructure:toBuffer:];
-[MTL4ComputeCommandEncoderSPI writeSerializedAccelerationStructureSize:toBuffer:];
```
