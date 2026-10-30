# `MTL4FXTemporalScalerSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4FXTemporalScaler`
- 0 instance variables, 10 properties, 17 instance methods, 0 class methods

## Properties

```
@property (TQ,N) colorTextureBarrierStages;
@property (TQ,R,N) outputTextureBarrierStages;
@property (T{CGPoint=dd},N) previousJitterOffset;
@property (T{?=[4]},N) currentWorldToViewMatrix;
@property (T{?=[4]},N) currentViewToClipMatrix;
@property (T{?=[4]},N) previousWorldToViewMatrix;
@property (T{?=[4]},N) previousViewToClipMatrix;
@property (T@"<MTLTexture>",R,N) dilatedMotionVectors;
@property (T@"<MTLTexture>",&,N) debugTexture;
@property (TQ,R,N) executionMode;
```

## Instance methods

```
-[MTL4FXTemporalScalerSPI debugTexture];
-[MTL4FXTemporalScalerSPI colorTextureBarrierStages];
-[MTL4FXTemporalScalerSPI currentViewToClipMatrix];
-[MTL4FXTemporalScalerSPI currentWorldToViewMatrix];
-[MTL4FXTemporalScalerSPI dilatedMotionVectors];
-[MTL4FXTemporalScalerSPI executionMode];
-[MTL4FXTemporalScalerSPI outputTextureBarrierStages];
-[MTL4FXTemporalScalerSPI previousJitterOffset];
-[MTL4FXTemporalScalerSPI previousViewToClipMatrix];
-[MTL4FXTemporalScalerSPI previousWorldToViewMatrix];
-[MTL4FXTemporalScalerSPI setColorTextureBarrierStages:];
-[MTL4FXTemporalScalerSPI setCurrentViewToClipMatrix:];
-[MTL4FXTemporalScalerSPI setCurrentWorldToViewMatrix:];
-[MTL4FXTemporalScalerSPI setDebugTexture:];
-[MTL4FXTemporalScalerSPI setPreviousJitterOffset:];
-[MTL4FXTemporalScalerSPI setPreviousViewToClipMatrix:];
-[MTL4FXTemporalScalerSPI setPreviousWorldToViewMatrix:];
```
