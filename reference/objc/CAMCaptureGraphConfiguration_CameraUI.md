# `CAMCaptureGraphConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 44 instance variables, 52 properties, 60 instance methods, 0 class methods

## Instance variables

```
B _mixAudioWithOthers;
B _enableAutoFPSVideo;
B _videoHDRSuspended;
B _captureMirrored;
B _previewMirrored;
B _enableRAWCaptureIfSupported;
B _enableContentAwareDistortionCorrection;
B _enableResponsiveShutter;
B _suspendLivePhotoCapture;
B _videoBinned;
B _enableMRCMetadata;
B _enableTextRegionMetadata;
B _enableDepthSuggestion;
B _enableZoomPIP;
B _windNoiseRemovalEnabled;
B _audioZoomEnabled;
B _trueVideoEnabled;
B _prefersHDR10BitVideo;
B _frontRearSimultaneousVideoEnabled;
B _personalPhotographerEnabled;
q _mode;
q _device;
q _macroMode;
q _videoConfiguration;
Q _audioConfiguration;
Q _previewConfiguration;
q _previewSampleBufferVideoFormat;
@"NSArray" _previewFilters;
@"CAMVideoThumbnailOutputConfiguration" _videoThumbnailOutputConfiguration;
q _photoEncodingBehavior;
q _videoEncodingBehavior;
q _aspectRatioCrop;
q _photoQualityPrioritization;
Q _semanticStyleSupport;
@"CAMSemanticStyle" _previewSemanticStyle;
@"NSArray" _smartStyles;
Q _disabledExposureCompensationFeatures;
q _videoStabilizationStrength;
q _maximumPhotoResolution;
q _photoPerformancePriority;
q _colorSpace;
@"NSArray" _customLensGroup;
q _videoDynamicAspectRatio;
q _smartFramingFieldOfView;
```

## Properties

```
@property (Tq,R,N,V_mode) mode;
@property (Tq,R,N) devicePosition;
@property (Tq,R,N,V_device) device;
@property (Tq,R,N,V_macroMode) macroMode;
@property (Tq,R,N,V_videoConfiguration) videoConfiguration;
@property (Tq,R,N) secondaryDeviceVideoConfiguration;
@property (TB,R,N) secondaryDeviceUsesPrimaryVideoConfigurationForFrameRate;
@property (TB,R,N,GisSecondaryDeviceVideoBinned) secondaryDeviceVideoBinned;
@property (TQ,R,N,V_audioConfiguration) audioConfiguration;
@property (TB,R,N,V_mixAudioWithOthers) mixAudioWithOthers;
@property (TQ,R,N,V_previewConfiguration) previewConfiguration;
@property (Tq,R,N,V_previewSampleBufferVideoFormat) previewSampleBufferVideoFormat;
@property (T@"NSArray",R,N,V_previewFilters) previewFilters;
@property (T@"CAMVideoThumbnailOutputConfiguration",R,N,V_videoThumbnailOutputConfiguration) videoThumbnailOutputConfiguration;
@property (Tq,R,N,V_photoEncodingBehavior) photoEncodingBehavior;
@property (Tq,R,N,V_videoEncodingBehavior) videoEncodingBehavior;
@property (TB,R,N,V_enableAutoFPSVideo) enableAutoFPSVideo;
@property (TB,R,N,GisVideoHDRSuspended,V_videoHDRSuspended) videoHDRSuspended;
@property (Tq,R,N,V_aspectRatioCrop) aspectRatioCrop;
@property (Tq,R,N,V_photoQualityPrioritization) photoQualityPrioritization;
@property (TB,R,N,GisCaptureMirrored,V_captureMirrored) captureMirrored;
@property (TB,R,N,GisPreviewMirrored,V_previewMirrored) previewMirrored;
@property (TB,R,N) isFrontCameraUsedAsBackCamera;
@property (TB,R,N,V_enableRAWCaptureIfSupported) enableRAWCaptureIfSupported;
@property (TQ,R,N,V_semanticStyleSupport) semanticStyleSupport;
@property (T@"CAMSemanticStyle",R,N,V_previewSemanticStyle) previewSemanticStyle;
@property (T@"NSArray",R,N,V_smartStyles) smartStyles;
@property (TB,R,N,V_enableContentAwareDistortionCorrection) enableContentAwareDistortionCorrection;
@property (TQ,R,N,V_disabledExposureCompensationFeatures) disabledExposureCompensationFeatures;
@property (TB,R,N,V_enableResponsiveShutter) enableResponsiveShutter;
@property (TB,R,N,V_suspendLivePhotoCapture) suspendLivePhotoCapture;
@property (Tq,R,N,V_videoStabilizationStrength) videoStabilizationStrength;
@property (Tq,R,N) secondaryDeviceVideoStabilizationStrength;
@property (Tq,R,N,V_maximumPhotoResolution) maximumPhotoResolution;
@property (Tq,R,N,V_photoPerformancePriority) photoPerformancePriority;
@property (Tq,R,N,V_colorSpace) colorSpace;
@property (TB,R,N,GisVideoBinned,V_videoBinned) videoBinned;
@property (Tq,R,N) secondaryDeviceColorSpace;
@property (TB,R,N,V_enableMRCMetadata) enableMRCMetadata;
@property (TB,R,N,V_enableTextRegionMetadata) enableTextRegionMetadata;
@property (TB,R,N,V_enableDepthSuggestion) enableDepthSuggestion;
@property (TB,R,N,V_enableZoomPIP) enableZoomPIP;
@property (T@"NSArray",R,N,V_customLensGroup) customLensGroup;
@property (TB,R,N,V_windNoiseRemovalEnabled) windNoiseRemovalEnabled;
@property (TB,R,N,V_audioZoomEnabled) audioZoomEnabled;
@property (TB,R,N,V_trueVideoEnabled) trueVideoEnabled;
@property (TB,R,N,V_prefersHDR10BitVideo) prefersHDR10BitVideo;
@property (TB,R,N,V_frontRearSimultaneousVideoEnabled) frontRearSimultaneousVideoEnabled;
@property (Tq,R,N,V_videoDynamicAspectRatio) videoDynamicAspectRatio;
@property (Tq,R,N) secondaryDeviceVideoDynamicAspectRatio;
@property (Tq,R,N,V_smartFramingFieldOfView) smartFramingFieldOfView;
@property (TB,R,N,V_personalPhotographerEnabled) personalPhotographerEnabled;
```

