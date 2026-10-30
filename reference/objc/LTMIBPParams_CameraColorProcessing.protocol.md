# `LTMIBPParams` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 31 properties, 64 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,N) tuningParameters;
@property (TB,N) doAdaptiveFaceBiasScaler;
@property (Ti,N) optimizationLevel;
@property (TB,N) enableAntiAliasing;
@property (TB,N) calcGlobalHistOnROI;
@property (TB,N) computeHDRCurvesWoFaceBoost;
@property (T@"<LTMRectangles>",&,N) rectangles;
@property (T@"NSDictionary",&,N) validTextureRect;
@property (TB,N) doGlobalCCM;
@property (TB,N) computeHDRCurves;
@property (TB,N) computeCurvesWoFaceBoost;
@property (TB,N) isHighlightCompressionEnabled;
@property (TB,N) isAdaptiveHighlightCompressionEnabled;
@property (TB,N) doHazeEstimation;
@property (TB,N) digitalFlash;
@property (TB,N) isSIFR;
@property (TB,N) clientBracket;
@property (TB,N) preserveExposureBias;
@property (Tf,N) ispDGainThreshold;
@property (Tf,N) adaptiveHCSlope;
@property (Tf,N) minimumAdaptiveHC_SIFR;
@property (TB,N) undoHRGainDownRatio;
@property (T@"NSArray",&,N) hazeEstimation;
@property (Tf,N) evmExpRatio;
@property (T@"NSDictionary",&,N) inMetaData;
@property (T@"<MTLTexture>",&,N) inRGBImageUInt16Tex;
@property (TB,N) isFinalImage;
@property (T@"<MTLTexture>",&,N) inLumaTex;
@property (T@"<MTLTexture>",&,N) inChromaTex;
@property (T@"<MTLTexture>",&,N) inRGBAFloatTex;
@property (T@"NSDictionary",&,N) outMetaData;
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
