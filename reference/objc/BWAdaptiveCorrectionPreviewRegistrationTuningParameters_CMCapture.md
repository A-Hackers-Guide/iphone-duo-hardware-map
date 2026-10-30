# `BWAdaptiveCorrectionPreviewRegistrationTuningParameters`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _keypointsMinSelectionScore;
I _configuredNumKeypoints;
d _epipolarWeightFalloffDistance;
d _macroDepthWeightFalloffDistance;
{BWAdaptiveCorrectionPreviewRegistrationRegToolBoxConfig="numPyrLevels"I"imageWidth"I"imageHeight"I"keypointGridWidth"I"keypointGridHeight"I"keypointsTemplateRadius"I"keypointsSearchRadius"I"keypointsMinNccScore"f} _regToolBoxConfig;
[3{AdaptiveCorrectionConfig="epErrorLimitWidePix_FirstPass"d"epErrorLimitWidePix_SecondPass"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"intermediateMacroDistMM"d"extremeMacroDistMM"d"minPointsForAdjustment"i"errorVal_GreaterThanInf"d"errorVal_LessThanExtremeMacro"d"errorVal_BetweenIntermediate_ExtremeMacro"d"runAnalyticalPreconditioning"B"spgEpsilon"d"keypointOutliersPercentile"f"epErrorLimitTelePix_ParallelCorrection"f"temporalFilteringStrength"f"temporalFilteringStrengthParallel"f"temporalInitializationFactor"f"scaleTuningWithDigitalZoomByFactor"f"overrideConfigPass1"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPass2"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPassDist"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}}] _adaptiveCorrectionConfigs;
r^{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}} _adaptiveCorrectionConfigsPtr;
```

## Properties

```
@property (Tf,R,N,V_keypointsMinSelectionScore) keypointsMinSelectionScore;
@property (TI,R,N,V_configuredNumKeypoints) configuredNumKeypoints;
@property (Td,R,N,V_epipolarWeightFalloffDistance) epipolarWeightFalloffDistance;
@property (Td,R,N,V_macroDepthWeightFalloffDistance) macroDepthWeightFalloffDistance;
@property (T{BWAdaptiveCorrectionPreviewRegistrationRegToolBoxConfig=IIIIIIIf},R,N,V_regToolBoxConfig) regToolBoxConfig;
@property (Tr^{AdaptiveCorrectionConfig=ddddddddddidddBdffffff{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}{ADCPassConfig=BBdddddddddddidii}},R,N,V_adaptiveCorrectionConfigsPtr) adaptiveCorrectionConfigsPtr;
```

## Class methods

```
+[BWAdaptiveCorrectionPreviewRegistrationTuningParameters initialize];
```

## Instance methods

```
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters init];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters macroDepthWeightFalloffDistance];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters adaptiveCorrectionConfigsPtr];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters configuredNumKeypoints];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters epipolarWeightFalloffDistance];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters initWithTuningDictionary:];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters keypointsMinSelectionScore];
-[BWAdaptiveCorrectionPreviewRegistrationTuningParameters regToolBoxConfig];
```