## Instance methods

```
-[CAMCaptureGraphConfiguration personalPhotographerEnabled];
-[CAMCaptureGraphConfiguration photoQualityPrioritization];
-[CAMCaptureGraphConfiguration maximumPhotoResolution];
-[CAMCaptureGraphConfiguration videoStabilizationStrength];
-[CAMCaptureGraphConfiguration audioZoomEnabled];
-[CAMCaptureGraphConfiguration modeDescription];
-[CAMCaptureGraphConfiguration photoEncodingBehavior];
-[CAMCaptureGraphConfiguration aspectRatioCrop];
-[CAMCaptureGraphConfiguration customLensGroup];
-[CAMCaptureGraphConfiguration windNoiseRemovalEnabled];
-[CAMCaptureGraphConfiguration isCaptureMirrored];
-[CAMCaptureGraphConfiguration mixAudioWithOthers];
-[CAMCaptureGraphConfiguration videoConfiguration];
-[CAMCaptureGraphConfiguration device];
-[CAMCaptureGraphConfiguration smartFramingFieldOfView];
-[CAMCaptureGraphConfiguration trueVideoEnabled];
-[CAMCaptureGraphConfiguration shortDescription];
-[CAMCaptureGraphConfiguration isVideoHDRSuspended];
-[CAMCaptureGraphConfiguration frontRearSimultaneousVideoEnabled];
-[CAMCaptureGraphConfiguration colorSpace];
-[CAMCaptureGraphConfiguration mode];
-[CAMCaptureGraphConfiguration devicePosition];
-[CAMCaptureGraphConfiguration audioConfiguration];
-[CAMCaptureGraphConfiguration description];
-[CAMCaptureGraphConfiguration macroMode];
-[CAMCaptureGraphConfiguration isVideoBinned];
-[CAMCaptureGraphConfiguration smartStyles];
-[CAMCaptureGraphConfiguration previewConfiguration];
-[CAMCaptureGraphConfiguration deviceDescription];
-[CAMCaptureGraphConfiguration completeDescription];
-[CAMCaptureGraphConfiguration devicePositionDescription];
-[CAMCaptureGraphConfiguration disabledExposureCompensationFeatures];
-[CAMCaptureGraphConfiguration enableAutoFPSVideo];
-[CAMCaptureGraphConfiguration enableContentAwareDistortionCorrection];
-[CAMCaptureGraphConfiguration enableDepthSuggestion];
-[CAMCaptureGraphConfiguration enableMRCMetadata];
-[CAMCaptureGraphConfiguration enableRAWCaptureIfSupported];
-[CAMCaptureGraphConfiguration enableResponsiveShutter];
-[CAMCaptureGraphConfiguration enableTextRegionMetadata];
-[CAMCaptureGraphConfiguration enableZoomPIP];
-[CAMCaptureGraphConfiguration initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:audioZoomEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:previewMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:disabledExposureCompensationFeatures:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:photoPerformancePriority:colorSpace:videoBinned:enableMRCMetadata:enableTextRegionMetadata:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:videoDynamicAspectRatio:smartFramingFieldOfView:personalPhotographerEnabled:];
-[CAMCaptureGraphConfiguration isFrontCameraUsedAsBackCamera];
-[CAMCaptureGraphConfiguration isPreviewMirrored];
-[CAMCaptureGraphConfiguration isSecondaryDeviceVideoBinned];
-[CAMCaptureGraphConfiguration photoPerformancePriority];
-[CAMCaptureGraphConfiguration prefersHDR10BitVideo];
-[CAMCaptureGraphConfiguration previewFilters];
-[CAMCaptureGraphConfiguration previewSampleBufferVideoFormat];
-[CAMCaptureGraphConfiguration previewSemanticStyle];
-[CAMCaptureGraphConfiguration secondaryDevice:];
-[CAMCaptureGraphConfiguration secondaryDeviceColorSpace];
-[CAMCaptureGraphConfiguration secondaryDeviceUsesPrimaryVideoConfigurationForFrameRate];
-[CAMCaptureGraphConfiguration secondaryDeviceVideoConfiguration];
-[CAMCaptureGraphConfiguration secondaryDeviceVideoDynamicAspectRatio];
-[CAMCaptureGraphConfiguration secondaryDeviceVideoStabilizationStrength];
-[CAMCaptureGraphConfiguration semanticStyleSupport];
-[CAMCaptureGraphConfiguration suspendLivePhotoCapture];
-[CAMCaptureGraphConfiguration videoDynamicAspectRatio];
-[CAMCaptureGraphConfiguration videoEncodingBehavior];
-[CAMCaptureGraphConfiguration videoThumbnailOutputConfiguration];
```
