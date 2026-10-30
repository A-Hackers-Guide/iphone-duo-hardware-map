# `CBABCurve`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 2 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"CBABCurveConfiguration" config;
@"NSString" _curvePrefsKey;
{?="bl1"f"bl2"f"e1"f"e2"f"eThresh"f} pref;
f minimumBrightness;
f maximumBrightness;
f currentLux;
f mappedBrightness;
B shouldClampLowLux;
@"NSObject<OS_os_log>" _logHandle;
f _scaleFactor;
Q _version;
```

## Properties

```
@property (TQ,R,V_version) version;
@property (Tf,V_scaleFactor) scaleFactor;
```

## Instance methods

```
-[CBABCurve setScaleFactor:];
-[CBABCurve dealloc];
-[CBABCurve setLux:];
-[CBABCurve version];
-[CBABCurve scaleFactor];
-[CBABCurve description];
-[CBABCurve copyWithZone:];
-[CBABCurve resetToDefaultState];
-[CBABCurve copyUserPrefState];
-[CBABCurve getLinearBrightness];
-[CBABCurve getLux];
-[CBABCurve getScaledBL1];
-[CBABCurve getScaledBL2];
-[CBABCurve initWithConfiguration:andCurvePrefsKey:];
-[CBABCurve initWithUUID:andCurvePrefsKey:];
-[CBABCurve initWithUUID:vendorID:andProductID:andCurvePrefsKey:];
-[CBABCurve provideDefaultPreferencesWithConfiguration:];
-[CBABCurve setLinearBrightnessMin:andMax:];
-[CBABCurve setSavedPrefences:];
-[CBABCurve setScaledBL1:];
-[CBABCurve setScaledBL2:];
-[CBABCurve updateALSParametersForDisplayBrightness:];
```
