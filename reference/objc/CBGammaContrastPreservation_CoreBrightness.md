# `CBGammaContrastPreservation`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBChromaticCorrection`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
f _AODFadeFactor;
f _enableFactor;
@"NSObject<CBRampManagerI>" _rampManager;
```

## Properties

```
@property (Tf,N,V_AODFadeFactor) AODFadeFactor;
@property (Tf,N,V_enableFactor) enableFactor;
@property (T@"NSObject<CBRampManagerI>",&,V_rampManager) rampManager;
```

## Instance methods

```
-[CBGammaContrastPreservation dealloc];
-[CBGammaContrastPreservation setEnableFactor:];
-[CBGammaContrastPreservation setRampManager:];
-[CBGammaContrastPreservation enableFactor];
-[CBGammaContrastPreservation currentStrength];
-[CBGammaContrastPreservation AODFadeFactor];
-[CBGammaContrastPreservation initWithParams:];
-[CBGammaContrastPreservation setAODFadeFactor:];
-[CBGammaContrastPreservation rampManager];
-[CBGammaContrastPreservation handleAutoBrightnessStateUpdate:];
-[CBGammaContrastPreservation combinedFactor];
```
