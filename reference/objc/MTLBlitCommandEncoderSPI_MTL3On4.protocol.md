# `MTLBlitCommandEncoderSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoderSPI`, `MTLBlitCommandEncoder`
- 0 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance methods

```
-[MTLBlitCommandEncoderSPI fillTexture:level:slice:region:color:];
-[MTLBlitCommandEncoderSPI fillBuffer:range:pattern4:];
-[MTLBlitCommandEncoderSPI fillTexture:level:slice:region:bytes:length:];
-[MTLBlitCommandEncoderSPI fillTexture:level:slice:region:color:pixelFormat:];
-[MTLBlitCommandEncoderSPI copyFromTensor:sourceSlice:toTensor:destinationSlice:];
-[MTLBlitCommandEncoderSPI invalidateCompressedTexture:];
-[MTLBlitCommandEncoderSPI invalidateCompressedTexture:slice:level:];
-[MTLBlitCommandEncoderSPI optimizeContentsForTexture:readAccessPattern:readAccessor:];
-[MTLBlitCommandEncoderSPI optimizeContentsForTexture:readAccessPattern:readAccessor:slice:level:];
-[MTLBlitCommandEncoderSPI copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:];
```
