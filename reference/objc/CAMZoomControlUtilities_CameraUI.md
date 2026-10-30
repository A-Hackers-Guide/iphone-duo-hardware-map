# `CAMZoomControlUtilities`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 19 class methods

## Class methods

```
+[CAMZoomControlUtilities _baseSingleCameraDeviceForDevice:];
+[CAMZoomControlUtilities _zoomControlRadiusForZoomControl:layoutSide:layoutStyle:width:centerOfZoomControlInContainerBounds:marginForZoomDiaFromEdge:];
+[CAMZoomControlUtilities appropriateSignificantZoomFactorForDevice:fromDevice:currentZoomFactor:targetZoomFactor:mode:];
+[CAMZoomControlUtilities deviceForEmulatingZoomFactor:fromDevice:mode:continuousZoomSupported:];
+[CAMZoomControlUtilities equivalentZoomFactor:forDevice:fromDevice:];
+[CAMZoomControlUtilities exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:frontRearSimultaneousVideoEnabled:];
+[CAMZoomControlUtilities layoutForExternalChromeZoomControl:bounds:viewportFrame:referenceYForControlsAboveShutterButton:];
+[CAMZoomControlUtilities layoutZoomControl:alignmentRect:zoomDialExpansionRegionHeight:zoomButtonMarginFromBottomOfExpansionRegion:];
+[CAMZoomControlUtilities layoutZoomControl:forLayoutStyle:bottomBarAlignmentRect:bottomBarTransparent:shutterButtonAlignmentRect:previewViewAlignmentRect:];
+[CAMZoomControlUtilities layoutZoomControl:layoutSide:forLayoutStyle:width:marginForZoomButtonFromEdge:marginForZoomDialFromEdge:zoomDialContentMaskingHeight:centerOfZoomControlInContainerView:useFixedZoomControlOrientation:];
+[CAMZoomControlUtilities linearMappingForX:x1:y1:x2:y2:clamp:];
+[CAMZoomControlUtilities piecewiseLinearMappingForX:fromXValues:toYValues:];
+[CAMZoomControlUtilities referenceYForControlsAboveShutterButtonFrame:viewportFrame:aspectRatio:shutterTopPadding:];
+[CAMZoomControlUtilities shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:zoomFactors:displayZoomFactors:];
+[CAMZoomControlUtilities shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:];
+[CAMZoomControlUtilities shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:];
+[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:];
+[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:];
+[CAMZoomControlUtilities zoomScaleFromDevice:toDevice:];
```
