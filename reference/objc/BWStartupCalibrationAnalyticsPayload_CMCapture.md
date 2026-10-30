# `BWStartupCalibrationAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 25 instance variables, 29 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
f _accelStandardDeviation;
f _gyroStandardDeviation;
f _sessionOffset;
f _deltaOffset;
i _apsVoltage;
f _maxAcceleration;
f _deltaAcceleration;
i _offsetEstimatorStatus;
B _headroomErrorOccurred;
B _convergeErrorOccurred;
B _motionErrorOccurred;
B _confidenceErrorOccurred;
B _largeOffsetErrorOccurred;
B _saturationErrorOccurred;
B _degradedAPSMagnetErrorOccurred;
B _success;
B _gcolEntry;
B _closedLoopEntry;
f _gravityX;
f _gravityY;
f _gravityZ;
f _completionTime;
f _hingeAngle;
i _reason;
```

## Properties

```
@property (T@"NSString",&,N,V_portType) portType;
@property (Tf,N,V_accelStandardDeviation) accelStandardDeviation;
@property (Tf,N,V_gyroStandardDeviation) gyroStandardDeviation;
@property (Tf,N,V_sessionOffset) sessionOffset;
@property (Tf,N,V_deltaOffset) deltaOffset;
@property (Ti,N,V_apsVoltage) apsVoltage;
@property (Tf,N,V_maxAcceleration) maxAcceleration;
@property (Tf,N,V_deltaAcceleration) deltaAcceleration;
@property (Ti,N,V_offsetEstimatorStatus) offsetEstimatorStatus;
@property (TB,N,V_headroomErrorOccurred) headroomErrorOccurred;
@property (TB,N,V_convergeErrorOccurred) convergeErrorOccurred;
@property (TB,N,V_motionErrorOccurred) motionErrorOccurred;
@property (TB,N,V_confidenceErrorOccurred) confidenceErrorOccurred;
@property (TB,N,V_largeOffsetErrorOccurred) largeOffsetErrorOccurred;
@property (TB,N,V_saturationErrorOccurred) saturationErrorOccurred;
@property (TB,N,V_degradedAPSMagnetErrorOccurred) degradedAPSMagnetErrorOccurred;
@property (TB,N,V_success) success;
@property (TB,N,V_gcolEntry) gcolEntry;
@property (TB,N,V_closedLoopEntry) closedLoopEntry;
@property (Tf,N,V_gravityX) gravityX;
@property (Tf,N,V_gravityY) gravityY;
@property (Tf,N,V_gravityZ) gravityZ;
@property (Tf,N,V_completionTime) completionTime;
@property (Tf,N,V_hingeAngle) hingeAngle;
@property (Ti,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWStartupCalibrationAnalyticsPayload headroomErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload setOffsetEstimatorStatus:];
-[BWStartupCalibrationAnalyticsPayload portType];
-[BWStartupCalibrationAnalyticsPayload setSuccess:];
-[BWStartupCalibrationAnalyticsPayload eventDictionary];
-[BWStartupCalibrationAnalyticsPayload setDeltaAcceleration:];
-[BWStartupCalibrationAnalyticsPayload success];
-[BWStartupCalibrationAnalyticsPayload motionErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload init];
-[BWStartupCalibrationAnalyticsPayload setDeltaOffset:];
-[BWStartupCalibrationAnalyticsPayload setMaxAcceleration:];
-[BWStartupCalibrationAnalyticsPayload hingeAngle];
-[BWStartupCalibrationAnalyticsPayload setLargeOffsetErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload setHingeAngle:];
-[BWStartupCalibrationAnalyticsPayload dealloc];
-[BWStartupCalibrationAnalyticsPayload confidenceErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload gravityZ];
-[BWStartupCalibrationAnalyticsPayload reset];
-[BWStartupCalibrationAnalyticsPayload degradedAPSMagnetErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload setReason:];
-[BWStartupCalibrationAnalyticsPayload offsetEstimatorStatus];
-[BWStartupCalibrationAnalyticsPayload sessionOffset];
-[BWStartupCalibrationAnalyticsPayload setGravityX:];
-[BWStartupCalibrationAnalyticsPayload completionTime];
-[BWStartupCalibrationAnalyticsPayload setApsVoltage:];
-[BWStartupCalibrationAnalyticsPayload setAccelStandardDeviation:];
-[BWStartupCalibrationAnalyticsPayload convergeErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload setPortType:];
-[BWStartupCalibrationAnalyticsPayload setSessionOffset:];
-[BWStartupCalibrationAnalyticsPayload eventName];
-[BWStartupCalibrationAnalyticsPayload setGravityZ:];
-[BWStartupCalibrationAnalyticsPayload gcolEntry];
-[BWStartupCalibrationAnalyticsPayload deltaAcceleration];
-[BWStartupCalibrationAnalyticsPayload deltaOffset];
-[BWStartupCalibrationAnalyticsPayload gyroStandardDeviation];
-[BWStartupCalibrationAnalyticsPayload setGcolEntry:];
-[BWStartupCalibrationAnalyticsPayload setMotionErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload setGravityY:];
-[BWStartupCalibrationAnalyticsPayload gravityX];
-[BWStartupCalibrationAnalyticsPayload setDegradedAPSMagnetErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload largeOffsetErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload setGyroStandardDeviation:];
-[BWStartupCalibrationAnalyticsPayload setClosedLoopEntry:];
-[BWStartupCalibrationAnalyticsPayload setCompletionTime:];
-[BWStartupCalibrationAnalyticsPayload maxAcceleration];
-[BWStartupCalibrationAnalyticsPayload gravityY];
-[BWStartupCalibrationAnalyticsPayload setSaturationErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload reason];
-[BWStartupCalibrationAnalyticsPayload apsVoltage];
-[BWStartupCalibrationAnalyticsPayload accelStandardDeviation];
-[BWStartupCalibrationAnalyticsPayload saturationErrorOccurred];
-[BWStartupCalibrationAnalyticsPayload closedLoopEntry];
-[BWStartupCalibrationAnalyticsPayload setConvergeErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload setConfidenceErrorOccurred:];
-[BWStartupCalibrationAnalyticsPayload setHeadroomErrorOccurred:];
```
