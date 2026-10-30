# `MTLTextureBinding` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLBinding`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TQ,R) textureType;
@property (TQ,R) textureDataType;
@property (TB,R,GisDepthTexture) depthTexture;
@property (TQ,R) arrayLength;
```

## Instance methods

```
-[MTLTextureBinding arrayLength];
-[MTLTextureBinding textureType];
-[MTLTextureBinding isDepthTexture];
-[MTLTextureBinding textureDataType];
```
