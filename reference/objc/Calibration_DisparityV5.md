# `Calibration`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 14 properties, 41 instance methods, 0 class methods

## Instance variables

```
^{AdaptiveCorrection=} _adc;
{CalModel="focalLengthPix"[2d]"opticalCenterX"[2d]"opticalCenterY"[2d]"extrinRotRefefenceToAuxiliary"[12d]"canonicalDisparityScale"d"calibrationDimensions"[2d]"pixelSize_um"[2d]} _initialCalibration;
[2{?="width"i"height"i}] _pixelBufferDimensions;
[2] _pixelBufferScalingFactor;
[2@"NSDictionary"] _metadata;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceFinalCropRect;
f _referenceCalibrationScalingFactor;
[2{DistortionModel="pixelSizeMM"d"focalLengthPix"d"opticalCenterX"d"opticalCenterY"d"polyBase"[8d]"polyDynamic"[8d]}] _distModels;
[2{DistortionModel="pixelSizeMM"d"focalLengthPix"d"opticalCenterX"d"opticalCenterY"d"polyBase"[8d]"polyDynamic"[8d]}] _undistModels;
_orientationVector;
I _keypointsCount;
[2^d] _adaptiveCorrectionKeypointsDistorted;
@"NSDictionary" _staticParametersByPortType;
{AdaptiveCorrectionConfig="epErrorLimitWidePix_FirstPass"d"epErrorLimitWidePix_SecondPass"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"intermediateMacroDistMM"d"extremeMacroDistMM"d"minPointsForAdjustment"i"errorVal_GreaterThanInf"d"errorVal_LessThanExtremeMacro"d"errorVal_BetweenIntermediate_ExtremeMacro"d"runAnalyticalPreconditioning"B"spgEpsilon"d"keypointOutliersPercentile"f"epErrorLimitTelePix_ParallelCorrection"f"temporalFilteringStrength"f"temporalFilteringStrengthParallel"f"temporalInitializationFactor"f"scaleTuningWithDigitalZoomByFactor"f"overrideConfigPass1"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPass2"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}"overrideConfigPassDist"{ADCPassConfig="isValid"B"isPassEnabled"B"epErrorLimitWidePix"d"rangePFL_T"d"rangePFL_W"d"rangeOCxT"d"rangeOCxW"d"rangeOCyT"d"rangeOCyW"d"rangePFL_T_dist"d"rangePFL_W_dist"d"rangeOCxT_dist"d"rangeOCxW_dist"d"minPointsForAdjustment"i"spgEpsilon"d"spgMaxIterations"i"spgMaxAlphaIterations"i}} _adaptiveCorrectionConfig;
[2f] _focalLength;
[2{CGPoint="x"d"y"d}] _opticalCenter;
[2{CGSize="width"d"height"d}] _rawSensorSize;
[2f] _ddf;
[2{CGPoint="x"d"y"d}] _distortionOpticalCenter;
[2@"NSString"] _portTypeName;
_limitDistances_mm;
f _rectificationAngleStep;
f _rectificationFocalLengthFactor;
B _distortionCorrectionEnabled;
{?="xyPointsTeleTransposed"^d"xyPointsWideTransposed"^d} _transposedKeypoints;
B _temporalCorrectionEnabled;
B _pixelBufferScalingEnabled;
f _aspectRatioErrorHardThreshold;
f _nearLimitDisparity;
f _midLimitDisparity;
{?="columns"[3]} _auxiliaryPaddingHInv;
{?="columns"[3]} _rectReferenceToReference;
{?="columns"[3]} _rectReferenceToAuxiliary;
{?="columns"[3]} _referenceToRectReference;
{CalModel="focalLengthPix"[2d]"opticalCenterX"[2d]"opticalCenterY"[2d]"extrinRotRefefenceToAuxiliary"[12d]"canonicalDisparityScale"d"calibrationDimensions"[2d]"pixelSize_um"[2d]} _correctedCalibration;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceFinalCropRect) referenceFinalCropRect;
@property (Tf,R,N) referenceMagnification;
@property (T{CalModel=[2d][2d][2d][12d]d[2d][2d]},R,N,V_initialCalibration) initialCalibration;
@property (T{CalModel=[2d][2d][2d][12d]d[2d][2d]},R,N,V_correctedCalibration) correctedCalibration;
@property (T,N,V_orientationVector) orientationVector;
@property (TB,N,V_distortionCorrectionEnabled) distortionCorrectionEnabled;
@property (TB,N,V_temporalCorrectionEnabled) temporalCorrectionEnabled;
@property (TB,N,V_pixelBufferScalingEnabled) pixelBufferScalingEnabled;
@property (Tf,R,N,V_nearLimitDisparity) nearLimitDisparity;
@property (Tf,R,N,V_midLimitDisparity) midLimitDisparity;
@property (T{?=[3]},R,N,V_auxiliaryPaddingHInv) auxiliaryPaddingHInv;
@property (T{?=[3]},R,N,V_rectReferenceToReference) rectReferenceToReference;
@property (T{?=[3]},R,N,V_rectReferenceToAuxiliary) rectReferenceToAuxiliary;
@property (T{?=[3]},R,N,V_referenceToRectReference) referenceToRectReference;
```

## Instance methods

```
-[Calibration releaseResources];
-[Calibration init];
-[Calibration dealloc];
-[Calibration undistModelFor:];
-[Calibration allocateResourcesForMaxNumPoints:];
-[Calibration applyCurrentTemporalState];
-[Calibration auxiliaryPaddingHInv];
-[Calibration computeAuxiliaryImageShiftForKeypoints:];
-[Calibration computeCalibration];
-[Calibration computeInitialCalibration];
-[Calibration computeStereoRectificationHomographies:alignedToAngle:];
-[Calibration correctedCalibration];
-[Calibration distModelFor:];
-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:];
-[Calibration orientationVector];
-[Calibration rectReferenceToAuxiliary];
-[Calibration rectReferenceToReference];
-[Calibration referenceMagnification];
-[Calibration referenceToRectReference];
-[Calibration setKeypointsForReference:auxiliary:keypointCount:];
-[Calibration setPixelBufferScalingEnabled:];
-[Calibration setReferenceBufferDimensions:auxillaryBufferDimensions:normalizedReferenceFinalCropRect:];
-[Calibration setTemporalCorrectionEnabled:];
-[Calibration setDistortionCorrectionEnabled:];
-[Calibration _allocateResourcesForMaxNumOfTransposedPoints:];
-[Calibration _checkADCStatus:];
-[Calibration _computeAdcDistortionModels];
-[Calibration _computeCalibrationWithoutDistortion];
-[Calibration _computeCanonicalDisparityScaleFactor];
-[Calibration _computeCenteredRectificationHomographies];
-[Calibration _computePaddedAuxiliaryRectificationHomography];
-[Calibration _releaseResourcesForTransformedPoints];
-[Calibration computeStereoRectificationHomographies:];
-[Calibration distortionCorrectionEnabled];
-[Calibration initialCalibration];
-[Calibration midLimitDisparity];
-[Calibration nearLimitDisparity];
-[Calibration pixelBufferScalingEnabled];
-[Calibration referenceFinalCropRect];
-[Calibration setOrientationVector:];
-[Calibration temporalCorrectionEnabled];
```
