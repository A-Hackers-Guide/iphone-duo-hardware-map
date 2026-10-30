# `BWEspressoInferenceBoundingBoxPropagator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePropagatable`
- 19 instance variables, 5 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"BWInferenceDataRequirement" _boxRequirement;
@"BWInferenceDataRequirement" _scoreRequirement;
@"BWInferenceDataRequirement" _angularOffsetRequirement;
@"BWInferenceDataRequirement" _fontSizeRequirement;
@"NSString" _inferenceResultKey;
B _suppressInterior;
f _interiorPadding;
f _maxMatchCost;
f _angularOffsetExponentialSmoothing;
f _fontSizeStartReportingThreshold;
f _fontSizeStopReportingThreshold;
@"FigCaptureLogSmartCameraGating" _logger;
@"FTBipartiteMatcher" _matcher;
q _maxRegionID;
B _inferenceInputUsesPortraitOrientation;
f _trackingThreshold;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _filterTemplate;
^{?=q{CGRect={CGPoint=dd}{CGSize=dd}}Bfff{CGRect={CGPoint=dd}{CGSize=dd}}f{BWSmartCameraScene=BBffffsssB*}} _lastRegions;
Q _lastRegionCount;
```

## Properties

```
@property (TB,R,N) allowsAsyncPropagation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWEspressoInferenceBoundingBoxPropagator initialize];
```

## Instance methods

```
-[BWEspressoInferenceBoundingBoxPropagator allowsAsyncPropagation];
-[BWEspressoInferenceBoundingBoxPropagator dealloc];
-[BWEspressoInferenceBoundingBoxPropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:];
-[BWEspressoInferenceBoundingBoxPropagator initWithBoxRequirement:scoreRequirement:angularOffsetRequirement:fontSizeRequirement:configuration:toInferenceResultKey:];
```
