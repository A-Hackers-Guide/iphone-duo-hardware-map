# `AVCapturePhotoPrivateClientMetadata`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _inferenceAttachments;
@"NSDictionary" _detectedObjectInfo;
```

## Properties

```
@property (T@"NSString",R) captureFolderClientPath;
@property (T@"NSDictionary",R) inferenceAttachments;
@property (T@"NSDictionary",R) detectedObjectInfo;
@property (TI,R) spatialOverCaptureImageStitchingConfidenceScore;
@property (TB,R) spatialOverCaptureImageHorizonLinePresent;
@property (Tf,R) spatialOverCaptureImageHorizonLineAngleInDegrees;
@property (Tf,R) spatialOverCaptureImageHorizonLineVerticalCenterlineIntersection;
```

## Class methods

```
+[AVCapturePhotoPrivateClientMetadata supportsSecureCoding];
```

## Instance methods

```
-[AVCapturePhotoPrivateClientMetadata dealloc];
-[AVCapturePhotoPrivateClientMetadata encodeWithCoder:];
-[AVCapturePhotoPrivateClientMetadata initWithCoder:];
-[AVCapturePhotoPrivateClientMetadata initWithMetadataDictionary:];
-[AVCapturePhotoPrivateClientMetadata captureFolderClientPath];
-[AVCapturePhotoPrivateClientMetadata detectedObjectInfo];
-[AVCapturePhotoPrivateClientMetadata inferenceAttachments];
-[AVCapturePhotoPrivateClientMetadata spatialOverCaptureImageHorizonLineAngleInDegrees];
-[AVCapturePhotoPrivateClientMetadata spatialOverCaptureImageHorizonLinePresent];
-[AVCapturePhotoPrivateClientMetadata spatialOverCaptureImageHorizonLineVerticalCenterlineIntersection];
-[AVCapturePhotoPrivateClientMetadata spatialOverCaptureImageStitchingConfidenceScore];
```
