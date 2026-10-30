# `MTLGenericBVHBuffersSPI`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 17 properties, 36 instance methods, 0 class methods

## Instance variables

```
Q _version;
@"<MTLBuffer>" _headerBuffer;
Q _headerBufferOffset;
@"<MTLBuffer>" _innerNodeBuffer;
Q _innerNodeBufferOffset;
@"<MTLBuffer>" _leafNodeBuffer;
Q _leafNodeBufferOffset;
@"<MTLBuffer>" _primitiveBuffer;
Q _primitiveBufferOffset;
@"<MTLBuffer>" _geometryBuffer;
Q _geometryBufferOffset;
@"<MTLBuffer>" _instanceTransformBuffer;
Q _instanceTransformBufferOffset;
@"<MTLBuffer>" _perPrimitiveDataBuffer;
Q _perPrimitiveDataBufferOffset;
@"<MTLBuffer>" _controlPointBuffer;
Q _controlPointBufferOffset;
```

## Properties

```
@property (TQ,R,N,V_version) version;
@property (T@"<MTLBuffer>",&,N,V_headerBuffer) headerBuffer;
@property (TQ,N,V_headerBufferOffset) headerBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_innerNodeBuffer) innerNodeBuffer;
@property (TQ,N,V_innerNodeBufferOffset) innerNodeBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_leafNodeBuffer) leafNodeBuffer;
@property (TQ,N,V_leafNodeBufferOffset) leafNodeBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_primitiveBuffer) primitiveBuffer;
@property (TQ,N,V_primitiveBufferOffset) primitiveBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_geometryBuffer) geometryBuffer;
@property (TQ,N,V_geometryBufferOffset) geometryBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_instanceTransformBuffer) instanceTransformBuffer;
@property (TQ,N,V_instanceTransformBufferOffset) instanceTransformBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_perPrimitiveDataBuffer) perPrimitiveDataBuffer;
@property (TQ,N,V_perPrimitiveDataBufferOffset) perPrimitiveDataBufferOffset;
@property (T@"<MTLBuffer>",&,N,V_controlPointBuffer) controlPointBuffer;
@property (TQ,N,V_controlPointBufferOffset) controlPointBufferOffset;
```

## Instance methods

```
-[MTLGenericBVHBuffersSPI init];
-[MTLGenericBVHBuffersSPI dealloc];
-[MTLGenericBVHBuffersSPI version];
-[MTLGenericBVHBuffersSPI initWithVersion:];
-[MTLGenericBVHBuffersSPI primitiveBuffer];
-[MTLGenericBVHBuffersSPI innerNodeBuffer];
-[MTLGenericBVHBuffersSPI controlPointBuffer];
-[MTLGenericBVHBuffersSPI controlPointBufferOffset];
-[MTLGenericBVHBuffersSPI geometryBuffer];
-[MTLGenericBVHBuffersSPI geometryBufferOffset];
-[MTLGenericBVHBuffersSPI headerBuffer];
-[MTLGenericBVHBuffersSPI headerBufferOffset];
-[MTLGenericBVHBuffersSPI innerNodeBufferOffset];
-[MTLGenericBVHBuffersSPI instanceTransformBuffer];
-[MTLGenericBVHBuffersSPI instanceTransformBufferOffset];
-[MTLGenericBVHBuffersSPI leafNodeBuffer];
-[MTLGenericBVHBuffersSPI leafNodeBufferOffset];
-[MTLGenericBVHBuffersSPI perPrimitiveDataBuffer];
-[MTLGenericBVHBuffersSPI perPrimitiveDataBufferOffset];
-[MTLGenericBVHBuffersSPI primitiveBufferOffset];
-[MTLGenericBVHBuffersSPI setControlPointBuffer:];
-[MTLGenericBVHBuffersSPI setControlPointBufferOffset:];
-[MTLGenericBVHBuffersSPI setGeometryBuffer:];
-[MTLGenericBVHBuffersSPI setGeometryBufferOffset:];
-[MTLGenericBVHBuffersSPI setHeaderBuffer:];
-[MTLGenericBVHBuffersSPI setHeaderBufferOffset:];
-[MTLGenericBVHBuffersSPI setInnerNodeBuffer:];
-[MTLGenericBVHBuffersSPI setInnerNodeBufferOffset:];
-[MTLGenericBVHBuffersSPI setInstanceTransformBuffer:];
-[MTLGenericBVHBuffersSPI setInstanceTransformBufferOffset:];
-[MTLGenericBVHBuffersSPI setLeafNodeBuffer:];
-[MTLGenericBVHBuffersSPI setLeafNodeBufferOffset:];
-[MTLGenericBVHBuffersSPI setPerPrimitiveDataBuffer:];
-[MTLGenericBVHBuffersSPI setPerPrimitiveDataBufferOffset:];
-[MTLGenericBVHBuffersSPI setPrimitiveBuffer:];
-[MTLGenericBVHBuffersSPI setPrimitiveBufferOffset:];
```
