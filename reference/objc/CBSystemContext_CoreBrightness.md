# `CBSystemContext`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBSystemContext`
- 6 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"CBPowerManagementModule" _pm;
@"CBRearALSModule" _rearALSModule;
@"<CBPowerManagement>" _cbpm;
@"<ALSClientRegistrationProtocol>" _alsClientRegistry;
@"CBFrameInfoProvider" _frameInfoProvider;
@"<CBLowPowerModeObservable>" _lpm;
```

## Properties

```
@property (T@"CBRearALSModule",R,V_rearALSModule) rearALSModule;
@property (T@"<CBPowerManagement>",R,V_cbpm) cbpm;
@property (T@"<ALSClientRegistrationProtocol>",R,V_alsClientRegistry) alsClientRegistry;
@property (T@"CBFrameInfoProvider",R,V_frameInfoProvider) frameInfoProvider;
@property (T@"<CBLowPowerModeObservable>",R,V_lpm) lpm;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBSystemContext dealloc];
-[CBSystemContext setLowPowerMode:];
-[CBSystemContext lpm];
-[CBSystemContext alsClientRegistry];
-[CBSystemContext cbpm];
-[CBSystemContext frameInfoProvider];
-[CBSystemContext rearALSModule];
-[CBSystemContext setAlsClientRegistry:];
-[CBSystemContext setCbpm:];
-[CBSystemContext setFrameInfoProvider:];
-[CBSystemContext setRearALSModule:];
```
