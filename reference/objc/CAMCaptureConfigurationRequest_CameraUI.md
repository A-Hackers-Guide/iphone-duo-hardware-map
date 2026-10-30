# `CAMCaptureConfigurationRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureGraphConfiguration" _graphConfiguration;
q _flashMode;
q _torchMode;
d _zoomFactor;
q _photoResolution;
@"CAMPhotographicStyle" _photographicStyle;
```

## Properties

```
@property (T@"CAMCaptureGraphConfiguration",R,N,V_graphConfiguration) graphConfiguration;
@property (Tq,R,N,V_flashMode) flashMode;
@property (Tq,R,N,V_torchMode) torchMode;
@property (Td,R,N,V_zoomFactor) zoomFactor;
@property (Tq,R,N,V_photoResolution) photoResolution;
@property (T@"CAMPhotographicStyle",R,N,V_photographicStyle) photographicStyle;
```

## Instance methods

```
-[CAMCaptureConfigurationRequest photoResolution];
-[CAMCaptureConfigurationRequest zoomFactor];
-[CAMCaptureConfigurationRequest graphConfiguration];
-[CAMCaptureConfigurationRequest torchMode];
-[CAMCaptureConfigurationRequest flashMode];
-[CAMCaptureConfigurationRequest photographicStyle];
-[CAMCaptureConfigurationRequest initWithGraphConfiguration:flashMode:torchMode:zoomFactor:photoResolution:photographicStyle:];
```
