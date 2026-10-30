# `CBAODState`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 34 properties, 70 instance methods, 0 class methods

## Instance variables

```
@"NSUserDefaults" _defaults;
@"NSObject<OS_os_log>" _logHandle;
@"SWSystemActivityAssertion" _systemActivityAssertion;
B _isAODSupported;
B _isFlipbookSupported;
B _isAODLiveOnEnabled;
B _isDCPBasedAODSupported;
B _isHighLuminanceAODSupported;
f _thresholdPCCLuxDelta;
f _AODTransitionProfileEaseInOut_K;
f _AODTransitionProfileSpring_mass;
f _AODTransitionProfileSpring_velocity;
f _AODTransitionProfileSpring_damping;
f _AODTransitionProfileSpring_stiffness;
f _AODTransitionTargetAlgoOptimised_dimmingThreshold;
f _pullALSUpdatePeriod;
f _nitsCap;
i _curveLevel;
f _whitepointTransitionLength;
f _whitepointTransitionLengthLowLux;
f _whitepointTransitionLengthLuxThreshold;
f _whitepointDeltaThreshold;
Q _AODState;
Q _AODStateExternal;
@"NSMutableArray" _thresholdsLuxBuckets;
@"NSMutableArray" _thresholdsDeltaPBrightenBuckets;
@"NSMutableArray" _thresholdsDeltaPDimBuckets;
@"NSMutableArray" _thresholdsAPLuxBuckets;
@"NSMutableArray" _thresholdsAPDeltaPBrightenBuckets;
@"NSMutableArray" _thresholdsAPDeltaPDimBuckets;
@"NSArray" _fixedLuxDimThresholds;
@"NSArray" _fixedLuxBrightenThresholds;
Q _AODTransitionProfile;
{?="_E"[20f]"_L"[20f]"size"i} _curve;
{?="_E"[20f]"_L"[20f]"size"i} _darkerCurve;
```

## Properties

```
@property (TQ,V_AODState) AODState;
@property (TQ,V_AODStateExternal) AODStateExternal;
@property (TB,R,N,V_isAODLiveOnEnabled) isAODLiveOnEnabled;
@property (TB,R,N,V_isAODSupported) isAODSupported;
@property (TB,R,N,V_isHighLuminanceAODSupported) isHighLuminanceAODSupported;
@property (TB,R,N,V_isFlipbookSupported) isFlipbookSupported;
@property (TB,R,N,V_isDCPBasedAODSupported) isDCPBasedAODSupported;
@property (T@"NSMutableArray",R,V_thresholdsLuxBuckets) thresholdsLuxBuckets;
@property (T@"NSMutableArray",R,V_thresholdsDeltaPBrightenBuckets) thresholdsDeltaPBrightenBuckets;
@property (T@"NSMutableArray",R,V_thresholdsDeltaPDimBuckets) thresholdsDeltaPDimBuckets;
@property (T@"NSMutableArray",R,V_thresholdsAPLuxBuckets) thresholdsAPLuxBuckets;
@property (T@"NSMutableArray",R,V_thresholdsAPDeltaPBrightenBuckets) thresholdsAPDeltaPBrightenBuckets;
@property (T@"NSMutableArray",R,V_thresholdsAPDeltaPDimBuckets) thresholdsAPDeltaPDimBuckets;
@property (Tf,R,V_thresholdPCCLuxDelta) thresholdPCCLuxDelta;
@property (T@"NSArray",R,V_fixedLuxDimThresholds) fixedLuxDimThresholds;
@property (T@"NSArray",R,V_fixedLuxBrightenThresholds) fixedLuxBrightenThresholds;
@property (Tf,V_pullALSUpdatePeriod) pullALSUpdatePeriod;
@property (Tf,V_nitsCap) nitsCap;
@property (Ti,V_curveLevel) curveLevel;
@property (T{?=[20f][20f]i},R,V_curve) curve;
@property (T{?=[20f][20f]i},R,V_darkerCurve) darkerCurve;
@property (Tf,R) maxAODNits;
@property (Tf,R) minAODNits;
@property (Tf,V_whitepointTransitionLength) whitepointTransitionLength;
@property (Tf,V_whitepointTransitionLengthLowLux) whitepointTransitionLengthLowLux;
@property (Tf,V_whitepointTransitionLengthLuxThreshold) whitepointTransitionLengthLuxThreshold;
@property (Tf,V_whitepointDeltaThreshold) whitepointDeltaThreshold;
@property (TQ,V_AODTransitionProfile) AODTransitionProfile;
@property (Tf,V_AODTransitionProfileEaseInOut_K) AODTransitionProfileEaseInOut_K;
@property (Tf,V_AODTransitionProfileSpring_mass) AODTransitionProfileSpring_mass;
@property (Tf,V_AODTransitionProfileSpring_velocity) AODTransitionProfileSpring_velocity;
@property (Tf,V_AODTransitionProfileSpring_damping) AODTransitionProfileSpring_damping;
@property (Tf,V_AODTransitionProfileSpring_stiffness) AODTransitionProfileSpring_stiffness;
@property (Tf,V_AODTransitionTargetAlgoOptimised_dimmingThreshold) AODTransitionTargetAlgoOptimised_dimmingThreshold;
```

