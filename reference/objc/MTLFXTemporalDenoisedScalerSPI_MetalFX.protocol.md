# `MTLFXTemporalDenoisedScalerSPI` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLFXTemporalDenoisedScaler`
- 0 instance variables, 5 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLTexture>",&,N) debugTexture;
@property (TB,N) reset;
@property (TQ,N) inputContentWidth;
@property (TQ,N) inputContentHeight;
@property (T@"<MTLTexture>",R,N) dilatedMotionVectors;
```

## Instance methods

```
-[MTLFXTemporalDenoisedScalerSPI setReset:];
-[MTLFXTemporalDenoisedScalerSPI reset];
-[MTLFXTemporalDenoisedScalerSPI encodeToCommandQueue:];
-[MTLFXTemporalDenoisedScalerSPI debugTexture];
-[MTLFXTemporalDenoisedScalerSPI dilatedMotionVectors];
-[MTLFXTemporalDenoisedScalerSPI inputContentHeight];
-[MTLFXTemporalDenoisedScalerSPI inputContentWidth];
-[MTLFXTemporalDenoisedScalerSPI setDebugTexture:];
-[MTLFXTemporalDenoisedScalerSPI setInputContentHeight:];
-[MTLFXTemporalDenoisedScalerSPI setInputContentWidth:];
```
