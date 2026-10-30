# `MTL4AccelerationStructureGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _opaque;
B _allowDuplicateIntersectionFunctionInvocation;
Q _intersectionFunctionTableOffset;
@"NSString" _label;
Q _primitiveDataStride;
Q _primitiveDataElementSize;
{MTL4BufferRange="bufferAddress"Q"length"Q} _primitiveDataBuffer;
```

## Properties

```
@property (TQ,N,V_intersectionFunctionTableOffset) intersectionFunctionTableOffset;
@property (TB,N,V_opaque) opaque;
@property (TB,N,V_allowDuplicateIntersectionFunctionInvocation) allowDuplicateIntersectionFunctionInvocation;
@property (T@"NSString",C,N,V_label) label;
@property (T{MTL4BufferRange=QQ},N,V_primitiveDataBuffer) primitiveDataBuffer;
@property (TQ,N,V_primitiveDataStride) primitiveDataStride;
@property (TQ,N,V_primitiveDataElementSize) primitiveDataElementSize;
```

## Instance methods

```
-[MTL4AccelerationStructureGeometryDescriptor opaque];
-[MTL4AccelerationStructureGeometryDescriptor init];
-[MTL4AccelerationStructureGeometryDescriptor label];
-[MTL4AccelerationStructureGeometryDescriptor setLabel:];
-[MTL4AccelerationStructureGeometryDescriptor dealloc];
-[MTL4AccelerationStructureGeometryDescriptor setOpaque:];
-[MTL4AccelerationStructureGeometryDescriptor type];
-[MTL4AccelerationStructureGeometryDescriptor hash];
-[MTL4AccelerationStructureGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureGeometryDescriptor intersectionFunctionTableOffset];
-[MTL4AccelerationStructureGeometryDescriptor allowDuplicateIntersectionFunctionInvocation];
-[MTL4AccelerationStructureGeometryDescriptor primitiveDataBuffer];
-[MTL4AccelerationStructureGeometryDescriptor primitiveDataElementSize];
-[MTL4AccelerationStructureGeometryDescriptor primitiveDataStride];
-[MTL4AccelerationStructureGeometryDescriptor setAllowDuplicateIntersectionFunctionInvocation:];
-[MTL4AccelerationStructureGeometryDescriptor setIntersectionFunctionTableOffset:];
-[MTL4AccelerationStructureGeometryDescriptor setPrimitiveDataBuffer:];
-[MTL4AccelerationStructureGeometryDescriptor setPrimitiveDataElementSize:];
-[MTL4AccelerationStructureGeometryDescriptor setPrimitiveDataStride:];
```
