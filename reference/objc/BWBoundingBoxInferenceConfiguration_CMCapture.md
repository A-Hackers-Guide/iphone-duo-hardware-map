# `BWBoundingBoxInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 10 instance variables, 10 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _inferenceInputUsesPortraitOrientation;
B _interiorSuppression;
f _trackingThreshold;
f _maxMatchCost;
f _interiorSuppressionPadding;
f _angularOffsetExponentialSmoothing;
f _fontSizeStartReportingThreshold;
f _fontSizeStopReportingThreshold;
@"FigCaptureLogSmartCameraGating" _logger;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _confidenceFilterSettings;
```

## Properties

```
@property (TB,N,V_inferenceInputUsesPortraitOrientation) inferenceInputUsesPortraitOrientation;
@property (Tf,N,V_trackingThreshold) trackingThreshold;
@property (Tf,N,V_maxMatchCost) maxMatchCost;
@property (T{BWSmartCameraScene=BBffffsssB*},N,V_confidenceFilterSettings) confidenceFilterSettings;
@property (TB,N,V_interiorSuppression) interiorSuppression;
@property (Tf,N,V_interiorSuppressionPadding) interiorSuppressionPadding;
@property (Tf,N,V_angularOffsetExponentialSmoothing) angularOffsetExponentialSmoothing;
@property (Tf,N,V_fontSizeStartReportingThreshold) fontSizeStartReportingThreshold;
@property (Tf,N,V_fontSizeStopReportingThreshold) fontSizeStopReportingThreshold;
@property (T@"FigCaptureLogSmartCameraGating",&,N,V_logger) logger;
```

## Class methods

```
+[BWBoundingBoxInferenceConfiguration initialize];
```

## Instance methods

```
-[BWBoundingBoxInferenceConfiguration logger];
-[BWBoundingBoxInferenceConfiguration setLogger:];
-[BWBoundingBoxInferenceConfiguration dealloc];
-[BWBoundingBoxInferenceConfiguration fontSizeStartReportingThreshold];
-[BWBoundingBoxInferenceConfiguration angularOffsetExponentialSmoothing];
-[BWBoundingBoxInferenceConfiguration confidenceFilterSettings];
-[BWBoundingBoxInferenceConfiguration fontSizeStopReportingThreshold];
-[BWBoundingBoxInferenceConfiguration inferenceInputUsesPortraitOrientation];
-[BWBoundingBoxInferenceConfiguration interiorSuppression];
-[BWBoundingBoxInferenceConfiguration interiorSuppressionPadding];
-[BWBoundingBoxInferenceConfiguration maxMatchCost];
-[BWBoundingBoxInferenceConfiguration setAngularOffsetExponentialSmoothing:];
-[BWBoundingBoxInferenceConfiguration setConfidenceFilterSettings:];
-[BWBoundingBoxInferenceConfiguration setFontSizeStartReportingThreshold:];
-[BWBoundingBoxInferenceConfiguration setFontSizeStopReportingThreshold:];
-[BWBoundingBoxInferenceConfiguration setInferenceInputUsesPortraitOrientation:];
-[BWBoundingBoxInferenceConfiguration setInteriorSuppression:];
-[BWBoundingBoxInferenceConfiguration setInteriorSuppressionPadding:];
-[BWBoundingBoxInferenceConfiguration setMaxMatchCost:];
-[BWBoundingBoxInferenceConfiguration setTrackingThreshold:];
-[BWBoundingBoxInferenceConfiguration trackingThreshold];
```
