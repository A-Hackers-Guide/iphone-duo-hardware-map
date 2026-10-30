# `MTLArgument`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 20 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"MTLArgument" _bufferIndirectArgumentType;
Q _indirectConstantAlignment;
Q _indirectConstantDataSize;
Q _indirectConstantDataType;
```

## Properties

```
@property (T@"MTLArgument",R,V_bufferIndirectArgumentType) bufferIndirectArgumentType;
@property (TQ,R,V_indirectConstantAlignment) indirectConstantAlignment;
@property (TQ,R,V_indirectConstantDataSize) indirectConstantDataSize;
@property (TQ,R,V_indirectConstantDataType) indirectConstantDataType;
@property (T@"NSString",R,D) name;
@property (TQ,R,D) type;
@property (TQ,R,D) access;
@property (TQ,R,D) index;
@property (TB,R,D,GisActive) active;
@property (TQ,R,D) bufferAlignment;
@property (TQ,R,D) bufferDataSize;
@property (TQ,R,D) bufferDataType;
@property (T@"MTLStructType",R,D) bufferStructType;
@property (T@"MTLPointerType",R,D) bufferPointerType;
@property (TQ,R,D) threadgroupMemoryAlignment;
@property (TQ,R,D) threadgroupMemoryDataSize;
@property (TQ,R,D) textureType;
@property (TQ,R,D) textureDataType;
@property (TB,R,D) isDepthTexture;
@property (TQ,R,D) arrayLength;
```

## Class methods

```
+[MTLArgument allocWithZone:];
+[MTLArgument alloc];
```

## Instance methods

```
-[MTLArgument bufferIndirectArgumentType];
-[MTLArgument indirectConstantAlignment];
-[MTLArgument indirectConstantDataSize];
-[MTLArgument indirectConstantDataType];
```
