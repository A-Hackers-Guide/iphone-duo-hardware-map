# `LTMIBPParams`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMIBPParams`
- 31 instance variables, 35 properties, 65 instance methods, 0 class methods

## Instance variables

```
B _doAdaptiveFaceBiasScaler;
B _enableAntiAliasing;
B _calcGlobalHistOnROI;
B _computeHDRCurves;
B _computeCurvesWoFaceBoost;
B _computeHDRCurvesWoFaceBoost;
B _isHighlightCompressionEnabled;
B _isAdaptiveHighlightCompressionEnabled;
B _doHazeEstimation;
B _doGlobalCCM;
B _undoHRGainDownRatio;
B _isFinalImage;
B _digitalFlash;
B _isSIFR;
B _clientBracket;
B _preserveExposureBias;
i _optimizationLevel;
f _evmExpRatio;
f _ispDGainThreshold;
f _adaptiveHCSlope;
f _minimumAdaptiveHC_SIFR;
@"NSDictionary" _tuningParameters;
@"<LTMRectangles>" _rectangles;
@"NSDictionary" _validTextureRect;
@"NSDictionary" _inMetaData;
@"<MTLTexture>" _inRGBImageUInt16Tex;
@"<MTLTexture>" _inRGBAFloatTex;
@"<MTLTexture>" _inLumaTex;
@"<MTLTexture>" _inChromaTex;
@"NSDictionary" _outMetaData;
@"NSArray" _hazeEstimation;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_tuningParameters) tuningParameters;
@property (TB,N,V_doAdaptiveFaceBiasScaler) doAdaptiveFaceBiasScaler;
@property (Ti,N,V_optimizationLevel) optimizationLevel;
@property (TB,N,V_enableAntiAliasing) enableAntiAliasing;
@property (TB,N,V_calcGlobalHistOnROI) calcGlobalHistOnROI;
@property (TB,N,V_computeHDRCurvesWoFaceBoost) computeHDRCurvesWoFaceBoost;
@property (T@"<LTMRectangles>",&,N,V_rectangles) rectangles;
@property (T@"NSDictionary",&,N,V_validTextureRect) validTextureRect;
@property (TB,N,V_doGlobalCCM) doGlobalCCM;
@property (TB,N,V_computeHDRCurves) computeHDRCurves;
@property (TB,N,V_computeCurvesWoFaceBoost) computeCurvesWoFaceBoost;
@property (TB,N,V_isHighlightCompressionEnabled) isHighlightCompressionEnabled;
@property (TB,N,V_isAdaptiveHighlightCompressionEnabled) isAdaptiveHighlightCompressionEnabled;
@property (TB,N,V_doHazeEstimation) doHazeEstimation;
@property (TB,N,V_digitalFlash) digitalFlash;
@property (TB,N,V_isSIFR) isSIFR;
@property (TB,N,V_clientBracket) clientBracket;
@property (TB,N,V_preserveExposureBias) preserveExposureBias;
@property (Tf,N,V_ispDGainThreshold) ispDGainThreshold;
@property (Tf,N,V_adaptiveHCSlope) adaptiveHCSlope;
@property (Tf,N,V_minimumAdaptiveHC_SIFR) minimumAdaptiveHC_SIFR;
@property (TB,N,V_undoHRGainDownRatio) undoHRGainDownRatio;
@property (T@"NSArray",&,N,V_hazeEstimation) hazeEstimation;
@property (Tf,N,V_evmExpRatio) evmExpRatio;
@property (T@"NSDictionary",&,N,V_inMetaData) inMetaData;
@property (T@"<MTLTexture>",&,N,V_inRGBImageUInt16Tex) inRGBImageUInt16Tex;
@property (TB,N,V_isFinalImage) isFinalImage;
@property (T@"<MTLTexture>",&,N,V_inLumaTex) inLumaTex;
@property (T@"<MTLTexture>",&,N,V_inChromaTex) inChromaTex;
@property (T@"<MTLTexture>",&,N,V_inRGBAFloatTex) inRGBAFloatTex;
@property (T@"NSDictionary",&,N,V_outMetaData) outMetaData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LTMIBPParams tuningParameters];
-[LTMIBPParams setInMetaData:];
-[LTMIBPParams inMetaData];
-[LTMIBPParams setTuningParameters:];
-[LTMIBPParams setIsSIFR:];
-[LTMIBPParams setInRGBImageUInt16Tex:];
-[LTMIBPParams minimumAdaptiveHC_SIFR];
-[LTMIBPParams computeCurvesWoFaceBoost];
-[LTMIBPParams isHighlightCompressionEnabled];
-[LTMIBPParams doHazeEstimation];
-[LTMIBPParams setDigitalFlash:];
-[LTMIBPParams setClientBracket:];
-[LTMIBPParams validTextureRect];
-[LTMIBPParams setIspDGainThreshold:];
-[LTMIBPParams setDoGlobalCCM:];
-[LTMIBPParams setIsHighlightCompressionEnabled:];
-[LTMIBPParams init];
-[LTMIBPParams isFinalImage];
-[LTMIBPParams undoHRGainDownRatio];
-[LTMIBPParams clientBracket];
-[LTMIBPParams calcGlobalHistOnROI];
-[LTMIBPParams setInRGBAFloatTex:];
-[LTMIBPParams setInLumaTex:];
-[LTMIBPParams preserveExposureBias];
-[LTMIBPParams adaptiveHCSlope];
-[LTMIBPParams reset];
-[LTMIBPParams enableAntiAliasing];
-[LTMIBPParams setDoAdaptiveFaceBiasScaler:];
-[LTMIBPParams setIsAdaptiveHighlightCompressionEnabled:];
-[LTMIBPParams doGlobalCCM];
-[LTMIBPParams setPreserveExposureBias:];
-[LTMIBPParams setUndoHRGainDownRatio:];
-[LTMIBPParams setOptimizationLevel:];
-[LTMIBPParams setComputeHDRCurves:];
-[LTMIBPParams optimizationLevel];
-[LTMIBPParams isAdaptiveHighlightCompressionEnabled];
-[LTMIBPParams setComputeCurvesWoFaceBoost:];
-[LTMIBPParams setEvmExpRatio:];
-[LTMIBPParams setRectangles:];
-[LTMIBPParams computeHDRCurvesWoFaceBoost];
-[LTMIBPParams setDoHazeEstimation:];
-[LTMIBPParams doAdaptiveFaceBiasScaler];
-[LTMIBPParams setInChromaTex:];
-[LTMIBPParams computeHDRCurves];
-[LTMIBPParams isSIFR];
-[LTMIBPParams ispDGainThreshold];
-[LTMIBPParams hazeEstimation];
-[LTMIBPParams setComputeHDRCurvesWoFaceBoost:];
-[LTMIBPParams setCalcGlobalHistOnROI:];
-[LTMIBPParams setMinimumAdaptiveHC_SIFR:];
-[LTMIBPParams setHazeEstimation:];
-[LTMIBPParams inChromaTex];
-[LTMIBPParams evmExpRatio];
-[LTMIBPParams setValidTextureRect:];
-[LTMIBPParams outMetaData];
-[LTMIBPParams setIsFinalImage:];
-[LTMIBPParams inRGBImageUInt16Tex];
-[LTMIBPParams setOutMetaData:];
-[LTMIBPParams inLumaTex];
-[LTMIBPParams rectangles];
-[LTMIBPParams setEnableAntiAliasing:];
-[LTMIBPParams inRGBAFloatTex];
-[LTMIBPParams digitalFlash];
-[LTMIBPParams releaseTextures];
-[LTMIBPParams setAdaptiveHCSlope:];
```
