# `MTLArgumentCompat` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 18 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R) name;
@property (Tq,R) type;
@property (TQ,R) access;
@property (TQ,R) index;
@property (TB,R,GisActive) active;
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
@property (TQ,R) arrayLength;
```

## Instance methods

```
-[MTLArgumentCompat arrayLength];
-[MTLArgumentCompat textureType];
-[MTLArgumentCompat bufferDataSize];
-[MTLArgumentCompat access];
-[MTLArgumentCompat index];
-[MTLArgumentCompat isDepthTexture];
-[MTLArgumentCompat bufferPointerType];
-[MTLArgumentCompat bufferAlignment];
-[MTLArgumentCompat bufferDataType];
-[MTLArgumentCompat type];
-[MTLArgumentCompat textureDataType];
-[MTLArgumentCompat isActive];
-[MTLArgumentCompat bufferStructType];
-[MTLArgumentCompat name];
-[MTLArgumentCompat objectPayloadAlignment];
-[MTLArgumentCompat objectPayloadDataSize];
-[MTLArgumentCompat threadgroupMemoryAlignment];
-[MTLArgumentCompat threadgroupMemoryDataSize];
```
