# `AVDepthData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"AVDepthDataInternal" _internal;
```

## Properties

```
@property (T@"NSArray",R) availableDepthDataTypes;
@property (TI,R) depthDataType;
@property (T^{__CVBuffer=},R) depthDataMap;
@property (Tq,R) depthDataQuality;
@property (TB,R,GisDepthDataFiltered) depthDataFiltered;
@property (Tq,R) depthDataAccuracy;
@property (T@"AVCameraCalibrationData",R) cameraCalibrationData;
```

## Class methods

```
+[AVDepthData initialize];
+[AVDepthData depthDataFromDictionaryRepresentation:error:];
+[AVDepthData _allSupportedDepthDataPixelFormatTypes];
```

## Instance methods

```
-[AVDepthData depthDataType];
-[AVDepthData auxiliaryImageType];
-[AVDepthData portraitLightingEffectStrength];
-[AVDepthData debugDescription];
-[AVDepthData dealloc];
-[AVDepthData isDepthDataFiltered];
-[AVDepthData description];
-[AVDepthData cameraCalibrationData];
-[AVDepthData depthDataByConvertingToDepthDataType:];
-[AVDepthData depthDataByReplacingDepthDataMapWithPixelBuffer:error:];
-[AVDepthData depthDataMap];
-[AVDepthData dictionaryRepresentationForAuxiliaryDataType:];
-[AVDepthData _copyPixelBufferRepresentationWithPixelFormatType:];
-[AVDepthData availableDepthDataTypes];
-[AVDepthData copyAuxiliaryMetadata];
-[AVDepthData depthBlurEffectRenderingParameters];
-[AVDepthData depthBlurEffectSimulatedAperture];
-[AVDepthData depthDataAccuracy];
-[AVDepthData depthDataByApplyingExifOrientation:];
-[AVDepthData depthDataQuality];
-[AVDepthData depthDataVersionMajor];
-[AVDepthData depthDataVersionMinor];
-[AVDepthData initWithPixelBuffer:auxiliaryMetadata:];
-[AVDepthData initWithPixelBuffer:depthMetadataDictionary:];
-[AVDepthData portraitScore];
-[AVDepthData portraitScoreIsHigh];
```
