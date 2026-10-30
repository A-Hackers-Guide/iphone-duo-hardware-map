# `AVMomentCaptureSettings`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 16 instance variables, 17 properties, 37 instance methods, 3 class methods

## Instance variables

```
@"AVCapturePhotoSettings" _photoSettings;
q _uniqueID;
Q _userInitiatedCaptureTime;
q _flashMode;
B _autoRedEyeReductionEnabled;
q _digitalFlashMode;
q _photoQualityPrioritization;
q _HDRMode;
B _autoOriginalPhotoDeliveryEnabled;
B _autoSpatialOverCaptureEnabled;
B _autoDeferredPhotoDeliveryEnabled;
I _rawOutputFormat;
{?="width"i"height"i} _maxPhotoDimensions;
B _depthDataDeliveryEnabled;
q _torchMode;
@"NSString" _bravoCameraSelectionBehaviorForRecording;
```

## Properties

```
@property (Tq,R,N) uniqueID;
@property (TQ,R,N) userInitiatedCaptureTime;
@property (T@"AVCapturePhotoSettings",R,N) photoSettings;
@property (Tq,N) torchMode;
@property (T@"NSString",C,N) bravoCameraSelectionBehaviorForRecording;
@property (Tq,N) flashMode;
@property (TB,N,GisAutoRedEyeReductionEnabled,V_autoRedEyeReductionEnabled) autoRedEyeReductionEnabled;
@property (Tq,N) digitalFlashMode;
@property (Tq,N) photoQualityPrioritization;
@property (Tq,N) HDRMode;
@property (TB,N,GisAutoOriginalPhotoDeliveryEnabled,V_autoOriginalPhotoDeliveryEnabled) autoOriginalPhotoDeliveryEnabled;
@property (TB,N,GisAutoSpatialOverCaptureEnabled,V_autoSpatialOverCaptureEnabled) autoSpatialOverCaptureEnabled;
@property (TB,N,GisAutoDeferredPhotoDeliveryEnabled,V_autoDeferredPhotoDeliveryEnabled) autoDeferredPhotoDeliveryEnabled;
@property (TB,N,GisAutoDeferredProcessingEnabled) autoDeferredProcessingEnabled;
@property (TI,N,V_rawOutputFormat) rawOutputFormat;
@property (T{?=ii},N,V_maxPhotoDimensions) maxPhotoDimensions;
@property (TB,N,GisDepthDataDeliveryEnabled,V_depthDataDeliveryEnabled) depthDataDeliveryEnabled;
```

## Class methods

```
+[AVMomentCaptureSettings settingsWithPhotoSettings:];
+[AVMomentCaptureSettings settingsWithUserInitiatedCaptureTime:];
+[AVMomentCaptureSettings settingsWithUserInitiatedCaptureTime:uniqueID:];
```

## Instance methods

```
-[AVMomentCaptureSettings photoQualityPrioritization];
-[AVMomentCaptureSettings isAutoDeferredProcessingEnabled];
-[AVMomentCaptureSettings isAutoDeferredPhotoDeliveryEnabled];
-[AVMomentCaptureSettings debugDescription];
-[AVMomentCaptureSettings setHDRMode:];
-[AVMomentCaptureSettings digitalFlashMode];
-[AVMomentCaptureSettings setRawOutputFormat:];
-[AVMomentCaptureSettings dealloc];
-[AVMomentCaptureSettings isAutoSpatialOverCaptureEnabled];
-[AVMomentCaptureSettings setAutoDeferredPhotoDeliveryEnabled:];
-[AVMomentCaptureSettings setDigitalFlashMode:];
-[AVMomentCaptureSettings setAutoDeferredProcessingEnabled:];
-[AVMomentCaptureSettings setTorchMode:];
-[AVMomentCaptureSettings uniqueID];
-[AVMomentCaptureSettings isAutoRedEyeReductionEnabled];
-[AVMomentCaptureSettings torchMode];
-[AVMomentCaptureSettings isDepthDataDeliveryEnabled];
-[AVMomentCaptureSettings setFlashMode:];
-[AVMomentCaptureSettings setAutoRedEyeReductionEnabled:];
-[AVMomentCaptureSettings description];
-[AVMomentCaptureSettings flashMode];
-[AVMomentCaptureSettings maxPhotoDimensions];
-[AVMomentCaptureSettings setDepthDataDeliveryEnabled:];
-[AVMomentCaptureSettings rawOutputFormat];
-[AVMomentCaptureSettings setMaxPhotoDimensions:];
-[AVMomentCaptureSettings copyWithZone:];
-[AVMomentCaptureSettings setPhotoQualityPrioritization:];
-[AVMomentCaptureSettings setAutoOriginalPhotoDeliveryEnabled:];
-[AVMomentCaptureSettings isAutoOriginalPhotoDeliveryEnabled];
-[AVMomentCaptureSettings HDRMode];
-[AVMomentCaptureSettings setAutoSpatialOverCaptureEnabled:];
-[AVMomentCaptureSettings userInitiatedCaptureTime];
-[AVMomentCaptureSettings photoSettings];
-[AVMomentCaptureSettings _initWithPhotoSettings:];
-[AVMomentCaptureSettings _initWithUserInitiatedCaptureTime:uniqueID:];
-[AVMomentCaptureSettings bravoCameraSelectionBehaviorForRecording];
-[AVMomentCaptureSettings setBravoCameraSelectionBehaviorForRecording:];
```
