# `MTLBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLArgument`
- Protocols: `MTLArgumentCompat`, `MTLBinding`
- 18 instance variables, 47 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
q _type;
Q _access;
Q _index;
B _isUsed;
Q _arrayLength;
@"MTLType" _typeInfo;
B _argument;
B _aliasImplicitImageBlock;
B _vertexDescriptorBuffer;
Q _builtInType;
Q _builtInDataType;
Q _imageBlockKind;
Q _imageBlockDataSize;
@"MTLStructTypeInternal" _imageBlockMasterStructMembers;
Q _aliasImplicitImageBlockRenderTarget;
Q _threadgroupMemoryDataType;
@"MTLStructType" _threadgroupMemoryStructType;
```

## Properties

```
@property (TB) isUsed;
@property (TB,GisArgument,SsetIsArgument:,V_argument) argument;
@property (TQ,R) bufferAlignment;
@property (TQ,R) bufferDataSize;
@property (TQ,R) bufferDataType;
@property (T@"MTLStructType",R) bufferStructType;
@property (T@"MTLPointerType",R) bufferPointerType;
@property (TQ,R) threadgroupMemoryAlignment;
@property (TQ,R) threadgroupMemoryDataSize;
@property (TQ,R) textureType;
@property (TQ,R) textureDataType;
@property (TB,R) isDepthTexture;
@property (TQ,R) objectPayloadAlignment;
@property (TQ,R) objectPayloadDataSize;
@property (TQ,R) meshVertexCount;
@property (TQ,R) meshPrimitiveCount;
@property (TQ,R) meshTopologyType;
@property (T@"MTLStructTypeInternal",R) meshVertexStruct;
@property (T@"MTLStructTypeInternal",R) meshPrimitiveStruct;
@property (T@"MTLArgument",R) bufferIndirectArgumentType;
@property (TQ,R) indirectConstantAlignment;
@property (TQ,R) indirectConstantDataSize;
@property (TQ,R) indirectConstantDataType;
@property (TQ,R,D) bufferPixelFormat;
@property (TQ,R,D) bufferALUType;
@property (T@"MTLStructType",R,D) structType;
@property (TQ,R,V_builtInType) builtInType;
@property (TQ,R,V_builtInDataType) builtInDataType;
@property (TQ,R,V_imageBlockKind) imageBlockKind;
@property (TQ,R,V_imageBlockDataSize) imageBlockDataSize;
@property (T@"MTLStructTypeInternal",R,V_imageBlockMasterStructMembers) imageBlockMasterStructMembers;
@property (TB,R,V_aliasImplicitImageBlock) aliasImplicitImageBlock;
@property (TQ,R,V_aliasImplicitImageBlockRenderTarget) aliasImplicitImageBlockRenderTarget;
@property (TB,R,GisVertexDescriptorBuffer,V_vertexDescriptorBuffer) vertexDescriptorBuffer;
@property (TQ,R,V_threadgroupMemoryDataType) threadgroupMemoryDataType;
@property (T@"MTLStructType",R,V_threadgroupMemoryStructType) threadgroupMemoryStructType;
@property (T@"NSString",R,V_name) name;
@property (Tq,R,V_type) type;
@property (TQ,R,V_access) access;
@property (TQ,R,V_index) index;
@property (TB,R,GisActive) active;
@property (TQ,R,V_arrayLength) arrayLength;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,GisUsed) used;
```

## Instance methods

```
-[MTLBindingInternal arrayLength];
-[MTLBindingInternal formattedDescription:];
-[MTLBindingInternal dealloc];
-[MTLBindingInternal textureType];
-[MTLBindingInternal bufferDataSize];
-[MTLBindingInternal access];
-[MTLBindingInternal isVertexDescriptorBuffer];
-[MTLBindingInternal index];
-[MTLBindingInternal isDepthTexture];
-[MTLBindingInternal bufferPointerType];
-[MTLBindingInternal structType];
-[MTLBindingInternal bufferAlignment];
-[MTLBindingInternal bufferIndirectArgumentType];
-[MTLBindingInternal bufferDataType];
-[MTLBindingInternal type];
-[MTLBindingInternal formattedDescription:withPrintedTypes:];
-[MTLBindingInternal description];
-[MTLBindingInternal textureDataType];
-[MTLBindingInternal isActive];
-[MTLBindingInternal isEqual:];
-[MTLBindingInternal dataTypeDescription];
-[MTLBindingInternal bufferStructType];
-[MTLBindingInternal builtInType];
-[MTLBindingInternal name];
-[MTLBindingInternal builtInDataType];
-[MTLBindingInternal meshVertexCount];
-[MTLBindingInternal aliasImplicitImageBlock];
-[MTLBindingInternal aliasImplicitImageBlockRenderTarget];
-[MTLBindingInternal imageBlockDataSize];
-[MTLBindingInternal imageBlockKind];
-[MTLBindingInternal imageBlockMasterStructMembers];
-[MTLBindingInternal indirectConstantAlignment];
-[MTLBindingInternal indirectConstantDataSize];
-[MTLBindingInternal indirectConstantDataType];
-[MTLBindingInternal initWithName:type:access:index:active:arrayLength:];
-[MTLBindingInternal initWithName:type:access:index:active:arrayLength:typeDescription:];
-[MTLBindingInternal isArgument];
-[MTLBindingInternal isUsed];
-[MTLBindingInternal meshPrimitiveCount];
-[MTLBindingInternal meshPrimitiveStruct];
-[MTLBindingInternal meshTopologyType];
-[MTLBindingInternal meshVertexStruct];
-[MTLBindingInternal objectPayloadAlignment];
-[MTLBindingInternal objectPayloadDataSize];
-[MTLBindingInternal setIsArgument:];
-[MTLBindingInternal setIsUsed:];
-[MTLBindingInternal threadgroupMemoryAlignment];
-[MTLBindingInternal threadgroupMemoryDataSize];
-[MTLBindingInternal threadgroupMemoryDataType];
-[MTLBindingInternal threadgroupMemoryStructType];
```
