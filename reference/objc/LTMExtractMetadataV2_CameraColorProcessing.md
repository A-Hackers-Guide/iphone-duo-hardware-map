# `LTMExtractMetadataV2`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMExtractMetadataBase`
- 11 instance variables, 4 properties, 5 instance methods, 8 class methods

## Instance variables

```
B _forceDisableLTMFaceBoost;
B _forceDisableLTMFaceExposureRatio;
B _forceDisableHR;
B _forceHighlightCompressionForEveryFrame;
B _forceDisableLTMHazeCorrection;
B _forceUseBt709;
f _faceBiasScaler;
f _faceBiasScalerMin;
f _faceBiasThreshold;
f _faceBiasThresholdMin;
i _allowPortraitOrientationLTCGridOverride;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LTMExtractMetadataV2 compareAWBMetadata:withReference:];
+[LTMExtractMetadataV2 extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:];
+[LTMExtractMetadataV2 extractAWBMetadataFromRawMetadata:toDriverInput:];
+[LTMExtractMetadataV2 extractCCMFromMetadata:toDriverInput:];
+[LTMExtractMetadataV2 extractFromRawMetadata:toDriverInput:];
+[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:];
+[LTMExtractMetadataV2 getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:];
+[LTMExtractMetadataV2 isLocalCCMEnabled:];
```

## Instance methods

```
-[LTMExtractMetadataV2 init];
-[LTMExtractMetadataV2 copyRectanglesInformationFrom:toDriverInput:ltmGeometry:];
-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:];
-[LTMExtractMetadataV2 extractHRGainDownRatioFrom:];
-[LTMExtractMetadataV2 extractRectanglesInformationFrom:toDriverInput:ltmGeometry:];
```
