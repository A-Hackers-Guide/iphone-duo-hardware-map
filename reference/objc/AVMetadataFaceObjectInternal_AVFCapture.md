# `AVMetadataFaceObjectInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 41 instance variables, 41 properties, 83 instance methods, 0 class methods

## Instance variables

```
q _faceID;
B _hasRollAngle;
d _rollAngle;
B _hasYawAngle;
d _yawAngle;
B _hasPitchAngle;
d _pitchAngle;
B _hasLeftEyeClosedConfidence;
i _leftEyeClosedConfidence;
B _hasRightEyeClosedConfidence;
i _rightEyeClosedConfidence;
B _hasSmileConfidence;
i _smileConfidence;
B _hasLeftEyeBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftEyeBounds;
B _hasRightEyeBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rightEyeBounds;
B _hasConfidence;
d _confidence;
B _hasPayingAttention;
B _payingAttention;
B _hasDistance;
d _distance;
B _hasOrientation;
Q _orientation;
B _hasOccludedFeatures;
B _occludedFeatures;
B _hasMaskConfidence;
d _maskConfidence;
B _hasEyesOpenConfidence;
d _eyesOpenConfidence;
B _hasEyesClosedConfidence;
d _eyesClosedConfidence;
B _hasEyesOccludedConfidence;
d _eyesOccludedConfidence;
B _hasEyeWearConfidence;
d _eyeWearConfidence;
B _hasLookingAtCameraConfidence;
d _lookingAtCameraConfidence;
@"AVMetadataFaceIDFrameProxy" _rawFrameProxy;
@"AVMetadataFaceIDFrameProxy" _metadataFrameProxy;
```

## Properties

```
@property (Tq,N,V_faceID) faceID;
@property (TB,N,V_hasRollAngle) hasRollAngle;
@property (Td,N,V_rollAngle) rollAngle;
@property (TB,N,V_hasYawAngle) hasYawAngle;
@property (Td,N,V_yawAngle) yawAngle;
@property (TB,N,V_hasPitchAngle) hasPitchAngle;
@property (Td,N,V_pitchAngle) pitchAngle;
@property (TB,N,V_hasLeftEyeClosedConfidence) hasLeftEyeClosedConfidence;
@property (Ti,N,V_leftEyeClosedConfidence) leftEyeClosedConfidence;
@property (TB,N,V_hasRightEyeClosedConfidence) hasRightEyeClosedConfidence;
@property (Ti,N,V_rightEyeClosedConfidence) rightEyeClosedConfidence;
@property (TB,N,V_hasSmileConfidence) hasSmileConfidence;
@property (Ti,N,V_smileConfidence) smileConfidence;
@property (TB,N,V_hasLeftEyeBounds) hasLeftEyeBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_leftEyeBounds) leftEyeBounds;
@property (TB,N,V_hasRightEyeBounds) hasRightEyeBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rightEyeBounds) rightEyeBounds;
@property (TB,N,V_hasConfidence) hasConfidence;
@property (Td,N,V_confidence) confidence;
@property (TB,N,V_hasMaskConfidence) hasMaskConfidence;
@property (Td,N,V_maskConfidence) maskConfidence;
@property (TB,N,V_hasEyesOpenConfidence) hasEyesOpenConfidence;
@property (Td,N,V_eyesOpenConfidence) eyesOpenConfidence;
@property (TB,N,V_hasEyesClosedConfidence) hasEyesClosedConfidence;
@property (Td,N,V_eyesClosedConfidence) eyesClosedConfidence;
@property (TB,N,V_hasEyesOccludedConfidence) hasEyesOccludedConfidence;
@property (Td,N,V_eyesOccludedConfidence) eyesOccludedConfidence;
@property (TB,N,V_hasEyeWearConfidence) hasEyeWearConfidence;
@property (Td,N,V_eyeWearConfidence) eyeWearConfidence;
@property (TB,N,V_hasLookingAtCameraConfidence) hasLookingAtCameraConfidence;
@property (Td,N,V_lookingAtCameraConfidence) lookingAtCameraConfidence;
@property (TB,N,V_hasPayingAttention) hasPayingAttention;
@property (TB,N,V_payingAttention) payingAttention;
@property (TB,N,V_hasDistance) hasDistance;
@property (Td,N,V_distance) distance;
@property (TB,N,V_hasOrientation) hasOrientation;
@property (TQ,N,V_orientation) orientation;
@property (TB,N,V_hasOccludedFeatures) hasOccludedFeatures;
@property (TB,N,V_occludedFeatures) occludedFeatures;
@property (T@"AVMetadataFaceIDFrameProxy",&,N,V_rawFrameProxy) rawFrameProxy;
@property (T@"AVMetadataFaceIDFrameProxy",&,N,V_metadataFrameProxy) metadataFrameProxy;
```

## Instance methods

