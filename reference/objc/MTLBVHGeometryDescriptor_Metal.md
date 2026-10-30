# `MTLBVHGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _primitiveCount;
@"<MTLBuffer>" _maskBuffer;
Q _maskBufferOffset;
@"<MTLBuffer>" _primitiveDataBuffer;
Q _primitiveDataBufferOffset;
Q _primitiveDataStride;
Q _primitiveDataElementSize;
```

## Properties

```
@property (TQ,R,N) primitiveType;
@property (TQ,N,V_primitiveCount) primitiveCount;
@property (T@"<MTLBuffer>",W,N,V_maskBuffer) maskBuffer;
@property (TQ,N,V_maskBufferOffset) maskBufferOffset;
@property (T@"<MTLBuffer>",W,N,V_primitiveDataBuffer) primitiveDataBuffer;
@property (TQ,N,V_primitiveDataBufferOffset) primitiveDataBufferOffset;
@property (TQ,N,V_primitiveDataStride) primitiveDataStride;
@property (TQ,N,V_primitiveDataElementSize) primitiveDataElementSize;
```

## Instance methods

```
-[MTLBVHGeometryDescriptor primitiveType];
-[MTLBVHGeometryDescriptor maskBuffer];
-[MTLBVHGeometryDescriptor maskBufferOffset];
-[MTLBVHGeometryDescriptor primitiveCount];
-[MTLBVHGeometryDescriptor primitiveDataBuffer];
-[MTLBVHGeometryDescriptor primitiveDataBufferOffset];
-[MTLBVHGeometryDescriptor primitiveDataElementSize];
-[MTLBVHGeometryDescriptor primitiveDataStride];
-[MTLBVHGeometryDescriptor setMaskBuffer:];
-[MTLBVHGeometryDescriptor setMaskBufferOffset:];
-[MTLBVHGeometryDescriptor setPrimitiveCount:];
-[MTLBVHGeometryDescriptor setPrimitiveDataBuffer:];
-[MTLBVHGeometryDescriptor setPrimitiveDataBufferOffset:];
-[MTLBVHGeometryDescriptor setPrimitiveDataElementSize:];
-[MTLBVHGeometryDescriptor setPrimitiveDataStride:];
```
