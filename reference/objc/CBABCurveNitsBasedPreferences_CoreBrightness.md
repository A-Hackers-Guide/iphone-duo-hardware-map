# `CBABCurveNitsBasedPreferences`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBABCurvePreferencesProtocol`
- 9 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"CBABCurveConfiguration" _config;
@"NSString" _curvePrefsKey;
f _l1;
f _l2;
f _e1;
f _e2;
f _eThresh;
Q _version;
```

## Properties

```
@property (Tf,V_l1) l1;
@property (Tf,V_l2) l2;
@property (Tf,V_e1) e1;
@property (Tf,V_e2) e2;
@property (Tf,V_eThresh) eThresh;
@property (TQ,V_version) version;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBABCurveNitsBasedPreferences dealloc];
-[CBABCurveNitsBasedPreferences version];
-[CBABCurveNitsBasedPreferences setVersion:];
-[CBABCurveNitsBasedPreferences copyWithZone:];
-[CBABCurveNitsBasedPreferences eThresh];
-[CBABCurveNitsBasedPreferences copyUserPreferences];
-[CBABCurveNitsBasedPreferences e1];
-[CBABCurveNitsBasedPreferences e2];
-[CBABCurveNitsBasedPreferences initWithConfiguration:andCurveVersion:andCurvePrefsKey:];
-[CBABCurveNitsBasedPreferences isPrefsDictComplete:];
-[CBABCurveNitsBasedPreferences l1];
-[CBABCurveNitsBasedPreferences l2];
-[CBABCurveNitsBasedPreferences loadPreferencesForUUID:andCurvePrefsKey:];
-[CBABCurveNitsBasedPreferences resetPrefs];
-[CBABCurveNitsBasedPreferences setE1:];
-[CBABCurveNitsBasedPreferences setE2:];
-[CBABCurveNitsBasedPreferences setEThresh:];
-[CBABCurveNitsBasedPreferences setL1:];
-[CBABCurveNitsBasedPreferences setL2:];
-[CBABCurveNitsBasedPreferences setPreferencesFromDictionary:];
```
