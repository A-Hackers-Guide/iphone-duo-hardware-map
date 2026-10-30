# `BWPixelTransferNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWNodeBackPressureSource`
- 67 instance variables, 6 properties, 69 instance methods, 1 class methods

## Instance variables

```
i _cropMode;
i _liveCropMode;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _liveInputCropRect;
B _haveLiveInputCropRect;
B _passesBuffersThroughWhenPossible;
B _livePassesBuffersThroughWhenPossible;
B _appliesUprightExifOrientationTransformToInput;
B _liveAppliesUprightExifOrientationTransformToInput;
i _rotationDegrees;
i _liveRotationDegrees;
B _flipHorizontal;
B _liveFlipHorizontal;
B _flipVertical;
B _liveFlipVertical;
B _liveZeroFillBuffers;
B _deviceOrientationCorrectionEnabled;
B _liveDeviceOrientationCorrectionEnabled;
@"BWDeviceOrientationMonitor" _deviceOrientationMonitor;
i _prevLiveDeviceOrientationCorrectionDegrees;
B _lowSpeed;
B _liveLowSpeed;
B _updatesSampleBufferMetadataForIrisVIS;
B _liveUpdatesSampleBufferMetadataForIrisVIS;
Q _outputWidth;
Q _outputHeight;
I _outputPixelFormat;
@"NSArray" _preferredOutputPixelFormats;
i _outputColorSpaceProperties;
{?="width"i"height"i} _validOutputDimensions;
{?="width"i"height"i} _liveValidOutputDimensions;
i _maxOutputLossyCompressionLevel;
i _maxInputLossyCompressionLevel;
{CGSize="width"d"height"d} _scalerMaxScaleFactors;
{CGSize="width"d"height"d} _scalerMinScaleFactors;
^{OpaqueVTPixelRotationSession=} _rotationSession;
i _rotationSessionRotationDegrees;
B _rotationSessionFlipHorizontal;
B _rotationSessionFlipVertical;
B _rotationSessionZeroFillBuffers;
B _rotationSessionLowSpeed;
B _rotationSessionEnablesHistogram;
i _rotationSessionColorSpaceProperties;
i _lastInputUprightExifOrientation;
^{OpaqueVTPixelTransferSession=} _transferSession;
@"BWPixelBufferPool" _intermediateBufferPool;
{?="width"i"height"i} _intermediatePoolDimensions;
@"BWPixelBufferTransferRenderer" _pixelBufferTransferRenderer;
^{opaqueCMFormatDescription=} _outputFormatDescription;
B _makeCurrentConfigurationLiveOnNextRenderCallback;
@"NSObject<OS_dispatch_semaphore>" _emitSampleBufferSemaphore;
B _expectsMarkerBuffers;
B _liveExpectsMarkerBuffers;
B _appliesPrimaryCaptureRect;
B _generatesHistogram;
i _conversionMethodForStillImagesDuringHDRVideo;
B _allows422To420Conversion;
B _isConverting10BitVideoRangeTo8BitFullRangeEncouraged;
B _allowsPassthroughViaAttachment;
B _liveAllowsPassthroughViaAttachment;
^{__CVBuffer=} _intermediatePixelBufferForStillHDRToSDRConversion;
@"HDRProcessor" _HDRProcessingProcessor;
^{__IOSurfaceAccelerator=} _msrScalerForHDRProcessing;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
B _doGMLogging;
B _fractionalSourceRectEnabled;
B _firstFrameProcessed;
```

## Properties

```
@property (TB,V_firstFrameProcessed) firstFrameProcessed;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N) emitSampleBufferSemaphore;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWPixelTransferNode initialize];
```

## Instance methods

