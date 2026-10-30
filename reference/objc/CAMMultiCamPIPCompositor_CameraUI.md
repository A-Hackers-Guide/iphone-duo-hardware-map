# `CAMMultiCamPIPCompositor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 23 properties, 55 instance methods, 0 class methods

## Instance variables

```
B _motionBlurDisabled;
B __useCoreImageCVTextureCache;
B __useCoreImageSurfacePool;
B __coreImageArchiveLoaded;
B __compositingSessionActive;
B __motionBlurDisabledForCurrentCompositingSession;
B __debugColorDuplicatedMovieFileBuffers;
B __debugDisableMotionBlur;
B __excessiveBlurRadiusReported;
B __pipTimestampTooOldReported;
i __pipRotationAngle;
@"<MTLDevice>" __metalDevice;
@"CIContext" __ciContext;
^{__CVMetalTextureCache=} __textureCache;
@"IOSurfaceMemoryPool" __surfaceMemoryPool;
@"CIContext" __gainMapCIContext;
q __pipMetricsMaxCapacity;
@"NSMutableDictionary" __pipMetricsByTimestamp;
d __pipMaxBlurRadius;
{?="value"q"timescale"i"flags"I"epoch"q} __mostRecentlyAddedPIPMetricsTimestamp;
{?="value"q"timescale"i"flags"I"epoch"q} __debugLastCompositedMovieFilePrimaryBufferPTS;
{?="value"q"timescale"i"flags"I"epoch"q} __debugLastCompositedMovieFileSecondaryBufferPTS;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __lastCompositedPictureInPictureFrameForMotionBlur;
```

## Properties

```
@property (Ti,N,V__pipRotationAngle) _pipRotationAngle;
@property (T@"<MTLDevice>",&,N,V__metalDevice) _metalDevice;
@property (TB,R,N,V__useCoreImageCVTextureCache) _useCoreImageCVTextureCache;
@property (TB,R,N,V__useCoreImageSurfacePool) _useCoreImageSurfacePool;
@property (T@"CIContext",&,N,V__ciContext) _ciContext;
@property (T^{__CVMetalTextureCache=},N,V__textureCache) _textureCache;
@property (T@"IOSurfaceMemoryPool",&,N,V__surfaceMemoryPool) _surfaceMemoryPool;
@property (TB,N,G_isCoreImageArchiveLoaded,V__coreImageArchiveLoaded) _coreImageArchiveLoaded;
@property (T@"CIContext",&,N,V__gainMapCIContext) _gainMapCIContext;
@property (TB,N,G_isCompositingSessionActive,V__compositingSessionActive) _compositingSessionActive;
@property (Tq,R,N,V__pipMetricsMaxCapacity) _pipMetricsMaxCapacity;
@property (T@"NSMutableDictionary",R,N,V__pipMetricsByTimestamp) _pipMetricsByTimestamp;
@property (T{?=qiIq},N,V__mostRecentlyAddedPIPMetricsTimestamp) _mostRecentlyAddedPIPMetricsTimestamp;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V__lastCompositedPictureInPictureFrameForMotionBlur) _lastCompositedPictureInPictureFrameForMotionBlur;
@property (Td,R,N,V__pipMaxBlurRadius) _pipMaxBlurRadius;
@property (TB,N,V__motionBlurDisabledForCurrentCompositingSession) _motionBlurDisabledForCurrentCompositingSession;
@property (TB,R,N,V__debugColorDuplicatedMovieFileBuffers) _debugColorDuplicatedMovieFileBuffers;
@property (T{?=qiIq},N,V__debugLastCompositedMovieFilePrimaryBufferPTS) _debugLastCompositedMovieFilePrimaryBufferPTS;
@property (T{?=qiIq},N,V__debugLastCompositedMovieFileSecondaryBufferPTS) _debugLastCompositedMovieFileSecondaryBufferPTS;
@property (TB,R,N,V__debugDisableMotionBlur) _debugDisableMotionBlur;
@property (TB,N,V__excessiveBlurRadiusReported) _excessiveBlurRadiusReported;
@property (TB,N,V__pipTimestampTooOldReported) _pipTimestampTooOldReported;
@property (TB,N,GisMotionBlurDisabled,V_motionBlurDisabled) motionBlurDisabled;
```

## Instance methods

