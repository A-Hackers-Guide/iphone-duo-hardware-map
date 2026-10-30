# `AGXG19FamilyArgumentTable_mtlnext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4ArgumentTable`
- 2 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@"AGXG19FamilyDevice" _device;
```

## Properties

```
@property (T^Q,R,N) bufferBindings;
@property (T^Q,R,N) textureBindings;
@property (T^Q,R,N) samplerBindings;
@property (TQ,R,N) bufferBindingCount;
@property (TQ,R,N) textureBindingCount;
@property (TQ,R,N) samplerBindingCount;
@property (T@"<MTLDevice>",R) device;
```

## Instance methods

```
-[AGXG19FamilyArgumentTable_mtlnext setTexture:atIndex:];
-[AGXG19FamilyArgumentTable_mtlnext device];
-[AGXG19FamilyArgumentTable_mtlnext setSamplerState:atIndex:];
-[AGXG19FamilyArgumentTable_mtlnext dealloc];
-[AGXG19FamilyArgumentTable_mtlnext setAddress:atIndex:];
-[AGXG19FamilyArgumentTable_mtlnext setAddress:attributeStride:atIndex:];
-[AGXG19FamilyArgumentTable_mtlnext setResource:atBufferIndex:];
-[AGXG19FamilyArgumentTable_mtlnext getBufferBindings:bindingCount:];
-[AGXG19FamilyArgumentTable_mtlnext bufferBindingCount];
-[AGXG19FamilyArgumentTable_mtlnext getTextureBindings:bindingCount:];
-[AGXG19FamilyArgumentTable_mtlnext initWithDescriptor:device:];
-[AGXG19FamilyArgumentTable_mtlnext samplerBindingCount];
-[AGXG19FamilyArgumentTable_mtlnext textureBindingCount];
-[AGXG19FamilyArgumentTable_mtlnext samplerBindings];
-[AGXG19FamilyArgumentTable_mtlnext textureBindings];
-[AGXG19FamilyArgumentTable_mtlnext bufferBindings];
```
