# `JFXFaceTrackingTransformCalculator`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 8 properties, 13 instance methods, 1 class methods

## Instance variables

```
f _pixelsPerUnit;
@"JFXARMetadata" _arMetadata;
q _interfaceOrientation;
{CGSize="width"d"height"d} _outputSize;
```

## Properties

```
@property (T@"JFXARMetadata",&,N,V_arMetadata) arMetadata;
@property (T{CGSize=dd},R,N,V_outputSize) outputSize;
@property (Tq,R,N,V_interfaceOrientation) interfaceOrientation;
@property (Tf,N,V_pixelsPerUnit) pixelsPerUnit;
@property (T{?=[4]},R,N) cameraProjection;
@property (T{?=[4]},R,N) cameraTransform;
@property (T{?=[4]},R,N) onFaceTransform;
@property (T{?=[4]},R,N) billboardTransform;
```

## Class methods

```
+[JFXFaceTrackingTransformCalculator interpolateFrom:to:fraction:];
```

## Instance methods

```
-[JFXFaceTrackingTransformCalculator interfaceOrientation];
-[JFXFaceTrackingTransformCalculator outputSize];
-[JFXFaceTrackingTransformCalculator cameraTransform];
-[JFXFaceTrackingTransformCalculator onFaceTransform];
-[JFXFaceTrackingTransformCalculator arMetadata];
-[JFXFaceTrackingTransformCalculator billboardTransform];
-[JFXFaceTrackingTransformCalculator calculateFaceTrackingTransform];
-[JFXFaceTrackingTransformCalculator cameraProjection];
-[JFXFaceTrackingTransformCalculator initWithARMetaData:outputSize:playableInterfaceOrientation:];
-[JFXFaceTrackingTransformCalculator nonScaledOrientedCameraTransform];
-[JFXFaceTrackingTransformCalculator pixelsPerUnit];
-[JFXFaceTrackingTransformCalculator setArMetadata:];
-[JFXFaceTrackingTransformCalculator setPixelsPerUnit:];
```
