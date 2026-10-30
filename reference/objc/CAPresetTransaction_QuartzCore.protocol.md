# `CAPresetTransaction` (protocol)

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 11 instance methods, 0 class methods

## Properties

```
@property (Tq,N) trinityCabalConfig;
@property (Tq,N) shortPresetID;
@property (TB,N) preserveAppleSRGBGammaResponse;
@property (TB,N) isReferencePreset;
```

## Instance methods

```
-[CAPresetTransaction setTrinityCabalConfig:];
-[CAPresetTransaction commitPreset];
-[CAPresetTransaction trinityCabalConfig];
-[CAPresetTransaction setShortPresetID:];
-[CAPresetTransaction setPreserveAppleSRGBGammaResponse:];
-[CAPresetTransaction isReferencePreset];
-[CAPresetTransaction disableDICOM];
-[CAPresetTransaction preserveAppleSRGBGammaResponse];
-[CAPresetTransaction enableDICOMWithLPrimeMax:LPrimeMin:LAmb:];
-[CAPresetTransaction setIsReferencePreset:];
-[CAPresetTransaction shortPresetID];
```
