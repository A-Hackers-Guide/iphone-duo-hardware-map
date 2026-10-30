# `RAWDemosaicFilterV9`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 19 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"CIImage" inputImage;
@"CIVector" inputBlacks;
@"NSNumber" inputRange;
@"CIVector" inputFactors;
@"NSNumber" inputPattern;
@"NSNumber" inputDespeckle;
@"CIVector" inputCropRect;
@"NSNumber" inputRepresentativeNoise;
@"NSNumber" inputDraftMode;
@"NSNumber" inputScaleFactor;
@"CIVector" inputNoiseModel;
@"NSNumber" inputBaselineExposure;
@"NSNumber" inputAddBackLimit;
@"NSNumber" inputAddBackOffset;
@"NSNumber" inputAddBackBlur;
@"NSString" inputInferenceDevice;
@"NSString" inputEnableCache;
@"NSString" inputModelDirectory;
@"NSNumber" inputModelDownloadTimeout;
```

## Instance methods

```
-[RAWDemosaicFilterV9 outputImage];
-[RAWDemosaicFilterV9 factors];
-[RAWDemosaicFilterV9 range];
-[RAWDemosaicFilterV9 noiseModel];
-[RAWDemosaicFilterV9 blacks];
-[RAWDemosaicFilterV9 reflectPad:kernel:];
```
