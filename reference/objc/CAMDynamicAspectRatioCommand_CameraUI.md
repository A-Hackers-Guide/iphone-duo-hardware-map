# `CAMDynamicAspectRatioCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
B __configureForSecondaryDevice;
q __smartFramingFieldOfView;
q __videoDynamicAspectRatio;
q __mode;
q __videoConfiguration;
q __devicePosition;
```

## Properties

```
@property (Tq,R,N,V__smartFramingFieldOfView) _smartFramingFieldOfView;
@property (Tq,R,N,V__videoDynamicAspectRatio) _videoDynamicAspectRatio;
@property (Tq,R,N,V__mode) _mode;
@property (Tq,R,N,V__videoConfiguration) _videoConfiguration;
@property (Tq,R,N,V__devicePosition) _devicePosition;
@property (TB,R,N,V__configureForSecondaryDevice) _configureForSecondaryDevice;
```

## Instance methods

```
-[CAMDynamicAspectRatioCommand _mode];
-[CAMDynamicAspectRatioCommand _configureForSecondaryDevice];
-[CAMDynamicAspectRatioCommand _executeForCurrentDeviceWithContext:];
-[CAMDynamicAspectRatioCommand _videoConfiguration];
-[CAMDynamicAspectRatioCommand _smartFramingFieldOfView];
-[CAMDynamicAspectRatioCommand _executeForSecondaryDeviceWithContext:];
-[CAMDynamicAspectRatioCommand _videoDynamicAspectRatio];
-[CAMDynamicAspectRatioCommand _dynamicAspectRatio];
-[CAMDynamicAspectRatioCommand initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:configureForSecondaryDevice:];
-[CAMDynamicAspectRatioCommand _devicePosition];
-[CAMDynamicAspectRatioCommand initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:];
-[CAMDynamicAspectRatioCommand executeWithContext:];
-[CAMDynamicAspectRatioCommand initForSecondaryDevice];
-[CAMDynamicAspectRatioCommand copyWithZone:];
```
