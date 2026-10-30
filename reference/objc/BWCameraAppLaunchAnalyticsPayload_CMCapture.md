# `BWCameraAppLaunchAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 13 instance variables, 17 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _isPrewarmed;
@"NSString" _launchMode;
i _devicePosition;
@"NSString" _prewarmReason;
i _launchDuration;
i _memoryStatusLevel;
i _thermalLevel;
i _numberOfGraphStartsDuringLaunch;
B _deviceIsLocked;
i _deviceStolenDuration;
B _isColdLaunch;
i _deviceStolenCondition;
i _ispStartDuration;
```

## Properties

```
@property (TB,N,V_isPrewarmed) isPrewarmed;
@property (T@"NSString",C,N,V_launchMode) launchMode;
@property (Ti,N,V_devicePosition) devicePosition;
@property (T@"NSString",C,N,V_prewarmReason) prewarmReason;
@property (Ti,N,V_launchDuration) launchDuration;
@property (Ti,N,V_memoryStatusLevel) memoryStatusLevel;
@property (Ti,N,V_thermalLevel) thermalLevel;
@property (Ti,N,V_ispStartDuration) ispStartDuration;
@property (Ti,N,V_numberOfGraphStartsDuringLaunch) numberOfGraphStartsDuringLaunch;
@property (TB,N,V_deviceIsLocked) deviceIsLocked;
@property (Ti,N,V_deviceStolenDuration) deviceStolenDuration;
@property (Ti,N,V_deviceStolenCondition) deviceStolenCondition;
@property (TB,N,V_isColdLaunch) isColdLaunch;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWCameraAppLaunchAnalyticsPayload eventDictionary];
-[BWCameraAppLaunchAnalyticsPayload init];
-[BWCameraAppLaunchAnalyticsPayload dealloc];
-[BWCameraAppLaunchAnalyticsPayload reset];
-[BWCameraAppLaunchAnalyticsPayload eventName];
-[BWCameraAppLaunchAnalyticsPayload devicePosition];
-[BWCameraAppLaunchAnalyticsPayload setThermalLevel:];
-[BWCameraAppLaunchAnalyticsPayload thermalLevel];
-[BWCameraAppLaunchAnalyticsPayload setDevicePosition:];
-[BWCameraAppLaunchAnalyticsPayload launchMode];
-[BWCameraAppLaunchAnalyticsPayload numberOfGraphStartsDuringLaunch];
-[BWCameraAppLaunchAnalyticsPayload setIsPrewarmed:];
-[BWCameraAppLaunchAnalyticsPayload deviceIsLocked];
-[BWCameraAppLaunchAnalyticsPayload deviceStolenCondition];
-[BWCameraAppLaunchAnalyticsPayload deviceStolenDuration];
-[BWCameraAppLaunchAnalyticsPayload isColdLaunch];
-[BWCameraAppLaunchAnalyticsPayload isPrewarmed];
-[BWCameraAppLaunchAnalyticsPayload ispStartDuration];
-[BWCameraAppLaunchAnalyticsPayload launchDuration];
-[BWCameraAppLaunchAnalyticsPayload memoryStatusLevel];
-[BWCameraAppLaunchAnalyticsPayload prewarmReason];
-[BWCameraAppLaunchAnalyticsPayload setDeviceIsLocked:];
-[BWCameraAppLaunchAnalyticsPayload setDeviceStolenCondition:];
-[BWCameraAppLaunchAnalyticsPayload setDeviceStolenDuration:];
-[BWCameraAppLaunchAnalyticsPayload setIsColdLaunch:];
-[BWCameraAppLaunchAnalyticsPayload setIspStartDuration:];
-[BWCameraAppLaunchAnalyticsPayload setLaunchDuration:];
-[BWCameraAppLaunchAnalyticsPayload setLaunchMode:];
-[BWCameraAppLaunchAnalyticsPayload setMemoryStatusLevel:];
-[BWCameraAppLaunchAnalyticsPayload setNumberOfGraphStartsDuringLaunch:];
-[BWCameraAppLaunchAnalyticsPayload setPrewarmReason:];
```
