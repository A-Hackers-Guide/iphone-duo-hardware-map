# `ABPK2DDetection`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 1 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"ABPK2DDetectionConfiguration" _config2D;
@"ABPKMLModelConfiguration2D" _mlConfig;
@"NSString" _previous_network_configuration;
^v _context;
^v _plan;
{?="plan"^v"network_index"i} _network;
@"NSArray" _inputTensorNames;
@"NSArray" _outputTensorNames;
q _deviceOrientation;
{networkparams_t="input"{inputparams_t="preprocessor"{?="bias_r"f"bias_g"f"bias_b"f"scale"f"network_wants_bgr"B}"resolution"{CGSize="width"d"height"d}}} _parameters;
{networkvariables_t="input"{inputvariables_t="imageTensor"{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i}}"output"{outputvariables_t="heatmapsTensor"{?="data"^v"reserved"^v"dim"[4Q]"stride"[4Q]"width"Q"height"Q"channels"Q"batch_number"Q"sequence_length"Q"stride_width"Q"stride_height"Q"stride_channels"Q"stride_batch_number"Q"stride_sequence_length"Q"storage_type"i}}} _variables;
@"NSString" _netSubPath;
@"NSString" _netPath;
{vector<__CVBuffer *, std::allocator<__CVBuffer *>>="__begin_"^^{__CVBuffer}"__end_"^^{__CVBuffer}""{?="__cap_"^^{__CVBuffer}}} _outputBuffers;
{vector<espresso_buffer_t, std::allocator<espresso_buffer_t>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _espressoOutputTensors;
{vector<__CVPixelBufferPool *, std::allocator<__CVPixelBufferPool *>>="__begin_"^^{__CVPixelBufferPool}"__end_"^^{__CVPixelBufferPool}""{?="__cap_"^^{__CVPixelBufferPool}}} _espressoOutputBufferPools;
@"ABPKMLNetworkV2" _networkV2;
@"NSMutableDictionary" _inputBufferDict;
@"NSMutableDictionary" _outputBufferDict;
B _useEspressoV2;
B _useEspressoZeroCopyOutput;
```

## Properties

```
@property (TB,N,V_useEspressoZeroCopyOutput) useEspressoZeroCopyOutput;
```

## Class methods

```
+[ABPK2DDetection inputDimensionsForDeviceOrientation:];
```

## Instance methods

```
-[ABPK2DDetection dealloc];
-[ABPK2DDetection initMLNetwork];
-[ABPK2DDetection _bindOutputTensor];
-[ABPK2DDetection _createResultDataFromImageDataForNeuralNetwork:originalImageData:outputPixelBuffer:numberOfOutputTensors:rotationOfResultTensor:];
-[ABPK2DDetection _endEvaluateBodyPoseForImageSignpostWithTimestamp:];
-[ABPK2DDetection _endLoadingMLModelSignpost];
-[ABPK2DDetection _startEvaluateBodyPoseForImageSignpostWithTimestamp:];
-[ABPK2DDetection _startLoadingMLModelSignpost];
-[ABPK2DDetection changeEspressoConfig:];
-[ABPK2DDetection createException:forNetwork:];
-[ABPK2DDetection initWithNetworkConfig:];
-[ABPK2DDetection runWithImage:abpkOrientation:atTimestamp:rotationOfResultTensor:];
-[ABPK2DDetection runWithImageDataForNeuralNetwork:originalImageData:abpkOrientation:atTimestamp:rotationOfResultTensor:];
-[ABPK2DDetection runWithMLImage:originalImage:abpkOrientation:atTimestamp:rotationOfResultTensor:];
-[ABPK2DDetection setUseEspressoZeroCopyOutput:];
-[ABPK2DDetection useEspressoZeroCopyOutput];
```
