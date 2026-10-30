# `AASettingsTelemetry`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[AASettingsTelemetry sharedInstance];
```

## Instance methods

```
-[AASettingsTelemetry dispatchQueue];
-[AASettingsTelemetry init];
-[AASettingsTelemetry setDispatchQueue:];
-[AASettingsTelemetry _sendSettingsChanges:device:];
-[AASettingsTelemetry _submitFeaturesChangeMetrics:forFeature:forDevice:];
-[AASettingsTelemetry sendSettingsChanges:device:];
```
