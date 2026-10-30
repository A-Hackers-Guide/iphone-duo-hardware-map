# `BWLearnedNRInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledEspressoInferenceProvider`
- 11 instance variables, 0 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceVideoRequirement" _inputVideoRequirement;
@"NSArray" _outputVideoRequirements;
{?="width"i"height"i} _preparedOutputDimensions;
@"NSMutableDictionary" _outputFormatDescriptionByAttachedMediaKey;
@"BWLearnedNRInferenceConfiguration" _configuration;
@"LearnedNRMetalStage" _metalStage;
_numTiles;
_tileSize;
I _tileOverlap;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _renderROI;
B _isInputFormatRaw;
```

## Class methods

```
+[BWLearnedNRInferenceProvider initialize];
```

## Instance methods

```
-[BWLearnedNRInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWLearnedNRInferenceProvider dealloc];
-[BWLearnedNRInferenceProvider type];
-[BWLearnedNRInferenceProvider purgeIntermediateResources];
-[BWLearnedNRInferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWLearnedNRInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWLearnedNRInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWLearnedNRInferenceProvider createInputTiles:withInputs:atPosition:cmdBuffer:];
-[BWLearnedNRInferenceProvider initWithConfiguration:resourceProvider:];
-[BWLearnedNRInferenceProvider outputRequirementsToProduceForInputSampleBuffer:];
-[BWLearnedNRInferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:atPosition:cmdBuffer:];
```
