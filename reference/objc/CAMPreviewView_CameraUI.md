# `CAMPreviewView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 26 instance variables, 28 properties, 85 instance methods, 2 class methods

## Instance variables

```
B _hideAllIndicators;
B __debugDrawZoomPIP;
i __exposureBiasSide;
q _orientation;
@"CAMVideoPreviewView" _videoPreviewView;
@"CAMPIPVideoPreviewView" _frontPIPVideoPreviewView;
@"CAMSmartTapMaskView" _smartTapMaskOverlayView;
@"CAMInterfaceModulationView" _overlayContainerView;
@"UIView" _indicatorContainerView;
q _indicatorClippingStyle;
@"CAMFocusIndicatorView" _continuousIndicator;
@"CAMFocusIndicatorView" _pointIndicator;
@"CAMFocusIndicatorView" _externalFocusLockIndicator;
@"CAMGridView" _gridView;
@"CAMLevelIndicatorView" _levelView;
@"CAMHorizonLevelView" _horizonLevelView;
@"CEKSubjectIndicatorView" _centeredSubjectIndicatorView;
q _frontPIPAnchor;
@"CAMStageLightOverlayView" _stageLightOverlayView;
d _bottomContentInset;
@"UILabel" __simulatorLabel;
@"CAShapeLayer" __overlayContainerMask;
@"UIImage" __cachedVideoPreviewSnapshotImage;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _viewportFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _overlayFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _normalizedZoomPIPRect;
```

## Properties

```
@property (T@"UILabel",R,N,V__simulatorLabel) _simulatorLabel;
@property (Ti,N,V__exposureBiasSide) _exposureBiasSide;
@property (T@"CAShapeLayer",&,N,S_setOverlayContainerMask:,V__overlayContainerMask) _overlayContainerMask;
@property (TB,R,N,V__debugDrawZoomPIP) _debugDrawZoomPIP;
@property (T@"UIImage",&,N,V__cachedVideoPreviewSnapshotImage) _cachedVideoPreviewSnapshotImage;
@property (Tq,N,V_orientation) orientation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewportFrame) viewportFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_overlayFrame) overlayFrame;
@property (T@"CAMVideoPreviewView",R,N,V_videoPreviewView) videoPreviewView;
@property (T@"AVCaptureVideoPreviewLayer",&,N) videoPreviewLayer;
@property (T@"CAMPIPVideoPreviewView",R,N,V_frontPIPVideoPreviewView) frontPIPVideoPreviewView;
@property (T@"AVCaptureVideoPreviewLayer",&,N) frontPIPVideoPreviewLayer;
@property (T@"CAMSmartTapMaskView",R,N,V_smartTapMaskOverlayView) smartTapMaskOverlayView;
@property (T@"CAMInterfaceModulationView",R,N,V_overlayContainerView) overlayContainerView;
@property (T@"UIView",R,N,V_indicatorContainerView) indicatorContainerView;
@property (TB,N,V_hideAllIndicators) hideAllIndicators;
@property (Tq,N,V_indicatorClippingStyle) indicatorClippingStyle;
@property (T@"CAMFocusIndicatorView",&,N,V_continuousIndicator) continuousIndicator;
@property (T@"CAMFocusIndicatorView",&,N,V_pointIndicator) pointIndicator;
@property (T@"CAMFocusIndicatorView",&,N,V_externalFocusLockIndicator) externalFocusLockIndicator;
@property (T@"CAMGridView",N,V_gridView) gridView;
@property (T@"CAMLevelIndicatorView",N,V_levelView) levelView;
@property (T@"CAMHorizonLevelView",N,V_horizonLevelView) horizonLevelView;
@property (T@"CEKSubjectIndicatorView",&,N,V_centeredSubjectIndicatorView) centeredSubjectIndicatorView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_normalizedZoomPIPRect) normalizedZoomPIPRect;
@property (Tq,N,V_frontPIPAnchor) frontPIPAnchor;
@property (T@"CAMStageLightOverlayView",&,N,V_stageLightOverlayView) stageLightOverlayView;
@property (Td,N,V_bottomContentInset) bottomContentInset;
```

## Class methods

```
+[CAMPreviewView layerClass];
+[CAMPreviewView _createPixelBufferFromCGImage:];
```

## Instance methods

