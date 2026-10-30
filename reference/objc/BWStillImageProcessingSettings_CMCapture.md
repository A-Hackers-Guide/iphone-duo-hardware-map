# `BWStillImageProcessingSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"BWPhotoManifest" _photoManifest;
B _processIntelligentDistortionCorrection;
B _provideDemosaicedRaw;
B _optimizedProcessingForZoomFOVEnabled;
B _optimizedProcessingWithCropAndDownscaleEnabled;
B _preferNRFDownscaleToTargetDimensions;
B _documentScanning;
B _photoFormat;
@"NSSet" _deferredAttachedMediaKeys;
@"NSDictionary" _snapshottedLCBDatabaseByPortType;
```

## Properties

```
@property (T@"BWPhotoManifest",R,N,V_photoManifest) photoManifest;
@property (Ti,R,N) expectedClientImageCount;
@property (TB,R,N,V_processIntelligentDistortionCorrection) processIntelligentDistortionCorrection;
@property (TB,R,N,V_provideDemosaicedRaw) provideDemosaicedRaw;
@property (TB,N,V_optimizedProcessingForZoomFOVEnabled) optimizedProcessingForZoomFOVEnabled;
@property (TB,N,V_optimizedProcessingWithCropAndDownscaleEnabled) optimizedProcessingWithCropAndDownscaleEnabled;
@property (TB,N,V_preferNRFDownscaleToTargetDimensions) preferNRFDownscaleToTargetDimensions;
@property (TB,N,V_documentScanning) documentScanning;
@property (TB,N,GisPhotoFormat,V_photoFormat) photoFormat;
@property (T@"NSDictionary",C,N,V_snapshottedLCBDatabaseByPortType) snapshottedLCBDatabaseByPortType;
```

## Class methods

```
+[BWStillImageProcessingSettings supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageProcessingSettings isPhotoFormat];
-[BWStillImageProcessingSettings preferNRFDownscaleToTargetDimensions];
-[BWStillImageProcessingSettings setPreferNRFDownscaleToTargetDimensions:];
-[BWStillImageProcessingSettings documentScanning];
-[BWStillImageProcessingSettings provideDemosaicedRaw];
-[BWStillImageProcessingSettings expectedClientImageCount];
-[BWStillImageProcessingSettings setOptimizedProcessingForZoomFOVEnabled:];
-[BWStillImageProcessingSettings hasDeferredAttachedMedia:];
-[BWStillImageProcessingSettings dealloc];
-[BWStillImageProcessingSettings initWithPhotoManifest:processIntelligentDistortionCorrection:];
-[BWStillImageProcessingSettings optimizedProcessingWithCropAndDownscaleEnabled];
-[BWStillImageProcessingSettings optimizedProcessingForZoomFOVEnabled];
-[BWStillImageProcessingSettings setSnapshottedLCBDatabaseByPortType:];
-[BWStillImageProcessingSettings processIntelligentDistortionCorrection];
-[BWStillImageProcessingSettings encodeWithCoder:];
-[BWStillImageProcessingSettings photoManifest];
-[BWStillImageProcessingSettings hash];
-[BWStillImageProcessingSettings description];
-[BWStillImageProcessingSettings setDocumentScanning:];
-[BWStillImageProcessingSettings setOptimizedProcessingWithCropAndDownscaleEnabled:];
-[BWStillImageProcessingSettings initWithCoder:];
-[BWStillImageProcessingSettings _setDeferredAttachedMediaKeys:];
-[BWStillImageProcessingSettings cannotProcessDepthPhotos];
-[BWStillImageProcessingSettings isEqual:];
-[BWStillImageProcessingSettings setPhotoFormat:];
-[BWStillImageProcessingSettings snapshottedLCBDatabaseByPortType];
```
