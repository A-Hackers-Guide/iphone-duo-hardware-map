# `ADCTuningParameters`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
f _keypointsDetectionThreshold;
f _defaultFocalLengthTeleMicrometers;
f _defaultFocalLengthTeleMaxDeviationMicrometers;
f _defaultFocalLengthWideMicrometers;
f _defaultFocalLengthWideMaxDeviationMicrometers;
{AdaptiveCorrectionConfig="epErrorLimitWidePix_FirstPass"d"epErrorLimitWidePix_SecondPass"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"intermediateMacroDistMM"d"extremeMacroDistMM"d"minPointsForAdjustment"i"errorVal_GreaterThanInf"d"errorVal_LessThanExtremeMacro"d"errorVal_BetweenIntermediate_ExtremeMacro"d"runAnalyticalPreconditioning"B"spgEpsilon"d"keypointOutliersPercentile"f"epErrorLimitTelePix_ParallelCorrection"f"temporalFilteringStrength"f"temporalFilteringStrengthParallel"f"temporalInitializationFactor"f"scaleTuningWithDigitalZoomByFactor"f"overrideConfigPass1"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPass2"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPassDist"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}} _adaptiveCorrectionConfig;
```

## Properties

```
@property (Tf,R,N,V_keypointsDetectionThreshold) keypointsDetectionThreshold;
@property (Tf,R,N,V_defaultFocalLengthTeleMicrometers) defaultFocalLengthTeleMicrometers;
@property (Tf,R,N,V_defaultFocalLengthTeleMaxDeviationMicrometers) defaultFocalLengthTeleMaxDeviationMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMicrometers) defaultFocalLengthWideMicrometers;
@property (Tf,R,N,V_defaultFocalLengthWideMaxDeviationMicrometers) defaultFocalLengthWideMaxDeviationMicrometers;
@property (T{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}},R,N,V_adaptiveCorrectionConfig) adaptiveCorrectionConfig;
```

## Instance methods

```
-[ADCTuningParameters initWithDictionary:];
-[ADCTuningParameters init];
-[ADCTuningParameters getAdaptiveCorrectionConfigPtr];
-[ADCTuningParameters defaultFocalLengthWideMicrometers];
-[ADCTuningParameters defaultFocalLengthTeleMicrometers];
-[ADCTuningParameters defaultFocalLengthWideMaxDeviationMicrometers];
-[ADCTuningParameters keypointsDetectionThreshold];
-[ADCTuningParameters adaptiveCorrectionConfig];
-[ADCTuningParameters defaultFocalLengthTeleMaxDeviationMicrometers];
-[ADCTuningParameters checkAndCorrectFocalLengthWide:];
-[ADCTuningParameters checkAndCorrectFocalLengthTele:];
-[ADCTuningParameters readAdaptiveCorrectionConfig:];
```
