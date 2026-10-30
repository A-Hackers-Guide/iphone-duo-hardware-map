# `CAMStillImageCaptureResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 20 properties, 26 instance methods, 0 class methods

## Instance variables

```
B _shouldPersistAdjustmentSidecar;
B _representsDeferredFilteredProxy;
B _expectingPairedVideo;
^{__IOSurface=} _stillImageFullsizeSurface;
Q _stillImageFullsizeSurfaceSize;
^{__IOSurface=} _stillImageUnfilteredPreviewSurface;
^{__IOSurface=} _stillImageFilteredPreviewSurface;
@"AVCapturePhoto" _capturePhoto;
@"NSString" _deferredPhotoIdentifier;
@"NSDate" _captureDate;
@"NSDictionary" _metadata;
@"NSError" _error;
@"NSArray" _adjustmentFilters;
@"NSString" _persistenceUUID;
@"CAMCaptureCoordinationInfo" _coordinationInfo;
q _semanticEnhancement;
```

## Properties

```
@property (T^{__IOSurface=},R,N,V_stillImageFullsizeSurface) stillImageFullsizeSurface;
@property (TQ,R,N,V_stillImageFullsizeSurfaceSize) stillImageFullsizeSurfaceSize;
@property (T^{__IOSurface=},R,N,V_stillImageUnfilteredPreviewSurface) stillImageUnfilteredPreviewSurface;
@property (T^{__IOSurface=},R,N,V_stillImageFilteredPreviewSurface) stillImageFilteredPreviewSurface;
@property (T@"AVCapturePhoto",R,N,V_capturePhoto) capturePhoto;
@property (T@"NSString",R,C,N,V_deferredPhotoIdentifier) deferredPhotoIdentifier;
@property (T@"NSDate",R,N,V_captureDate) captureDate;
@property (T@"NSDictionary",R,C,N,V_metadata) metadata;
@property (T@"NSDictionary",R,N) compactMetadata;
@property (T@"NSError",R,N,V_error) error;
@property (TB,R,N,V_shouldPersistAdjustmentSidecar) shouldPersistAdjustmentSidecar;
@property (T@"NSArray",R,N,V_adjustmentFilters) adjustmentFilters;
@property (TB,R,N,V_representsDeferredFilteredProxy) representsDeferredFilteredProxy;
@property (T@"NSString",R,C,N,V_persistenceUUID) persistenceUUID;
@property (T@"CAMCaptureCoordinationInfo",R,N,V_coordinationInfo) coordinationInfo;
@property (T@"NSString",R,C,N) imageGroupIdentifier;
@property (TB,R,N,GisExpectingPairedVideo,V_expectingPairedVideo) expectingPairedVideo;
@property (Tq,R,N,V_semanticEnhancement) semanticEnhancement;
@property (T{?=ii},R,N) predictedFinalAssetPhotoDimensions;
@property (TB,R,N,GisPromotedProxyImage) promotedProxyImage;
```

## Instance methods

```
-[CAMStillImageCaptureResult adjustmentFilters];
-[CAMStillImageCaptureResult persistenceUUID];
-[CAMStillImageCaptureResult capturePhoto];
-[CAMStillImageCaptureResult isExpectingPairedVideo];
-[CAMStillImageCaptureResult captureDate];
-[CAMStillImageCaptureResult _captureDateFromMetadata:];
-[CAMStillImageCaptureResult stillImageFullsizeSurface];
-[CAMStillImageCaptureResult isPromotedProxyImage];
-[CAMStillImageCaptureResult deferredPhotoIdentifier];
-[CAMStillImageCaptureResult dealloc];
-[CAMStillImageCaptureResult stillImageUnfilteredPreviewSurface];
-[CAMStillImageCaptureResult representsDeferredFilteredProxy];
-[CAMStillImageCaptureResult imageGroupIdentifier];
-[CAMStillImageCaptureResult error];
-[CAMStillImageCaptureResult compactMetadata];
-[CAMStillImageCaptureResult metadata];
-[CAMStillImageCaptureResult initWithCapturePhoto:expectingPairedVideo:adjustmentFilters:filteredPreviewSurface:shouldPersistAdjustmentSidecar:persistenceUUID:coordinationInfo:semanticEnhancement:error:];
-[CAMStillImageCaptureResult stillImageFullsizeSurfaceSize];
-[CAMStillImageCaptureResult description];
-[CAMStillImageCaptureResult initWithFullsizeSurface:size:unfilteredPreviewSurface:filteredPreviewSurface:metadata:expectingPairedVideo:shouldPersistAdjustmentSidecar:adjustmentFilters:persistenceUUID:coordinationInfo:error:];
-[CAMStillImageCaptureResult stillImageFilteredPreviewSurface];
-[CAMStillImageCaptureResult shouldPersistAdjustmentSidecar];
-[CAMStillImageCaptureResult coordinationInfo];
-[CAMStillImageCaptureResult initWithCaptureDeferredPhotoProxy:expectingPairedVideo:adjustmentFilters:filteredPreviewSurface:shouldPersistAdjustmentSidecar:persistenceUUID:coordinationInfo:semanticEnhancement:error:];
-[CAMStillImageCaptureResult semanticEnhancement];
-[CAMStillImageCaptureResult predictedFinalAssetPhotoDimensions];
```
