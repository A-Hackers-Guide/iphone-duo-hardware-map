# `AVSpatialOverCaptureVideoPreviewLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureVideoPreviewLayer`
- 29 instance variables, 10 properties, 52 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _primaryCaptureRectLock;
{CGPoint="x"d"y"d} _primaryCaptureRectCenterPoint;
d _primaryCaptureRectAspectRatio;
d _primaryCaptureRectTrueVideoTransitionPercentComplete;
d _primaryCaptureRectSmartFramingTransitionPercentComplete;
@"NSString" _primaryCaptureRectSmartFramingTransitionTargetFieldOfView;
q _primaryCaptureRectUniqueID;
B _lastCamerasMountedInLandscapeOrientation;
B _havePendingPrimaryCaptureRectChange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _primaryCaptureRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _overCaptureRect;
{CGSize="width"d"height"d} _contentSize;
B _primaryAndOverCaptureCompositingEnabled;
q _overCaptureStatus;
B _isPresentationLayer;
B _appliesOverCaptureGradient;
f _overCaptureGradientPercentInset;
q _primaryDisplayRegion;
B _automaticallyDimsOverCaptureRegion;
@"CALayer" _topDimmingOverlay;
@"CALayer" _bottomDimmingOverlay;
@"CAGradientLayer" _topGradientOverlay;
@"CAGradientLayer" _bottomGradientOverlay;
d _lastAspectCenterUpdateTime;
B _semanticStyleRenderingSupported;
B _semanticStyleRenderingEnabled;
@"NSArray" _semanticStyles;
@"NSArray" _semanticStylesRegions;
Q _maxSemanticStyles;
```

## Properties

```
@property (T{CGPoint=dd},R,N) primaryCaptureRectCenterPoint;
@property (Td,R,N) primaryCaptureRectAspectRatio;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_primaryCaptureRect) primaryCaptureRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_overCaptureRect) overCaptureRect;
@property (T{CGSize=dd},R,N,V_contentSize) contentSize;
@property (TB,N,GisPrimaryAndOverCaptureCompositingEnabled) primaryAndOverCaptureCompositingEnabled;
@property (Tq,R,N) overCaptureStatus;
@property (TB,N) automaticallyDimsOverCaptureRegion;
@property (TB,N) appliesOverCaptureGradient;
@property (Tq,N) primaryDisplayRegion;
```

## Class methods

```
+[AVSpatialOverCaptureVideoPreviewLayer uniqueID];
```

## Instance methods

```
-[AVSpatialOverCaptureVideoPreviewLayer overCaptureGradientPercentInset];
-[AVSpatialOverCaptureVideoPreviewLayer primaryDisplayRegion];
-[AVSpatialOverCaptureVideoPreviewLayer setSubstrateSaturation:substrateBrightness:convergenceTime:];
-[AVSpatialOverCaptureVideoPreviewLayer primaryCaptureRectUniqueID];
-[AVSpatialOverCaptureVideoPreviewLayer _createOverlayPayloadWithColor:threshold:convergenceTime:];
-[AVSpatialOverCaptureVideoPreviewLayer setPrimaryDisplayRegion:];
-[AVSpatialOverCaptureVideoPreviewLayer didUpdatePreviewImageQueueSlot:imageQueue:rotationDegrees:size:];
-[AVSpatialOverCaptureVideoPreviewLayer primaryCaptureRectAspectRatio];
-[AVSpatialOverCaptureVideoPreviewLayer setFocusPeakingOverlayColor:threshold:convergenceTime:];
-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyles:semanticStylesRegions:];
-[AVSpatialOverCaptureVideoPreviewLayer observeValueForKeyPath:ofObject:change:context:];
-[AVSpatialOverCaptureVideoPreviewLayer _updatePrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:];
-[AVSpatialOverCaptureVideoPreviewLayer semanticStyles];
-[AVSpatialOverCaptureVideoPreviewLayer overCaptureRect];
-[AVSpatialOverCaptureVideoPreviewLayer appliesOverCaptureGradient];
-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyleRenderingEnabled:];
-[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:];
-[AVSpatialOverCaptureVideoPreviewLayer primaryCaptureRectCenterPoint];
-[AVSpatialOverCaptureVideoPreviewLayer setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:];
-[AVSpatialOverCaptureVideoPreviewLayer setPrimaryCaptureRectAspectRatio:centerPoint:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:];
-[AVSpatialOverCaptureVideoPreviewLayer setPrimaryAndOverCaptureCompositingEnabled:];
-[AVSpatialOverCaptureVideoPreviewLayer detachSafelyFromFigCaptureSession:];
-[AVSpatialOverCaptureVideoPreviewLayer resetAllOverlays:];
-[AVSpatialOverCaptureVideoPreviewLayer dealloc];
-[AVSpatialOverCaptureVideoPreviewLayer _initWithSession:makeConnection:];
-[AVSpatialOverCaptureVideoPreviewLayer contentSize];
-[AVSpatialOverCaptureVideoPreviewLayer initWithLayer:];
-[AVSpatialOverCaptureVideoPreviewLayer _handleSpatialNotification:payload:];
-[AVSpatialOverCaptureVideoPreviewLayer semanticStylesRegions];
-[AVSpatialOverCaptureVideoPreviewLayer performContentUpdates:];
-[AVSpatialOverCaptureVideoPreviewLayer primaryCaptureRect];
-[AVSpatialOverCaptureVideoPreviewLayer _updateSemanticStyleRenderingSupported];
-[AVSpatialOverCaptureVideoPreviewLayer automaticallyDimsOverCaptureRegion];
-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:];
-[AVSpatialOverCaptureVideoPreviewLayer setPrimaryCaptureRectAspectRatio:centerPoint:];
-[AVSpatialOverCaptureVideoPreviewLayer getPrimaryCaptureRectCenter:aspectRatio:uniqueID:];
-[AVSpatialOverCaptureVideoPreviewLayer maxSemanticStyles];
-[AVSpatialOverCaptureVideoPreviewLayer isSemanticStyleRenderingEnabled];
-[AVSpatialOverCaptureVideoPreviewLayer semanticStyle];
-[AVSpatialOverCaptureVideoPreviewLayer isPrimaryAndOverCaptureCompositingEnabled];
-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyle:animated:];
-[AVSpatialOverCaptureVideoPreviewLayer layoutSublayers];
-[AVSpatialOverCaptureVideoPreviewLayer setAppliesOverCaptureGradient:];
-[AVSpatialOverCaptureVideoPreviewLayer setAutomaticallyDimsOverCaptureRegion:];
-[AVSpatialOverCaptureVideoPreviewLayer setHighlightClippingOverlayColor:threshold:convergenceTime:];
-[AVSpatialOverCaptureVideoPreviewLayer removeConnection:];
-[AVSpatialOverCaptureVideoPreviewLayer getPrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:uniqueID:];
-[AVSpatialOverCaptureVideoPreviewLayer attachSafelyToFigCaptureSession:];
-[AVSpatialOverCaptureVideoPreviewLayer addConnection:error:];
-[AVSpatialOverCaptureVideoPreviewLayer isSemanticStyleRenderingSupported];
-[AVSpatialOverCaptureVideoPreviewLayer dimSubstrate:convergenceTime:];
-[AVSpatialOverCaptureVideoPreviewLayer overCaptureStatus];
```
