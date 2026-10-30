# `CLBackgroundInertialOdometrySample`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 13 instance variables, 13 properties, 22 instance methods, 3 class methods

## Instance variables

```
@"NSDate" _cfAbsTimestamp;
d _machContinuousTimestamp_s;
d _sampleInterval_s;
@"CLBIO_DeltaPosition" _deltaPosition_m;
@"CLBIO_DeltaVelocity" _deltaVelocity_mps;
@"CLBIO_Quaternion" _quaternion;
Q _referenceFrameContinuity;
Q _sessionReferenceFrame;
Q _staticFlag;
Q _mountState;
Q _zupt;
Q _dotBiasChange;
@"CLBIO_Calibration" _calibration;
```

## Properties

```
@property (T@"NSDate",R,N,V_cfAbsTimestamp) cfAbsTimestamp;
@property (Td,R,N,V_machContinuousTimestamp_s) machContinuousTimestamp_s;
@property (Td,R,N,V_sampleInterval_s) sampleInterval_s;
@property (T@"CLBIO_DeltaPosition",R,N,V_deltaPosition_m) deltaPosition_m;
@property (T@"CLBIO_DeltaVelocity",R,N,V_deltaVelocity_mps) deltaVelocity_mps;
@property (T@"CLBIO_Quaternion",R,N,V_quaternion) quaternion;
@property (TQ,R,N,V_referenceFrameContinuity) referenceFrameContinuity;
@property (TQ,R,N,V_sessionReferenceFrame) sessionReferenceFrame;
@property (TQ,R,N,V_staticFlag) staticFlag;
@property (TQ,R,N,V_mountState) mountState;
@property (TQ,R,N,V_zupt) zupt;
@property (TQ,R,N,V_dotBiasChange) dotBiasChange;
@property (T@"CLBIO_Calibration",R,N,V_calibration) calibration;
```

## Class methods

```
+[CLBackgroundInertialOdometrySample supportsSecureCoding];
+[CLBackgroundInertialOdometrySample samplesFromPackedBytes:length:];
+[CLBackgroundInertialOdometrySample packedDataFromSamples:];
```

## Instance methods

```
-[CLBackgroundInertialOdometrySample dealloc];
-[CLBackgroundInertialOdometrySample encodeWithCoder:];
-[CLBackgroundInertialOdometrySample description];
-[CLBackgroundInertialOdometrySample initWithCoder:];
-[CLBackgroundInertialOdometrySample copyWithZone:];
-[CLBackgroundInertialOdometrySample isEqual:];
-[CLBackgroundInertialOdometrySample staticFlag];
-[CLBackgroundInertialOdometrySample quaternion];
-[CLBackgroundInertialOdometrySample deltaPosition_m];
-[CLBackgroundInertialOdometrySample calibration];
-[CLBackgroundInertialOdometrySample cfAbsTimestamp];
-[CLBackgroundInertialOdometrySample deltaVelocity_mps];
-[CLBackgroundInertialOdometrySample dotBiasChange];
-[CLBackgroundInertialOdometrySample initWithTimestamp:machContinuousTimestamp:sampleInterval:deltaPosition:deltaVelocity:quaternion:];
-[CLBackgroundInertialOdometrySample initWithTimestamp:machContinuousTimestamp:sampleInterval:deltaPosition:deltaVelocity:quaternion:referenceFrameContinuity:referenceFrame:staticFlag:];
-[CLBackgroundInertialOdometrySample initWithTimestamp:machContinuousTimestamp:sampleInterval:deltaPosition:deltaVelocity:quaternion:referenceFrameContinuity:referenceFrame:staticFlag:mountState:zupt:dotBiasChange:calibration:];
-[CLBackgroundInertialOdometrySample machContinuousTimestamp_s];
-[CLBackgroundInertialOdometrySample mountState];
-[CLBackgroundInertialOdometrySample referenceFrameContinuity];
-[CLBackgroundInertialOdometrySample sampleInterval_s];
-[CLBackgroundInertialOdometrySample sessionReferenceFrame];
-[CLBackgroundInertialOdometrySample zupt];
```
