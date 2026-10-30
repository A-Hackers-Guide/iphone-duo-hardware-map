# `LTMCurvesComputeV1`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMCurvesComputeBase`
- 14 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"LTMComputeRefV1" _computeLTM;
@"LTMDriverRefV1" _driverLTM;
@"LTMStats" _ltmStats;
B _isDigitalFlash;
B _computeHDRCurves;
B _computeCurvesWoFaceBoost;
B _computeHDRCurvesWoFaceBoost;
@"<LTMGeometryDataBase>" _geometryData;
^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffffffffff}]BfCCBBi} _driverInputMetadata;
^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIii^vI[10{faceHistogram=IIB}]BIIIII} _procHITHStat;
{sLtmComputeInput="localHist"[3072f]"averageLocalHist"[64f]"globalHist"[1024f]"tMaxArray"[48f]"nLumArray"[48f]"thumbnailHist"[64f]"thumbnailHistEV0"[64f]"thumbnailLumaHist"[65f]"faceWeightForTone"[48f]"sceneLux"f"bin0Ratio"f"pixelCountRatio"f"exposureRatio"f"exposureBias"f"preBiasExposureRatio"f"faceExposureRatio"f"darkExposureRatio"f"luminanceRatio"f"flareScale"f"rGainRatio"f"bGainRatio"f"gamutSizeIndex"S"ccm"[9f]"ccmWeights"[192f]"ccmMixFactor"f"eit"f"darkEit"f"LTMHazeCorrectionOff"B"useBt709"B"ltcGridScaleLogLumaThumb"[48f]"faceBiasScaler"f} _computeInputs;
{sLtmComputeMeta_SOFTISP="ltmComputeMeta"{sLtmComputeMeta="useLinearLTCs"B"useSpatialCCM"B"useGlobalCCM"B"useDigitalFlash"B"useFlash"B"gammaCurve"i"updateMixLUT"B"levelSmoothNumPasses"i"levelSmoothCenterWeight"f}"channel"C"tuningParametersOverride"[6{LTMTuning="histDampingExponentHighlight"f"histDampingExponentMax"f"hmaxHeadroom"f"maxPaddingRange"f"dispRangeActiveRatio"f"sceneBlackRatio"f"sceneBlackRatioDark"f"sceneBgOffset"f"desatStrength"f"minFlareDark"f"shadowSuppressBase"f"shadowSuppressMax"f"shadowSuppressEITAdj"f"minSceneLux"f"histSmoothingMax"f"smoothingStrength"f"dispRangeDarkRatio"f"sceneModelSmoothing"f"nonFaceRatioFloor"f"fstart"f"shadowDesat"f"darkSceneLux"f"darkSceneLuxThreshold""ambientViewingLux"f"ambientViewingChromaticityX"f"ambientViewingChromaticityY"f"sceneBlackMax"f"dispLum"f"dispBlack"f"faceGlobalWeight"f"faceGlobalWeightBG"f"highlightContrastScale"f"highlightContrastScaleCB"f"defaultHistWeightMultiplicator"f"flareConfidence"f}]"useTuningParametersOverride"B} _computeInputsMetadata;
{sLtmComputeOutput="LTC"[3120f]"averageLTC"[65f]"globalLUT"[257f]"rgbToneCurve"[257f]"spatialCCM"[5184f]"WMixLUT"[257f]"midLuminance"f"eit"Q"encodedExpRatio"f"bWMixLUTUpdated"b1"bCCMUpdated"b1"bLTMUpdated"b1"bGlobalLUTUpdated"b1"bRgbToneCurveUpdated"b1"rsvd"b3} _computeOutput;
B _optimized;
```

## Instance methods

```
-[LTMCurvesComputeV1 compute];
-[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:];
```
