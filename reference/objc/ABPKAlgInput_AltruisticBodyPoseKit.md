# `ABPKAlgInput`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _isDepthDataValid;
^{__CVBuffer=} _image;
@"ABPKImagePreProcessingParams" _imagePreProcessingParams;
^{__CVBuffer=} _depthMap;
^{__CVBuffer=} _depthConfidenceBuffer;
d _timestamp;
{CGSize="width"d"height"d} _imageResolution;
{?="columns"[3]} _imageCameraIntrinsics;
```

## Properties

```
@property (T^{__CVBuffer=},V_image) image;
@property (T{CGSize=dd},N,V_imageResolution) imageResolution;
@property (T{?=[3]},N,V_imageCameraIntrinsics) imageCameraIntrinsics;
@property (T@"ABPKImagePreProcessingParams",N,V_imagePreProcessingParams) imagePreProcessingParams;
@property (T^{__CVBuffer=},N,V_depthMap) depthMap;
@property (T^{__CVBuffer=},N,V_depthConfidenceBuffer) depthConfidenceBuffer;
@property (TB,V_isDepthDataValid) isDepthDataValid;
@property (Td,V_timestamp) timestamp;
```

## Instance methods

```
-[ABPKAlgInput setTimestamp:];
-[ABPKAlgInput init];
-[ABPKAlgInput timestamp];
-[ABPKAlgInput image];
-[ABPKAlgInput setImage:];
-[ABPKAlgInput depthConfidenceBuffer];
-[ABPKAlgInput setDepthConfidenceBuffer:];
-[ABPKAlgInput setDepthMap:];
-[ABPKAlgInput setIsDepthDataValid:];
-[ABPKAlgInput imageResolution];
-[ABPKAlgInput depthMap];
-[ABPKAlgInput setImageResolution:];
-[ABPKAlgInput imageCameraIntrinsics];
-[ABPKAlgInput imagePreProcessingParams];
-[ABPKAlgInput isDepthDataValid];
-[ABPKAlgInput setImageCameraIntrinsics:];
-[ABPKAlgInput setImagePreProcessingParams:];
```
