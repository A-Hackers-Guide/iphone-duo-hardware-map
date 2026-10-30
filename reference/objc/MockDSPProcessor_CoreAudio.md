# `MockDSPProcessor`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_IOProcessor`
- 6 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _lastEnablementState;
i _featureFlag;
^v _dspCallbacks;
@"<HAL_DSP_HostCallbacks>" _hostCallbacks;
@"MockPropertySet" _processorProperties;
@"NSString" _lastEnabledDeviceUID;
```

## Properties

```
@property (T^v,N,V_dspCallbacks) dspCallbacks;
@property (T@"<HAL_DSP_HostCallbacks>",&,N,V_hostCallbacks) hostCallbacks;
@property (Ti,N,V_featureFlag) featureFlag;
@property (T@"MockPropertySet",&,N,V_processorProperties) processorProperties;
@property (T@"NSString",&,N,V_lastEnabledDeviceUID) lastEnabledDeviceUID;
@property (TB,N,V_lastEnablementState) lastEnablementState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MockDSPProcessor init];
-[MockDSPProcessor dealloc];
-[MockDSPProcessor negotiateConfigurationChange:error:];
-[MockDSPProcessor adaptToConfigurationChange:withCallbacks:error:];
-[MockDSPProcessor getProcessorPropertySet];
-[MockDSPProcessor simulateConfigurationChange:error:];
-[MockDSPProcessor featureFlag];
-[MockDSPProcessor setFeatureFlag:];
-[MockDSPProcessor canHandleFormat:];
-[MockDSPProcessor dspCallbacks];
-[MockDSPProcessor hostCallbacks];
-[MockDSPProcessor lastEnabledDeviceUID];
-[MockDSPProcessor lastEnablementState];
-[MockDSPProcessor processorProperties];
-[MockDSPProcessor returnNilDictAndPopulateError:errorCode:error:];
-[MockDSPProcessor setDspCallbacks:];
-[MockDSPProcessor setHostCallbacks:];
-[MockDSPProcessor setLastEnabledDeviceUID:];
-[MockDSPProcessor setLastEnablementState:];
-[MockDSPProcessor setProcessorProperties:];
-[MockDSPProcessor setPropertyValueHook:];
```
