# `RAWDemosaicFilter`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 25 instance variables, 0 properties, 15 instance methods, 0 class methods

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
@"NSNumber" inputVersion;
@"NSString" inputInferenceDevice;
@"NSString" inputEnableCache;
@"NSString" inputModelDirectory;
@"NSNumber" inputModelDownloadTimeout;
@"NSDictionary" inputFocusPixelPatternsDict;
@"NSDictionary" inputDNGMetadata;
@"CIVector" inputSuperCCDSRRawCrop;
@"CIVector" inputSuperCCDSROutputSize;
@"NSNumber" inputSuperCCDSRLayout;
@"CIVector" inputFujiEXRRawCrop;
@"CIVector" inputFujiEXROutputSize;
@"CIVector" inputFujiEXRPhase;
```

## Instance methods

```
-[RAWDemosaicFilter outputImage];
-[RAWDemosaicFilter sensorType];
-[RAWDemosaicFilter range];
-[RAWDemosaicFilter crop];
-[RAWDemosaicFilter regionOf:destRect:userInfo:];
-[RAWDemosaicFilter noiseModel];
-[RAWDemosaicFilter blacks];
-[RAWDemosaicFilter exposureFactor];
-[RAWDemosaicFilter forceVersion];
-[RAWDemosaicFilter phaseFor:];
-[RAWDemosaicFilter phaseForBayer];
-[RAWDemosaicFilter phaseForQuadra];
-[RAWDemosaicFilter phaseForRGBE];
-[RAWDemosaicFilter phaseForXtrans];
-[RAWDemosaicFilter versionfor:];
```
