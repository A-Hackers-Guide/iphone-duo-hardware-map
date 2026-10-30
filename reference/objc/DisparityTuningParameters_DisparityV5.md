# `DisparityTuningParameters`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 20 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _alignAuxiliaryImageForKeypoints;
B _useLKTKeypointDetection;
f _maxAnalogGain;
f _nearLimitDistanceMM;
f _midLimitDistanceMM;
f _keypointsDetectionThreshold;
f _defaultFocalLengthTeleMicrometers;
f _defaultFocalLengthTeleMaxDeviationMicrometers;
f _defaultFocalLengthWideMicrometers;
f _defaultFocalLengthWideMaxDeviationMicrometers;
f _minDisparityClampingPercentile;
f _maxDisparityClampingPercentile;
i _stereoDisparityEstimatorLevels;
f _bidirectionalError;
f _confidenceRadialWeight;
f _confidenceMinimum;
i _blockSize;
i _lastScale;
i _nwarps;
{AdaptiveCorrectionConfig="epErrorLimitWidePix_FirstPass"d"epErrorLimitWidePix_SecondPass"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"intermediateMacroDistMM"d"extremeMacroDistMM"d"minPointsForAdjustment"i"errorVal_GreaterThanInf"d"errorVal_LessThanExtremeMacro"d"errorVal_BetweenIntermediate_ExtremeMacro"d"runAnalyticalPreconditioning"B"spgEpsilon"d"keypointOutliersPercentile"f"epErrorLimitTelePix_ParallelCorrection"f"temporalFilteringStrength"f"temporalFilteringStrengthParallel"f"temporalInitializationFactor"f"scaleTuningWithDigitalZoomByFactor"f"overrideConfigPass1"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPass2"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPassDist"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}} _adaptiveCorrectionConfig;
```

## Properties

```
@property (Tf,R,N,V_maxAnalogGain) maxAnalogGain;
@property (Tf,R,N,V_nearLimitDistanceMM) nearLimitDistanceMM;
@property (Tf,R,N,V_midLimitDistanceMM) midLimitDistanceMM;
@property (Tf,R,N,V_keypointsDetectionThreshold) keypointsDetectionThreshold;
@property (Tf,R,N,V_defaultFocalLengthTeleMicrometers) defaultFocalLengthTeleMicrometers;
@property (Tf,R,N,V_defaultFocalLengthTeleMaxDeviationMicrometers) defaultFocalLengthTeleMaxDeviationMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMicrometers) defaultFocalLengthWideMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMaxDeviationMicrometers) defaultFocalLengthWideMaxDeviationMicrometers;
@property (TB,R,N,V_alignAuxiliaryImageForKeypoints) alignAuxiliaryImageForKeypoints;
@property (T{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}},R,N,V_adaptiveCorrectionConfig) adaptiveCorrectionConfig;
@property (Tf,R,N,V_minDisparityClampingPercentile) minDisparityClampingPercentile;
@property (Tf,R,N,V_maxDisparityClampingPercentile) maxDisparityClampingPercentile;
@property (Ti,R,N,V_stereoDisparityEstimatorLevels) stereoDisparityEstimatorLevels;
@property (TB,R,N,V_useLKTKeypointDetection) useLKTKeypointDetection;
@property (Tf,R,N,V_bidirectionalError) bidirectionalError;
@property (Tf,R,N,V_confidenceRadialWeight) confidenceRadialWeight;
@property (Tf,R,N,V_confidenceMinimum) confidenceMinimum;
@property (Ti,R,N,V_blockSize) blockSize;
@property (Ti,R,N,V_lastScale) lastScale;
@property (Ti,R,N,V_nwarps) nwarps;
```

## Instance methods

```
-[DisparityTuningParameters setDefaultMaxAnalogGain];
-[DisparityTuningParameters minDisparityClampingPercentile];
-[DisparityTuningParameters lastScale];
-[DisparityTuningParameters readAdaptiveCorrectionConfig:isUpdating:];
-[DisparityTuningParameters confidenceRadialWeight];
-[DisparityTuningParameters setDefaultLKTParameters];
-[DisparityTuningParameters blockSize];
-[DisparityTuningParameters init];
-[DisparityTuningParameters updateTuningParametersWith:];
-[DisparityTuningParameters stereoDisparityEstimatorLevels];
-[DisparityTuningParameters initWithTuningDictionary:cameraInfoByPortType:];
-[DisparityTuningParameters setDefaultAdaptiveCorrectionParameters];
-[DisparityTuningParameters bidirectionalError];
-[DisparityTuningParameters nearLimitDistanceMM];
-[DisparityTuningParameters getAdaptiveCorrectionConfigPtr];
-[DisparityTuningParameters readDisparityClampingConfig:isUpdating:];
-[DisparityTuningParameters defaultFocalLengthWideMicrometers];
-[DisparityTuningParameters defaultFocalLengthTeleMicrometers];
-[DisparityTuningParameters confidenceMinimum];
-[DisparityTuningParameters alignAuxiliaryImageForKeypoints];
-[DisparityTuningParameters readMaxAnalogGain:isUpdating:];
-[DisparityTuningParameters maxDisparityClampingPercentile];
-[DisparityTuningParameters setDefaultCalibrationParameters];
-[DisparityTuningParameters defaultFocalLengthWideMaxDeviationMicrometers];
-[DisparityTuningParameters readLKTConfig:isUpdating:];
-[DisparityTuningParameters nwarps];
-[DisparityTuningParameters readCalibrationConfig:isUpdating:];
-[DisparityTuningParameters midLimitDistanceMM];
-[DisparityTuningParameters setDefaultDisparityClampingParameters];
-[DisparityTuningParameters keypointsDetectionThreshold];
-[DisparityTuningParameters useLKTKeypointDetection];
-[DisparityTuningParameters setDefaultRPDParameters];
-[DisparityTuningParameters adaptiveCorrectionConfig];
-[DisparityTuningParameters maxAnalogGain];
-[DisparityTuningParameters defaultFocalLengthTeleMaxDeviationMicrometers];
```
