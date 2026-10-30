# `ABPK3DLiftingSequence`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ABPK3DLiftingAlgorithm`
- 21 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
{RingBuffer<std::vector<std::array<float, 3>>, 243UL>="_insertionIndex"Q"_storage"{array<std::vector<std::array<float, 3>>, 243UL>="__elems_"[243{vector<std::array<float, 3>, std::allocator<std::array<float, 3>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}]}"_filled"B} _3DLiftingInputBuffer;
d _imageWidth;
d _imageHeight;
i _frameCount;
@"NSArray" _inputTensorFirstStageNames;
@"NSArray" _outputTensorFirstStageNames;
^v _context_first_stage;
^v _plan_first_stage;
{?="plan"^v"network_index"i} _network_first_stage;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _inputTensorFirstStage;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _outputTensorFirstStage;
@"ABPK3DLiftingResult" _liftingResult;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _liftingResultAsModelPoses;
{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}} _gaussianSmoothingFilter;
{RingBuffer<std::vector<float>, 9UL>="_insertionIndex"Q"_storage"{array<std::vector<float>, 9UL>="__elems_"[9{vector<float, std::allocator<float>>="__begin_"^f"__end_"^f""{?="__cap_"^f}}]}"_filled"B} _smoothingFilterRingBuffer;
@"ABPKMLModelConfiguration3DLiftingSequenceFirstStage" _mlConfigFirstStage;
@"ABPKSkeletonDefinition" _abpkLiftingSkeletonDefinition;
@"ABPKMLNetworkV2" _networkV2;
@"NSMutableDictionary" _inputBufferDict;
@"NSMutableDictionary" _outputBufferDict;
B _useEspressoV2;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ABPK3DLiftingSequence init];
-[ABPK3DLiftingSequence dealloc];
-[ABPK3DLiftingSequence initMLNetwork];
-[ABPK3DLiftingSequence get3DLiftingResultsAsModelPoses];
-[ABPK3DLiftingSequence _adjustBoneLength:];
-[ABPK3DLiftingSequence _endLoading3DLiftingSequenceMLModelSignpost];
-[ABPK3DLiftingSequence _endPostProcessFor3DLiftingSequenceModelDataSignpostWithTimestamp:];
-[ABPK3DLiftingSequence _endPrepareLiftingSequenceInputSignpostWithTimestamp:];
-[ABPK3DLiftingSequence _endRunLiftingSequenceModelSignpostWithTimestamp:];
-[ABPK3DLiftingSequence _startLoading3DLiftingSequenceMLModelSignpost];
-[ABPK3DLiftingSequence _startPostProcessFor3DLiftingSequenceModelDataSignpostWithTimestamp:];
-[ABPK3DLiftingSequence _startPrepareLiftingSequenceInputSignpostWithTimestamp:];
-[ABPK3DLiftingSequence _startRunLiftingSequenceModelSignpostWithTimestamp:];
-[ABPK3DLiftingSequence getGaussianSmoothedOutput:];
-[ABPK3DLiftingSequence getLiftingResults];
-[ABPK3DLiftingSequence runLiftingModelWithBuffer:with2DReferenceResults:atTimestamp:exportDebuggingData:];
-[ABPK3DLiftingSequence runLiftingModelWithData:atTimestamp:];
-[ABPK3DLiftingSequence runLiftingModelWithData:imageResolution:deviceOrientation:atTimestamp:];
-[ABPK3DLiftingSequence saveDataToFilePath:with2DInputBuffer:withFirstStageOutput:withSmoothedOutput:withPostprocessedLiftingResults:];
-[ABPK3DLiftingSequence updateInputImageResolution:];
```
