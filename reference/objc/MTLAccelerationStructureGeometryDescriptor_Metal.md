# `MTLAccelerationStructureGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _opaque;
B _allowDuplicateIntersectionFunctionInvocation;
Q _intersectionFunctionTableOffset;
@"NSString" _label;
@"<MTLBuffer>" _primitiveDataBuffer;
Q _primitiveDataBufferOffset;
Q _primitiveDataStride;
Q _primitiveDataElementSize;
```

## Properties

```
@property (TQ,N,V_intersectionFunctionTableOffset) intersectionFunctionTableOffset;
@property (TB,N,V_opaque) opaque;
@property (TB,N,V_allowDuplicateIntersectionFunctionInvocation) allowDuplicateIntersectionFunctionInvocation;
@property (T@"NSString",C,N,V_label) label;
@property (T@"<MTLBuffer>",&,N,V_primitiveDataBuffer) primitiveDataBuffer;
@property (TQ,N,V_primitiveDataBufferOffset) primitiveDataBufferOffset;
@property (TQ,N,V_primitiveDataStride) primitiveDataStride;
@property (TQ,N,V_primitiveDataElementSize) primitiveDataElementSize;
```

## Instance methods

```
-[MTLAccelerationStructureGeometryDescriptor opaque];
-[MTLAccelerationStructureGeometryDescriptor init];
-[MTLAccelerationStructureGeometryDescriptor label];
-[MTLAccelerationStructureGeometryDescriptor setLabel:];
-[MTLAccelerationStructureGeometryDescriptor dealloc];
-[MTLAccelerationStructureGeometryDescriptor setOpaque:];
-[MTLAccelerationStructureGeometryDescriptor type];
-[MTLAccelerationStructureGeometryDescriptor hash];
-[MTLAccelerationStructureGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureGeometryDescriptor isEqual:];
-[MTLAccelerationStructureGeometryDescriptor intersectionFunctionTableOffset];
-[MTLAccelerationStructureGeometryDescriptor allowDuplicateIntersectionFunctionInvocation];
-[MTLAccelerationStructureGeometryDescriptor primitiveDataBuffer];
-[MTLAccelerationStructureGeometryDescriptor primitiveDataBufferOffset];
-[MTLAccelerationStructureGeometryDescriptor primitiveDataElementSize];
-[MTLAccelerationStructureGeometryDescriptor primitiveDataStride];
-[MTLAccelerationStructureGeometryDescriptor setAllowDuplicateIntersectionFunctionInvocation:];
-[MTLAccelerationStructureGeometryDescriptor setIntersectionFunctionTableOffset:];
-[MTLAccelerationStructureGeometryDescriptor setPrimitiveDataBuffer:];
-[MTLAccelerationStructureGeometryDescriptor setPrimitiveDataBufferOffset:];
-[MTLAccelerationStructureGeometryDescriptor setPrimitiveDataElementSize:];
-[MTLAccelerationStructureGeometryDescriptor setPrimitiveDataStride:];
```