```
-[CAMMultiCamPIPCompositor set_pipTimestampTooOldReported:];
-[CAMMultiCamPIPCompositor _applyMaskAndBorderToImage:cornerRadius:borderWidth:borderColor:];
-[CAMMultiCamPIPCompositor _calculateMotionBlurAngle:motionBlurRadius:forPictureInPictureFrame:fromPictureInPictureFrame:];
-[CAMMultiCamPIPCompositor _ciContext];
-[CAMMultiCamPIPCompositor _compositePrimaryGainMapImage:pipGainMapImage:primarySDRImage:pipSDRImage:compositeSDRImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:];
-[CAMMultiCamPIPCompositor _compositePrimaryImage:pipImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:motionBlurAngle:motionBlurRadius:debugColorDuplicatedPrimaryImage:debugColorDuplicatedPIPImage:];
-[CAMMultiCamPIPCompositor _cropPIP:toSizeAspectRatioIfNecessary:];
-[CAMMultiCamPIPCompositor _debugColorDuplicatedMovieFileBuffers];
-[CAMMultiCamPIPCompositor _debugDisableMotionBlur];
-[CAMMultiCamPIPCompositor _debugImageWithDuplicatedColorTint:];
-[CAMMultiCamPIPCompositor _debugLastCompositedMovieFilePrimaryBufferPTS];
-[CAMMultiCamPIPCompositor _debugLastCompositedMovieFileSecondaryBufferPTS];
-[CAMMultiCamPIPCompositor _excessiveBlurRadiusReported];
-[CAMMultiCamPIPCompositor _gainMapCIContext];
-[CAMMultiCamPIPCompositor _isCompositingSessionActive];
-[CAMMultiCamPIPCompositor _isCoreImageArchiveLoaded];
-[CAMMultiCamPIPCompositor _lastCompositedPictureInPictureFrameForMotionBlur];
-[CAMMultiCamPIPCompositor _metalDevice];
-[CAMMultiCamPIPCompositor _mostRecentlyAddedPIPMetricsTimestamp];
-[CAMMultiCamPIPCompositor _motionBlurDisabledForCurrentCompositingSession];
-[CAMMultiCamPIPCompositor _pipFrameEqualsMostRecentlyAdded:];
-[CAMMultiCamPIPCompositor _pipMaxBlurRadius];
-[CAMMultiCamPIPCompositor _pipMetricsByTimestamp];
-[CAMMultiCamPIPCompositor _pipMetricsForCompositingClosestToTimestamp:];
-[CAMMultiCamPIPCompositor _pipMetricsMaxCapacity];
-[CAMMultiCamPIPCompositor _pipRotationAngle];
-[CAMMultiCamPIPCompositor _pipTimestampTooOldReported];
-[CAMMultiCamPIPCompositor _scaledPIPMetrics:toPrimaryImageSize:];
-[CAMMultiCamPIPCompositor _sortedPIPTimestamps];
-[CAMMultiCamPIPCompositor _surfaceMemoryPool];
-[CAMMultiCamPIPCompositor _textureCache];
-[CAMMultiCamPIPCompositor _useCoreImageCVTextureCache];
-[CAMMultiCamPIPCompositor _useCoreImageSurfacePool];
-[CAMMultiCamPIPCompositor compositeWithCompositingData:strategy:captureOrientation:mirrorPIP:];
-[CAMMultiCamPIPCompositor ensureCompositingResources];
-[CAMMultiCamPIPCompositor initWithPictureInPictureRotationAngle:];
-[CAMMultiCamPIPCompositor isMotionBlurDisabled];
-[CAMMultiCamPIPCompositor prepareForCompositing];
-[CAMMultiCamPIPCompositor resetCompositingState:];
-[CAMMultiCamPIPCompositor setMotionBlurDisabled:];
-[CAMMultiCamPIPCompositor setPictureInPictureMetrics:];
-[CAMMultiCamPIPCompositor set_ciContext:];
-[CAMMultiCamPIPCompositor set_compositingSessionActive:];
-[CAMMultiCamPIPCompositor set_coreImageArchiveLoaded:];
-[CAMMultiCamPIPCompositor set_debugLastCompositedMovieFilePrimaryBufferPTS:];
-[CAMMultiCamPIPCompositor set_debugLastCompositedMovieFileSecondaryBufferPTS:];
-[CAMMultiCamPIPCompositor set_excessiveBlurRadiusReported:];
-[CAMMultiCamPIPCompositor set_gainMapCIContext:];
-[CAMMultiCamPIPCompositor set_lastCompositedPictureInPictureFrameForMotionBlur:];
-[CAMMultiCamPIPCompositor set_metalDevice:];
-[CAMMultiCamPIPCompositor set_mostRecentlyAddedPIPMetricsTimestamp:];
-[CAMMultiCamPIPCompositor set_motionBlurDisabledForCurrentCompositingSession:];
-[CAMMultiCamPIPCompositor set_pipRotationAngle:];
-[CAMMultiCamPIPCompositor set_surfaceMemoryPool:];
-[CAMMultiCamPIPCompositor set_textureCache:];
```
