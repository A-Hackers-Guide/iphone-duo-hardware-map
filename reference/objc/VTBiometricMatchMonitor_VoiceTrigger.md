# `VTBiometricMatchMonitor`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `VTEventMonitor`
- Protocols: `BKDeviceDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"<VTBiometricMatchMonitorDelegate>" _delegate;
@"BKDevice" _biometricDevice;
```

## Properties

```
@property (T@"BKDevice",&,N,V_biometricDevice) biometricDevice;
@property (T@"<VTBiometricMatchMonitorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTBiometricMatchMonitor sharedInstance];
```

## Instance methods

```
-[VTBiometricMatchMonitor startObserving];
-[VTBiometricMatchMonitor init];
-[VTBiometricMatchMonitor setDelegate:];
-[VTBiometricMatchMonitor delegate];
-[VTBiometricMatchMonitor device:matchEventOccurred:];
-[VTBiometricMatchMonitor biometricDevice];
-[VTBiometricMatchMonitor getLastBiometricMatchEvent:atTime:];
-[VTBiometricMatchMonitor setBiometricDevice:];
```