```
-[AVMetadataFaceObjectInternal setOrientation:];
-[AVMetadataFaceObjectInternal setYawAngle:];
-[AVMetadataFaceObjectInternal hasRightEyeClosedConfidence];
-[AVMetadataFaceObjectInternal setHasEyesClosedConfidence:];
-[AVMetadataFaceObjectInternal distance];
-[AVMetadataFaceObjectInternal setHasPitchAngle:];
-[AVMetadataFaceObjectInternal setRollAngle:];
-[AVMetadataFaceObjectInternal setDistance:];
-[AVMetadataFaceObjectInternal setHasEyesOccludedConfidence:];
-[AVMetadataFaceObjectInternal setEyeWearConfidence:];
-[AVMetadataFaceObjectInternal setMaskConfidence:];
-[AVMetadataFaceObjectInternal setHasRollAngle:];
-[AVMetadataFaceObjectInternal setLookingAtCameraConfidence:];
-[AVMetadataFaceObjectInternal rightEyeBounds];
-[AVMetadataFaceObjectInternal hasMaskConfidence];
-[AVMetadataFaceObjectInternal occludedFeatures];
-[AVMetadataFaceObjectInternal hasPayingAttention];
-[AVMetadataFaceObjectInternal setHasRightEyeClosedConfidence:];
-[AVMetadataFaceObjectInternal hasYawAngle];
-[AVMetadataFaceObjectInternal setHasMaskConfidence:];
-[AVMetadataFaceObjectInternal eyesClosedConfidence];
-[AVMetadataFaceObjectInternal setLeftEyeBounds:];
-[AVMetadataFaceObjectInternal setHasEyeWearConfidence:];
-[AVMetadataFaceObjectInternal pitchAngle];
-[AVMetadataFaceObjectInternal orientation];
-[AVMetadataFaceObjectInternal setHasEyesOpenConfidence:];
-[AVMetadataFaceObjectInternal dealloc];
-[AVMetadataFaceObjectInternal hasLookingAtCameraConfidence];
-[AVMetadataFaceObjectInternal metadataFrameProxy];
-[AVMetadataFaceObjectInternal hasOrientation];
-[AVMetadataFaceObjectInternal setFaceID:];
-[AVMetadataFaceObjectInternal eyesOpenConfidence];
-[AVMetadataFaceObjectInternal hasRightEyeBounds];
-[AVMetadataFaceObjectInternal setHasSmileConfidence:];
-[AVMetadataFaceObjectInternal setHasOrientation:];
-[AVMetadataFaceObjectInternal lookingAtCameraConfidence];
-[AVMetadataFaceObjectInternal hasLeftEyeBounds];
-[AVMetadataFaceObjectInternal maskConfidence];
-[AVMetadataFaceObjectInternal setConfidence:];
-[AVMetadataFaceObjectInternal hasConfidence];
-[AVMetadataFaceObjectInternal setEyesClosedConfidence:];
-[AVMetadataFaceObjectInternal hasSmileConfidence];
-[AVMetadataFaceObjectInternal leftEyeClosedConfidence];
-[AVMetadataFaceObjectInternal hasEyesOccludedConfidence];
-[AVMetadataFaceObjectInternal setEyesOpenConfidence:];
-[AVMetadataFaceObjectInternal setMetadataFrameProxy:];
-[AVMetadataFaceObjectInternal payingAttention];
-[AVMetadataFaceObjectInternal rollAngle];
-[AVMetadataFaceObjectInternal setHasDistance:];
-[AVMetadataFaceObjectInternal setHasPayingAttention:];
-[AVMetadataFaceObjectInternal setRawFrameProxy:];
-[AVMetadataFaceObjectInternal setPayingAttention:];
-[AVMetadataFaceObjectInternal hasEyesClosedConfidence];
-[AVMetadataFaceObjectInternal setLeftEyeClosedConfidence:];
-[AVMetadataFaceObjectInternal setPitchAngle:];
-[AVMetadataFaceObjectInternal faceID];
-[AVMetadataFaceObjectInternal setHasOccludedFeatures:];
-[AVMetadataFaceObjectInternal hasDistance];
-[AVMetadataFaceObjectInternal hasOccludedFeatures];
-[AVMetadataFaceObjectInternal setHasLeftEyeClosedConfidence:];
-[AVMetadataFaceObjectInternal setSmileConfidence:];
-[AVMetadataFaceObjectInternal rawFrameProxy];
-[AVMetadataFaceObjectInternal eyesOccludedConfidence];
-[AVMetadataFaceObjectInternal smileConfidence];
-[AVMetadataFaceObjectInternal rightEyeClosedConfidence];
-[AVMetadataFaceObjectInternal setHasRightEyeBounds:];
-[AVMetadataFaceObjectInternal setEyesOccludedConfidence:];
-[AVMetadataFaceObjectInternal setHasYawAngle:];
-[AVMetadataFaceObjectInternal hasLeftEyeClosedConfidence];
-[AVMetadataFaceObjectInternal setHasLeftEyeBounds:];
-[AVMetadataFaceObjectInternal hasEyesOpenConfidence];
-[AVMetadataFaceObjectInternal setRightEyeClosedConfidence:];
-[AVMetadataFaceObjectInternal hasRollAngle];
-[AVMetadataFaceObjectInternal setHasConfidence:];
-[AVMetadataFaceObjectInternal yawAngle];
-[AVMetadataFaceObjectInternal setOccludedFeatures:];
-[AVMetadataFaceObjectInternal confidence];
-[AVMetadataFaceObjectInternal setRightEyeBounds:];
-[AVMetadataFaceObjectInternal hasEyeWearConfidence];
-[AVMetadataFaceObjectInternal setHasLookingAtCameraConfidence:];
-[AVMetadataFaceObjectInternal hasPitchAngle];
-[AVMetadataFaceObjectInternal leftEyeBounds];
-[AVMetadataFaceObjectInternal eyeWearConfidence];
```
