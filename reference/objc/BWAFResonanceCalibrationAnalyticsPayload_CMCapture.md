# `BWAFResonanceCalibrationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 12 instance variables, 16 properties, 29 instance methods, 0 class methods

## Instance variables

```
q _magneticFieldMagnitude;
@"NSString" _portType;
I _calibrationStatus;
i _afAxisResonantFreq;
i _deltaAFAxisResonantFreq;
i _afAxisDampingCoefficient;
i _deltaAFAxisDampingCoefficient;
i _afLoopGain;
i _afGelModelD1Coefficient;
i _afGelModelD2Coefficient;
i _afGelModelP1Coefficient;
i _afGelModelP2Coefficient;
```

## Properties

```
@property (Tq,N,V_magneticFieldMagnitude) magneticFieldMagnitude;
@property (T@"NSString",&,N,V_portType) portType;
@property (TI,N,V_calibrationStatus) calibrationStatus;
@property (Ti,N,V_afAxisResonantFreq) afAxisResonantFreq;
@property (Ti,N,V_deltaAFAxisResonantFreq) deltaAFAxisResonantFreq;
@property (Ti,N,V_afAxisDampingCoefficient) afAxisDampingCoefficient;
@property (Ti,N,V_deltaAFAxisDampingCoefficient) deltaAFAxisDampingCoefficient;
@property (Ti,N,V_afLoopGain) afLoopGain;
@property (Ti,N,V_afGelModelD1Coefficient) afGelModelD1Coefficient;
@property (Ti,N,V_afGelModelD2Coefficient) afGelModelD2Coefficient;
@property (Ti,N,V_afGelModelP1Coefficient) afGelModelP1Coefficient;
@property (Ti,N,V_afGelModelP2Coefficient) afGelModelP2Coefficient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWAFResonanceCalibrationAnalyticsPayload portType];
-[BWAFResonanceCalibrationAnalyticsPayload eventDictionary];
-[BWAFResonanceCalibrationAnalyticsPayload init];
-[BWAFResonanceCalibrationAnalyticsPayload dealloc];
-[BWAFResonanceCalibrationAnalyticsPayload reset];
-[BWAFResonanceCalibrationAnalyticsPayload setPortType:];
-[BWAFResonanceCalibrationAnalyticsPayload eventName];
-[BWAFResonanceCalibrationAnalyticsPayload calibrationStatus];
-[BWAFResonanceCalibrationAnalyticsPayload setCalibrationStatus:];
-[BWAFResonanceCalibrationAnalyticsPayload afAxisDampingCoefficient];
-[BWAFResonanceCalibrationAnalyticsPayload afAxisResonantFreq];
-[BWAFResonanceCalibrationAnalyticsPayload afGelModelD1Coefficient];
-[BWAFResonanceCalibrationAnalyticsPayload afGelModelD2Coefficient];
-[BWAFResonanceCalibrationAnalyticsPayload afGelModelP1Coefficient];
-[BWAFResonanceCalibrationAnalyticsPayload afGelModelP2Coefficient];
-[BWAFResonanceCalibrationAnalyticsPayload afLoopGain];
-[BWAFResonanceCalibrationAnalyticsPayload deltaAFAxisDampingCoefficient];
-[BWAFResonanceCalibrationAnalyticsPayload deltaAFAxisResonantFreq];
-[BWAFResonanceCalibrationAnalyticsPayload magneticFieldMagnitude];
-[BWAFResonanceCalibrationAnalyticsPayload setAfAxisDampingCoefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfAxisResonantFreq:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfGelModelD1Coefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfGelModelD2Coefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfGelModelP1Coefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfGelModelP2Coefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setAfLoopGain:];
-[BWAFResonanceCalibrationAnalyticsPayload setDeltaAFAxisDampingCoefficient:];
-[BWAFResonanceCalibrationAnalyticsPayload setDeltaAFAxisResonantFreq:];
-[BWAFResonanceCalibrationAnalyticsPayload setMagneticFieldMagnitude:];
```
