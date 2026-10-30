# `BWSoftISPProcessorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 25 instance variables, 25 properties, 51 instance methods, 0 class methods

## Instance variables

```
{?="width"i"height"i} _inputDimensions;
{CGPoint="x"d"y"d} _sensorCenterOffset;
{?="width"i"height"i} _outputDimensions;
{?="width"i"height"i} _enhancedResolutionDimensions;
@"NSDictionary" _inputDimensionsByResolutionFlavorByPortType;
@"NSDictionary" _outputDimensionsByResolutionFlavor;
I _sensorRawPixelFormat;
B _cmiResourceEnabled;
B _standardYUVProcessingEnabled;
B _rawNightModeEnabled;
B _deepFusionEnabled;
B _learnedFusionEnabled;
B _adaptiveFusionEnabled;
B _learnedNREnabled;
B _learnedNRDraftDemosaicEnabled;
B _gdcEnabled;
B _quadraProcessingEnabled;
i _qBinProcessingMode;
i _lossyCompressionLevel;
B _linearRGBForDisparityEnabled;
B _ltmHDRCurvesEnabled;
B _sfhrSupportEnabled;
B _lowlightSFHRSupportEnabled;
B _calibrationEnabled;
B _auxiliaryTypesForFocusPixelDisparityEnabled;
```

## Properties

```
@property (T{?=ii},N,V_inputDimensions) inputDimensions;
@property (T{CGPoint=dd},N,V_sensorCenterOffset) sensorCenterOffset;
@property (T{?=ii},N,V_outputDimensions) outputDimensions;
@property (T{?=ii},N,V_enhancedResolutionDimensions) enhancedResolutionDimensions;
@property (T@"NSDictionary",&,N,V_inputDimensionsByResolutionFlavorByPortType) inputDimensionsByResolutionFlavorByPortType;
@property (T@"NSDictionary",&,N,V_outputDimensionsByResolutionFlavor) outputDimensionsByResolutionFlavor;
@property (TI,N,V_sensorRawPixelFormat) sensorRawPixelFormat;
@property (TB,N,V_cmiResourceEnabled) cmiResourceEnabled;
@property (TB,N,V_standardYUVProcessingEnabled) standardYUVProcessingEnabled;
@property (TB,N,V_rawNightModeEnabled) rawNightModeEnabled;
@property (TB,N,V_deepFusionEnabled) deepFusionEnabled;
@property (TB,N,V_learnedFusionEnabled) learnedFusionEnabled;
@property (TB,N,V_adaptiveFusionEnabled) adaptiveFusionEnabled;
@property (TB,N,V_learnedNREnabled) learnedNREnabled;
@property (TB,N,V_learnedNRDraftDemosaicEnabled) learnedNRDraftDemosaicEnabled;
@property (TB,N,V_gdcEnabled) gdcEnabled;
@property (TB,N,V_quadraProcessingEnabled) quadraProcessingEnabled;
@property (Ti,N,V_qBinProcessingMode) qBinProcessingMode;
@property (Ti,N,V_lossyCompressionLevel) lossyCompressionLevel;
@property (TB,N,V_linearRGBForDisparityEnabled) linearRGBForDisparityEnabled;
@property (TB,N,V_auxiliaryTypesForFocusPixelDisparityEnabled) auxiliaryTypesForFocusPixelDisparityEnabled;
@property (TB,N,V_ltmHDRCurvesEnabled) ltmHDRCurvesEnabled;
@property (TB,N,V_sfhrSupportEnabled) sfhrSupportEnabled;
@property (TB,N,V_lowlightSFHRSupportEnabled) lowlightSFHRSupportEnabled;
@property (TB,N,V_calibrationEnabled) calibrationEnabled;
```

## Instance methods

