# `MTLComputeCommandEncoderSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoderSPI`, `MTLComputeCommandEncoder`
- 0 instance variables, 0 properties, 26 instance methods, 0 class methods

## Instance methods

```
-[MTLComputeCommandEncoderSPI useResidencySet:];
-[MTLComputeCommandEncoderSPI useResidencySets:count:];
-[MTLComputeCommandEncoderSPI setThreadgroupDistributionMode:];
-[MTLComputeCommandEncoderSPI setThreadgroupDistributionModeWithClusterGroupIndex:];
-[MTLComputeCommandEncoderSPI setThreadgroupPackingDisabled:];
-[MTLComputeCommandEncoderSPI setToolsDispatchBufferSPI:atIndex:];
-[MTLComputeCommandEncoderSPI newKernelDebugInfo];
-[MTLComputeCommandEncoderSPI encodeStartElse];
-[MTLComputeCommandEncoderSPI signalProgress:];
-[MTLComputeCommandEncoderSPI beginVirtualSubstream];
-[MTLComputeCommandEncoderSPI enableNullBufferBinds:];
-[MTLComputeCommandEncoderSPI encodeEndDoWhile:offset:comparison:referenceValue:];
-[MTLComputeCommandEncoderSPI encodeEndIf];
-[MTLComputeCommandEncoderSPI encodeEndWhile];
-[MTLComputeCommandEncoderSPI encodeStartDoWhile];
-[MTLComputeCommandEncoderSPI encodeStartIf:offset:comparison:referenceValue:];
-[MTLComputeCommandEncoderSPI encodeStartWhile:offset:comparison:referenceValue:];
-[MTLComputeCommandEncoderSPI endVirtualSubstream];
-[MTLComputeCommandEncoderSPI insertCompressedTextureReinterpretationFlush];
-[MTLComputeCommandEncoderSPI nextVirtualSubstream];
-[MTLComputeCommandEncoderSPI setSubstream:];
-[MTLComputeCommandEncoderSPI waitForProgress:];
-[MTLComputeCommandEncoderSPI waitForVirtualSubstream:];
-[MTLComputeCommandEncoderSPI dispatchThreadsWithIndirectBuffer:indirectBufferOffset:];
-[MTLComputeCommandEncoderSPI insertUncompressedToCompressedFlush];
-[MTLComputeCommandEncoderSPI useResourceGroup:usage:];
```
