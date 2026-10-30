# `CBGammaContrastPreservationParams`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBChromaticCorectionParamsProtocol`, `CBSerializable`
- 25 instance variables, 28 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
f _rampUpDuration;
f _rampDownDuration;
f _rampUpLuxDeltaThreshold;
f _rampDownLuxDeltaThreshold;
f _aodRampDuration;
f _rampUpdateRate;
I _supported;
f _luxActivationThreshold;
f _nitsActivationThreshold;
f _referenceWhiteBrightness;
f _referenceLux;
f _Lmin;
f _Lmax;
f _ambientFactor;
f _Bmin;
f _Bmax;
f _gammaMin;
f _gammaMax;
f _gcpFactorLow;
f _gcpFactorHigh;
f _ASb;
f _Kb;
f _Kl;
@"NSDictionary" _codingKeys;
```

## Properties

```
@property (Tf,R,V_referenceWhiteBrightness) referenceWhiteBrightness;
@property (Tf,R,V_referenceLux) referenceLux;
@property (Tf,R,V_Lmin) Lmin;
@property (Tf,R,V_Lmax) Lmax;
@property (Tf,R,V_ambientFactor) ambientFactor;
@property (Tf,R,V_Bmin) Bmin;
@property (Tf,R,V_Bmax) Bmax;
@property (Tf,R,V_gammaMin) gammaMin;
@property (Tf,R,V_gammaMax) gammaMax;
@property (Tf,R,V_gcpFactorLow) gcpFactorLow;
@property (Tf,R,V_gcpFactorHigh) gcpFactorHigh;
@property (Tf,R,V_ASb) ASb;
@property (Tf,R,V_Kb) Kb;
@property (Tf,R,V_Kl) Kl;
@property (Tf,R,V_luxActivationThreshold) luxActivationThreshold;
@property (Tf,R,V_nitsActivationThreshold) nitsActivationThreshold;
@property (Tf,R,V_rampUpdateRate) rampUpdateRate;
@property (Tf,R,V_rampUpDuration) rampUpDuration;
@property (Tf,R,V_rampUpLuxDeltaThreshold) rampUpLuxDeltaThreshold;
@property (Tf,R,V_rampDownDuration) rampDownDuration;
@property (Tf,R,V_rampDownLuxDeltaThreshold) rampDownLuxDeltaThreshold;
@property (Tf,R,V_aodRampDuration) aodRampDuration;
@property (TI,R,V_supported) supported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,V_codingKeys) codingKeys;
```

## Class methods

```
+[CBGammaContrastPreservationParams paramsWithProvider:];
```

## Instance methods

```
-[CBGammaContrastPreservationParams supported];
-[CBGammaContrastPreservationParams dealloc];
-[CBGammaContrastPreservationParams luxActivationThreshold];
-[CBGammaContrastPreservationParams initWithProvider:];
-[CBGammaContrastPreservationParams isEqual:];
-[CBGammaContrastPreservationParams rampUpDuration];
-[CBGammaContrastPreservationParams Bmin];
-[CBGammaContrastPreservationParams Kb];
-[CBGammaContrastPreservationParams Lmin];
-[CBGammaContrastPreservationParams aodRampDuration];
-[CBGammaContrastPreservationParams ASb];
-[CBGammaContrastPreservationParams Bmax];
-[CBGammaContrastPreservationParams Kl];
-[CBGammaContrastPreservationParams Lmax];
-[CBGammaContrastPreservationParams ambientFactor];
-[CBGammaContrastPreservationParams codingKeys];
-[CBGammaContrastPreservationParams gammaMax];
-[CBGammaContrastPreservationParams gammaMin];
-[CBGammaContrastPreservationParams gcpFactorHigh];
-[CBGammaContrastPreservationParams gcpFactorLow];
-[CBGammaContrastPreservationParams nitsActivationThreshold];
-[CBGammaContrastPreservationParams rampDownDuration];
-[CBGammaContrastPreservationParams rampDownLuxDeltaThreshold];
-[CBGammaContrastPreservationParams rampUpLuxDeltaThreshold];
-[CBGammaContrastPreservationParams rampUpdateRate];
-[CBGammaContrastPreservationParams referenceLux];
-[CBGammaContrastPreservationParams referenceWhiteBrightness];
```
