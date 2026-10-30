# `CFXRenderer`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PVLivePlayerDelegate`
- 12 instance variables, 15 properties, 36 instance methods, 2 class methods

## Instance variables

```
B _rgbOnlyMemoji;
B _isAnimojiOnlyMode;
@"UIColor" _animojiBackgroundColor;
q _captureMode;
q _cameraMode;
@"JFXPixelRotationSession" _pixelRotationSession;
@"JFXMetadataValidator" _metadataValidator;
@"<CFXRendererDelegate>" _delegate;
@"PVLivePlayer" _livePlayer;
@"PVLivePlayerCameraSource" _cameraSource;
@"JFXAnimojiEffectRenderer" _animojiRenderer;
@"JTFrameRateCalculator" _fpsCalc;
```

## Properties

```
@property (Tq,N,V_captureMode) captureMode;
@property (Tq,R,N,V_cameraMode) cameraMode;
@property (T@"JFXPixelRotationSession",&,N,V_pixelRotationSession) pixelRotationSession;
@property (T@"JFXMetadataValidator",&,N,V_metadataValidator) metadataValidator;
@property (T@"<CFXRendererDelegate>",W,N,V_delegate) delegate;
@property (T@"PVLivePlayer",&,N,V_livePlayer) livePlayer;
@property (TB,R,N) livePlayerIsSaturated;
@property (T@"PVLivePlayerCameraSource",&,N,V_cameraSource) cameraSource;
@property (T@"JFXAnimojiEffectRenderer",&,N,V_animojiRenderer) animojiRenderer;
@property (T@"JTFrameRateCalculator",R,N,V_fpsCalc) fpsCalc;
@property (T@"UIColor",&,N,V_animojiBackgroundColor) animojiBackgroundColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXRenderer initialize];
+[CFXRenderer createBufferWith:size:];
```

## Instance methods

```
-[CFXRenderer pause];
-[CFXRenderer shutdown];
-[CFXRenderer flush];
-[CFXRenderer dealloc];
-[CFXRenderer setCaptureMode:];
-[CFXRenderer setDelegate:];
-[CFXRenderer captureMode];
-[CFXRenderer delegate];
-[CFXRenderer resume];
-[CFXRenderer animojiBackgroundColor];
-[CFXRenderer setAnimojiBackgroundColor:];
-[CFXRenderer cameraSource];
-[CFXRenderer setCameraSource:];
-[CFXRenderer cameraMode];
-[CFXRenderer pixelRotationSession];
-[CFXRenderer CFX_PVFrameSetFromCFXFrame:];
-[CFXRenderer fpsCalc];
-[CFXRenderer CFX_JTEffectsFromCFXEffectComposition:forRenderTime:];
-[CFXRenderer CFX_getPreviewColorSpace];
-[CFXRenderer animojiRenderer];
-[CFXRenderer buildRenderRequest:time:];
-[CFXRenderer createJFXAnimojiEffectRenderer];
-[CFXRenderer initWithDelegate:captureMode:];
-[CFXRenderer livePlayer];
-[CFXRenderer livePlayerDroppedFrame:sources:time:];
-[CFXRenderer livePlayerIsSaturated];
-[CFXRenderer metadataValidator];
-[CFXRenderer renderFrame:effectComposition:];
-[CFXRenderer renderRequestComplete:results:completedOutOfOrder:];
-[CFXRenderer resetMetadataValidation];
-[CFXRenderer setAnimojiRenderer:];
-[CFXRenderer setLivePlayer:];
-[CFXRenderer setMetadataValidator:];
-[CFXRenderer setPixelRotationSession:];
-[CFXRenderer setTrackingLossDelegate:];
-[CFXRenderer willDropCameraFrame];
```
