# `ABPK3DLiftingLSTM`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
d _imageWidth;
d _imageHeight;
i _frameCount;
@"NSArray" _inputTensorLSTMNames;
@"NSArray" _outputTensorLSTMNames;
@"ABPK3DLiftingResult" _liftingResult;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _liftingResultAsModelPoses;
@"ABPKMLModelConfiguration3DLiftingLSTM" _mlConfigLSTM;
@"ABPKSkeletonDefinition" _abpkLiftingSkeletonDefinition;
@"ABPKMLNetworkV2" _networkV2;
@"NSMutableDictionary" _inputBufferDict;
@"NSMutableDictionary" _outputBufferDict;
B _useEspressoV2;
B _setUpStatus;
```

## Instance methods

```
-[ABPK3DLiftingLSTM init];
-[ABPK3DLiftingLSTM initMLNetwork];
-[ABPK3DLiftingLSTM get3DLiftingResultsAsModelPoses];
-[ABPK3DLiftingLSTM _adjustBoneLength:];
-[ABPK3DLiftingLSTM _endLoading3DLiftingLSTMMLModelSignpost];
-[ABPK3DLiftingLSTM _endPostProcessFor3DLiftingLSTMModelDataSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM _endPrepareLiftingLSTMInputSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM _endRunLiftingLSTMModelSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM _startLoading3DLiftingLSTMMLModelSignpost];
-[ABPK3DLiftingLSTM _startPostProcessFor3DLiftingLSTMModelDataSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM _startPrepareLiftingLSTMInputSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM _startRunLiftingLSTMModelSignpostWithTimestamp:];
-[ABPK3DLiftingLSTM getLiftingResults];
-[ABPK3DLiftingLSTM resetCellStateAndHiddenStateInput];
-[ABPK3DLiftingLSTM resetInputCellStateBuffer];
-[ABPK3DLiftingLSTM resetInputHiddenStateBuffer];
-[ABPK3DLiftingLSTM runLiftingModelWithData:atTimestamp:];
-[ABPK3DLiftingLSTM runLiftingModelWithData:imageResolution:deviceOrientation:atTimestamp:];
-[ABPK3DLiftingLSTM runLiftingModelWithRawDetectionXYVisbility:with2DReferenceResults:atTimestamp:exportDebuggingData:];
-[ABPK3DLiftingLSTM saveDataToFilePath:with2DInput:withLSTMOutput:withPostprocessedLiftingResults:];
-[ABPK3DLiftingLSTM updateInputImageResolution:];
```
