# `CAMPreparePhotoSettingsCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureConfigurationRequest" __configurationRequest;
@"CAMStillImageCaptureRequest" __stillImageCaptureRequest;
```

## Properties

```
@property (T@"CAMCaptureConfigurationRequest",R,N,V__configurationRequest) _configurationRequest;
@property (T@"CAMStillImageCaptureRequest",R,N,V__stillImageCaptureRequest) _stillImageCaptureRequest;
```

## Instance methods

```
-[CAMPreparePhotoSettingsCommand _executeWithPhotoOutput:mode:device:encoding:quality:resolution:];
-[CAMPreparePhotoSettingsCommand executeWithContext:];
-[CAMPreparePhotoSettingsCommand _stillImageCaptureRequest];
-[CAMPreparePhotoSettingsCommand _configurationRequest];
-[CAMPreparePhotoSettingsCommand copyWithZone:];
-[CAMPreparePhotoSettingsCommand _photoSettingsForEncoding:photoOutput:];
-[CAMPreparePhotoSettingsCommand initWithConfigurationRequest:];
-[CAMPreparePhotoSettingsCommand initWithStillImageCaptureRequest:];
```
