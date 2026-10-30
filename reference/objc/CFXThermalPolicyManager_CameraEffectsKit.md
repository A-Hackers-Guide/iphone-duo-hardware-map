# `CFXThermalPolicyManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXVideoCameraThermalDelegate`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _recordingPolicy;
@"JFXThermalPolicyManager" _policyManager;
```

## Properties

```
@property (T@"JFXThermalPolicyManager",&,N,V_policyManager) policyManager;
@property (TB,N,V_recordingPolicy) recordingPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CFXThermalPolicyManager init];
-[CFXThermalPolicyManager policyManager];
-[CFXThermalPolicyManager setPolicyManager:];
-[CFXThermalPolicyManager CFX_notifyPolicyChanged];
-[CFXThermalPolicyManager recordingPolicy];
-[CFXThermalPolicyManager cameraFPSForThermalLevel:deviceType:minRate:maxRate:];
-[CFXThermalPolicyManager setRecordingPolicy:];
```
