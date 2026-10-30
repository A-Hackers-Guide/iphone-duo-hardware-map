# `CAMBurstFaceStat`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 34 instance variables, 34 properties, 70 instance methods, 0 class methods

## Instance variables

```
B leftEyeOpen;
B rightEyeOpen;
B smiling;
B foundByFaceCore;
B hasLeftEye;
B hasRightEye;
B hasRollAngle;
B hasYawAngle;
B smallFace;
B _isSyncedWithImage;
f normalizedSigma;
i faceId;
i hwFaceId;
i framesSinceLast;
f focusScore;
f normalizedFocusScore;
f faceScore;
f leftEyeBlinkScore;
f rightEyeBlinkScore;
f smileScore;
i FCRLeftEyeFeaturesOffset;
i FCRRightEyeFeaturesOffset;
i FCRSmileFeaturesOffset;
i FCRBlinkFeaturesSize;
i FCRSmileFeaturesSize;
f rollAngle;
f yawAngle;
@"NSMutableArray" FCRSmileAndBlinkFeatures;
d timestamp;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} faceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} normalizedFaceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} leftEyeRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} rightEyeRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hwFaceRect;
```

## Properties

```
@property (TB,VleftEyeOpen) leftEyeOpen;
@property (TB,VrightEyeOpen) rightEyeOpen;
@property (TB,Vsmiling) smiling;
@property (Tf,VleftEyeBlinkScore) leftEyeBlinkScore;
@property (Tf,VrightEyeBlinkScore) rightEyeBlinkScore;
@property (Tf,VsmileScore) smileScore;
@property (TB,VhasLeftEye) hasLeftEye;
@property (TB,VhasRightEye) hasRightEye;
@property (TB,VfoundByFaceCore) foundByFaceCore;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VfaceRect) faceRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VnormalizedFaceRect) normalizedFaceRect;
@property (Ti,VfaceId) faceId;
@property (Ti,VframesSinceLast) framesSinceLast;
@property (Tf,VfocusScore) focusScore;
@property (Tf,VfaceScore) faceScore;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VleftEyeRect) leftEyeRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},VrightEyeRect) rightEyeRect;
@property (Ti,VFCRLeftEyeFeaturesOffset) FCRLeftEyeFeaturesOffset;
@property (Ti,VFCRRightEyeFeaturesOffset) FCRRightEyeFeaturesOffset;
@property (Ti,VFCRSmileFeaturesOffset) FCRSmileFeaturesOffset;
@property (Ti,VFCRBlinkFeaturesSize) FCRBlinkFeaturesSize;
@property (Ti,VFCRSmileFeaturesSize) FCRSmileFeaturesSize;
@property (T@"NSMutableArray",VFCRSmileAndBlinkFeatures) FCRSmileAndBlinkFeatures;
@property (Ti,VhwFaceId) hwFaceId;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_hwFaceRect) hwFaceRect;
@property (Tf,VnormalizedFocusScore) normalizedFocusScore;
@property (Tf,VnormalizedSigma) normalizedSigma;
@property (TB,VhasRollAngle) hasRollAngle;
@property (TB,VhasYawAngle) hasYawAngle;
@property (Tf,VrollAngle) rollAngle;
@property (Tf,VyawAngle) yawAngle;
@property (Td,Vtimestamp) timestamp;
@property (TB,V_isSyncedWithImage) isSyncedWithImage;
@property (TB,VsmallFace) smallFace;
```

## Instance methods

```
-[CAMBurstFaceStat setYawAngle:];
-[CAMBurstFaceStat setTimestamp:];
-[CAMBurstFaceStat setRollAngle:];
-[CAMBurstFaceStat setHasRollAngle:];
-[CAMBurstFaceStat hasYawAngle];
-[CAMBurstFaceStat timestamp];
-[CAMBurstFaceStat rollAngle];
-[CAMBurstFaceStat copyWithZone:];
-[CAMBurstFaceStat setHasYawAngle:];
-[CAMBurstFaceStat hasRollAngle];
-[CAMBurstFaceStat yawAngle];
-[CAMBurstFaceStat faceRect];
-[CAMBurstFaceStat setFaceRect:];
-[CAMBurstFaceStat normalizedFaceRect];
-[CAMBurstFaceStat faceId];
-[CAMBurstFaceStat setFaceId:];
-[CAMBurstFaceStat FCRLeftEyeFeaturesOffset];
-[CAMBurstFaceStat FCRSmileAndBlinkFeatures];
-[CAMBurstFaceStat FCRSmileFeaturesSize];
-[CAMBurstFaceStat foundByFaceCore];
-[CAMBurstFaceStat framesSinceLast];
-[CAMBurstFaceStat normalizedSigma];
-[CAMBurstFaceStat setHasRightEye:];
-[CAMBurstFaceStat setLeftEyeOpen:];
-[CAMBurstFaceStat smiling];
-[CAMBurstFaceStat FCRBlinkFeaturesSize];
-[CAMBurstFaceStat FCRRightEyeFeaturesOffset];
-[CAMBurstFaceStat FCRSmileFeaturesOffset];
-[CAMBurstFaceStat setLeftEyeRect:];
-[CAMBurstFaceStat faceScore];
-[CAMBurstFaceStat focusScore];
-[CAMBurstFaceStat hasLeftEye];
-[CAMBurstFaceStat hasRightEye];
-[CAMBurstFaceStat hwFaceId];
-[CAMBurstFaceStat hwFaceRect];
-[CAMBurstFaceStat initWithFaceStat:];
-[CAMBurstFaceStat isSyncedWithImage];
-[CAMBurstFaceStat leftEyeBlinkScore];
-[CAMBurstFaceStat leftEyeOpen];
-[CAMBurstFaceStat leftEyeRect];
-[CAMBurstFaceStat normalizedFocusScore];
-[CAMBurstFaceStat rightEyeBlinkScore];
-[CAMBurstFaceStat rightEyeOpen];
-[CAMBurstFaceStat rightEyeRect];
-[CAMBurstFaceStat setFCRBlinkFeaturesSize:];
-[CAMBurstFaceStat setFCRLeftEyeFeaturesOffset:];
-[CAMBurstFaceStat setFCRRightEyeFeaturesOffset:];
-[CAMBurstFaceStat setFCRSmileAndBlinkFeatures:];
-[CAMBurstFaceStat setFCRSmileFeaturesOffset:];
-[CAMBurstFaceStat setFCRSmileFeaturesSize:];
-[CAMBurstFaceStat setFaceScore:];
-[CAMBurstFaceStat setFocusScore:];
-[CAMBurstFaceStat setFoundByFaceCore:];
-[CAMBurstFaceStat setFramesSinceLast:];
-[CAMBurstFaceStat setHasLeftEye:];
-[CAMBurstFaceStat setHwFaceId:];
-[CAMBurstFaceStat setHwFaceRect:];
-[CAMBurstFaceStat setIsSyncedWithImage:];
-[CAMBurstFaceStat setLeftEyeBlinkScore:];
-[CAMBurstFaceStat setNormalizedFaceRect:];
-[CAMBurstFaceStat setNormalizedFocusScore:];
-[CAMBurstFaceStat setNormalizedSigma:];
-[CAMBurstFaceStat setRightEyeBlinkScore:];
-[CAMBurstFaceStat setRightEyeOpen:];
-[CAMBurstFaceStat setRightEyeRect:];
-[CAMBurstFaceStat setSmallFace:];
-[CAMBurstFaceStat setSmileScore:];
-[CAMBurstFaceStat setSmiling:];
-[CAMBurstFaceStat smallFace];
-[CAMBurstFaceStat smileScore];
```
