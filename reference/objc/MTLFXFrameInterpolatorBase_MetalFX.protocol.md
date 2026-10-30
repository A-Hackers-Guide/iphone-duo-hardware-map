# `MTLFXFrameInterpolatorBase` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 48 properties, 82 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) colorTextureUsage;
@property (TQ,R,N) outputTextureUsage;
@property (TQ,R,N) depthTextureUsage;
@property (TQ,R,N) motionTextureUsage;
@property (TQ,R,N) uiTextureUsage;
@property (TQ,R,N) colorTextureFormat;
@property (TQ,R,N) depthTextureFormat;
@property (TQ,R,N) motionTextureFormat;
@property (TQ,R,N) outputTextureFormat;
@property (TQ,R,N) inputWidth;
@property (TQ,R,N) inputHeight;
@property (TQ,R,N) outputWidth;
@property (TQ,R,N) outputHeight;
@property (TQ,R,N) uiTextureFormat;
@property (TQ,N) contentWidth;
@property (TQ,N) contentHeight;
@property (TQ,N) depthContentOffsetX;
@property (TQ,N) depthContentOffsetY;
@property (TQ,N) motionContentOffsetX;
@property (TQ,N) motionContentOffsetY;
@property (TQ,N) outputOffsetX;
@property (TQ,N) outputOffsetY;
@property (TQ,N) distortionOffsetX;
@property (TQ,N) distortionOffsetY;
@property (TQ,N) distortionWidth;
@property (TQ,N) distortionHeight;
@property (T@"<MTLTexture>",&,N) colorTexture;
@property (T@"<MTLTexture>",&,N) prevColorTexture;
@property (T@"<MTLTexture>",&,N) depthTexture;
@property (T@"<MTLTexture>",&,N) motionTexture;
@property (Tf,N) motionVectorScaleX;
@property (Tf,N) motionVectorScaleY;
@property (Tf,N) deltaTime;
@property (Tf,N) nearPlane;
@property (Tf,N) farPlane;
@property (Tf,N) fieldOfView;
@property (Tf,N) aspectRatio;
@property (T{?=[4]},N) worldToViewMatrix;
@property (T{?=[4]},N) viewToClipMatrix;
@property (T@"<MTLTexture>",&,N,SsetUITexture:) uiTexture;
@property (Tf,N) jitterOffsetX;
@property (Tf,N) jitterOffsetY;
@property (TB,N,GisUITextureComposited,SsetIsUITextureComposited:) uiTextureComposited;
@property (TB,N) shouldResetHistory;
@property (T@"<MTLTexture>",&,N) outputTexture;
@property (T@"<MTLTexture>",&,N) distortionTexture;
@property (T@"<MTLFence>",&,N) fence;
@property (TB,N,GisDepthReversed) depthReversed;
```

## Instance methods

```
-[MTLFXFrameInterpolatorBase outputHeight];
-[MTLFXFrameInterpolatorBase setContentWidth:];
-[MTLFXFrameInterpolatorBase aspectRatio];
-[MTLFXFrameInterpolatorBase setAspectRatio:];
-[MTLFXFrameInterpolatorBase deltaTime];
-[MTLFXFrameInterpolatorBase setOutputTexture:];
-[MTLFXFrameInterpolatorBase outputTexture];
-[MTLFXFrameInterpolatorBase contentWidth];
-[MTLFXFrameInterpolatorBase outputWidth];
-[MTLFXFrameInterpolatorBase contentHeight];
-[MTLFXFrameInterpolatorBase setFieldOfView:];
-[MTLFXFrameInterpolatorBase inputHeight];
-[MTLFXFrameInterpolatorBase fieldOfView];
-[MTLFXFrameInterpolatorBase inputWidth];
-[MTLFXFrameInterpolatorBase setContentHeight:];
-[MTLFXFrameInterpolatorBase depthTexture];
-[MTLFXFrameInterpolatorBase setColorTexture:];
-[MTLFXFrameInterpolatorBase setDepthReversed:];
-[MTLFXFrameInterpolatorBase setDepthTexture:];
-[MTLFXFrameInterpolatorBase setJitterOffsetX:];
-[MTLFXFrameInterpolatorBase setJitterOffsetY:];
-[MTLFXFrameInterpolatorBase setMotionTexture:];
-[MTLFXFrameInterpolatorBase setMotionVectorScaleX:];
-[MTLFXFrameInterpolatorBase setMotionVectorScaleY:];
-[MTLFXFrameInterpolatorBase setViewToClipMatrix:];
-[MTLFXFrameInterpolatorBase setWorldToViewMatrix:];
-[MTLFXFrameInterpolatorBase colorTexture];
-[MTLFXFrameInterpolatorBase distortionWidth];
-[MTLFXFrameInterpolatorBase isDepthReversed];
-[MTLFXFrameInterpolatorBase uiTextureFormat];
-[MTLFXFrameInterpolatorBase colorTextureFormat];
-[MTLFXFrameInterpolatorBase colorTextureUsage];
-[MTLFXFrameInterpolatorBase depthContentOffsetX];
-[MTLFXFrameInterpolatorBase depthContentOffsetY];
-[MTLFXFrameInterpolatorBase depthTextureFormat];
-[MTLFXFrameInterpolatorBase depthTextureUsage];
-[MTLFXFrameInterpolatorBase distortionHeight];
-[MTLFXFrameInterpolatorBase distortionOffsetX];
-[MTLFXFrameInterpolatorBase distortionOffsetY];
-[MTLFXFrameInterpolatorBase distortionTexture];
-[MTLFXFrameInterpolatorBase farPlane];
-[MTLFXFrameInterpolatorBase fence];
-[MTLFXFrameInterpolatorBase isUITextureComposited];
-[MTLFXFrameInterpolatorBase jitterOffsetX];
-[MTLFXFrameInterpolatorBase jitterOffsetY];
-[MTLFXFrameInterpolatorBase motionContentOffsetX];
-[MTLFXFrameInterpolatorBase motionContentOffsetY];
-[MTLFXFrameInterpolatorBase motionTexture];
-[MTLFXFrameInterpolatorBase motionTextureFormat];
-[MTLFXFrameInterpolatorBase motionTextureUsage];
-[MTLFXFrameInterpolatorBase motionVectorScaleX];
-[MTLFXFrameInterpolatorBase motionVectorScaleY];
-[MTLFXFrameInterpolatorBase nearPlane];
-[MTLFXFrameInterpolatorBase outputOffsetX];
-[MTLFXFrameInterpolatorBase outputOffsetY];
-[MTLFXFrameInterpolatorBase outputTextureFormat];
-[MTLFXFrameInterpolatorBase outputTextureUsage];
-[MTLFXFrameInterpolatorBase prevColorTexture];
-[MTLFXFrameInterpolatorBase setDeltaTime:];
-[MTLFXFrameInterpolatorBase setDepthContentOffsetX:];
-[MTLFXFrameInterpolatorBase setDepthContentOffsetY:];
-[MTLFXFrameInterpolatorBase setDistortionHeight:];
-[MTLFXFrameInterpolatorBase setDistortionOffsetX:];
-[MTLFXFrameInterpolatorBase setDistortionOffsetY:];
-[MTLFXFrameInterpolatorBase setDistortionTexture:];
-[MTLFXFrameInterpolatorBase setDistortionWidth:];
-[MTLFXFrameInterpolatorBase setFarPlane:];
-[MTLFXFrameInterpolatorBase setFence:];
-[MTLFXFrameInterpolatorBase setIsUITextureComposited:];
-[MTLFXFrameInterpolatorBase setMotionContentOffsetX:];
-[MTLFXFrameInterpolatorBase setMotionContentOffsetY:];
-[MTLFXFrameInterpolatorBase setNearPlane:];
-[MTLFXFrameInterpolatorBase setOutputOffsetX:];
-[MTLFXFrameInterpolatorBase setOutputOffsetY:];
-[MTLFXFrameInterpolatorBase setPrevColorTexture:];
-[MTLFXFrameInterpolatorBase setShouldResetHistory:];
-[MTLFXFrameInterpolatorBase setUITexture:];
-[MTLFXFrameInterpolatorBase shouldResetHistory];
-[MTLFXFrameInterpolatorBase uiTexture];
-[MTLFXFrameInterpolatorBase uiTextureUsage];
-[MTLFXFrameInterpolatorBase viewToClipMatrix];
-[MTLFXFrameInterpolatorBase worldToViewMatrix];
```
