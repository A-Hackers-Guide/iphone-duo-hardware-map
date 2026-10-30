# `FigCaptureCameraSourcePipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSourcePipeline`
- Protocols: `BWVISOverscanPredictionDelegate`
- 80 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
B _useCaptureOutputForPreview;
B _hostingSupported;
i _deviceType;
i _devicePosition;
@"FigCaptureCameraSourcePipelineConfiguration" _configuration;
@"NSMutableArray" _sourceNodes;
@"BWMultiStreamCameraSourceNode" _sourceNode;
@"BWMultiStreamCameraSourceNode" _telephotoSourceNode;
@"BWMultiStreamCameraSourceNode" _superWideSourceNode;
@"BWMultiStreamCameraSourceNode" _infraredSourceNode;
@"BWMultiStreamCameraSourceNode" _renoSuperWideSourceNode;
@"BWMultiStreamCameraSourceNode" _colorAssistSourceNode;
B _attachedInfraredSourcePipeline;
@"BWDockKitNode" _dockKitNode;
@"BWNodeOutput" _sourceFormatReferenceOutput;
@"NSMutableArray" _synchronizerNodes;
@"BWSlaveFrameSynchronizerNode" _slaveFrameSynchronizerNode;
@"NSArray" _previewFilters;
@"NSMutableDictionary" _cinematicFramingNodesBySourceDeviceType;
@"NSMutableDictionary" _smartCropNodesBySourceDeviceType;
B _isSmartCropOutputDimensionsTransposed;
@"NSMutableDictionary" _backgroundBlurNodesBySourceDeviceType;
B _usingVideoCaptureOutputNetworkCrossoverNodeForPreview;
@"NSDictionary" _previewOutputsArrayBySourceDeviceType;
@"NSDictionary" _stillImageOutputsByPortType;
@"NSDictionary" _stillImageSensorRawOutputsByPortType;
@"NSDictionary" _sensorRawOutputsByPortType;
@"NSDictionary" _hueMapOutputsByPortType;
@"NSDictionary" _videoCaptureOutputsArrayBySourceDeviceType;
@"NSDictionary" _numberOfFaceTrackingConnectionConfigurationsBySourceDeviceType;
[30I] _nextVideoCaptureOutputIndexBySourceDeviceType;
[30I] _nextPreviewOutputIndexBySourceDeviceType;
@"NSArray" _pointCloudOutputs;
I _nextPointCloudOutputIndex;
@"NSMutableDictionary" _metadataOutputsByCategoryAndSourceDeviceType;
@"NSDictionary" _visionDataOutputsBySourceDeviceType;
@"NSDictionary" _secureVideoOutputsBySourceDeviceType;
@"BWNodeOutput" _depthOutput;
@"NSMutableArray" _sourceDeviceTypesWithLightSourceMaskEnabledOnVideoCaptureOutputs;
@"NSMutableArray" _sourceDeviceTypesWithKeypointDescriptorDataEnabledOnVideoCaptureOutputs;
@"NSDictionary" _semanticMasksOutputsBySourceDeviceType;
@"NSDictionary" _semanticMasksMetadataOutputBySourceDeviceType;
@"NSDictionary" _semanticMasksSceneClassifierOutputBySourceDeviceType;
@"NSMutableDictionary" _metadataOutputsByCategoryForSessionIDAndSourceDeviceType;
@"NSMutableDictionary" _metadataConnectionConfigurationBySessionID;
@"BWFigVideoCaptureDevice" _captureDevice;
@"BWCinematographyObjectTrackingNode" _cinematographyObjectTrackingNodeForMetadata;
^{OpaqueFigCaptureSource=} _captureSource;
@"FigCaptureSourceVideoFormat" _captureSourceVideoFormat;
@"FigCaptureSourceDepthDataFormat" _captureSourceDepthDataFormat;
B _stillImageOutputDerivesFromVideoCaptureOutput;
@"BWMemoryPool" _memoryPool;
B _overCapturePercentage;
i _depthType;
B _hardwareDepthFilteringEnabled;
B _videoHDRImageStatisticsEnabled;
i _maxFrameRateClientOverride;
@"NSMutableDictionary" _metadataFanOutNodeByMetadataCategory;
@"BWFanOutNode" _videoCaptureSplitterNode;
@"<BWCinematicFramingStatesProvider>" _cinematicFramingCameraStatesProvider;
@"BWDeskCamNode" _deskCamNode;
@"<BWSmartCropHomographyProvider>" _smartCropHomographyProvider;
B _enableSlaveFrameSynchronizerForZoomPIPOnly;
B _powerOptimizedVISOverscanEnabled;
@"NSMutableDictionary" _smartStyleLearningNodesBySourceDeviceType;
@"NSMutableDictionary" _smartStyleMetadataSynchronizerNodesBySourceDeviceType;
B _trueVideoCaptureEnabled;
B _preLTMThumbnailEnabled;
B _postColorProcessingThumbnailEnabled;
B _secondaryPreviewOutputEnabled;
B _smartStyleOnPreviewOutputEnabled;
B _smartStyleOnSecondaryPreviewOutputEnabled;
B _smartStyleRenderedAttachmentEnabled;
@"FigCaptureSmartStyle" _smartStyle;
@"FigCaptureTextureStyle" _textureStyle;
B _lowLightVideoNoiseReductionEnabled;
i _omahaPrimaryStreamSourceDeviceType;
B _weightSegmentMapEnabled;
B _lowLatencyStabilizationEnabled;
i _stillImageOutputRetainedBufferCountOverride;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCaptureCameraSourcePipeline initialize];
```

## Instance methods

```
-[FigCaptureCameraSourcePipeline dealloc];
-[FigCaptureCameraSourcePipeline description];
-[FigCaptureCameraSourcePipeline visOverscanPredictor:allowsReducedOverscan:];
```
