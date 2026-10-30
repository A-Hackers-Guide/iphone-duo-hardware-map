# `BWDepthConverterNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 54 instance variables, 15 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _depthProcessingEnabled;
B _streamingGDRFilteringEnabled;
B _stillGDRFilteringSupportEnabled;
B _streamingSMPFilteringEnabled;
B _streamingMonocularToDepthDataOutput;
B _streamingMonocularFilteringRequested;
@"NSDictionary" _sensorIDDictionary;
@"NSDictionary" _cameraInfoByPortType;
B _forceCPath;
{?="width"i"height"i} _inputDepthDimensions;
^{opaqueCMFormatDescription=} _outputFormatDescription;
I _outputFormat;
{?="width"i"height"i} _outputDimensions;
B _nonAspectPreservingScaleEnabled;
B _backPressureDrivenPipelining;
{?="columns"[4]} _identityExtrinsicMatrix;
i _depthAccuracy;
B _depthLensDistortionCorrectionPolynomialsAvailable;
{?="forwardOrders"[8f]"inverseOrders"[8f]} _depthLensDistortionCorrectionBasePolynomial;
{?="forwardOrders"[8f]"inverseOrders"[8f]} _depthLensDistortionCorrectionDynamicPolynomial;
f _depthRelativePixelSizeInMicrons;
i _baseRotationDegrees;
i _rotationDegrees;
B _mirroringEnabled;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputCropRect;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
B _providesUnfilteredDepthAsAttachedMedia;
^{opaqueCMFormatDescription=} _unfilteredDepthFormatDescription;
^{OpaqueVTPixelTransferSession=} _unfilteredDepthTransferSession;
B _depthIsAlwaysHighQuality;
B _depthOriginatesFromNeuralNetwork;
^{__CVBuffer=} _fixedPointScaledIntermediateBuffer;
^{__CVBuffer=} _fixedPointRotatedIntermediateBuffer;
^{__CVBuffer=} _filteringInputBuffer;
^{__CVBuffer=} _streamingFilteringScaledDepthInputBuffer;
^{__CVBuffer=} _streamingFilteringScaledDepthOutputBuffer;
^{__CVBuffer=} _filteringScaledYUVBuffer;
^{__CVBuffer=} _filteringOutputBuffer;
B _conversionAfterFilteringRequired;
B _depthFromInfrared;
@"FigMetalContext" _metalContext;
@"FigDepthValueMultiplier" _depthValueMultiplier;
@"NSString" _depthProcessorClassName;
^{CMPhotoScaleAndRotateSession=} _scaler;
@"<DepthProcessor>" _depthProcessor;
i _depthProcessorVersion;
i _depthBufferOriginalExifOrientation;
i _depthBufferFinalExifOrientation;
@"NSObject<OS_dispatch_queue>" _depthProcessorWorkerQueue;
@"BWStillImageNodeConfiguration" _stillImageNodeConfiguration;
B _skipSmartStyleBuffer;
@"ADMonocularStillsPipeline" _monocularStillsPipeline;
@"BWDisparityAPSScaling" _disparityAPSScaling;
```

## Properties

```
@property (TB,N,V_streamingGDRFilteringEnabled) streamingGDRFilteringEnabled;
@property (TB,N,V_stillGDRFilteringSupportEnabled) stillGDRFilteringSupportEnabled;
@property (TB,N,V_streamingSMPFilteringEnabled) streamingSMPFilteringEnabled;
@property (TB,N,V_streamingMonocularToDepthDataOutput) streamingMonocularToDepthDataOutput;
@property (TB,N,V_streamingMonocularFilteringRequested) streamingMonocularFilteringRequested;
@property (TI,N) outputFormat;
@property (T{?=ii},N) outputDimensions;
@property (TB,N,V_nonAspectPreservingScaleEnabled) nonAspectPreservingScaleEnabled;
@property (Ti,N,V_baseRotationDegrees) baseRotationDegrees;
@property (Ti,N,V_rotationDegrees) rotationDegrees;
@property (TB,N,V_mirroringEnabled) mirroringEnabled;
@property (Ti,N,V_horizontalSensorBinningFactor) horizontalSensorBinningFactor;
@property (Ti,N,V_verticalSensorBinningFactor) verticalSensorBinningFactor;
@property (TB,N,V_providesUnfilteredDepthAsAttachedMedia) providesUnfilteredDepthAsAttachedMedia;
@property (TB,N,V_skipSmartStyleBuffer) skipSmartStyleBuffer;
```

## Class methods

```
+[BWDepthConverterNode initialize];
```

## Instance methods

```
-[BWDepthConverterNode verticalSensorBinningFactor];
-[BWDepthConverterNode setHorizontalSensorBinningFactor:];
-[BWDepthConverterNode prepareForCurrentConfigurationToBecomeLive];
-[BWDepthConverterNode horizontalSensorBinningFactor];
-[BWDepthConverterNode setVerticalSensorBinningFactor:];
-[BWDepthConverterNode renderSampleBuffer:forInput:];
-[BWDepthConverterNode setOutputDimensions:];
-[BWDepthConverterNode setOutputFormat:];
-[BWDepthConverterNode setNonAspectPreservingScaleEnabled:];
-[BWDepthConverterNode setBaseRotationDegrees:];
-[BWDepthConverterNode rotationDegrees];
-[BWDepthConverterNode nonAspectPreservingScaleEnabled];
-[BWDepthConverterNode dealloc];
-[BWDepthConverterNode setProvidesUnfilteredDepthAsAttachedMedia:];
-[BWDepthConverterNode outputDimensions];
-[BWDepthConverterNode setStreamingMonocularToDepthDataOutput:];
-[BWDepthConverterNode setMirroringEnabled:];
-[BWDepthConverterNode setStreamingSMPFilteringEnabled:];
-[BWDepthConverterNode setStreamingMonocularFilteringRequested:];
-[BWDepthConverterNode mirroringEnabled];
-[BWDepthConverterNode providesUnfilteredDepthAsAttachedMedia];
-[BWDepthConverterNode setStreamingGDRFilteringEnabled:];
-[BWDepthConverterNode streamingMonocularFilteringRequested];
-[BWDepthConverterNode stillGDRFilteringSupportEnabled];
-[BWDepthConverterNode setRotationDegrees:];
-[BWDepthConverterNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWDepthConverterNode setStillGDRFilteringSupportEnabled:];
-[BWDepthConverterNode setSkipSmartStyleBuffer:];
-[BWDepthConverterNode baseRotationDegrees];
-[BWDepthConverterNode streamingSMPFilteringEnabled];
-[BWDepthConverterNode nodeSubType];
-[BWDepthConverterNode initWithStillImageNodeConfiguration:cameraInfoByPortType:sensorIDDictionary:rgbPersonSegmentationEnabled:depthIsAlwaysHighQuality:depthOriginatesFromNeuralNetwork:backPressureDrivenPipelining:];
-[BWDepthConverterNode streamingGDRFilteringEnabled];
-[BWDepthConverterNode skipSmartStyleBuffer];
-[BWDepthConverterNode streamingMonocularToDepthDataOutput];
-[BWDepthConverterNode outputFormat];
-[BWDepthConverterNode nodeType];
```