```
-[BWSoftISPProcessorControllerConfiguration deepFusionEnabled];
-[BWSoftISPProcessorControllerConfiguration sensorRawPixelFormat];
-[BWSoftISPProcessorControllerConfiguration setRawNightModeEnabled:];
-[BWSoftISPProcessorControllerConfiguration setSensorCenterOffset:];
-[BWSoftISPProcessorControllerConfiguration setCmiResourceEnabled:];
-[BWSoftISPProcessorControllerConfiguration setDeepFusionEnabled:];
-[BWSoftISPProcessorControllerConfiguration enhancedResolutionDimensions];
-[BWSoftISPProcessorControllerConfiguration sensorCenterOffset];
-[BWSoftISPProcessorControllerConfiguration setEnhancedResolutionDimensions:];
-[BWSoftISPProcessorControllerConfiguration setLtmHDRCurvesEnabled:];
-[BWSoftISPProcessorControllerConfiguration setOutputDimensions:];
-[BWSoftISPProcessorControllerConfiguration linearRGBForDisparityEnabled];
-[BWSoftISPProcessorControllerConfiguration setStandardYUVProcessingEnabled:];
-[BWSoftISPProcessorControllerConfiguration setLearnedNRDraftDemosaicEnabled:];
-[BWSoftISPProcessorControllerConfiguration dealloc];
-[BWSoftISPProcessorControllerConfiguration outputDimensions];
-[BWSoftISPProcessorControllerConfiguration gdcEnabled];
-[BWSoftISPProcessorControllerConfiguration inputDimensions];
-[BWSoftISPProcessorControllerConfiguration rawNightModeEnabled];
-[BWSoftISPProcessorControllerConfiguration ltmHDRCurvesEnabled];
-[BWSoftISPProcessorControllerConfiguration setCalibrationEnabled:];
-[BWSoftISPProcessorControllerConfiguration lowlightSFHRSupportEnabled];
-[BWSoftISPProcessorControllerConfiguration setAdaptiveFusionEnabled:];
-[BWSoftISPProcessorControllerConfiguration learnedNREnabled];
-[BWSoftISPProcessorControllerConfiguration quadraProcessingEnabled];
-[BWSoftISPProcessorControllerConfiguration setLearnedNREnabled:];
-[BWSoftISPProcessorControllerConfiguration qBinProcessingMode];
-[BWSoftISPProcessorControllerConfiguration calibrationEnabled];
-[BWSoftISPProcessorControllerConfiguration setAuxiliaryTypesForFocusPixelDisparityEnabled:];
-[BWSoftISPProcessorControllerConfiguration setLossyCompressionLevel:];
-[BWSoftISPProcessorControllerConfiguration setInputDimensionsByResolutionFlavorByPortType:];
-[BWSoftISPProcessorControllerConfiguration setOutputDimensionsByResolutionFlavor:];
-[BWSoftISPProcessorControllerConfiguration inputDimensionsByResolutionFlavorByPortType];
-[BWSoftISPProcessorControllerConfiguration sfhrSupportEnabled];
-[BWSoftISPProcessorControllerConfiguration lossyCompressionLevel];
-[BWSoftISPProcessorControllerConfiguration setSensorRawPixelFormat:];
-[BWSoftISPProcessorControllerConfiguration setLearnedFusionEnabled:];
-[BWSoftISPProcessorControllerConfiguration adaptiveFusionEnabled];
-[BWSoftISPProcessorControllerConfiguration learnedFusionEnabled];
-[BWSoftISPProcessorControllerConfiguration setQBinProcessingMode:];
-[BWSoftISPProcessorControllerConfiguration setInputDimensions:];
-[BWSoftISPProcessorControllerConfiguration setGdcEnabled:];
-[BWSoftISPProcessorControllerConfiguration setQuadraProcessingEnabled:];
-[BWSoftISPProcessorControllerConfiguration setLowlightSFHRSupportEnabled:];
-[BWSoftISPProcessorControllerConfiguration setLinearRGBForDisparityEnabled:];
-[BWSoftISPProcessorControllerConfiguration standardYUVProcessingEnabled];
-[BWSoftISPProcessorControllerConfiguration auxiliaryTypesForFocusPixelDisparityEnabled];
-[BWSoftISPProcessorControllerConfiguration learnedNRDraftDemosaicEnabled];
-[BWSoftISPProcessorControllerConfiguration outputDimensionsByResolutionFlavor];
-[BWSoftISPProcessorControllerConfiguration cmiResourceEnabled];
-[BWSoftISPProcessorControllerConfiguration setSfhrSupportEnabled:];
```
