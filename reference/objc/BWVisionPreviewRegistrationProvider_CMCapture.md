# `BWVisionPreviewRegistrationProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPreviewRegistrationProvider`
- 8 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"BWPixelBufferPool" _registrationPool;
^{OpaqueVTPixelRotationSession=} _registrationRotationSession;
{CGPoint="x"d"y"d} _superWideOpticalCenterOffset;
{CGPoint="x"d"y"d} _wideOpticalCenterOffset;
{CGPoint="x"d"y"d} _teleOpticalCenterOffset;
{?="width"i"height"i} _sensorBinningFactor;
{?="previousSpherePosition"[3{?="x"f"y"f}]"currentSpherePosition"[3{?="x"f"y"f}]"filteredSpherePosition"[3{?="x"f"y"f}]"estimatedSagPosition"[3{?="x"f"y"f}]"supportAverageSpherePositionKey"B"bravoData"{?="configuration"I"opticalCenterOffset"[3{?="x"f"y"f}]"baseZoomFactor"[3f]"baseZoomFactorAdjustment"[3f]"pixelSizeInMicron"[3f]"quadraBinningFactor"[3i]"quadraBinningFactorStashed"i"currentToReferenceScaleRatio"[7f]"currentToReferenceExtrinsicMatrix"[7[12f]]"referencePortIndex"i"previousPortIndex"i"parallaxShift"{?="x"f"y"f}"stashedSpherePos"[3{?="x"f"y"f}]"lastPracticalFocalLength"[3f]"lastEffectiveFocalLength"[3f]"lastPinholeCameraFocalLength"[3f]"decoupleBravoParallaxShiftFromSphereLensPosition"B"minDistanceForBravoParallaxShift"f"sphereScalingFactorUsedForParallaxShiftComputation"f}"sagEstimationAlpha"d} _superWideToWideShiftState;
{?="previousSpherePosition"[3{?="x"f"y"f}]"currentSpherePosition"[3{?="x"f"y"f}]"filteredSpherePosition"[3{?="x"f"y"f}]"estimatedSagPosition"[3{?="x"f"y"f}]"supportAverageSpherePositionKey"B"bravoData"{?="configuration"I"opticalCenterOffset"[3{?="x"f"y"f}]"baseZoomFactor"[3f]"baseZoomFactorAdjustment"[3f]"pixelSizeInMicron"[3f]"quadraBinningFactor"[3i]"quadraBinningFactorStashed"i"currentToReferenceScaleRatio"[7f]"currentToReferenceExtrinsicMatrix"[7[12f]]"referencePortIndex"i"previousPortIndex"i"parallaxShift"{?="x"f"y"f}"stashedSpherePos"[3{?="x"f"y"f}]"lastPracticalFocalLength"[3f]"lastEffectiveFocalLength"[3f]"lastPinholeCameraFocalLength"[3f]"decoupleBravoParallaxShiftFromSphereLensPosition"B"minDistanceForBravoParallaxShift"f"sphereScalingFactorUsedForParallaxShiftComputation"f}"sagEstimationAlpha"d} _wideToTeleShiftState;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWVisionPreviewRegistrationProvider initialize];
```

## Instance methods

```
-[BWVisionPreviewRegistrationProvider dealloc];
-[BWVisionPreviewRegistrationProvider cleanupResources];
-[BWVisionPreviewRegistrationProvider allocateResourcesWithVideoFormat:metalContext:];
-[BWVisionPreviewRegistrationProvider computeCameraShiftForWiderCamera:narrowerCamera:widerToNarrowerCameraScale:];
-[BWVisionPreviewRegistrationProvider initWithCameraInfoByPortType:sensorBinningFactor:];
-[BWVisionPreviewRegistrationProvider registerWiderCamera:narrowerCamera:widerToNarrowerCameraScale:isMacroScene:macroTransitionType:registerHorizontalEdges:];
```
