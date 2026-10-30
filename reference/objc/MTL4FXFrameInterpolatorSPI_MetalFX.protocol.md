# `MTL4FXFrameInterpolatorSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4FXFrameInterpolator`
- 0 instance variables, 5 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TB,N) reset;
@property (TQ,N) colorTextureBarrierStages;
@property (TQ,R,N) outputTextureBarrierStages;
@property (TB,N) compositedUITexture;
@property (T@"<MTLTexture>",&,N) debugTexture;
```

## Instance methods

```
-[MTL4FXFrameInterpolatorSPI setReset:];
-[MTL4FXFrameInterpolatorSPI reset];
-[MTL4FXFrameInterpolatorSPI debugTexture];
-[MTL4FXFrameInterpolatorSPI colorTextureBarrierStages];
-[MTL4FXFrameInterpolatorSPI compositedUITexture];
-[MTL4FXFrameInterpolatorSPI outputTextureBarrierStages];
-[MTL4FXFrameInterpolatorSPI setColorTextureBarrierStages:];
-[MTL4FXFrameInterpolatorSPI setCompositedUITexture:];
-[MTL4FXFrameInterpolatorSPI setDebugTexture:];
```
