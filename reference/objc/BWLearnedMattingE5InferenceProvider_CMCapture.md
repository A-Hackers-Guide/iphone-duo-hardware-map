# `BWLearnedMattingE5InferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledE5InferenceProvider`
- 17 instance variables, 6 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceVideoRequirement" _inputImageVideoRequirement;
@"BWInferenceVideoRequirement" _inputAlphaVideoRequirement;
@"BWInferenceVideoRequirement" _outputAlphaVideoRequirement;
@"BWInferenceVideoRequirement" _outputLowResSegmentationCloneVideoRequirement;
^{opaqueCMFormatDescription=} _outputFormatDescription;
^{opaqueCMFormatDescription=} _outputLowResSegmentationCloneFormatDescription;
@"FigLearnedMattingMetalStage" _metalProcessor;
@"BWLearnedMattingInferenceConfiguration" _configuration;
^{OpaqueVTPixelTransferSession=} _lowResSegmentationCloneCopySession;
_outputTileSize;
_inputTileSize;
_inputAlphaScale;
_outputTileOverlap;
_inputTileOverlap;
_numTiles;
B _didConfigureAndLoadEspressoNetwork;
@"NSURL" _networkURL;
```

## Properties

```
@property (T@"BWInferenceVideoRequirement",&,N,V_inputImageVideoRequirement) inputImageVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_inputAlphaVideoRequirement) inputAlphaVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_outputAlphaVideoRequirement) outputAlphaVideoRequirement;
@property (T@"BWInferenceVideoRequirement",&,N,V_outputLowResSegmentationCloneVideoRequirement) outputLowResSegmentationCloneVideoRequirement;
@property (T^{opaqueCMFormatDescription=},N) outputFormatDescription;
@property (T^{opaqueCMFormatDescription=},N) outputLowResSegmentationCloneFormatDescription;
```

## Class methods

```
+[BWLearnedMattingE5InferenceProvider initialize];
```

## Instance methods

```
-[BWLearnedMattingE5InferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWLearnedMattingE5InferenceProvider setOutputFormatDescription:];
-[BWLearnedMattingE5InferenceProvider createInputTiles:withInputs:tileInputInfo:tileOutputInfo:];
-[BWLearnedMattingE5InferenceProvider setOutputLowResSegmentationCloneVideoRequirement:];
-[BWLearnedMattingE5InferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:tileInputInfo:tileOutputInfo:];
-[BWLearnedMattingE5InferenceProvider migrateVideoRequirementsToTiledHarness];
-[BWLearnedMattingE5InferenceProvider outputAlphaVideoRequirement];
-[BWLearnedMattingE5InferenceProvider inputAlphaVideoRequirement];
-[BWLearnedMattingE5InferenceProvider dealloc];
-[BWLearnedMattingE5InferenceProvider reconcileWithPlaceholderProvider:];
-[BWLearnedMattingE5InferenceProvider setOutputAlphaVideoRequirement:];
-[BWLearnedMattingE5InferenceProvider outputFormatDescription];
-[BWLearnedMattingE5InferenceProvider setInputImageVideoRequirement:];
-[BWLearnedMattingE5InferenceProvider outputLowResSegmentationCloneVideoRequirement];
-[BWLearnedMattingE5InferenceProvider setInputAlphaVideoRequirement:];
-[BWLearnedMattingE5InferenceProvider type];
-[BWLearnedMattingE5InferenceProvider inputImageVideoRequirement];
-[BWLearnedMattingE5InferenceProvider purgeIntermediateResources];
-[BWLearnedMattingE5InferenceProvider initWithConfiguration:networkURL:resourceProvider:];
-[BWLearnedMattingE5InferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWLearnedMattingE5InferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWLearnedMattingE5InferenceProvider setOutputLowResSegmentationCloneFormatDescription:];
-[BWLearnedMattingE5InferenceProvider outputLowResSegmentationCloneFormatDescription];
-[BWLearnedMattingE5InferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
```
