# `ABPK3DLifting`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ABPK3DLiftingAlgorithm`
- 14 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _inputTensorNames;
@"NSArray" _outputTensorNames;
^v _context;
^v _plan;
{?="plan"^v"network_index"i} _network;
@"ABPKMLNetworkV2" _networkV2;
@"NSMutableDictionary" inputBufferDict;
@"NSMutableDictionary" outputBufferDict;
B _useEspressoV2;
{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i} _outputTensor;
@"ABPK3DLiftingResult" _liftingResult;
{vector<simd_float4x4, std::allocator<simd_float4x4>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _liftingResultAsModelPoses;
@"ABPKSkeletonDefinition" _abpkLiftingSkeletonDefinition;
@"ABPKMLModelConfiguration3DLifting" _mlConfig;
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
-[ABPK3DLifting init];
-[ABPK3DLifting dealloc];
-[ABPK3DLifting initMLNetwork];
-[ABPK3DLifting get3DLiftingResultsAsModelPoses];
-[ABPK3DLifting _adjustBoneLength:];
-[ABPK3DLifting _endLoading3DLiftingMLModelSignpost];
-[ABPK3DLifting _endPostProcessDataSignpostWithTimestamp:];
-[ABPK3DLifting _endPrepareLiftingInputSignpostWithTimestamp:];
-[ABPK3DLifting _endRunLiftingModelSignpostWithTimestamp:];
-[ABPK3DLifting _startLoading3DLiftingMLModelSignpost];
-[ABPK3DLifting _startPostProcessDataSignpostWithTimestamp:];
-[ABPK3DLifting _startPrepareLiftingInputSignpostWithTimestamp:];
-[ABPK3DLifting _startRunLiftingModelSignpostWithTimestamp:];
-[ABPK3DLifting _transformRelativeToHip:count:];
-[ABPK3DLifting getLiftingResults];
-[ABPK3DLifting runLiftingModelWithData:atTimestamp:];
```