## Instance methods

```
-[CBAODState setProperty:forKey:];
-[CBAODState AODState];
-[CBAODState isAODActive];
-[CBAODState observeValueForKeyPath:ofObject:change:context:];
-[CBAODState init];
-[CBAODState dealloc];
-[CBAODState checkBootArgsConfiguration];
-[CBAODState setCurveLevel:];
-[CBAODState curve];
-[CBAODState curveLevel];
-[CBAODState initWithDisplayID:];
-[CBAODState releasePowerAssertion];
-[CBAODState AODTransitionProfileSpring_mass];
-[CBAODState AODStateExternal];
-[CBAODState AODTransitionProfile];
-[CBAODState AODTransitionProfileSpring_stiffness];
-[CBAODState AODTransitionTargetAlgoOptimised_dimmingThreshold];
-[CBAODState nitsCap];
-[CBAODState thresholdsDeltaPBrightenBuckets];
-[CBAODState AODTransitionProfileEaseInOut_K];
-[CBAODState AODStateString];
-[CBAODState AODTransitionProfileSpring_damping];
-[CBAODState AODTransitionProfileSpring_velocity];
-[CBAODState acquirePowerAssertion];
-[CBAODState checkDefaultsConfiguration];
-[CBAODState copyNumberFromPrefsForKey:];
-[CBAODState darkerCurve];
-[CBAODState fixedLuxBrightenThresholds];
-[CBAODState fixedLuxDimThresholds];
-[CBAODState handleAODCurveUpdate:];
-[CBAODState handleAODDarkerCurveUpdate:];
-[CBAODState initialiseHighLuminanceAODSupport];
-[CBAODState initializeAODLiveOnEnabled];
-[CBAODState initializeAODSupport];
-[CBAODState initializeAODSupportConfiguration];
-[CBAODState isAODLiveOnEnabled];
-[CBAODState isAODSupported];
-[CBAODState isDCPBasedAODSupported];
-[CBAODState isFlipbookSupported];
-[CBAODState isHighLuminanceAODActive];
-[CBAODState isHighLuminanceAODSupported];
-[CBAODState logAODCurve:name:];
-[CBAODState maxAODNits];
-[CBAODState minAODNits];
-[CBAODState pullALSUpdatePeriod];
-[CBAODState setAODState:];
-[CBAODState setAODStateExternal:];
-[CBAODState setAODTransitionProfile:];
-[CBAODState setAODTransitionProfileEaseInOut_K:];
-[CBAODState setAODTransitionProfileSpring_damping:];
-[CBAODState setAODTransitionProfileSpring_mass:];
-[CBAODState setAODTransitionProfileSpring_stiffness:];
-[CBAODState setAODTransitionProfileSpring_velocity:];
-[CBAODState setAODTransitionTargetAlgoOptimised_dimmingThreshold:];
-[CBAODState setNitsCap:];
-[CBAODState setPullALSUpdatePeriod:];
-[CBAODState setWhitepointDeltaThreshold:];
-[CBAODState setWhitepointTransitionLength:];
-[CBAODState setWhitepointTransitionLengthLowLux:];
-[CBAODState setWhitepointTransitionLengthLuxThreshold:];
-[CBAODState thresholdPCCLuxDelta];
-[CBAODState thresholdsAPDeltaPBrightenBuckets];
-[CBAODState thresholdsAPDeltaPDimBuckets];
-[CBAODState thresholdsAPLuxBuckets];
-[CBAODState thresholdsDeltaPDimBuckets];
-[CBAODState thresholdsLuxBuckets];
-[CBAODState whitepointDeltaThreshold];
-[CBAODState whitepointTransitionLength];
-[CBAODState whitepointTransitionLengthLowLux];
-[CBAODState whitepointTransitionLengthLuxThreshold];
```
