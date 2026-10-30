# `JFXCapturePreviewRequestBuilder`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _selfieBGLoadQ;
B _logged_render_request_failure_animoji;
B _logged_render_request_failure_facetracking;
@"JFXCapturePreviewProperties" _previewProperties;
@"PVColorSpace" _outputColorSpace;
{PVTransformAnimationInfo="time"{?="value"q"timescale"i"flags"I"epoch"q}"translation"{CGPoint="x"d"y"d}"scale"d"rotation"d} _requestTransformAnimation;
```

## Properties

```
@property (T@"PVColorSpace",R,N,V_outputColorSpace) outputColorSpace;
@property (T@"JFXCapturePreviewProperties",R,N,V_previewProperties) previewProperties;
@property (T{PVTransformAnimationInfo={?=qiIq}{CGPoint=dd}dd},N,V_requestTransformAnimation) requestTransformAnimation;
```

## Instance methods

```
-[JFXCapturePreviewRequestBuilder outputColorSpace];
-[JFXCapturePreviewRequestBuilder JFX_getEffectsOfType:ofType:];
-[JFXCapturePreviewRequestBuilder JFX_visibleEffects:];
-[JFXCapturePreviewRequestBuilder createPVRenderRequestUsingAnimojiRenderer:metadataValidator:additionalTransform:effectStack:animojiTapPoint:animojiUsesInterfaceOrientation:requestHandler:];
-[JFXCapturePreviewRequestBuilder initWithPreviewProperties:outputColorSpace:];
-[JFXCapturePreviewRequestBuilder previewProperties];
-[JFXCapturePreviewRequestBuilder requestTransformAnimation];
-[JFXCapturePreviewRequestBuilder setRequestTransformAnimation:];
```
