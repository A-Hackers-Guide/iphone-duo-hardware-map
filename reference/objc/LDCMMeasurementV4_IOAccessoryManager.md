# `LDCMMeasurementV4`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 31 instance variables, 31 properties, 34 instance methods, 0 class methods

## Instance variables

```
C ldcmRREFGated;
C ldcmPortStatus;
C ldcmMitigationsStatus;
C ldcmFeatureStatus;
C ldcmLowImp;
C ldcmCompletion;
C ldcmWet;
C ldcmMeasurePin;
C ldcmWetStateTooLong;
C ldcmIncompSNRAmpCnt;
C ldcmIncompOVPCnt;
C ldcmIncompTimeoutCnt;
C _ldcmWetTooLongLDCMDisabled;
S ldcmSuccessfulCnt;
I ldcmWetStateDuration;
d ldcmLoadImpMag;
d ldcmLoadImpPhase;
d ldcmCalculatedRes;
d ldcmCalculatedCap;
d ldcmTIACurrentAmp;
d ldcmVoltageAmp;
d ldcmLeakageCurrentAmp;
d ldcmMeasureTIASNR;
d ldcmMeasureVoltageSNR;
d ldcmCalTIAAmp;
d ldcmCalVoltageAmp;
d ldcmCalTIASNR;
d ldcmCalVoltageSNR;
d ldcmTIAGainCorrection;
d ldcmVoltageGainCorrection;
d ldcmPhaseComp;
```

## Properties

```
@property (Td,R,N,VldcmLoadImpMag) ldcmLoadImpMag;
@property (Td,R,N,VldcmLoadImpPhase) ldcmLoadImpPhase;
@property (Td,R,N,VldcmCalculatedRes) ldcmCalculatedRes;
@property (Td,R,N,VldcmCalculatedCap) ldcmCalculatedCap;
@property (Td,R,N,VldcmTIACurrentAmp) ldcmTIACurrentAmp;
@property (Td,R,N,VldcmVoltageAmp) ldcmVoltageAmp;
@property (Td,R,N,VldcmLeakageCurrentAmp) ldcmLeakageCurrentAmp;
@property (Td,R,N,VldcmMeasureTIASNR) ldcmMeasureTIASNR;
@property (Td,R,N,VldcmMeasureVoltageSNR) ldcmMeasureVoltageSNR;
@property (Td,R,N,VldcmCalTIAAmp) ldcmCalTIAAmp;
@property (Td,R,N,VldcmCalVoltageAmp) ldcmCalVoltageAmp;
@property (Td,R,N,VldcmCalTIASNR) ldcmCalTIASNR;
@property (Td,R,N,VldcmCalVoltageSNR) ldcmCalVoltageSNR;
@property (Td,R,N,VldcmTIAGainCorrection) ldcmTIAGainCorrection;
@property (Td,R,N,VldcmVoltageGainCorrection) ldcmVoltageGainCorrection;
@property (Td,R,N,VldcmPhaseComp) ldcmPhaseComp;
@property (TC,R,N,VldcmRREFGated) ldcmRREFGated;
@property (TC,R,N,VldcmPortStatus) ldcmPortStatus;
@property (TC,R,N,VldcmMitigationsStatus) ldcmMitigationsStatus;
@property (TC,R,N,VldcmFeatureStatus) ldcmFeatureStatus;
@property (TC,R,N,VldcmLowImp) ldcmLowImp;
@property (TC,R,N,VldcmCompletion) ldcmCompletion;
@property (TC,R,N,VldcmWet) ldcmWet;
@property (TC,R,N,VldcmMeasurePin) ldcmMeasurePin;
@property (TI,R,N,VldcmWetStateDuration) ldcmWetStateDuration;
@property (TC,R,N,VldcmWetStateTooLong) ldcmWetStateTooLong;
@property (TC,R,N,V_ldcmWetTooLongLDCMDisabled) ldcmWetTooLongLDCMDisabled;
@property (TC,R,N,VldcmIncompSNRAmpCnt) ldcmIncompSNRAmpCnt;
@property (TC,R,N,VldcmIncompOVPCnt) ldcmIncompOVPCnt;
@property (TC,R,N,VldcmIncompTimeoutCnt) ldcmIncompTimeoutCnt;
@property (TS,R,N,VldcmSuccessfulCnt) ldcmSuccessfulCnt;
```

## Instance methods

```
-[LDCMMeasurementV4 ldcmWetTooLongLDCMDisabled];
-[LDCMMeasurementV4 ldcmLoadImpMag];
-[LDCMMeasurementV4 ldcmPhaseComp];
-[LDCMMeasurementV4 ldcmIncompTimeoutCnt];
-[LDCMMeasurementV4 ldcmFeatureStatus];
-[LDCMMeasurementV4 ldcmPortStatus];
-[LDCMMeasurementV4 ldcmWet];
-[LDCMMeasurementV4 ldcmCompletion];
-[LDCMMeasurementV4 ldcmLowImp];
-[LDCMMeasurementV4 ldcmTIACurrentAmp];
-[LDCMMeasurementV4 ldcmCalVoltageAmp];
-[LDCMMeasurementV4 ldcmRREFGated];
-[LDCMMeasurementV4 ldcmCalTIASNR];
-[LDCMMeasurementV4 ldcmIncompSNRAmpCnt];
-[LDCMMeasurementV4 ldcmMitigationsStatus];
-[LDCMMeasurementV4 ldcmTIAGainCorrection];
-[LDCMMeasurementV4 ldcmCalVoltageSNR];
-[LDCMMeasurementV4 ldcmWetStateDuration];
-[LDCMMeasurementV4 ldcmSuccessfulCnt];
-[LDCMMeasurementV4 parseData:];
-[LDCMMeasurementV4 ldcmWetStateTooLong];
-[LDCMMeasurementV4 ldcmCalculatedCap];
-[LDCMMeasurementV4 ldcmMeasureTIASNR];
-[LDCMMeasurementV4 ldcmVoltageGainCorrection];
-[LDCMMeasurementV4 ldcmIncompOVPCnt];
-[LDCMMeasurementV4 getBits:shift:mask:];
-[LDCMMeasurementV4 ldcmMeasureVoltageSNR];
-[LDCMMeasurementV4 ldcmCalTIAAmp];
-[LDCMMeasurementV4 ldcmVoltageAmp];
-[LDCMMeasurementV4 ldcmLoadImpPhase];
-[LDCMMeasurementV4 ldcmMeasurePin];
-[LDCMMeasurementV4 initWithParams::];
-[LDCMMeasurementV4 ldcmCalculatedRes];
-[LDCMMeasurementV4 ldcmLeakageCurrentAmp];
```
