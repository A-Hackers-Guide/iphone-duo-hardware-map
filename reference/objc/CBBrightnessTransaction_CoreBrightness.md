# `CBBrightnessTransaction`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBBrightnessAdjustment`
- 9 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BrightnessSystemClient" _client;
@"CBDisplayHandle" _handle;
{optional<float>=""(?="__null_state_"c"__val_"f)"__engaged_"B} _lastBrightness;
Q _commitType;
{optional<float>=""(?="__null_state_"c"__val_"f)"__engaged_"B} _timeout;
@"NSObject<OS_dispatch_source>" _timer;
@"NSObject<OS_os_log>" _logHandle;
B _valid;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSUUID",R,V_uuid) uuid;
@property (TB,R,GisValid,V_valid) valid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBBrightnessTransaction uuid];
-[CBBrightnessTransaction completeWithError:];
-[CBBrightnessTransaction dealloc];
-[CBBrightnessTransaction complete];
-[CBBrightnessTransaction _completeWithError:];
-[CBBrightnessTransaction isValid];
-[CBBrightnessTransaction _setBrightness:withError:];
-[CBBrightnessTransaction initWithClient:andHandle:commitType:timeout:];
-[CBBrightnessTransaction setBrightness:withError:];
```
