# `CMCaptureLocalSessionVideoConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
{?="width"i"height"i} _dimensions;
I _outputFormat;
B _supportsCenterStage;
B _cinematicFramingEnabled;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _centerStageRectOfInterest;
i _centerStageFramingMode;
d _manualFramingPanningAngleX;
d _manualFramingPanningAngleY;
d _manualFramingZoomFactor;
B _supports10BitTemporalFiltering;
B _supports10BitFromISP;
B _temporalFilterLowLightBandingMitigationEnabled;
B _ringLightAutoSupported;
B _ringLightEnabled;
```

## Properties

```
@property (T{?=ii},N,V_dimensions) dimensions;
@property (TI,N,V_outputFormat) outputFormat;
@property (TB,N,V_supportsCenterStage) supportsCenterStage;
@property (TB,N,V_cinematicFramingEnabled) cinematicFramingEnabled;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_centerStageRectOfInterest) centerStageRectOfInterest;
@property (Ti,N,V_centerStageFramingMode) centerStageFramingMode;
@property (Td,N,V_manualFramingPanningAngleX) manualFramingPanningAngleX;
@property (Td,N,V_manualFramingPanningAngleY) manualFramingPanningAngleY;
@property (Td,N,V_manualFramingZoomFactor) manualFramingZoomFactor;
@property (TB,N,V_supports10BitTemporalFiltering) supports10BitTemporalFiltering;
@property (TB,N,V_supports10BitFromISP) supports10BitFromISP;
@property (TB,N,V_temporalFilterLowLightBandingMitigationEnabled) temporalFilterLowLightBandingMitigationEnabled;
@property (TB,N,V_ringLightAutoSupported) ringLightAutoSupported;
@property (TB,N,V_ringLightEnabled) ringLightEnabled;
```

## Instance methods

```
-[CMCaptureLocalSessionVideoConfiguration setCenterStageRectOfInterest:];
-[CMCaptureLocalSessionVideoConfiguration cinematicFramingEnabled];
-[CMCaptureLocalSessionVideoConfiguration setDimensions:];
-[CMCaptureLocalSessionVideoConfiguration centerStageRectOfInterest];
-[CMCaptureLocalSessionVideoConfiguration centerStageFramingMode];
-[CMCaptureLocalSessionVideoConfiguration dimensions];
-[CMCaptureLocalSessionVideoConfiguration setCinematicFramingEnabled:];
-[CMCaptureLocalSessionVideoConfiguration setOutputFormat:];
-[CMCaptureLocalSessionVideoConfiguration setManualFramingPanningAngleY:];
-[CMCaptureLocalSessionVideoConfiguration setCenterStageFramingMode:];
-[CMCaptureLocalSessionVideoConfiguration setRingLightEnabled:];
-[CMCaptureLocalSessionVideoConfiguration manualFramingPanningAngleX];
-[CMCaptureLocalSessionVideoConfiguration setTemporalFilterLowLightBandingMitigationEnabled:];
-[CMCaptureLocalSessionVideoConfiguration manualFramingPanningAngleY];
-[CMCaptureLocalSessionVideoConfiguration description];
-[CMCaptureLocalSessionVideoConfiguration ringLightEnabled];
-[CMCaptureLocalSessionVideoConfiguration temporalFilterLowLightBandingMitigationEnabled];
-[CMCaptureLocalSessionVideoConfiguration setManualFramingPanningAngleX:];
-[CMCaptureLocalSessionVideoConfiguration outputFormat];
-[CMCaptureLocalSessionVideoConfiguration manualFramingZoomFactor];
-[CMCaptureLocalSessionVideoConfiguration ringLightAutoSupported];
-[CMCaptureLocalSessionVideoConfiguration setManualFramingZoomFactor:];
-[CMCaptureLocalSessionVideoConfiguration setRingLightAutoSupported:];
-[CMCaptureLocalSessionVideoConfiguration setSupports10BitFromISP:];
-[CMCaptureLocalSessionVideoConfiguration setSupports10BitTemporalFiltering:];
-[CMCaptureLocalSessionVideoConfiguration setSupportsCenterStage:];
-[CMCaptureLocalSessionVideoConfiguration supports10BitFromISP];
-[CMCaptureLocalSessionVideoConfiguration supports10BitTemporalFiltering];
-[CMCaptureLocalSessionVideoConfiguration supportsCenterStage];
```
