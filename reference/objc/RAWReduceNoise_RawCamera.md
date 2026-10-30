# `RAWReduceNoise`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 26 instance variables, 0 properties, 76 instance methods, 3 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSNumber" inputLNRAmount;
@"NSNumber" inputCNRAmount;
@"NSNumber" inputSharpenAmount;
@"NSNumber" inputSharpenThreshold;
@"NSNumber" inputContrastAmount;
@"NSNumber" inputDetailAmount;
@"NSNumber" inputMoireRadius;
@"NSNumber" inputMoireAmount;
@"NSNumber" inputOpponentColorEnabled;
@"CIVector" inputNeutralFactors;
@"NSNumber" inputRepresentativeNoise;
@"NSNumber" inputScaleFactor;
@"NSNumber" inputBoostMethod;
@"CIVector" inputLumFactors;
@"NSNumber" inputBaselineExposure;
@"NSNumber" inputISO;
@"NSNumber" inputSensorPattern;
@"NSDictionary" inputISODictionary;
@"NSDictionary" inputTrimParameters;
@"NSArray" inputLowCurvatureThreshold;
@"NSDictionary" inputDespeckleParameters;
@"NSNumber" inputHighFrequencyFactor;
@"NSNumber" inputShowHF;
@"NSNumber" inputVersion;
@ inputColorSpace;
```

## Class methods

```
+[RAWReduceNoise customAttributes];
+[RAWReduceNoise smartNoiseAdjustmentsForValue:andStatistics:];
+[RAWReduceNoise smartNoiseStatistics:];
```

## Instance methods

```
-[RAWReduceNoise customAttributes];
-[RAWReduceNoise outputImage];
-[RAWReduceNoise reduce:];
-[RAWReduceNoise fineGrainNoise:];
-[RAWReduceNoise V8OutputImage];
-[RAWReduceNoise YAndRGBGather:cnrRGB:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise fineGrainNoise2:tinyBlurFactor:];
-[RAWReduceNoise YAndRGBGatherOpponentColor:cnrRGB:originalY:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise addNoise:noise:amount:];
-[RAWReduceNoise adjustedRNAmount];
-[RAWReduceNoise blurGradient:lothresh:factor:];
-[RAWReduceNoise blurGradientPlusCurvature:lothresh:factor:cthresh:cfactor:];
-[RAWReduceNoise compositeThroughGradientMask:fullSize:fullSizeMask:];
-[RAWReduceNoise computeLowThreshold:andFactor:withThreshold:andSoftness:];
-[RAWReduceNoise computeScaleA:B:withSmoothingAmount:];
-[RAWReduceNoise directionsToCurvature:threshold:];
-[RAWReduceNoise expandAndAddDetailsThroughGradientMask2:halfSize:fullSizeDetails:soften:sharpen:];
-[RAWReduceNoise expandAndAddDetailsThroughGradientMask3:fullSize:fullSizeDetails:fullSizeMask:amount:sharpen:interpolant:];
-[RAWReduceNoise expandAndAddDetailsThroughGradientMask:fullSize:fullSizeDetails:fullSizeMask:amount:contrastOverdrive:interpolant:];
-[RAWReduceNoise expandAndAddDetailsWithOverdrive:fullSize:contrast:];
-[RAWReduceNoise expandAndMakeDetails:halfSize:];
-[RAWReduceNoise expandAndSharpenDetailsThroughGradientMaskGather:halfSizeY:cnrRGB:sharpen:soften:floor:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise expandAndSharpenDetailsThroughGradientMaskGatherOpponentColor:halfSizeY:cnrRGB:originalY:sharpen:soften:floor:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise expandAndSharpenThroughGradientMask:fullSizeY:sharpen:];
-[RAWReduceNoise expandAndSharpenThroughGradientMaskGather:halfSizeY:cnrRGB:sharpen:floor:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise expandAndSharpenThroughGradientMaskGatherOpponentColor:halfSizeY:cnrRGB:originalY:sharpen:floor:sushiFactors:crop:lumFactors:];
-[RAWReduceNoise expandHalfSizeRGB:];
-[RAWReduceNoise extractHalfSizeRGB:neutralFactors:];
-[RAWReduceNoise extractHalfSizeRGBHF:neutralFactors:threshold:];
-[RAWReduceNoise extractY:neutralFactors:];
-[RAWReduceNoise extractYOpponentColor:neutralFactors:luminanceFactors:noiseVector:];
-[RAWReduceNoise gaborFiltersToLuminanceAndVectorField:thresh:];
-[RAWReduceNoise gaborFiltersToSmoothedLuminanceAndGradient:smoothAmt:tinyBlurFactor:];
-[RAWReduceNoise gaborFiltersToVectorField:];
-[RAWReduceNoise highFrequencyIntoAlpha:threshold:neutralFactors:];
-[RAWReduceNoise image:croppedTo:];
-[RAWReduceNoise isBayerGreenAlignedforImage:andPattern:];
-[RAWReduceNoise kernelWithName:inArray:];
-[RAWReduceNoise mergeHalfSizeCurvature:intoFullSizeCurvature:];
-[RAWReduceNoise multiply:byNeutralFactors:];
-[RAWReduceNoise outputBoost:];
-[RAWReduceNoise outputCNR:E0:E1:];
-[RAWReduceNoise outputCNR:extent:returningDebugProduct:];
-[RAWReduceNoise outputUnboost:];
-[RAWReduceNoise perceptualToLinear:];
-[RAWReduceNoise powerBlur:threshold:scale:];
-[RAWReduceNoise powerBlurDespeckle:threshold:scale:countThreshold:luminanceThreshold:diffAmount:];
-[RAWReduceNoise powerBlurDespeckleHF:threshold:moireAmount:scale:countThreshold:luminanceThreshold:diffAmount:];
-[RAWReduceNoise powerBlurEarlyOut2:threshold:scale:neutralThreshold:thresholdScale:];
-[RAWReduceNoise powerBlurEarlyOut2HF:threshold:moireAmount:scale:neutralThreshold:thresholdScale:];
-[RAWReduceNoise powerBlurEarlyOut:threshold:scale:];
-[RAWReduceNoise powerBlurEarlyOutHF:threshold:moireAmount:scale:];
-[RAWReduceNoise powerBlurFS:threshold:neutralFactors:];
-[RAWReduceNoise powerBlurFSHF:threshold:moireAmount:neutralFactors:];
-[RAWReduceNoise powerBlurHF:threshold:moireAmount:scale:];
-[RAWReduceNoise powerBlurY:threshold:];
-[RAWReduceNoise samplerForImage:];
-[RAWReduceNoise smoothDetailsAlongDirections:directions:amount:];
-[RAWReduceNoise smoothDetailsAlongDirectionsAtScale:directions:scale:thresh:smooth:];
-[RAWReduceNoise smoothDetailsAlongDirectionsAtScaleAntiBloom:directions:scale:thresh:smooth:maxContrast:];
-[RAWReduceNoise smoothDetailsAlongDirectionsAtScaleWithSharpen:directions:scale:thresh:smooth:sharp:pscale:coringThreshold:];
-[RAWReduceNoise smoothDetailsAlongDirectionsAtScaleWithSharpenAntiBloom:directions:scale:thresh:smooth:sharp:pscale:coringThreshold:maxContrast:];
-[RAWReduceNoise smoothVectorFieldAlongVectors:];
-[RAWReduceNoise vectorFieldToDirectionsAndGradients:];
-[RAWReduceNoise viewBlend:sushiFactors:crop:];
-[RAWReduceNoise viewC:crop:];
-[RAWReduceNoise viewD:factor:crop:];
-[RAWReduceNoise viewDIR:do360:crop:];
-[RAWReduceNoise viewG:scale:crop:];
-[RAWReduceNoise viewGDIR:do360:crop:];
-[RAWReduceNoise viewHue:sushiFactors:crop:];
-[RAWReduceNoise viewRGB:sushiFactors:crop:];
-[RAWReduceNoise viewTG:lothresh:factor:crop:];
-[RAWReduceNoise viewTGDIR:lothresh:factor:do360:crop:];
-[RAWReduceNoise viewVF:crop:];
-[RAWReduceNoise viewY:sushiFactors:crop:];
```
