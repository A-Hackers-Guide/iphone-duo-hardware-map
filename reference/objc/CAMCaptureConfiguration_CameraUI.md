# `CAMCaptureConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 33 instance variables, 34 properties, 42 instance methods, 5 class methods

## Instance variables

```
B _mixAudioWithOthers;
B _mirrorFrontCameraCaptures;
B _photoBooth;
B _zoomPIPEnabled;
B _optionalDepthEffectEnabled;
B _frontRearSimultaneousVideoEnabled;
B _personalPhotographerEnabled;
q _mode;
q _device;
q _videoConfiguration;
Q _audioConfiguration;
q _flashMode;
q _torchMode;
q _HDRMode;
q _timerDuration;
q _irisMode;
q _photoModeAspectRatioCrop;
q _photoModeEffectFilterType;
q _squareModeEffectFilterType;
q _portraitModeEffectFilterType;
q _portraitModeLightingEffectType;
@"NSDictionary" _exposureBiasesByMode;
d _explicitPortraitModeApertureValue;
d _portraitModeIntensityValue;
q _macroMode;
q _photoResolution;
q _rawMode;
q _proResVideoMode;
@"NSArray" _semanticStyles;
Q _semanticStylesSelectedIndex;
@"CAMPhotographicStylesModel" _stylesModel;
q _videoStabilizationMode;
q _sharedLibraryMode;
```

## Properties

```
@property (Tq,R,N,V_mode) mode;
@property (Tq,R,N,V_device) device;
@property (Tq,R,N) devicePosition;
@property (Tq,R,N,V_videoConfiguration) videoConfiguration;
@property (TQ,R,N,V_audioConfiguration) audioConfiguration;
@property (TB,R,N,V_mixAudioWithOthers) mixAudioWithOthers;
@property (Tq,R,N,V_flashMode) flashMode;
@property (Tq,R,N,V_torchMode) torchMode;
@property (Tq,R,N,V_HDRMode) HDRMode;
@property (Tq,R,N,V_timerDuration) timerDuration;
@property (Tq,R,N,V_irisMode) irisMode;
@property (Tq,R,N,V_photoModeAspectRatioCrop) photoModeAspectRatioCrop;
@property (Tq,R,N,V_photoModeEffectFilterType) photoModeEffectFilterType;
@property (Tq,R,N,V_squareModeEffectFilterType) squareModeEffectFilterType;
@property (Tq,R,N,V_portraitModeEffectFilterType) portraitModeEffectFilterType;
@property (Tq,R,N,V_portraitModeLightingEffectType) portraitModeLightingEffectType;
@property (T@"NSDictionary",R,N,V_exposureBiasesByMode) exposureBiasesByMode;
@property (Td,R,N,V_explicitPortraitModeApertureValue) explicitPortraitModeApertureValue;
@property (Td,R,N,V_portraitModeIntensityValue) portraitModeIntensityValue;
@property (TB,N,V_mirrorFrontCameraCaptures) mirrorFrontCameraCaptures;
@property (Tq,R,N,V_macroMode) macroMode;
@property (Tq,R,N,V_photoResolution) photoResolution;
@property (Tq,R,N,V_rawMode) rawMode;
@property (Tq,R,N,V_proResVideoMode) proResVideoMode;
@property (T@"NSArray",&,N,V_semanticStyles) semanticStyles;
@property (TQ,N,V_semanticStylesSelectedIndex) semanticStylesSelectedIndex;
@property (T@"CAMPhotographicStylesModel",R,N,V_stylesModel) stylesModel;
@property (TB,R,N,GisPhotoBooth,V_photoBooth) photoBooth;
@property (Tq,R,N,V_videoStabilizationMode) videoStabilizationMode;
@property (TB,R,N,V_zoomPIPEnabled) zoomPIPEnabled;
@property (TB,R,N,V_optionalDepthEffectEnabled) optionalDepthEffectEnabled;
@property (Tq,N,V_sharedLibraryMode) sharedLibraryMode;
@property (TB,R,N,V_frontRearSimultaneousVideoEnabled) frontRearSimultaneousVideoEnabled;
@property (TB,R,N,V_personalPhotographerEnabled) personalPhotographerEnabled;
```

