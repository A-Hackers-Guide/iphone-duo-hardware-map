# `MTLSamplerDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 2 instance variables, 20 properties, 5 instance methods, 2 class methods

## Instance variables

```
B _lodAverage;
f _lodBias;
```

## Properties

```
@property (TB,D,N) forceResourceIndex;
@property (TQ,D,N) resourceIndex;
@property (TQ,D,N) pixelFormat;
@property (TQ,D,N) minFilter;
@property (TQ,D,N) magFilter;
@property (TQ,D,N) mipFilter;
@property (TQ,D,N) maxAnisotropy;
@property (TQ,D,N) sAddressMode;
@property (TQ,D,N) tAddressMode;
@property (TQ,D,N) rAddressMode;
@property (TQ,D,N) borderColor;
@property (TQ,D,N) reductionMode;
@property (TB,D,N) normalizedCoordinates;
@property (Tf,D,N) lodMinClamp;
@property (Tf,D,N) lodMaxClamp;
@property (TB,N,V_lodAverage) lodAverage;
@property (Tf,N,V_lodBias) lodBias;
@property (TQ,D,N) compareFunction;
@property (TB,D,N) supportArgumentBuffers;
@property (T@"NSString",C,D,N) label;
```

## Class methods

```
+[MTLSamplerDescriptor allocWithZone:];
+[MTLSamplerDescriptor alloc];
```

## Instance methods

```
-[MTLSamplerDescriptor setLodBias:];
-[MTLSamplerDescriptor setLodAverage:];
-[MTLSamplerDescriptor lodBias];
-[MTLSamplerDescriptor lodAverage];
-[MTLSamplerDescriptor copyWithZone:];
```
