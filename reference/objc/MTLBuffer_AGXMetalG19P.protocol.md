# `MTLBuffer` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResource`
- 0 instance variables, 3 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R) length;
@property (TQ,R) gpuAddress;
@property (Tq,R) sparseBufferTier;
```

## Instance methods

```
-[MTLBuffer didModifyRange:];
-[MTLBuffer removeAllDebugMarkers];
-[MTLBuffer addDebugMarker:range:];
-[MTLBuffer contents];
-[MTLBuffer gpuAddress];
-[MTLBuffer length];
-[MTLBuffer newTensorWithDescriptor:offset:error:];
-[MTLBuffer newTextureWithDescriptor:offset:bytesPerRow:];
-[MTLBuffer sparseBufferTier];
```
