# `MTL4FXTemporalDenoisedScalerSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4FXTemporalDenoisedScaler`
- 0 instance variables, 7 properties, 12 instance methods, 0 class methods

## Properties

```
@property (TQ,N) inputContentWidth;
@property (TQ,N) inputContentHeight;
@property (TB,N) reset;
@property (TQ,N) colorTextureBarrierStages;
@property (TQ,R,N) outputTextureBarrierStages;
@property (T@"<MTLTexture>",&,N) debugTexture;
@property (T@"<MTLTexture>",R,N) dilatedMotionVectors;
```

## Instance methods

```
-[MTL4FXTemporalDenoisedScalerSPI setReset:];
-[MTL4FXTemporalDenoisedScalerSPI reset];
-[MTL4FXTemporalDenoisedScalerSPI debugTexture];
-[MTL4FXTemporalDenoisedScalerSPI colorTextureBarrierStages];
-[MTL4FXTemporalDenoisedScalerSPI dilatedMotionVectors];
-[MTL4FXTemporalDenoisedScalerSPI inputContentHeight];
-[MTL4FXTemporalDenoisedScalerSPI inputContentWidth];
-[MTL4FXTemporalDenoisedScalerSPI outputTextureBarrierStages];
-[MTL4FXTemporalDenoisedScalerSPI setColorTextureBarrierStages:];
-[MTL4FXTemporalDenoisedScalerSPI setDebugTexture:];
-[MTL4FXTemporalDenoisedScalerSPI setInputContentHeight:];
-[MTL4FXTemporalDenoisedScalerSPI setInputContentWidth:];
```
