# `BWLearnedMattingInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledEspressoInferenceProvider`
- 17 instance variables, 6 properties, 23 instance methods, 1 class methods

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
+[BWLearnedMattingInferenceProvider initialize];
```

## Instance methods

```
-[BWLearnedMattingInferenceProvider setOutputFormatDescription:];
-[BWLearnedMattingInferenceProvider setOutputLowResSegmentationCloneVideoRequirement:];
-[BWLearnedMattingInferenceProvider migrateVideoRequirementsToTiledHarness];
-[BWLearnedMattingInferenceProvider outputAlphaVideoRequirement];
-[BWLearnedMattingInferenceProvider inputAlphaVideoRequirement];
-[BWLearnedMattingInferenceProvider dealloc];
-[BWLearnedMattingInferenceProvider reconcileWithPlaceholderProvider:];
-[BWLearnedMattingInferenceProvider setOutputAlphaVideoRequirement:];
-[BWLearnedMattingInferenceProvider outputFormatDescription];
-[BWLearnedMattingInferenceProvider setInputImageVideoRequirement:];
-[BWLearnedMattingInferenceProvider outputLowResSegmentationCloneVideoRequirement];
-[BWLearnedMattingInferenceProvider setInputAlphaVideoRequirement:];
-[BWLearnedMattingInferenceProvider type];
-[BWLearnedMattingInferenceProvider inputImageVideoRequirement];
-[BWLearnedMattingInferenceProvider purgeIntermediateResources];
-[BWLearnedMattingInferenceProvider initWithConfiguration:networkURL:resourceProvider:];
-[BWLearnedMattingInferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWLearnedMattingInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWLearnedMattingInferenceProvider setOutputLowResSegmentationCloneFormatDescription:];
-[BWLearnedMattingInferenceProvider outputLowResSegmentationCloneFormatDescription];
-[BWLearnedMattingInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWLearnedMattingInferenceProvider createInputTiles:withInputs:atPosition:cmdBuffer:];
-[BWLearnedMattingInferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:atPosition:cmdBuffer:];
```
