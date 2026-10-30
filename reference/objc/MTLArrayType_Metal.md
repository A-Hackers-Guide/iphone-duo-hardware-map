# `MTLArrayType`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLType`
- 0 instance variables, 4 properties, 5 instance methods, 2 class methods

## Properties

```
@property (TQ,R,D) elementType;
@property (TQ,R,D) arrayLength;
@property (TQ,R,D) stride;
@property (TQ,R,D) argumentIndexStride;
```

## Class methods

```
+[MTLArrayType allocWithZone:];
+[MTLArrayType alloc];
```

## Instance methods

```
-[MTLArrayType elementStructType];
-[MTLArrayType elementArrayType];
-[MTLArrayType elementIndirectArgumentType];
-[MTLArrayType elementPointerType];
-[MTLArrayType elementTextureReferenceType];
```
