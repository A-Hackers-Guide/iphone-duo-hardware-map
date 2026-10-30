# `BWSphereResonanceCalibrationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 13 instance variables, 17 properties, 31 instance methods, 0 class methods

## Instance variables

```
q _magneticFieldMagnitude;
@"NSString" _portType;
I _calibrationStatus;
i _sphereXAxisResonantFrequency;
i _sphereYAxisResonantFrequency;
i _deltaSphereXAxisResonantFrequency;
i _deltaSphereYAxisResonantFrequency;
i _sphereXAxisDampingCoefficient;
i _sphereYAxisDampingCoefficient;
i _deltaSphereXAxisDampingCoefficient;
i _deltaSphereYAxisDampingCoefficient;
i _sphereXAxisLoopGain;
i _sphereYAxisLoopGain;
```

## Properties

```
@property (Tq,N,V_magneticFieldMagnitude) magneticFieldMagnitude;
@property (T@"NSString",C,N,V_portType) portType;
@property (TI,N,V_calibrationStatus) calibrationStatus;
@property (Ti,N,V_sphereXAxisResonantFrequency) sphereXAxisResonantFrequency;
@property (Ti,N,V_sphereYAxisResonantFrequency) sphereYAxisResonantFrequency;
@property (Ti,N,V_deltaSphereXAxisResonantFrequency) deltaSphereXAxisResonantFrequency;
@property (Ti,N,V_deltaSphereYAxisResonantFrequency) deltaSphereYAxisResonantFrequency;
@property (Ti,N,V_sphereXAxisDampingCoefficient) sphereXAxisDampingCoefficient;
@property (Ti,N,V_sphereYAxisDampingCoefficient) sphereYAxisDampingCoefficient;
@property (Ti,N,V_deltaSphereXAxisDampingCoefficient) deltaSphereXAxisDampingCoefficient;
@property (Ti,N,V_deltaSphereYAxisDampingCoefficient) deltaSphereYAxisDampingCoefficient;
@property (Ti,N,V_sphereXAxisLoopGain) sphereXAxisLoopGain;
@property (Ti,N,V_sphereYAxisLoopGain) sphereYAxisLoopGain;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWSphereResonanceCalibrationAnalyticsPayload portType];
-[BWSphereResonanceCalibrationAnalyticsPayload eventDictionary];
-[BWSphereResonanceCalibrationAnalyticsPayload init];
-[BWSphereResonanceCalibrationAnalyticsPayload dealloc];
-[BWSphereResonanceCalibrationAnalyticsPayload reset];
-[BWSphereResonanceCalibrationAnalyticsPayload setPortType:];
-[BWSphereResonanceCalibrationAnalyticsPayload eventName];
-[BWSphereResonanceCalibrationAnalyticsPayload calibrationStatus];
-[BWSphereResonanceCalibrationAnalyticsPayload setCalibrationStatus:];
-[BWSphereResonanceCalibrationAnalyticsPayload deltaSphereXAxisDampingCoefficient];
-[BWSphereResonanceCalibrationAnalyticsPayload deltaSphereXAxisResonantFrequency];
-[BWSphereResonanceCalibrationAnalyticsPayload deltaSphereYAxisDampingCoefficient];
-[BWSphereResonanceCalibrationAnalyticsPayload deltaSphereYAxisResonantFrequency];
-[BWSphereResonanceCalibrationAnalyticsPayload magneticFieldMagnitude];
-[BWSphereResonanceCalibrationAnalyticsPayload setDeltaSphereXAxisDampingCoefficient:];
-[BWSphereResonanceCalibrationAnalyticsPayload setDeltaSphereXAxisResonantFrequency:];
-[BWSphereResonanceCalibrationAnalyticsPayload setDeltaSphereYAxisDampingCoefficient:];
-[BWSphereResonanceCalibrationAnalyticsPayload setDeltaSphereYAxisResonantFrequency:];
-[BWSphereResonanceCalibrationAnalyticsPayload setMagneticFieldMagnitude:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereXAxisDampingCoefficient:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereXAxisLoopGain:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereXAxisResonantFrequency:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereYAxisDampingCoefficient:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereYAxisLoopGain:];
-[BWSphereResonanceCalibrationAnalyticsPayload setSphereYAxisResonantFrequency:];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereXAxisDampingCoefficient];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereXAxisLoopGain];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereXAxisResonantFrequency];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereYAxisDampingCoefficient];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereYAxisLoopGain];
-[BWSphereResonanceCalibrationAnalyticsPayload sphereYAxisResonantFrequency];
```
