# `CBABCurveNitsBased`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAABCurveProtocol`
- 7 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CBABCurveConfiguration" _config;
@"NSString" _curvePrefsKey;
@"CBABCurveNitsBasedPreferences" _pref;
B _shouldClampLowLux;
@"NSObject<OS_os_log>" _logHandle;
f _scaleFactor;
Q _version;
```

## Properties

```
@property (Tf,N,V_scaleFactor) scaleFactor;
@property (TQ,R,N,V_version) version;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBABCurveNitsBased setScaleFactor:];
-[CBABCurveNitsBased dealloc];
-[CBABCurveNitsBased version];
-[CBABCurveNitsBased scaleFactor];
-[CBABCurveNitsBased description];
-[CBABCurveNitsBased copyWithZone:];
-[CBABCurveNitsBased resetToDefaultState];
-[CBABCurveNitsBased copyUserPrefState];
-[CBABCurveNitsBased getNitsForLux:];
-[CBABCurveNitsBased getScaledL1];
-[CBABCurveNitsBased getScaledL2];
-[CBABCurveNitsBased initWithConfiguration:andCurvePrefsKey:];
-[CBABCurveNitsBased setSavedPreferences:];
-[CBABCurveNitsBased setScaledL1:];
-[CBABCurveNitsBased setScaledL2:];
-[CBABCurveNitsBased transferStateFrom:];
-[CBABCurveNitsBased updateALSParametersForNits:andLux:];
```
