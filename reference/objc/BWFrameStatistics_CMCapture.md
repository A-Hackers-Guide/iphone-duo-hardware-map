# `BWFrameStatistics`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 72 properties, 80 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
@"NSDictionary" _aeStatistics;
@"NSArray" _displayStrobeRGBEstimate;
@"NSData" _colorCorrectionMatrix;
f _defaultFNumber;
^{?={?=qiIq}f{CGRect={CGPoint=dd}{CGSize=dd}}IIIIffdIIIfffdfIIIIBBBiBfiBiiiiiiiiiififii@q@IfiBBSSSSSSSSSII} _storage;
```

## Properties

```
@property (T@"NSString",R,N) portType;
@property (TB,R,N,GisValid) valid;
@property (T{?=qiIq},R,N) pts;
@property (Tf,R,N) currentFrameRate;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) finalCropRect;
@property (Td,R,N) eit;
@property (Td,R,N) normalizedEIT;
@property (TI,R,N) luxLevel;
@property (TI,R,N) conversionGain;
@property (TI,R,N) readNoise_1x;
@property (TI,R,N) readNoise_8x;
@property (Tf,R,N) normalizedSNR;
@property (Tf,R,N) normalizedQsumSNR;
@property (Td,R,N) integrationTime;
@property (TI,R,N) agc;
@property (TI,R,N) ispDGain;
@property (TI,R,N) sensorDGain;
@property (Tf,R,N) ispDGainRangeExpansionFactor;
@property (Tf,R,N) gain;
@property (Tf,R,N) baseISO;
@property (Td,R,N) exposureBias;
@property (Tf,R,N) defaultFNumber;
@property (Tf,R,N) fNumber;
@property (TI,R,N) exposureSignals;
@property (TI,R,N) aeAverage;
@property (TI,R,N) aeFaceAverage;
@property (TI,R,N) aeTarget;
@property (TB,R,N) aeLimitsReached;
@property (TB,R,N) aeStable;
@property (TB,R,N) aeLocked;
@property (Ti,R,N) motionFromAEMatrix;
@property (T@"NSDictionary",R,N) aeStatistics;
@property (TB,R,N) hrEnabled;
@property (Tf,R,N) sifrGain;
@property (Ti,R,N) afStatus;
@property (TB,R,N) afLocked;
@property (Ti,R,N) afStationaryCount;
@property (Ti,R,N) focusingMethod;
@property (Ti,R,N) lastFocusingMethod;
@property (Ti,R,N) focusPosition;
@property (Ti,R,N) focusPositionStep;
@property (Ti,R,N) logicalFocusLensPosition;
@property (Ti,R,N) logicalFocusLensPositionStep;
@property (Ti,R,N) filteredLogicalFocusLensPosition;
@property (Ti,R,N) filteredLogicalFocusLensPositionStep;
@property (Ti,R,N) hyperfocalLogicalFocusLensPosition;
@property (Tf,R,N) focusDistance;
@property (Ti,R,N) focusRegionType;
@property (Tf,R,N) tofMeasuredDepth;
@property (Ti,R,N) tofSensorConfidence;
@property (Ti,R,N) tofROIType;
@property (T@"NSString",R,N) afRecommendedPrimaryPortType;
@property (Tq,R,N) afRecommendedPrimaryPortTypeChangeTime;
@property (T@"NSString",R,N) afConvergenceRequiresHigherFPSForPortType;
@property (TI,R,N) motionDataStatus;
@property (Tf,R,N) motionDataBiasErrorEstimate;
@property (Ti,R,N) ltmCurve;
@property (T@"NSArray",R,N) displayStrobeRGBEstimate;
@property (TB,R,N) awbStable;
@property (TB,R,N) awbLocked;
@property (TS,R,N) awbRGain;
@property (TS,R,N) awbGGain;
@property (TS,R,N) awbBGain;
@property (TS,R,N) awbComboRGain;
@property (TS,R,N) awbComboGGain;
@property (TS,R,N) awbComboBGain;
@property (TS,R,N) awbSkinRGain;
@property (TS,R,N) awbSkinGGain;
@property (TS,R,N) awbSkinBGain;
@property (TI,R,N) awbSpatialCCMMixingFactor;
@property (TI,R,N) cct;
@property (T@"NSData",R,N) colorCorrectionMatrix;
```

## Instance methods

```
-[BWFrameStatistics gain];
-[BWFrameStatistics pts];
-[BWFrameStatistics aeStatistics];
-[BWFrameStatistics exposureSignals];
-[BWFrameStatistics focusDistance];
-[BWFrameStatistics setBaseISO:];
-[BWFrameStatistics motionFromAEMatrix];
-[BWFrameStatistics sifrGain];
-[BWFrameStatistics aeLimitsReached];
-[BWFrameStatistics motionDataBiasErrorEstimate];
-[BWFrameStatistics aeAverage];
-[BWFrameStatistics portType];
-[BWFrameStatistics tofSensorConfidence];
-[BWFrameStatistics afStatus];
-[BWFrameStatistics focusRegionType];
-[BWFrameStatistics tofROIType];
-[BWFrameStatistics baseISO];
-[BWFrameStatistics afRecommendedPrimaryPortType];
-[BWFrameStatistics afLocked];
-[BWFrameStatistics readNoise_1x];
-[BWFrameStatistics _setColorCorrectionMatrix:];
-[BWFrameStatistics awbBGain];
-[BWFrameStatistics finalCropRect];
-[BWFrameStatistics afRecommendedPrimaryPortTypeChangeTime];
-[BWFrameStatistics ispDGain];
-[BWFrameStatistics dealloc];
-[BWFrameStatistics focusPosition];
-[BWFrameStatistics readNoise_8x];
-[BWFrameStatistics hrEnabled];
-[BWFrameStatistics normalizedSNR];
-[BWFrameStatistics afStationaryCount];
-[BWFrameStatistics afConvergenceRequiresHigherFPSForPortType];
-[BWFrameStatistics awbSkinGGain];
-[BWFrameStatistics awbSkinBGain];
-[BWFrameStatistics awbComboBGain];
-[BWFrameStatistics awbStable];
-[BWFrameStatistics aeTarget];
-[BWFrameStatistics normalizedQsumSNR];
-[BWFrameStatistics eit];
-[BWFrameStatistics aeLocked];
-[BWFrameStatistics sensorDGain];
-[BWFrameStatistics lastFocusingMethod];
-[BWFrameStatistics awbRGain];
-[BWFrameStatistics logicalFocusLensPositionStep];
-[BWFrameStatistics tofMeasuredDepth];
-[BWFrameStatistics currentFrameRate];
-[BWFrameStatistics aeFaceAverage];
-[BWFrameStatistics fNumber];
-[BWFrameStatistics normalizedEITUsingFrameMetadata:];
-[BWFrameStatistics _setDisplayStrobeRGBEstimate:];
-[BWFrameStatistics luxLevel];
-[BWFrameStatistics awbLocked];
-[BWFrameStatistics isValid];
-[BWFrameStatistics integrationTime];
-[BWFrameStatistics agc];
-[BWFrameStatistics focusPositionStep];
-[BWFrameStatistics aeStable];
-[BWFrameStatistics displayStrobeRGBEstimate];
-[BWFrameStatistics description];
-[BWFrameStatistics motionDataStatus];
-[BWFrameStatistics focusingMethod];
-[BWFrameStatistics ispDGainRangeExpansionFactor];
-[BWFrameStatistics awbGGain];
-[BWFrameStatistics filteredLogicalFocusLensPositionStep];
-[BWFrameStatistics filteredLogicalFocusLensPosition];
-[BWFrameStatistics awbSpatialCCMMixingFactor];
-[BWFrameStatistics ltmCurve];
-[BWFrameStatistics normalizedEIT];
-[BWFrameStatistics hyperfocalLogicalFocusLensPosition];
-[BWFrameStatistics logicalFocusLensPosition];
-[BWFrameStatistics awbSkinRGain];
-[BWFrameStatistics frameStatisticsStorage];
-[BWFrameStatistics awbComboGGain];
-[BWFrameStatistics _setAEStatistics:];
-[BWFrameStatistics awbComboRGain];
-[BWFrameStatistics conversionGain];
-[BWFrameStatistics cct];
-[BWFrameStatistics exposureBias];
-[BWFrameStatistics colorCorrectionMatrix];
-[BWFrameStatistics defaultFNumber];
```
