# `MTL4CommandBufferGGDSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandBufferSPI`
- 0 instance variables, 4 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLBuffer>",&,N) privateData;
@property (TQ,N) privateDataOffset;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
@property (TQ,R) globalTraceObjectID;
```

## Instance methods

```
-[MTL4CommandBufferGGDSPI setPrivateDataOffset:];
-[MTL4CommandBufferGGDSPI useInternalResidencySet:];
-[MTL4CommandBufferGGDSPI setPrivateData:];
-[MTL4CommandBufferGGDSPI privateData];
-[MTL4CommandBufferGGDSPI privateDataOffset];
-[MTL4CommandBufferGGDSPI encodeSignalEvent:value:];
-[MTL4CommandBufferGGDSPI useInternalResidencySets:count:];
-[MTL4CommandBufferGGDSPI globalTraceObjectID];
-[MTL4CommandBufferGGDSPI encodeWaitForEvent:value:];
-[MTL4CommandBufferGGDSPI encodeWaitForEvent:value:timeout:];
-[MTL4CommandBufferGGDSPI addFeedbackHandler:];
-[MTL4CommandBufferGGDSPI commandAllocator];
-[MTL4CommandBufferGGDSPI computeCommandEncoderWithSubstreamCount:];
-[MTL4CommandBufferGGDSPI resetCommandBuffer];
```
