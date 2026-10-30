# `MTLToolsResourceStateCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandEncoder`
- Protocols: `MTLResourceStateCommandEncoderSPI`
- 0 instance variables, 6 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsResourceStateCommandEncoder waitForFence:];
-[MTLToolsResourceStateCommandEncoder updateFence:];
-[MTLToolsResourceStateCommandEncoder updateTextureMappings:mode:regions:mipLevels:slices:numRegions:];
-[MTLToolsResourceStateCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTLToolsResourceStateCommandEncoder initWithBaseObject:parent:];
-[MTLToolsResourceStateCommandEncoder moveTextureMappingsFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:];
-[MTLToolsResourceStateCommandEncoder updateTextureMapping:mode:indirectBuffer:indirectBufferOffset:];
-[MTLToolsResourceStateCommandEncoder updateTextureMapping:mode:region:mipLevel:slice:];
-[MTLToolsResourceStateCommandEncoder copyMappingStateFromTexture:mipLevel:slice:toBuffer:offset:numTiles:];
-[MTLToolsResourceStateCommandEncoder initWithResourceStateCommandEncoder:parent:descriptor:];
```
