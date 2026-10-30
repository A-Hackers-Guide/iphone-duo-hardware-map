# `CAMCaptureEngineDevice`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDeviceInput" _captureDeviceInput;
@"AVCaptureDevice" _captureDevice;
@"AVCaptureSystemZoomSlider" _systemZoomSlider;
@"AVCaptureSystemLensSelector" _systemLensSelector;
@"AVCaptureSystemExposureBiasSlider" _systemExposureSlider;
@"<CAMCaptureEngineDeviceSystemAction>" _systemDeviceActionDelegate;
@"CAMCaptureEngine" __captureEngine;
@"CAMMemoizationCache" __videoDeviceFormatForVideoConfiguration;
@"CAMMemoizationCache" __videoSessionPresetForVideoConfiguration;
@"AVCaptureDeviceFormat" __cachedPanoramaDeviceFormat;
@"AVCaptureDeviceFormat" __cachedPortraitDeviceFormat;
@"CAMMemoizationCache" __cachedDynamicAspectRatioFormat;
```

## Properties

```
@property (T@"CAMCaptureEngine",R,W,N,V__captureEngine) _captureEngine;
@property (T@"CAMMemoizationCache",R,N,V__videoDeviceFormatForVideoConfiguration) _videoDeviceFormatForVideoConfiguration;
@property (T@"CAMMemoizationCache",R,N,V__videoSessionPresetForVideoConfiguration) _videoSessionPresetForVideoConfiguration;
@property (T@"AVCaptureDeviceFormat",R,N,V__cachedPanoramaDeviceFormat) _cachedPanoramaDeviceFormat;
@property (T@"AVCaptureDeviceFormat",R,N,V__cachedPortraitDeviceFormat) _cachedPortraitDeviceFormat;
@property (T@"CAMMemoizationCache",R,N,V__cachedDynamicAspectRatioFormat) _cachedDynamicAspectRatioFormat;
@property (T@"AVCaptureDevice",R,N,V_captureDevice) captureDevice;
@property (T@"AVCaptureDeviceInput",R,N,V_captureDeviceInput) captureDeviceInput;
@property (T@"AVCaptureSystemZoomSlider",R,N,V_systemZoomSlider) systemZoomSlider;
@property (T@"AVCaptureSystemLensSelector",R,N,V_systemLensSelector) systemLensSelector;
@property (T@"AVCaptureSystemExposureBiasSlider",R,N,V_systemExposureSlider) systemExposureSlider;
@property (T@"<CAMCaptureEngineDeviceSystemAction>",W,N,V_systemDeviceActionDelegate) systemDeviceActionDelegate;
```

## Instance methods

```
-[CAMCaptureEngineDevice systemZoomSlider];
-[CAMCaptureEngineDevice _panoramaDeviceFormatForConfiguration:];
-[CAMCaptureEngineDevice _cachedDynamicAspectRatioFormat];
-[CAMCaptureEngineDevice captureDevice];
-[CAMCaptureEngineDevice _preferredPortraitModeSessionPreset];
-[CAMCaptureEngineDevice systemExposureSlider];
-[CAMCaptureEngineDevice _deviceFormatForDynamicAspectRatioWithGraphConfiguration:deviceIsSecondary:];
-[CAMCaptureEngineDevice _videoSessionPresetForVideoConfiguration];
-[CAMCaptureEngineDevice _photoBasedModeSessionPresetWithCaptureSession:];
-[CAMCaptureEngineDevice videoDeviceFormatForGraphConfiguration:captureSession:deviceIsSecondary:];
-[CAMCaptureEngineDevice initWithEngine:captureDevice:];
-[CAMCaptureEngineDevice _preferredPhotoBasedModeSessionPreset];
-[CAMCaptureEngineDevice _videoDeviceFormatForVideoConfiguration];
-[CAMCaptureEngineDevice _keyForVideoConfiguration:videoEncodingBehavior:colorSpace:requireVideoBinned:];
-[CAMCaptureEngineDevice _portraitModeSessionPresetWithCaptureSession:];
-[CAMCaptureEngineDevice _preferredTimelapseSessionPreset];
-[CAMCaptureEngineDevice _photoBasedModeDeviceFormatWithCaptureSession:];
-[CAMCaptureEngineDevice captureDeviceInput];
-[CAMCaptureEngineDevice _portraitModeDeviceFormatWithCaptureSession:];
-[CAMCaptureEngineDevice systemLensSelector];
-[CAMCaptureEngineDevice _cachedPortraitDeviceFormat];
-[CAMCaptureEngineDevice _cachedPanoramaDeviceFormat];
-[CAMCaptureEngineDevice _captureEngine];
-[CAMCaptureEngineDevice _timelapseSessionPresetWithCaptureSession:];
-[CAMCaptureEngineDevice _highestQualityDeviceFormatForVideoConfiguration:videoEncodingBehavior:colorSpace:requireVideoBinned:];
-[CAMCaptureEngineDevice setSystemDeviceActionDelegate:];
-[CAMCaptureEngineDevice systemDeviceActionDelegate];
-[CAMCaptureEngineDevice _highestQualitySessionPresetForVideoConfiguration:videoEncodingBehavior:colorSpace:];
-[CAMCaptureEngineDevice _timelapseDeviceFormatWithCaptureSession:];
-[CAMCaptureEngineDevice videoDevicePresetForGraphConfiguration:captureSession:];
```
