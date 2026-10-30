# `ABPKInput`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isDepthDataValid;
B _isVioPoseValid;
^{__CVBuffer=} _image;
^{__CVBuffer=} _depthMap;
^{__CVBuffer=} _depthConfidenceBuffer;
d _timestamp;
@"ABPKCameraParams" _cameraParams;
{?="columns"[4]} _vioPose;
```

## Properties

```
@property (T^{__CVBuffer=},V_image) image;
@property (T^{__CVBuffer=},N,V_depthMap) depthMap;
@property (T^{__CVBuffer=},N,V_depthConfidenceBuffer) depthConfidenceBuffer;
@property (TB,N,V_isDepthDataValid) isDepthDataValid;
@property (T{?=[4]},V_vioPose) vioPose;
@property (TB,V_isVioPoseValid) isVioPoseValid;
@property (Td,V_timestamp) timestamp;
@property (T@"ABPKCameraParams",&,V_cameraParams) cameraParams;
```

## Instance methods

```
-[ABPKInput setTimestamp:];
-[ABPKInput init];
-[ABPKInput timestamp];
-[ABPKInput image];
-[ABPKInput setImage:];
-[ABPKInput cameraParams];
-[ABPKInput depthConfidenceBuffer];
-[ABPKInput setCameraParams:];
-[ABPKInput setDepthConfidenceBuffer:];
-[ABPKInput setDepthMap:];
-[ABPKInput setIsDepthDataValid:];
-[ABPKInput setIsVioPoseValid:];
-[ABPKInput setVioPose:];
-[ABPKInput depthMap];
-[ABPKInput vioPose];
-[ABPKInput isDepthDataValid];
-[ABPKInput isVioPoseValid];
-[ABPKInput saveDataToDir:withFileNamePrefix:];
```
