# `MTLFXFrameInterpolatorSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFXFrameInterpolator`
- 0 instance variables, 5 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLTexture>",&,N) debugTexture;
@property (TB,N) compositedUITexture;
@property (TB,N) reset;
@property (TQ,N) width;
@property (TQ,N) height;
```

## Instance methods

```
-[MTLFXFrameInterpolatorSPI setReset:];
-[MTLFXFrameInterpolatorSPI reset];
-[MTLFXFrameInterpolatorSPI setHeight:];
-[MTLFXFrameInterpolatorSPI setWidth:];
-[MTLFXFrameInterpolatorSPI width];
-[MTLFXFrameInterpolatorSPI height];
-[MTLFXFrameInterpolatorSPI encodeToCommandQueue:];
-[MTLFXFrameInterpolatorSPI debugTexture];
-[MTLFXFrameInterpolatorSPI compositedUITexture];
-[MTLFXFrameInterpolatorSPI setCompositedUITexture:];
-[MTLFXFrameInterpolatorSPI setDebugTexture:];
```
