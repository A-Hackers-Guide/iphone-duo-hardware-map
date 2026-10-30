# `MTL4ComputeCommandEncoderGGDSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4ComputeCommandEncoderSPI`, `MTL4CommandEncoderGGDSPI`
- 0 instance variables, 1 properties, 26 instance methods, 0 class methods

## Properties

```
@property (T@"<MTL4ArgumentTable>",R,N) currentArgumentTable;
```

## Instance methods

```
-[MTL4ComputeCommandEncoderGGDSPI encodeStartElse];
-[MTL4ComputeCommandEncoderGGDSPI setThreadgroupDistributionMode:];
-[MTL4ComputeCommandEncoderGGDSPI signalProgress:];
-[MTL4ComputeCommandEncoderGGDSPI beginVirtualSubstream];
-[MTL4ComputeCommandEncoderGGDSPI copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTL4ComputeCommandEncoderGGDSPI currentArgumentTable];
-[MTL4ComputeCommandEncoderGGDSPI enableNullBufferBinds:];
-[MTL4ComputeCommandEncoderGGDSPI encodeEndDoWhile:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI encodeEndIf];
-[MTL4ComputeCommandEncoderGGDSPI encodeEndWhile];
-[MTL4ComputeCommandEncoderGGDSPI encodeStartDoWhile];
-[MTL4ComputeCommandEncoderGGDSPI encodeStartIf:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI encodeStartIf:offset:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI encodeStartWhile:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI encodeStartWhile:offset:comparison:referenceValue:];
-[MTL4ComputeCommandEncoderGGDSPI endVirtualSubstream];
-[MTL4ComputeCommandEncoderGGDSPI flushCompressionMetadata];
-[MTL4ComputeCommandEncoderGGDSPI insertCompressedTextureReinterpretationFlush];
-[MTL4ComputeCommandEncoderGGDSPI invalidateCompressedTexture:];
-[MTL4ComputeCommandEncoderGGDSPI invalidateCompressedTexture:slice:level:];
-[MTL4ComputeCommandEncoderGGDSPI nextVirtualSubstream];
-[MTL4ComputeCommandEncoderGGDSPI setSubstream:];
-[MTL4ComputeCommandEncoderGGDSPI setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTL4ComputeCommandEncoderGGDSPI waitForProgress:];
-[MTL4ComputeCommandEncoderGGDSPI waitForVirtualSubstream:];
```
