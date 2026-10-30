# `LTMProcessor`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMImageBufferProcessor`
- 44 instance variables, 10 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
Q _allocatorForceSize;
B _allocatorWireMemory;
B _allocatorSetupComplete;
{sRefDriverInputs_SOFTISP="HROn"B"hrGainDownRatio"S"exposureTime"I"gainAnal"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gainDigi"I"hardIspDGain"f"softIspDGain"f"expBias"S"realizedExpBias"S"hdrRatio"S"ev0Ratio"S"overflowDGain"I"faceExpRatioFiltered"f"panoExpRatio"S"bLTMSingleFrameMode"B"ltmProcMode"C"bracketingMode"C"bracketingExpRatio"I"gainDigiSensor"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"luxLevel"f"useSpatialCCM"B"channel"C"flashStatus"B"manualWB"B"isHLGMode"B"LTMGridConfig"{sBTRect="x"i"y"i"width"I"height"I}"localHistGridConfig"{sBTRect="x"i"y"i"width"I"height"I}"flashMixPercentage"[512S]"flashProjMixWeighting"f"tileStatsRegion"{sBTRect="x"i"y"i"width"I"height"I}"ccm"{sAWBColorCorrectionMatrix_local="coeff"[9(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})]}"isLEDMainFlashforAWB"B"awbGains"{sBTRGGB16="r"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gr"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gb"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"b"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})}"awbGainsSkinOnly"{sBTRGGB16="r"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gr"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gb"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"b"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})}"awbGainsFlashProj"{sBTRGGB16="r"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gr"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"gb"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})"b"(uBTColorEntry16="v16"S"v88"{uBT88="fractional"C"integer"C})}"fdAWBChistMixFactor"I"awbColorspace"C"faceInfo"{sFaceInfo_SOFTISP="rectArray"[10{sCIspFDRect="x"i"y"i"width"I"height"I}]"primaryFaceIndex"I"numFaces"I}"forceDisableFaceBoost"B"gammaCurve"i"useHighlightCompression"B"useAdaptiveHighlightCompression"B"highlightCompressionGain"f"isSIFRFrame"B"LTMHazeCorrectionOff"B"useBt709"B"useHazeCorrection"B"hazeCorrection""tuningParametersOverride"[6{LTMTuning="histDampingExponentHighlight"f"histDampingExponentMax"f"hmaxHeadroom"f"maxPaddingRange"f"dispRangeActiveRatio"f"sceneBlackRatio"f"sceneBlackRatioDark"f"sceneBgOffset"f"desatStrength"f"minFlareDark"f"shadowSuppressBase"f"shadowSuppressMax"f"shadowSuppressEITAdj"f"minSceneLux"f"histSmoothingMax"f"smoothingStrength"f"dispRangeDarkRatio"f"sceneModelSmoothing"f"nonFaceRatioFloor"f"fstart"f"shadowDesat"f"darkSceneLux"f"darkSceneLuxThreshold""ambientViewingLux"f"ambientViewingChromaticityX"f"ambientViewingChromaticityY"f"sceneBlackMax"f"dispLum"f"dispBlack"f"faceGlobalWeight"f"faceGlobalWeightBG"f"highlightContrastScale"f"highlightContrastScaleCB"f"defaultHistWeightMultiplicator"f"flareConfidence"f}]"useTuningParametersOverride"B"faceBiasScaler"f"faceLTMVer"C"CBVer"C"enableDualLTC"B"useHiResLocalHistogram"B"thumbnailSizeMult"i} _driverInputMetadata;
{sCLRProcHITHStat_SOFTISP="thumbnailWindow"I"thumbnailEnable"[6S]"thumbnailDownsampleX"S"thumbnailDownsampleY"S"thumbnailTotal"I"localHistWindow"I"localHistEnable"S"localHistBinSize"S"localHistBlockSizeX"S"localHistBlockSizeY"S"localHistStrideX"S"localHistStrideY"S"localHistNumHorBlocks"S"localHistNumVerBlocks"S"localHistCountBitShift"C"globalHistEnable"S"globalHistWindow"I"thumbnailStat"^v"thumbnailOffset"I"thumbnailStatSize"I"localHistStat"^v"localHistOffset"I"localHistStatSize"I"globalHistStat"^v"globalHistOffset"I"globalHistStatSize"I"primaryFaceIndex"i"globalFacesHistCount"i"globalFaceHistStat"^v"globalFaceHistStatSize"I"globalFacesHist"[10{faceHistogram="globalFaceHistOffset"I"globalFaceHistWindow"I"enable"B}]"calculatedOnPortraitOrientation"B"gridOriginX"I"gridOriginY"I"localHistogramOriginalTilePixelCount"I"localHistLowThreshold"I"localHistHighThreshold"I} _procHITHStat;
[17680S] thumbnailStat;
[6336S] localHistStat;
[1024I] globalHistStat;
[2560I] globalFaceHistStat;
@"<MTLComputePipelineState>" _ltmDownsampleYCbCrToRGB;
@"<MTLComputePipelineState>" _ltmDownsampleRGBAFloatToRGB;
@"<MTLComputePipelineState>" _ltmRGBToRGBAFloat;
@"<MTLComputePipelineState>" _ltmCompressHighlight;
@"<MTLComputePipelineState>" _ltmDehaze;
@"<MTLComputePipelineState>" _ltmApplyGlobalCCM;
@"<LTMGeometryDataBase>" _geometryData;
@"<LTMExtractMetadataBase>" _metadataExtractor;
@"HazeEstimation" _hazeEstimator;
B _enablePreLTMHazeCorrection;
B _isHazeEstimationEnabled;
B _enableDualLTC;
B _enableCB;
B _enableFATE;
B _enableHiResLocalHistogram;
B _enableHiResThumbnail;
@"AdaptiveGain" _adaptiveGain;
B _enableAdaptiveGain;
i _adaptiveGainVersion;
f _adaptiveGainRange;
f _adaptiveGainMax;
B _enableHardGainForLowLight;
B _enableFaceExposure;
@"NSArray" _faceExposureTargetSkinTone;
B _enableFaceGlobalWeight;
f _faceGlobalWeightOverride;
f _faceGlobalWeightBGOverride;
B _enableMultiFaceFATE;
f _LTMProcessotInputTexToLTMInTexScale;
@"<MTLCommandQueue>" _metalCommandQueue;
@"NSDictionary" cameraInfoByPortType;
@"<LTMIBPParams>" _ltmParams;
@"CMIExternalMemoryResource" _externalMemoryResource;
@"NSDictionary" tuningParameters;
```

## Properties

```
@property (T@"<LTMIBPParams>",R,N,V_ltmParams) ltmParams;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N,V_externalMemoryResource) externalMemoryResource;
@property (T@"NSDictionary",&,N,VtuningParameters) tuningParameters;
@property (T@"NSDictionary",&,N,VcameraInfoByPortType) cameraInfoByPortType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LTMProcessor resetState];
-[LTMProcessor tuningParameters];
-[LTMProcessor finishProcessing];
-[LTMProcessor externalMemoryResource];
-[LTMProcessor purgeResources];
-[LTMProcessor setMetalCommandQueue:];
-[LTMProcessor setCameraInfoByPortType:];
-[LTMProcessor setExternalMemoryResource:];
-[LTMProcessor prewarm];
-[LTMProcessor prepareToProcess:];
-[LTMProcessor getHITHStat];
-[LTMProcessor setup];
-[LTMProcessor metalCommandQueue];
-[LTMProcessor getLTMTuningFromTuningParams:from:];
-[LTMProcessor generateLinearRGBATexture:];
-[LTMProcessor cameraInfoByPortType];
-[LTMProcessor setTuningParameters:];
-[LTMProcessor _readDefaultsMetalAllocator];
-[LTMProcessor initWithCommandQueue:];
-[LTMProcessor process];
-[LTMProcessor createLTMInTextureFromLuma:chroma:];
-[LTMProcessor _readDefaultsDehaze];
-[LTMProcessor createLTMInTextureFromRGBAFloatTex:undoScaleDown:];
-[LTMProcessor ltmParams];
-[LTMProcessor _readDefaultsLTMparam];
-[LTMProcessor _applyGlobalCCM:globalCCM:];
-[LTMProcessor createIntermediateRGBAMetalTexture:width:height:];
-[LTMProcessor setLTMTuningParamsFrom:];
-[LTMProcessor createShaders:];
-[LTMProcessor setLTMComputeTuningParams:from:];
-[LTMProcessor _dehaze:hazeValues:];
-[LTMProcessor createRGBAFloatFromLTMInTexture:];
-[LTMProcessor _isOptimized:];
-[LTMProcessor _prepareHighlightCompressionCurve];
-[LTMProcessor _compressHighlight:];
-[LTMProcessor setDehazeTuningParamsFrom:];
-[LTMProcessor _printDefaultsLTMparam];
```