```
-[BWPixelTransferNode cropMode];
-[BWPixelTransferNode setEmitSampleBufferSemaphore:];
-[BWPixelTransferNode prepareForCurrentConfigurationToBecomeLive];
-[BWPixelTransferNode emitSampleBufferSemaphore];
-[BWPixelTransferNode setCropMode:];
-[BWPixelTransferNode outputHeight];
-[BWPixelTransferNode flipHorizontal];
-[BWPixelTransferNode setOutputColorSpaceProperties:];
-[BWPixelTransferNode renderSampleBuffer:forInput:];
-[BWPixelTransferNode makeCurrentConfigurationLive];
-[BWPixelTransferNode setFirstFrameProcessed:];
-[BWPixelTransferNode setPreferredOutputPixelFormats:];
-[BWPixelTransferNode lowSpeed];
-[BWPixelTransferNode rotationDegrees];
-[BWPixelTransferNode setMaxLossyCompressionLevel:];
-[BWPixelTransferNode setPassesBuffersThroughWhenPossible:];
-[BWPixelTransferNode init];
-[BWPixelTransferNode maxLossyCompressionLevel];
-[BWPixelTransferNode isConverting10BitVideoRangeTo8BitFullRangeEncouraged];
-[BWPixelTransferNode dealloc];
-[BWPixelTransferNode allowsPassthroughViaAttachment];
-[BWPixelTransferNode maxOutputLossyCompressionLevel];
-[BWPixelTransferNode preferredOutputPixelFormats];
-[BWPixelTransferNode updatesSampleBufferMetadataForIrisVIS];
-[BWPixelTransferNode hasNonLiveConfigurationChanges];
-[BWPixelTransferNode initWithfractionalSourceRectEnabled:];
-[BWPixelTransferNode setValidOutputDimensions:];
-[BWPixelTransferNode conversionMethodForStillImagesDuringHDRVideos];
-[BWPixelTransferNode appliesUprightExifOrientationTransformToInput];
-[BWPixelTransferNode passesBuffersThroughWhenPossible];
-[BWPixelTransferNode setInputCropRect:];
-[BWPixelTransferNode setOutputWidth:];
-[BWPixelTransferNode maxInputLossyCompressionLevel];
-[BWPixelTransferNode setAllowsPassthroughViaAttachment:];
-[BWPixelTransferNode setFlipHorizontal:];
-[BWPixelTransferNode setOutputPixelFormat:];
-[BWPixelTransferNode setAppliesUprightExifOrientationTransformToInput:];
-[BWPixelTransferNode setOutputHeight:];
-[BWPixelTransferNode appliesPrimaryCaptureRect];
-[BWPixelTransferNode inputCropRect];
-[BWPixelTransferNode flipVertical];
-[BWPixelTransferNode setExpectsMarkerBuffers:];
-[BWPixelTransferNode firstFrameProcessed];
-[BWPixelTransferNode deviceOrientationCorrectionEnabled];
-[BWPixelTransferNode setConverting10BitVideoRangeTo8BitFullRangeEncouraged:];
-[BWPixelTransferNode setRotationDegrees:];
-[BWPixelTransferNode handleDroppedSample:forInput:];
-[BWPixelTransferNode setDeviceOrientationCorrectionEnabled:];
-[BWPixelTransferNode didReachEndOfDataForConfigurationID:input:];
-[BWPixelTransferNode setAllows422To420Conversion:];
-[BWPixelTransferNode expectsMarkerBuffers];
-[BWPixelTransferNode outputWidth];
-[BWPixelTransferNode setFlipVertical:];
-[BWPixelTransferNode setConversionMethodForStillImagesDuringHDRVideos:];
-[BWPixelTransferNode setAppliesPrimaryCaptureRect:];
-[BWPixelTransferNode generatesHistogram];
-[BWPixelTransferNode allows422To420Conversion];
-[BWPixelTransferNode nodeSubType];
-[BWPixelTransferNode outputColorSpaceProperties];
-[BWPixelTransferNode setMaxInputLossyCompressionLevel:];
-[BWPixelTransferNode didSelectFormat:forInput:];
-[BWPixelTransferNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWPixelTransferNode setUpdatesSampleBufferMetadataForIrisVIS:];
-[BWPixelTransferNode nodeType];
-[BWPixelTransferNode outputPixelFormat];
-[BWPixelTransferNode validOutputDimensions];
-[BWPixelTransferNode setLowSpeed:];
-[BWPixelTransferNode setGeneratesHistogram:];
-[BWPixelTransferNode setMaxOutputLossyCompressionLevel:];
```
