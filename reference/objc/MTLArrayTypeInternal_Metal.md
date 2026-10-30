# `MTLArrayTypeInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLArrayType`
- 10 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
Q _dataType;
b32 _arrayLength;
b32 _stride;
@ _details;
Q _elementType;
Q _pixelFormat;
Q _aluType;
@"MTLType" _elementTypeInfo;
B _isIndirectArgumentBuffer;
Q _argumentIndexStride;
```

## Properties

```
@property (TB,V_isIndirectArgumentBuffer) isIndirectArgumentBuffer;
@property (TQ,R,V_pixelFormat) pixelFormat;
@property (TQ,R,V_aluType) aluType;
@property (TQ,N,V_argumentIndexStride) argumentIndexStride;
@property (TQ,N) indirectArgumentIndexStride;
```

## Instance methods

```
-[MTLArrayTypeInternal arrayLength];
-[MTLArrayTypeInternal setIsIndirectArgumentBuffer:];
-[MTLArrayTypeInternal dealloc];
-[MTLArrayTypeInternal aluType];
-[MTLArrayTypeInternal isIndirectArgumentBuffer];
-[MTLArrayTypeInternal elementStructType];
-[MTLArrayTypeInternal elementTypeDescription];
-[MTLArrayTypeInternal formattedDescription:withPrintedTypes:];
-[MTLArrayTypeInternal dataType];
-[MTLArrayTypeInternal stride];
-[MTLArrayTypeInternal elementArrayType];
-[MTLArrayTypeInternal elementType];
-[MTLArrayTypeInternal pixelFormat];
-[MTLArrayTypeInternal isEqual:];
-[MTLArrayTypeInternal setStride:];
-[MTLArrayTypeInternal setIndirectArgumentIndexStride:];
-[MTLArrayTypeInternal argumentIndexStride];
-[MTLArrayTypeInternal elementIndirectArgumentType];
-[MTLArrayTypeInternal elementPointerType];
-[MTLArrayTypeInternal elementTensorReferenceType];
-[MTLArrayTypeInternal elementTextureReferenceType];
-[MTLArrayTypeInternal indirectArgumentIndexStride];
-[MTLArrayTypeInternal initWithArrayLength:elementType:stride:pixelFormat:aluType:details:];
-[MTLArrayTypeInternal isArrayLayoutThreadSafeWith:];
-[MTLArrayTypeInternal setArgumentIndexStride:];
```
