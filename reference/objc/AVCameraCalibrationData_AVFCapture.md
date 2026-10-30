# `AVCameraCalibrationData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"AVCameraCalibrationDataInternal" _internal;
```

## Properties

```
@property (T{?=[3]},R,N) intrinsicMatrix;
@property (T{CGSize=dd},R,N) intrinsicMatrixReferenceDimensions;
@property (T{?=[4]},R,N) extrinsicMatrix;
@property (Tf,R,N) pixelSize;
@property (T@"NSData",R,N) lensDistortionLookupTable;
@property (T@"NSData",R,N) inverseLensDistortionLookupTable;
@property (T{CGPoint=dd},R,N) lensDistortionCenter;
```

## Instance methods

```
-[AVCameraCalibrationData debugDescription];
-[AVCameraCalibrationData dealloc];
-[AVCameraCalibrationData pixelSize];
-[AVCameraCalibrationData description];
-[AVCameraCalibrationData extrinsicMatrix];
-[AVCameraCalibrationData cameraCalibrationDataDictionary];
-[AVCameraCalibrationData intrinsicMatrix];
-[AVCameraCalibrationData initWithCameraCalibrationDataDictionary:error:];
-[AVCameraCalibrationData intrinsicMatrixReferenceDimensions];
-[AVCameraCalibrationData inverseLensDistortionLookupTable];
-[AVCameraCalibrationData lensDistortionCenter];
-[AVCameraCalibrationData lensDistortionLookupTable];
-[AVCameraCalibrationData _distortionLookupTableFromCoefficients:distortionCenter:pixelSize:referenceDimensions:lookupTableLength:];
-[AVCameraCalibrationData _initEmpty];
-[AVCameraCalibrationData cameraCalibrationDataWithExifOrientation:];
-[AVCameraCalibrationData copyAuxiliaryMetadata];
-[AVCameraCalibrationData initWithAuxiliaryMetadata:];
-[AVCameraCalibrationData initWithDepthMetadataDictionary:];
```
