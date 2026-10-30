# `MTLTextureViewDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 10 properties, 28 instance methods, 1 class methods

## Instance variables

```
{MTLTextureViewDescriptorPrivate="pixelFormat"Q"textureType"Q"levels"{_NSRange="location"Q"length"Q}"slices"{_NSRange="location"Q"length"Q}"writeAccessPattern"q"swizzle"I"resourceIndex"Q"minLOD"f} _private;
Q _resourceIndex;
```

## Properties

```
@property (T{_NSRange=QQ},N) levels;
@property (T{_NSRange=QQ},N) slices;
@property (TQ,N,V_resourceIndex) resourceIndex;
@property (Tq,N) writeAccessPattern;
@property (TQ,N) pixelFormat;
@property (TQ,N) textureType;
@property (T{_NSRange=QQ},N) levelRange;
@property (T{_NSRange=QQ},N) sliceRange;
@property (T{?=CCCC},N) swizzle;
@property (Tf,N) minLOD;
```

## Class methods

```
+[MTLTextureViewDescriptor textureViewDescriptorWithTexture:];
```

## Instance methods

```
-[MTLTextureViewDescriptor setResourceIndex:];
-[MTLTextureViewDescriptor resourceIndex];
-[MTLTextureViewDescriptor formattedDescription:];
-[MTLTextureViewDescriptor init];
-[MTLTextureViewDescriptor levels];
-[MTLTextureViewDescriptor textureType];
-[MTLTextureViewDescriptor slices];
-[MTLTextureViewDescriptor swizzle];
-[MTLTextureViewDescriptor hash];
-[MTLTextureViewDescriptor setWriteAccessPattern:];
-[MTLTextureViewDescriptor description];
-[MTLTextureViewDescriptor pixelFormat];
-[MTLTextureViewDescriptor swizzleKey];
-[MTLTextureViewDescriptor setSwizzle:];
-[MTLTextureViewDescriptor copyWithZone:];
-[MTLTextureViewDescriptor setSwizzleKey:];
-[MTLTextureViewDescriptor setPixelFormat:];
-[MTLTextureViewDescriptor isEqual:];
-[MTLTextureViewDescriptor writeAccessPattern];
-[MTLTextureViewDescriptor setTextureType:];
-[MTLTextureViewDescriptor setLevels:];
-[MTLTextureViewDescriptor minLOD];
-[MTLTextureViewDescriptor levelRange];
-[MTLTextureViewDescriptor setLevelRange:];
-[MTLTextureViewDescriptor setMinLOD:];
-[MTLTextureViewDescriptor setSliceRange:];
-[MTLTextureViewDescriptor setSlices:];
-[MTLTextureViewDescriptor sliceRange];
```
