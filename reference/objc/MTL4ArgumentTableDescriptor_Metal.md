# `MTL4ArgumentTableDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
Q _maxBufferBindCount;
Q _maxTextureBindCount;
Q _maxSamplerStateBindCount;
B _initializeBindings;
B _supportAttributeStrides;
@"NSString" _label;
```

## Properties

```
@property (TQ,N,V_maxBufferBindCount) maxBufferBindCount;
@property (TQ,N,V_maxTextureBindCount) maxTextureBindCount;
@property (TQ,N,V_maxSamplerStateBindCount) maxSamplerStateBindCount;
@property (TB,N,V_initializeBindings) initializeBindings;
@property (TB,N,V_supportAttributeStrides) supportAttributeStrides;
@property (T@"NSString",C,N,V_label) label;
```

## Instance methods

```
-[MTL4ArgumentTableDescriptor init];
-[MTL4ArgumentTableDescriptor label];
-[MTL4ArgumentTableDescriptor setLabel:];
-[MTL4ArgumentTableDescriptor dealloc];
-[MTL4ArgumentTableDescriptor hash];
-[MTL4ArgumentTableDescriptor copyWithZone:];
-[MTL4ArgumentTableDescriptor isEqual:];
-[MTL4ArgumentTableDescriptor setMaxBufferBindCount:];
-[MTL4ArgumentTableDescriptor setMaxTextureBindCount:];
-[MTL4ArgumentTableDescriptor initializeBindings];
-[MTL4ArgumentTableDescriptor maxBufferBindCount];
-[MTL4ArgumentTableDescriptor maxSamplerStateBindCount];
-[MTL4ArgumentTableDescriptor maxTextureBindCount];
-[MTL4ArgumentTableDescriptor setInitializeBindings:];
-[MTL4ArgumentTableDescriptor setMaxSamplerStateBindCount:];
-[MTL4ArgumentTableDescriptor setSupportAttributeStrides:];
-[MTL4ArgumentTableDescriptor supportAttributeStrides];
```
