# `BWPreviewStitcherFramePairInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 22 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _cameraInfo;
^{opaqueCMSampleBuffer=} _widerCameraSampleBuffer;
^{opaqueCMSampleBuffer=} _narrowerCameraSampleBuffer;
@"NSDictionary" _widerCameraMetadata;
@"NSDictionary" _narrowerCameraMetadata;
i _widerCameraType;
i _narrowerCameraType;
i _lastNarrowerCameraType;
i _recommendedMasterType;
i _preferredMasterType;
i _lastRecommendedMasterType;
i _lastPreferredMasterType;
i _lastRecommendedMasterSelectionReason;
f _widerCameraNondisruptiveSwitchingScaleFactor;
f _narrowerCameraNondisruptiveSwitchingScaleFactor;
f _totalZoomFactor;
f _uiZoomFactor;
B _narrowerCameraNondisruptiveSwitchingCurrentFrameIsCropped;
B _nondisruptiveSwitchingCompleted;
[3f] _nondisruptiveSwitchingScaleFactors;
[3f] _lastNondisruptiveSwitchingScaleFactors;
f _wideBaseZoomFactorOverride;
f _wideBaseZoomFactorDynamicOverride;
f _wideBaseZoomFactorDynamicOverrideScaled;
f _teleBaseZoomFactorOverride;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N,V_widerCameraSampleBuffer) widerCameraSampleBuffer;
@property (T^{opaqueCMSampleBuffer=},R,N,V_narrowerCameraSampleBuffer) narrowerCameraSampleBuffer;
@property (T@"NSDictionary",R,N,V_widerCameraMetadata) widerCameraMetadata;
@property (T@"NSDictionary",R,N,V_narrowerCameraMetadata) narrowerCameraMetadata;
@property (Ti,R,N,V_widerCameraType) widerCameraType;
@property (Ti,R,N,V_narrowerCameraType) narrowerCameraType;
@property (Ti,R,N,V_lastNarrowerCameraType) lastNarrowerCameraType;
@property (Ti,R,N,V_recommendedMasterType) recommendedMasterType;
@property (Ti,R,N,V_preferredMasterType) preferredMasterType;
@property (Ti,R,N,V_lastRecommendedMasterType) lastRecommendedMasterType;
@property (Ti,R,N,V_lastPreferredMasterType) lastPreferredMasterType;
@property (Ti,R,N,V_lastRecommendedMasterSelectionReason) lastRecommendedMasterSelectionReason;
@property (Tf,R,N,V_totalZoomFactor) totalZoomFactor;
@property (Tf,R,N,V_uiZoomFactor) uiZoomFactor;
@property (Tf,R,N,V_widerCameraNondisruptiveSwitchingScaleFactor) widerCameraNondisruptiveSwitchingScaleFactor;
@property (Tf,R,N,V_narrowerCameraNondisruptiveSwitchingScaleFactor) narrowerCameraNondisruptiveSwitchingScaleFactor;
@property (TB,R,N,V_narrowerCameraNondisruptiveSwitchingCurrentFrameIsCropped) narrowerCameraNondisruptiveSwitchingCurrentFrameIsCropped;
@property (TB,R,N,V_nondisruptiveSwitchingCompleted) nondisruptiveSwitchingCompleted;
@property (Tf,N,V_wideBaseZoomFactorOverride) wideBaseZoomFactorOverride;
@property (Tf,N,V_wideBaseZoomFactorDynamicOverride) wideBaseZoomFactorDynamicOverride;
@property (Tf,N,V_wideBaseZoomFactorDynamicOverrideScaled) wideBaseZoomFactorDynamicOverrideScaled;
@property (Tf,N,V_teleBaseZoomFactorOverride) teleBaseZoomFactorOverride;
```

## Instance methods

```
-[BWPreviewStitcherFramePairInfo baseZoomFactorForCamera:override:applyNondisruptiveSwitchingScaleFactor:];
-[BWPreviewStitcherFramePairInfo widerCameraType];
-[BWPreviewStitcherFramePairInfo setTeleBaseZoomFactorOverride:];
-[BWPreviewStitcherFramePairInfo preferredMasterType];
-[BWPreviewStitcherFramePairInfo totalZoomFactor];
-[BWPreviewStitcherFramePairInfo widerCameraSampleBuffer];
-[BWPreviewStitcherFramePairInfo dealloc];
-[BWPreviewStitcherFramePairInfo nondisruptiveSwitchingCompleted];
-[BWPreviewStitcherFramePairInfo wideBaseZoomFactorOverride];
-[BWPreviewStitcherFramePairInfo narrowerCameraType];
-[BWPreviewStitcherFramePairInfo narrowerCameraMetadata];
-[BWPreviewStitcherFramePairInfo lastRecommendedMasterSelectionReason];
-[BWPreviewStitcherFramePairInfo recommendedMasterType];
-[BWPreviewStitcherFramePairInfo wideBaseZoomFactorDynamicOverrideScaled];
-[BWPreviewStitcherFramePairInfo widerCameraNondisruptiveSwitchingScaleFactor];
-[BWPreviewStitcherFramePairInfo mostRecentNondisruptiveSwitchingScaleFactorForCamera:];
-[BWPreviewStitcherFramePairInfo widerCameraMetadata];
-[BWPreviewStitcherFramePairInfo narrowerCameraNondisruptiveSwitchingCurrentFrameIsCropped];
-[BWPreviewStitcherFramePairInfo teleBaseZoomFactorOverride];
-[BWPreviewStitcherFramePairInfo setWideBaseZoomFactorDynamicOverride:];
-[BWPreviewStitcherFramePairInfo lastRecommendedMasterType];
-[BWPreviewStitcherFramePairInfo narrowerCameraNondisruptiveSwitchingScaleFactor];
-[BWPreviewStitcherFramePairInfo setWideBaseZoomFactorOverride:];
-[BWPreviewStitcherFramePairInfo wideBaseZoomFactorDynamicOverride];
-[BWPreviewStitcherFramePairInfo clearStateForActivePair];
-[BWPreviewStitcherFramePairInfo updateFromWiderCameraSampleBuffer:narrowerCameraSampleBuffer:];
-[BWPreviewStitcherFramePairInfo initWithCameraInfoArray:];
-[BWPreviewStitcherFramePairInfo lastNarrowerCameraType];
-[BWPreviewStitcherFramePairInfo lastPreferredMasterType];
-[BWPreviewStitcherFramePairInfo narrowerCameraSampleBuffer];
-[BWPreviewStitcherFramePairInfo setWideBaseZoomFactorDynamicOverrideScaled:];
-[BWPreviewStitcherFramePairInfo baseZoomFactorForWiderCamera:override:applyNondisruptiveSwitchingScaleFactor:];
-[BWPreviewStitcherFramePairInfo uiZoomFactor];
```
