# `IOAccessoryUserLdcmParamClass`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 33 instance methods, 0 class methods

## Instance variables

```
i _userBehaviorMask;
i _fdpBehaviorMask;
Q _minVhiDurationSec;
Q _maxVhiDurationSec;
Q _maxUpFluctuationMv;
Q _numEisHalogenSamples;
Q _wetPollingIntervalSec;
Q _dryPollingIntervalSec;
Q _ldcmArbiterRetrySec;
Q _ldcmStartMeasurementsDelayMs;
Q _ldcmStartMeasurementsRetryMs;
Q _minDryReadings;
Q _enableHalogenSnrTtr;
Q _enableHalogenMitigationsAndUI;
d _wetTransitionCapacitanceThreshold;
d _dryTransitionCapacitanceThreshold;
```

## Properties

```
@property (TQ,V_minVhiDurationSec) minVhiDurationSec;
@property (TQ,V_maxVhiDurationSec) maxVhiDurationSec;
@property (TQ,V_maxUpFluctuationMv) maxUpFluctuationMv;
@property (Ti,V_userBehaviorMask) userBehaviorMask;
@property (Ti,V_fdpBehaviorMask) fdpBehaviorMask;
@property (TQ,V_numEisHalogenSamples) numEisHalogenSamples;
@property (TQ,V_wetPollingIntervalSec) wetPollingIntervalSec;
@property (TQ,V_dryPollingIntervalSec) dryPollingIntervalSec;
@property (TQ,V_ldcmArbiterRetrySec) ldcmArbiterRetrySec;
@property (TQ,V_ldcmStartMeasurementsDelayMs) ldcmStartMeasurementsDelayMs;
@property (TQ,V_ldcmStartMeasurementsRetryMs) ldcmStartMeasurementsRetryMs;
@property (TQ,V_minDryReadings) minDryReadings;
@property (TQ,V_enableHalogenSnrTtr) enableHalogenSnrTtr;
@property (TQ,V_enableHalogenMitigationsAndUI) enableHalogenMitigationsAndUI;
@property (Td,V_wetTransitionCapacitanceThreshold) wetTransitionCapacitanceThreshold;
@property (Td,V_dryTransitionCapacitanceThreshold) dryTransitionCapacitanceThreshold;
```

## Instance methods

```
-[IOAccessoryUserLdcmParamClass init];
-[IOAccessoryUserLdcmParamClass fdpBehaviorMask];
-[IOAccessoryUserLdcmParamClass dryPollingIntervalSec];
-[IOAccessoryUserLdcmParamClass dryTransitionCapacitanceThreshold];
-[IOAccessoryUserLdcmParamClass enableHalogenMitigationsAndUI];
-[IOAccessoryUserLdcmParamClass enableHalogenSnrTtr];
-[IOAccessoryUserLdcmParamClass ldcmArbiterRetrySec];
-[IOAccessoryUserLdcmParamClass ldcmStartMeasurementsDelayMs];
-[IOAccessoryUserLdcmParamClass ldcmStartMeasurementsRetryMs];
-[IOAccessoryUserLdcmParamClass maxUpFluctuationMv];
-[IOAccessoryUserLdcmParamClass maxVhiDurationSec];
-[IOAccessoryUserLdcmParamClass minDryReadings];
-[IOAccessoryUserLdcmParamClass minVhiDurationSec];
-[IOAccessoryUserLdcmParamClass numEisHalogenSamples];
-[IOAccessoryUserLdcmParamClass setDryPollingIntervalSec:];
-[IOAccessoryUserLdcmParamClass setDryTransitionCapacitanceThreshold:];
-[IOAccessoryUserLdcmParamClass setEnableHalogenMitigationsAndUI:];
-[IOAccessoryUserLdcmParamClass setEnableHalogenSnrTtr:];
-[IOAccessoryUserLdcmParamClass setFdpBehaviorMask:];
-[IOAccessoryUserLdcmParamClass setLdcmArbiterRetrySec:];
-[IOAccessoryUserLdcmParamClass setLdcmStartMeasurementsDelayMs:];
-[IOAccessoryUserLdcmParamClass setLdcmStartMeasurementsRetryMs:];
-[IOAccessoryUserLdcmParamClass setMaxUpFluctuationMv:];
-[IOAccessoryUserLdcmParamClass setMaxVhiDurationSec:];
-[IOAccessoryUserLdcmParamClass setMinDryReadings:];
-[IOAccessoryUserLdcmParamClass setMinVhiDurationSec:];
-[IOAccessoryUserLdcmParamClass setNumEisHalogenSamples:];
-[IOAccessoryUserLdcmParamClass setUserBehaviorMask:];
-[IOAccessoryUserLdcmParamClass setWetPollingIntervalSec:];
-[IOAccessoryUserLdcmParamClass setWetTransitionCapacitanceThreshold:];
-[IOAccessoryUserLdcmParamClass userBehaviorMask];
-[IOAccessoryUserLdcmParamClass wetPollingIntervalSec];
-[IOAccessoryUserLdcmParamClass wetTransitionCapacitanceThreshold];
```
