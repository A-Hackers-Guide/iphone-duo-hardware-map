# `LTMExtractMetadataV1`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMExtractMetadataBase`
- 10 instance variables, 4 properties, 3 instance methods, 8 class methods

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
+[LTMExtractMetadataV1 compareAWBMetadata:withReference:];
+[LTMExtractMetadataV1 extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:];
+[LTMExtractMetadataV1 extractAWBMetadataFromRawMetadata:toDriverInput:];
+[LTMExtractMetadataV1 extractCCMFromMetadata:toDriverInput:];
+[LTMExtractMetadataV1 extractFromRawMetadata:toDriverInput:];
+[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:];
+[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:];
+[LTMExtractMetadataV1 isLocalCCMEnabled:];
```

## Instance methods

```
-[LTMExtractMetadataV1 init];
-[LTMExtractMetadataV1 extractFrom:toDriverInput:ltmGeometry:];
-[LTMExtractMetadataV1 extractHRGainDownRatioFrom:];
```