## Class methods

```
+[CAMCaptureConfiguration _fallbackVideoConfigurationForUnsupportedConfiguration:frontRearSimultaneousVideoEnabled:];
+[CAMCaptureConfiguration captureGraphConfigurationUsingConfiguration:outputToExternalStorage:captureOrientation:];
+[CAMCaptureConfiguration captureGraphConfigurationUsingConfiguration:outputToExternalStorage:captureOrientation:deviceDirection:];
+[CAMCaptureConfiguration previewConfigurationForMode:histogramEnabled:videoThumbnailOutputEnabled:duplicatePreviewLayerEnabled:];
+[CAMCaptureConfiguration sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:];
```

## Instance methods

```
-[CAMCaptureConfiguration personalPhotographerEnabled];
-[CAMCaptureConfiguration isPhotoBooth];
-[CAMCaptureConfiguration portraitModeLightingEffectType];
-[CAMCaptureConfiguration irisMode];
-[CAMCaptureConfiguration rawMode];
-[CAMCaptureConfiguration photoModeAspectRatioCrop];
-[CAMCaptureConfiguration portraitModeEffectFilterType];
-[CAMCaptureConfiguration photoResolution];
-[CAMCaptureConfiguration mixAudioWithOthers];
-[CAMCaptureConfiguration timerDuration];
-[CAMCaptureConfiguration optionalDepthEffectEnabled];
-[CAMCaptureConfiguration semanticStyles];
-[CAMCaptureConfiguration sharedLibraryMode];
-[CAMCaptureConfiguration videoConfiguration];
-[CAMCaptureConfiguration device];
-[CAMCaptureConfiguration explicitPortraitModeApertureValue];
-[CAMCaptureConfiguration setMirrorFrontCameraCaptures:];
-[CAMCaptureConfiguration initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:mixAudioWithOthers:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:explicitPortraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:photoResolution:rawMode:proResVideoMode:semanticStyles:semanticStylesSelectedIndex:stylesModel:videoStabilizationMode:zoomPIPEnabled:optionalDepthEffectEnabled:sharedLibraryMode:frontRearSimultaneousVideoEnabled:personalPhotographerEnabled:];
-[CAMCaptureConfiguration exposureBiasesByMode];
-[CAMCaptureConfiguration frontRearSimultaneousVideoEnabled];
-[CAMCaptureConfiguration stylesModel];
-[CAMCaptureConfiguration zoomPIPEnabled];
-[CAMCaptureConfiguration setSharedLibraryMode:];
-[CAMCaptureConfiguration portraitModeIntensityValue];
-[CAMCaptureConfiguration torchMode];
-[CAMCaptureConfiguration mirrorFrontCameraCaptures];
-[CAMCaptureConfiguration proResVideoMode];
-[CAMCaptureConfiguration mode];
-[CAMCaptureConfiguration devicePosition];
-[CAMCaptureConfiguration audioConfiguration];
-[CAMCaptureConfiguration setSemanticStylesSelectedIndex:];
-[CAMCaptureConfiguration squareModeEffectFilterType];
-[CAMCaptureConfiguration flashMode];
-[CAMCaptureConfiguration semanticStylesSelectedIndex];
-[CAMCaptureConfiguration _previewFilters];
-[CAMCaptureConfiguration photoModeEffectFilterType];
-[CAMCaptureConfiguration setSemanticStyles:];
-[CAMCaptureConfiguration videoStabilizationMode];
-[CAMCaptureConfiguration macroMode];
-[CAMCaptureConfiguration currentPhotographicStyle];
-[CAMCaptureConfiguration initForPhotoBoothWithCaptureDevice:];
-[CAMCaptureConfiguration HDRMode];
```
