# `JFXAnimojiEffectRenderer`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PVCompositeDelegate`, `JFXSupportProtocol`
- 24 instance variables, 20 properties, 57 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _puppetLoadingQ;
@"NSObject<OS_dispatch_queue>" _puppetRenderingQ;
B _logged_render_failed;
B _rgbOnlyMemoji;
^{OpaqueVTPixelRotationSession=} _rotationSession;
^{__CVBuffer=} _mirroredDepthBuffer;
@"PTEffect" _effect;
^{OpaqueVTPixelTransferSession=} _transferSession;
^{__CVBuffer=} _segmentationPixelBuffer;
B _asynchronouslyLoadNewPuppets;
B _allowAntialiasing;
B _constrainHeadPose;
@"<JFXAnimojiTrackingLossDelegate>" _trackingLossDelegate;
@"AVTRenderer" _renderer;
@"AVTAvatarStore" _avatarStore;
@"JFXAnimojiEffect" _currentPuppet;
@"NSLock" _renderPassLock;
@"NSLock" _rendererLock;
^{__CVMetalTextureCache=} _metalTextureCache;
^{__CVPixelBufferPool=} _inputBufferPool;
^{__CVPixelBufferPool=} _deviceOrientedColorBufferPool;
d _systemTimeForAVTRenderer;
^{__CVMetalTextureCache=} _metalDepthTextureCache;
{CGSize="width"d"height"d} _workingSize;
```

## Properties

```
@property (T@"AVTRenderer",&,N,V_renderer) renderer;
@property (T@"AVTAvatarStore",&,N,V_avatarStore) avatarStore;
@property (T@"JFXAnimojiEffect",&,N,V_currentPuppet) currentPuppet;
@property (T@"NSLock",R,N,V_renderPassLock) renderPassLock;
@property (T@"NSLock",&,N,V_rendererLock) rendererLock;
@property (T^{__CVMetalTextureCache=},N,V_metalTextureCache) metalTextureCache;
@property (T{CGSize=dd},N,V_workingSize) workingSize;
@property (T^{__CVPixelBufferPool=},N,V_inputBufferPool) inputBufferPool;
@property (T^{__CVPixelBufferPool=},N,V_deviceOrientedColorBufferPool) deviceOrientedColorBufferPool;
@property (Td,N,V_systemTimeForAVTRenderer) systemTimeForAVTRenderer;
@property (T^{__CVMetalTextureCache=},N,V_metalDepthTextureCache) metalDepthTextureCache;
@property (TB,R,N,V_constrainHeadPose) constrainHeadPose;
@property (TB,R,N,V_rgbOnlyMemoji) rgbOnlyMemoji;
@property (TB,N,V_asynchronouslyLoadNewPuppets) asynchronouslyLoadNewPuppets;
@property (T@"<JFXAnimojiTrackingLossDelegate>",W,N,V_trackingLossDelegate) trackingLossDelegate;
@property (TB,N,V_allowAntialiasing) allowAntialiasing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXAnimojiEffectRenderer isSupported];
+[JFXAnimojiEffectRenderer animojiBufferSizeWithImageSize:interfaceOrientation:];
+[JFXAnimojiEffectRenderer setupAVTMetalShaderCache];
```

## Instance methods

```
-[JFXAnimojiEffectRenderer clear];
-[JFXAnimojiEffectRenderer renderer];
-[JFXAnimojiEffectRenderer init];
-[JFXAnimojiEffectRenderer flush];
-[JFXAnimojiEffectRenderer dealloc];
-[JFXAnimojiEffectRenderer description];
-[JFXAnimojiEffectRenderer setRenderer:];
-[JFXAnimojiEffectRenderer avatarStore];
-[JFXAnimojiEffectRenderer setAvatarStore:];
-[JFXAnimojiEffectRenderer JFX_blendShapesForRenderer:];
-[JFXAnimojiEffectRenderer JFX_depthDataToTexture:];
-[JFXAnimojiEffectRenderer computeHighQualitySegmentation:];
-[JFXAnimojiEffectRenderer JFX_getRenderer:forAnimojiEffect:primeFrame:captureOrientation:interfaceOrientation:backgroundColor:];
-[JFXAnimojiEffectRenderer JFX_inputBufferIsPortraitAspect:];
-[JFXAnimojiEffectRenderer JFX_focalLengthForFrame:renderer:workingSize:interfaceOrientation:];
-[JFXAnimojiEffectRenderer inputBufferPool];
-[JFXAnimojiEffectRenderer setWorkingSize:];
-[JFXAnimojiEffectRenderer allowAntialiasing];
-[JFXAnimojiEffectRenderer asyncLoadNewPuppet:currentPuppet:captureOrientation:interfaceOrientation:primeFrame:backgroundColor:];
-[JFXAnimojiEffectRenderer asynchronouslyLoadNewPuppets];
-[JFXAnimojiEffectRenderer clearRenderer_renderLocked];
-[JFXAnimojiEffectRenderer constrainHeadPose];
-[JFXAnimojiEffectRenderer createNewRendererForPuppet:];
-[JFXAnimojiEffectRenderer createTextureCaches];
-[JFXAnimojiEffectRenderer currentPuppet];
-[JFXAnimojiEffectRenderer currentPuppetIsEqualTo:];
-[JFXAnimojiEffectRenderer deviceOrientedColorBufferPool];
-[JFXAnimojiEffectRenderer initWithConstrainedHeadPose:rgbOnlyMemoji:];
-[JFXAnimojiEffectRenderer metalDepthTextureCache];
-[JFXAnimojiEffectRenderer metalTextureCache];
-[JFXAnimojiEffectRenderer newPixelBufferRenderedFromARFrame:withEffect:depthData:captureOrientation:interfaceOrientation:preRecordedBlendShapes:backgroundColor:];
-[JFXAnimojiEffectRenderer preRecordedBlendShapesForFrame:captureOrientation:interfaceOrientation:backgroundColor:];
-[JFXAnimojiEffectRenderer renderAnimoji:withPresentationTime:frame:depthData:backgroundColor:completionBlock:];
-[JFXAnimojiEffectRenderer renderFrame:withEffect:depthData:captureOrientation:interfaceOrientation:preRecordedBlendShapes:backgroundColor:completionBlock:];
-[JFXAnimojiEffectRenderer renderPassLock];
-[JFXAnimojiEffectRenderer renderWithInputs:time:userContext:compositeContext:];
-[JFXAnimojiEffectRenderer renderWithTime:metadata:];
-[JFXAnimojiEffectRenderer rendererLock];
-[JFXAnimojiEffectRenderer rgbOnlyMemoji];
-[JFXAnimojiEffectRenderer setAllowAntialiasing:];
-[JFXAnimojiEffectRenderer setAsynchronouslyLoadNewPuppets:];
-[JFXAnimojiEffectRenderer setCurrentPuppet:];
-[JFXAnimojiEffectRenderer setDeviceOrientedColorBufferPool:];
-[JFXAnimojiEffectRenderer setInputBufferPool:];
-[JFXAnimojiEffectRenderer setMetalDepthTextureCache:];
-[JFXAnimojiEffectRenderer setMetalTextureCache:];
-[JFXAnimojiEffectRenderer setRendererLock:];
-[JFXAnimojiEffectRenderer setSystemTimeForAVTRenderer:];
-[JFXAnimojiEffectRenderer setTrackingLossDelegate:];
-[JFXAnimojiEffectRenderer setupHeadPoseAndBlendShapesForFrame:forRenderer:captureOrientation:interfaceOrientation:isInitialSetup:];
-[JFXAnimojiEffectRenderer setupInputBufferPoolForSize:capturedImage:];
-[JFXAnimojiEffectRenderer setupPoseForPreRecordedBlendShapes:forRenderer:captureOrientation:interfaceOrientation:withFrame:];
-[JFXAnimojiEffectRenderer systemTimeForAVTRenderer];
-[JFXAnimojiEffectRenderer trackingLossDelegate];
-[JFXAnimojiEffectRenderer updateCurrentRenderer:withPuppet:];
-[JFXAnimojiEffectRenderer useDepth];
-[JFXAnimojiEffectRenderer workingSize];
```
