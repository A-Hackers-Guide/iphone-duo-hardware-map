# `FigMomentCaptureSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 18 instance variables, 18 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"FigCaptureIrisStillImageSettings" _stillImageSettings;
q _settingsID;
@"NSString" _captureRequestIdentifier;
Q _userInitiatedCaptureTime;
i _torchMode;
i _flashMode;
B _autoRedEyeReductionEnabled;
i _digitalFlashMode;
i _qualityPrioritization;
i _clientQualityPrioritization;
i _HDRMode;
B _autoOriginalPhotoDeliveryEnabled;
B _autoSpatialOverCaptureEnabled;
B _autoDeferredProcessingEnabled;
I _rawOutputFormat;
I _outputWidth;
I _outputHeight;
B _depthDataDeliveryEnabled;
```

## Properties

```
@property (T@"FigCaptureIrisStillImageSettings",R,N,V_stillImageSettings) stillImageSettings;
@property (Tq,R,N) settingsID;
@property (T@"NSString",R,N) captureRequestIdentifier;
@property (TQ,R,N) userInitiatedCaptureTime;
@property (Ti,N,V_torchMode) torchMode;
@property (Ti,N,V_flashMode) flashMode;
@property (TB,N,V_autoRedEyeReductionEnabled) autoRedEyeReductionEnabled;
@property (Ti,N,V_digitalFlashMode) digitalFlashMode;
@property (Ti,N,V_qualityPrioritization) qualityPrioritization;
@property (Ti,N,V_clientQualityPrioritization) clientQualityPrioritization;
@property (Ti,N,V_HDRMode) HDRMode;
@property (TB,N,GisAutoOriginalPhotoDeliveryEnabled,V_autoOriginalPhotoDeliveryEnabled) autoOriginalPhotoDeliveryEnabled;
@property (TB,N,GisAutoSpatialOverCaptureEnabled,V_autoSpatialOverCaptureEnabled) autoSpatialOverCaptureEnabled;
@property (TB,N,GisAutoDeferredProcessingEnabled,V_autoDeferredProcessingEnabled) autoDeferredProcessingEnabled;
@property (TI,N,V_rawOutputFormat) rawOutputFormat;
@property (TI,N,V_outputWidth) outputWidth;
@property (TI,N,V_outputHeight) outputHeight;
@property (TB,N,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
```

## Class methods

```
+[FigMomentCaptureSettings supportsSecureCoding];
```

## Instance methods

```
-[FigMomentCaptureSettings setClientQualityPrioritization:];
-[FigMomentCaptureSettings clientQualityPrioritization];
-[FigMomentCaptureSettings outputHeight];
-[FigMomentCaptureSettings stillImageSettings];
-[FigMomentCaptureSettings isAutoDeferredProcessingEnabled];
-[FigMomentCaptureSettings setHDRMode:];
-[FigMomentCaptureSettings digitalFlashMode];
-[FigMomentCaptureSettings setRawOutputFormat:];
-[FigMomentCaptureSettings dealloc];
-[FigMomentCaptureSettings settingsID];
-[FigMomentCaptureSettings isAutoSpatialOverCaptureEnabled];
-[FigMomentCaptureSettings qualityPrioritization];
-[FigMomentCaptureSettings setDigitalFlashMode:];
-[FigMomentCaptureSettings setAutoDeferredProcessingEnabled:];
-[FigMomentCaptureSettings setTorchMode:];
-[FigMomentCaptureSettings setQualityPrioritization:];
-[FigMomentCaptureSettings setOutputWidth:];
-[FigMomentCaptureSettings torchMode];
-[FigMomentCaptureSettings setOutputHeight:];
-[FigMomentCaptureSettings captureRequestIdentifier];
-[FigMomentCaptureSettings encodeWithCoder:];
-[FigMomentCaptureSettings setFlashMode:];
-[FigMomentCaptureSettings hash];
-[FigMomentCaptureSettings setAutoRedEyeReductionEnabled:];
-[FigMomentCaptureSettings description];
-[FigMomentCaptureSettings flashMode];
-[FigMomentCaptureSettings initWithCoder:];
-[FigMomentCaptureSettings outputWidth];
-[FigMomentCaptureSettings setDepthDataDeliveryEnabled:];
-[FigMomentCaptureSettings rawOutputFormat];
-[FigMomentCaptureSettings copyWithZone:];
-[FigMomentCaptureSettings initWithSettingsID:captureRequestIdentifier:userInitiatedCaptureTime:];
-[FigMomentCaptureSettings autoRedEyeReductionEnabled];
-[FigMomentCaptureSettings isEqual:];
-[FigMomentCaptureSettings initWithStillImageSettings:];
-[FigMomentCaptureSettings depthDataDeliveryEnabled];
-[FigMomentCaptureSettings setAutoOriginalPhotoDeliveryEnabled:];
-[FigMomentCaptureSettings isAutoOriginalPhotoDeliveryEnabled];
-[FigMomentCaptureSettings HDRMode];
-[FigMomentCaptureSettings setAutoSpatialOverCaptureEnabled:];
-[FigMomentCaptureSettings userInitiatedCaptureTime];
```
