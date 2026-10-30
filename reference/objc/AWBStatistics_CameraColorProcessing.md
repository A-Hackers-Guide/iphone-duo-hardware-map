# `AWBStatistics`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLComputePipelineState>" _computeAWBStatsBayerFastPipelineState;
@"<MTLComputePipelineState>" _computeAWBStatsQuadraFastPipelineState;
@"<MTLComputePipelineState>" _resetMtlBufferPipelineState;
@"<MTLComputePipelineState>" _normTileStatsPipelineState;
@"<MTLComputePipelineState>" _normWindowStatsPipelineState;
@"<MTLComputePipelineState>" _resizeANSTPipelineState;
@"<MTLComputePipelineState>" _fitWbTmRGBToANSTInputPipelineState;
@"ANSTInferenceWrapper" _anstInferenceWrapper;
{?="layout"i"firstPix"C"greenAverage"C"downsizeRatio"C"ispDGain"f"ccm"{?="coeff"{?="columns"[3]}"min""max""offsetIn""offsetOut"}"gam"{?="lut"[257S]"gammaOffsetIn""gammaOffsetOut""offsetIn"S"offsetOut"S"po2CfgMode"i"po2CfgExpand"B"po2CfgDenseLeft"{?="flipOp"B"offOp"B"symmetric"B"maxCode"i"pivot1"i"lutLen"S"startExp"S"spacingStart"S"numIntervalArray"[16S]"log2NumIntervalArrayAdj"[16S]}}"csc"{?="lin3x3"{?="coeff"{?="columns"[3]}"min""max""offsetIn""offsetOut"}"scale"}"csc2"{?="lin3x3"{?="coeff"{?="columns"[3]}"min""max""offsetIn""offsetOut"}"scale"}"colorHist"{?="enable"B"countClipEn"B"startX"S"startY"S"endX"S"endY"S"offsetC1"f"offsetC2"f"scaleC1"f"scaleC2"f"count"[16S]"yThd"[16S]"debiasGain""debiasMax""debiasMin""debiasOffset"}"pixFilt"[2{?="condSel"C"statSel"C"countClipEn"B"Ymin"i"Ymax"i"C1min"i"C1max"i"C2min"i"C2max"i"distMax"I"offset"i"C1delta"i"C2delta"i}]"debiasCfg"[2{?="offset""gain"}]"fastLSCCfg"{AWBFastLSCConfig="enabled"B"gridWidth"S"gridHeight"S"gridMaxGain"f"modulationWeight"f"gridIntervalReciprocal""yOffset"(?="vec"""{?="gr"S"r"S"b"S"gb"S})"xCropOffset"S"yCropOffset"S}"windows"[2{?="enable"B"bitDepth"B"pfSel"[2i]"startX"i"startY"i"endX"i"endY"i}]"tiles"{?="bitDepth"B"startX"i"startY"i"endX"i"endY"i"horzInt"S"vertInt"S}"linearRGBToANSTInputCfg"{AWBLinearRGBToANSTInputConfig="awbGains""ccm"{?="columns"[3]}"gtcRatio"[257S]"gtcFinal"[257S]"ltmHardGain"f}"regionOfInterestRect"{?="startX"S"startY"S"endX"S"endY"S}"skipDemosaic"B"digitalFlashBehaviorMode"i} _awbStatCfg;
@"NSNumber" _digitalFlash;
@"NSNumber" _skipDemosaic;
@"NSNumber" _lscMaxGain;
@"NSNumber" _lscModulationWeight;
@"NSNumber" _faceAssistedBehaviorMode;
@"NSNumber" _downsizeFactor;
```

## Properties

```
@property (T@"NSNumber",&,N,V_digitalFlash) digitalFlash;
@property (T@"NSNumber",&,N,V_skipDemosaic) skipDemosaic;
@property (T@"NSNumber",&,N,V_lscMaxGain) lscMaxGain;
@property (T@"NSNumber",&,N,V_lscModulationWeight) lscModulationWeight;
@property (T@"NSNumber",&,N,V_faceAssistedBehaviorMode) faceAssistedBehaviorMode;
@property (T@"NSNumber",&,N,V_downsizeFactor) downsizeFactor;
```

## Class methods

```
+[AWBStatistics getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:];
```

## Instance methods

```
-[AWBStatistics faceAssistedBehaviorMode];
-[AWBStatistics setDigitalFlash:];
-[AWBStatistics setFaceAssistedBehaviorMode:];
-[AWBStatistics setLscModulationWeight:];
-[AWBStatistics setSkipDemosaic:];
-[AWBStatistics configWithModuleConfig:metadata:cameraInfo:awbParams:];
-[AWBStatistics skipDemosaic];
-[AWBStatistics _createShaders];
-[AWBStatistics setLscMaxGain:];
-[AWBStatistics downsizeFactor];
-[AWBStatistics initWithMetalContext:];
-[AWBStatistics setDownsizeFactor:];
-[AWBStatistics lscMaxGain];
-[AWBStatistics digitalFlash];
-[AWBStatistics lscModulationWeight];
-[AWBStatistics _adjustConfigToValidRectInBufferCoords:validRectInSensorReadoutCoords:regionOfInterestRectInBufferCoords:];
-[AWBStatistics _loadANSTNetwork];
-[AWBStatistics _purgeANSTNetwork];
-[AWBStatistics configWindowsV2:metadata:tilesConfig:validRect:regionOfInterestRect:];
-[AWBStatistics process:awbStatsBuffer:awbTileStatsConfig:anstSkinMaskData:skyMaskData:downsizeFactor:];
```
