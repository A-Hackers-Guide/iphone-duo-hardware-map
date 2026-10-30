# `CAMRampToVideoZoomFactorCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
f __rate;
d __videoZoomFactor;
d __duration;
q __videoZoomRampTuning;
@"CAMCaptureGraphConfiguration" __graphConfiguration;
```

## Properties

```
@property (Td,R,N,V__videoZoomFactor) _videoZoomFactor;
@property (Tf,R,N,V__rate) _rate;
@property (Td,R,N,V__duration) _duration;
@property (Tq,R,N,V__videoZoomRampTuning) _videoZoomRampTuning;
@property (T@"CAMCaptureGraphConfiguration",R,N,V__graphConfiguration) _graphConfiguration;
```

## Instance methods

```
-[CAMRampToVideoZoomFactorCommand _duration];
-[CAMRampToVideoZoomFactorCommand _graphConfiguration];
-[CAMRampToVideoZoomFactorCommand executeWithContext:];
-[CAMRampToVideoZoomFactorCommand copyWithZone:];
-[CAMRampToVideoZoomFactorCommand _rate];
-[CAMRampToVideoZoomFactorCommand _videoZoomFactor];
-[CAMRampToVideoZoomFactorCommand _videoZoomRampTuning];
-[CAMRampToVideoZoomFactorCommand initWithVideoZoomFactor:duration:zoomRampTuning:graphConfiguration:];
-[CAMRampToVideoZoomFactorCommand initWithVideoZoomFactor:rate:graphConfiguration:];
```
