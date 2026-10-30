# `ABPKOutput`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 15 properties, 39 instance methods, 0 class methods

## Instance variables

```
^{OpaqueVTPixelTransferSession=} _vtPixelTransferSession;
^{__CVBuffer=} _sensorImageBGRA;
@"NSMutableArray" _rawDetection2dSkeletonABPKArray;
f _timeABPKAlgorithmFinished;
f _timeABPKAlgorithmStart;
i _algorithmReturnCode;
d _timestamp;
^{__CVBuffer=} _mlImage;
@"ABPKCameraParams" _cameraParams;
@"ABPK2dSkeleton" _rawDetection2dSkeletonABPK;
@"ABPK2dSkeleton" _detection2dSkeletonABPK;
@"ABPKSkeleton" _liftingSkeletonABPK;
^ _rawLiftingNetworkOutputJoints;
@"ABPK2dSkeleton" _registered2dSkeletonABPK;
@"ABPKSkeleton" _retargetedSkeletonABPK;
@"ABPKAlgorithmParams" _algorithmParams;
@"ABPKAlgorithmState" _algState;
^{__CVBuffer=} _mlOverlayImage;
```

## Properties

```
@property (Tf,V_timeABPKAlgorithmFinished) timeABPKAlgorithmFinished;
@property (Tf,V_timeABPKAlgorithmStart) timeABPKAlgorithmStart;
@property (Td,V_timestamp) timestamp;
@property (T^{__CVBuffer=},V_mlImage) mlImage;
@property (T@"ABPKCameraParams",&,V_cameraParams) cameraParams;
@property (T@"ABPK2dSkeleton",&,V_rawDetection2dSkeletonABPK) rawDetection2dSkeletonABPK;
@property (T@"ABPK2dSkeleton",&,V_detection2dSkeletonABPK) detection2dSkeletonABPK;
@property (T@"ABPKSkeleton",&,V_liftingSkeletonABPK) liftingSkeletonABPK;
@property (T^,V_rawLiftingNetworkOutputJoints) rawLiftingNetworkOutputJoints;
@property (T@"ABPK2dSkeleton",&,V_registered2dSkeletonABPK) registered2dSkeletonABPK;
@property (T@"ABPKSkeleton",&,V_retargetedSkeletonABPK) retargetedSkeletonABPK;
@property (T@"ABPKAlgorithmParams",&,V_algorithmParams) algorithmParams;
@property (Ti,V_algorithmReturnCode) algorithmReturnCode;
@property (T@"ABPKAlgorithmState",&,V_algState) algState;
@property (T^{__CVBuffer=},V_mlOverlayImage) mlOverlayImage;
```

## Instance methods

```
-[ABPKOutput setTimestamp:];
-[ABPKOutput init];
-[ABPKOutput dealloc];
-[ABPKOutput timestamp];
-[ABPKOutput algorithmReturnCode];
-[ABPKOutput cameraParams];
-[ABPKOutput liftingSkeletonABPK];
-[ABPKOutput setCameraParams:];
-[ABPKOutput getDetection2dSkeletonABPKArray];
-[ABPKOutput mlImage];
-[ABPKOutput algorithmParams];
-[ABPKOutput algState];
-[ABPKOutput convertToStreamingDictionary:withSkeletonType:referenceFrame:includeFingerRotation:yOffset:];
-[ABPKOutput detection2dSkeletonABPK];
-[ABPKOutput mlOverlayImage];
-[ABPKOutput overlayResultsOnImage:withCameraIntrinsics:];
-[ABPKOutput overlayResultsOnImage:withCameraIntrinsics:withConfig:];
-[ABPKOutput rawDetection2dSkeletonABPK];
-[ABPKOutput rawLiftingNetworkOutputJoints];
-[ABPKOutput registered2dSkeletonABPK];
-[ABPKOutput retargetedSkeletonABPK];
-[ABPKOutput saveDataToDir:withFileNamePrefix:];
-[ABPKOutput saveOnlyPoseDataToDir:withFileNamePrefix:];
-[ABPKOutput setAlgState:];
-[ABPKOutput setAlgorithmParams:];
-[ABPKOutput setAlgorithmReturnCode:];
-[ABPKOutput setDetection2dSkeletonABPK:];
-[ABPKOutput setLiftingSkeletonABPK:];
-[ABPKOutput setMlImage:];
-[ABPKOutput setMlOverlayImage:];
-[ABPKOutput setRawDetection2dSkeletonABPK:];
-[ABPKOutput setRawDetection2dSkeletonABPKArray:];
-[ABPKOutput setRawLiftingNetworkOutputJoints:];
-[ABPKOutput setRegistered2dSkeletonABPK:];
-[ABPKOutput setRetargetedSkeletonABPK:];
-[ABPKOutput setTimeABPKAlgorithmFinished:];
-[ABPKOutput setTimeABPKAlgorithmStart:];
-[ABPKOutput timeABPKAlgorithmFinished];
-[ABPKOutput timeABPKAlgorithmStart];
```
