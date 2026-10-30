# `CAMStillImageCaptureResolvedSettings`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _HDREnabled;
B _portraitEffectEnabled;
B _nightModeCaptureHasInitialPreviewFeedbackSensitivity;
B _nightModeCaptureHasConstantPreviewFeedbackSensitivity;
B _captureBeforeResolvingSettingsEnabled;
B _personalPhotographerDuplicate;
d _nightModeCaptureTime;
^{CGColor=} _nightModePreviewColorEstimate;
```

## Properties

```
@property (TB,R,N,GisHDREnabled,V_HDREnabled) HDREnabled;
@property (TB,R,N,GisPortraitEffectEnabled,V_portraitEffectEnabled) portraitEffectEnabled;
@property (Td,R,N,V_nightModeCaptureTime) nightModeCaptureTime;
@property (T^{CGColor=},R,N,V_nightModePreviewColorEstimate) nightModePreviewColorEstimate;
@property (TB,R,N,V_nightModeCaptureHasInitialPreviewFeedbackSensitivity) nightModeCaptureHasInitialPreviewFeedbackSensitivity;
@property (TB,R,N,V_nightModeCaptureHasConstantPreviewFeedbackSensitivity) nightModeCaptureHasConstantPreviewFeedbackSensitivity;
@property (TB,R,N,GisCaptureBeforeResolvingSettingsEnabled,V_captureBeforeResolvingSettingsEnabled) captureBeforeResolvingSettingsEnabled;
@property (TB,R,N,GisPersonalPhotographerDuplicate,V_personalPhotographerDuplicate) personalPhotographerDuplicate;
```

## Instance methods

```
-[CAMStillImageCaptureResolvedSettings isPersonalPhotographerDuplicate];
-[CAMStillImageCaptureResolvedSettings isPortraitEffectEnabled];
-[CAMStillImageCaptureResolvedSettings dealloc];
-[CAMStillImageCaptureResolvedSettings isHDREnabled];
-[CAMStillImageCaptureResolvedSettings isCaptureBeforeResolvingSettingsEnabled];
-[CAMStillImageCaptureResolvedSettings initWithHDREnabled:portraitEffectEnabled:nightModeCaptureTime:nightModePreviewColorEstimate:nightModeCaptureHasInitialPreviewFeedbackSensitivity:nightModeCaptureHasConstantPreviewFeedbackSensitivity:captureBeforeResolvingSettingsEnabled:personalPhotographerDuplicate:];
-[CAMStillImageCaptureResolvedSettings nightModeCaptureHasConstantPreviewFeedbackSensitivity];
-[CAMStillImageCaptureResolvedSettings nightModeCaptureHasInitialPreviewFeedbackSensitivity];
-[CAMStillImageCaptureResolvedSettings nightModeCaptureTime];
-[CAMStillImageCaptureResolvedSettings nightModePreviewColorEstimate];
```
