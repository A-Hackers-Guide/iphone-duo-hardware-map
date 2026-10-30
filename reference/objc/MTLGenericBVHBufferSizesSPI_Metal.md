# `MTLGenericBVHBufferSizesSPI`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _version;
Q _headerBufferSize;
Q _innerNodeBufferSize;
Q _leafNodeBufferSize;
Q _primitiveBufferSize;
Q _geometryBufferSize;
Q _instanceTransformBufferSize;
Q _perPrimitiveDataBufferSize;
Q _controlPointBufferSize;
```

## Properties

```
@property (TQ,R,N,V_version) version;
@property (TQ,N,V_headerBufferSize) headerBufferSize;
@property (TQ,N,V_innerNodeBufferSize) innerNodeBufferSize;
@property (TQ,N,V_leafNodeBufferSize) leafNodeBufferSize;
@property (TQ,N,V_primitiveBufferSize) primitiveBufferSize;
@property (TQ,N,V_geometryBufferSize) geometryBufferSize;
@property (TQ,N,V_instanceTransformBufferSize) instanceTransformBufferSize;
@property (TQ,N,V_perPrimitiveDataBufferSize) perPrimitiveDataBufferSize;
@property (TQ,N,V_controlPointBufferSize) controlPointBufferSize;
```

## Instance methods

```
-[MTLGenericBVHBufferSizesSPI version];
-[MTLGenericBVHBufferSizesSPI initWithVersion:];
-[MTLGenericBVHBufferSizesSPI setInstanceTransformBufferSize:];
-[MTLGenericBVHBufferSizesSPI controlPointBufferSize];
-[MTLGenericBVHBufferSizesSPI geometryBufferSize];
-[MTLGenericBVHBufferSizesSPI headerBufferSize];
-[MTLGenericBVHBufferSizesSPI innerNodeBufferSize];
-[MTLGenericBVHBufferSizesSPI instanceTransformBufferSize];
-[MTLGenericBVHBufferSizesSPI leafNodeBufferSize];
-[MTLGenericBVHBufferSizesSPI perPrimitiveDataBufferSize];
-[MTLGenericBVHBufferSizesSPI primitiveBufferSize];
-[MTLGenericBVHBufferSizesSPI setControlPointBufferSize:];
-[MTLGenericBVHBufferSizesSPI setGeometryBufferSize:];
-[MTLGenericBVHBufferSizesSPI setHeaderBufferSize:];
-[MTLGenericBVHBufferSizesSPI setInnerNodeBufferSize:];
-[MTLGenericBVHBufferSizesSPI setLeafNodeBufferSize:];
-[MTLGenericBVHBufferSizesSPI setPerPrimitiveDataBufferSize:];
-[MTLGenericBVHBufferSizesSPI setPrimitiveBufferSize:];
```