```
-[CAMPreviewView viewportFrame];
-[CAMPreviewView setOrientation:animated:];
-[CAMPreviewView setOrientation:];
-[CAMPreviewView _simulatorLabel];
-[CAMPreviewView fixedSizeSubjectIndicatorFrameForBodyResult:];
-[CAMPreviewView captureDevicePointOfInterestForPoint:];
-[CAMPreviewView setHideAllIndicators:];
-[CAMPreviewView overlayContainerView];
-[CAMPreviewView frameForMetadataObjectResult:];
-[CAMPreviewView setVideoPreviewLayer:];
-[CAMPreviewView setBottomContentInset:];
-[CAMPreviewView pointIndicator];
-[CAMPreviewView activityItemsConfiguration];
-[CAMPreviewView frameForMetadataObjectResult:minimumPreviewInset:];
-[CAMPreviewView _debugDrawZoomPIP];
-[CAMPreviewView _overlayContainerMask];
-[CAMPreviewView _frameClampedToBounds:minimumPreviewInset:];
-[CAMPreviewView gridView];
-[CAMPreviewView frontPIPVideoPreviewLayer];
-[CAMPreviewView levelView];
-[CAMPreviewView viewportAnchorsForFrontPIP];
-[CAMPreviewView _faceOrientationForRollAngle:];
-[CAMPreviewView setFrontPIPVideoPreviewLayer:];
-[CAMPreviewView setGridView:];
-[CAMPreviewView orientation];
-[CAMPreviewView initWithFrame:initialPreviewAspectMode:initialWindowedPreviewAspectMode:];
-[CAMPreviewView dealloc];
-[CAMPreviewView normalizedZoomPIPRect];
-[CAMPreviewView setFrontPIPAnchor:];
-[CAMPreviewView indicatorContainerView];
-[CAMPreviewView _frameForAVMetadataObject:];
-[CAMPreviewView setCenteredSubjectIndicatorView:];
-[CAMPreviewView indicatePointOfInterest:animated:];
-[CAMPreviewView setPointIndicator:];
-[CAMPreviewView _drawZoomPIP];
-[CAMPreviewView layoutSubviews];
-[CAMPreviewView setContinuousIndicator:];
-[CAMPreviewView frontPIPAnchor];
-[CAMPreviewView setStageLightOverlayView:];
-[CAMPreviewView externalFocusLockIndicator];
-[CAMPreviewView _snapshotOfVideoPreviewViewWithScale:cacheResult:];
-[CAMPreviewView _frameClampedToBounds:];
-[CAMPreviewView videoPreviewLayer];
-[CAMPreviewView setNormalizedZoomPIPRect:];
-[CAMPreviewView createAndInsertSmartTapMaskOverlayViewIfNeeded];
-[CAMPreviewView _compareCGPointsToAccuracy:point1:point2:];
-[CAMPreviewView viewportSnapshotImageWithScale:];
-[CAMPreviewView _cachedVideoPreviewSnapshotImage];
-[CAMPreviewView setViewportFrame:];
-[CAMPreviewView indicatorClippingStyle];
-[CAMPreviewView releaseCachedVideoPreviewSnapshot];
-[CAMPreviewView stageLightOverlayView];
-[CAMPreviewView overlayFrame];
-[CAMPreviewView bottomContentInset];
-[CAMPreviewView frameForMetadataObjectResult:fixedSize:];
-[CAMPreviewView horizonLevelView];
-[CAMPreviewView _updateOverlayContainerMask];
-[CAMPreviewView continuousIndicator];
-[CAMPreviewView _isZoomPIPRectValid];
-[CAMPreviewView setLevelView:];
-[CAMPreviewView centeredSubjectIndicatorView];
-[CAMPreviewView _snapshotOfVideoPreviewView];
-[CAMPreviewView _exposureBiasSide];
-[CAMPreviewView _aspectFaceRectFromSquareFaceRect:angle:];
-[CAMPreviewView setIndicatorClippingStyle:];
-[CAMPreviewView frameForSubjectGroupResult:minimumSize:];
-[CAMPreviewView frontPIPVideoPreviewView];
-[CAMPreviewView hideAllIndicators];
-[CAMPreviewView videoPreviewView];
-[CAMPreviewView setHorizonLevelView:];
-[CAMPreviewView setExternalFocusLockIndicator:];
-[CAMPreviewView pointForCaptureDevicePointOfInterest:];
-[CAMPreviewView smartTapMaskOverlayView];
-[CAMPreviewView viewportAnchorsForFrontPIPOriginWithSize:];
-[CAMPreviewView set_cachedVideoPreviewSnapshotImage:];
-[CAMPreviewView _isFrontPIPAtAnAnchor];
-[CAMPreviewView faceIndicatorFrameForFaceResult:];
-[CAMPreviewView set_exposureBiasSide:];
-[CAMPreviewView setOverlayFrame:];
-[CAMPreviewView _pipAnchorPointForPIPSize:];
-[CAMPreviewView viewportSnapshotImageAllowingCachedSnapshot:];
-[CAMPreviewView _setOverlayContainerMask:];
-[CAMPreviewView fixedSizeSubjectIndicatorFrameForFaceResult:];
-[CAMPreviewView frameForTextRegionResult:];
-[CAMPreviewView createViewportPixelBufferAllowingCachedSnapshot:];
```
