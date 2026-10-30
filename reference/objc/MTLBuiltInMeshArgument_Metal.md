# `MTLBuiltInMeshArgument`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
S _builtInType;
S _builtInDataType;
S _meshVertexCount;
S _meshPrimitiveCount;
S _meshTopologyType;
@"MTLStructTypeInternal" _meshVertexStruct;
@"MTLStructTypeInternal" _meshPrimitiveStruct;
```

## Instance methods

```
-[MTLBuiltInMeshArgument formattedDescription:];
-[MTLBuiltInMeshArgument dealloc];
-[MTLBuiltInMeshArgument isEqual:];
-[MTLBuiltInMeshArgument builtInType];
-[MTLBuiltInMeshArgument builtInDataType];
-[MTLBuiltInMeshArgument meshVertexCount];
-[MTLBuiltInMeshArgument initWithName:type:access:active:index:dataType:builtInType:meshVertexStructType:meshPrimitiveStructType:meshVertexCount:meshPrimitiveCount:meshTopologyType:];
-[MTLBuiltInMeshArgument meshPrimitiveCount];
-[MTLBuiltInMeshArgument meshPrimitiveStruct];
-[MTLBuiltInMeshArgument meshTopologyType];
-[MTLBuiltInMeshArgument meshVertexStruct];
```
