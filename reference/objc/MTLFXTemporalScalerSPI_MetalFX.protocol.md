# `MTLFXTemporalScalerSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFXTemporalScaler`
- 0 instance variables, 8 properties, 15 instance methods, 0 class methods

## Properties

```
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
-[MTLFXTemporalScalerSPI encodeToCommandQueue:];
-[MTLFXTemporalScalerSPI debugTexture];
-[MTLFXTemporalScalerSPI currentViewToClipMatrix];
-[MTLFXTemporalScalerSPI currentWorldToViewMatrix];
-[MTLFXTemporalScalerSPI dilatedMotionVectors];
-[MTLFXTemporalScalerSPI executionMode];
-[MTLFXTemporalScalerSPI previousJitterOffset];
-[MTLFXTemporalScalerSPI previousViewToClipMatrix];
-[MTLFXTemporalScalerSPI previousWorldToViewMatrix];
-[MTLFXTemporalScalerSPI setCurrentViewToClipMatrix:];
-[MTLFXTemporalScalerSPI setCurrentWorldToViewMatrix:];
-[MTLFXTemporalScalerSPI setDebugTexture:];
-[MTLFXTemporalScalerSPI setPreviousJitterOffset:];
-[MTLFXTemporalScalerSPI setPreviousViewToClipMatrix:];
-[MTLFXTemporalScalerSPI setPreviousWorldToViewMatrix:];
```
