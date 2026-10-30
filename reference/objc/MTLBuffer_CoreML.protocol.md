# `MTLBuffer` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
