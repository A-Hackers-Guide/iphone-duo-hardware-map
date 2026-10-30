# `DSP_HALBypass_IOProcessor`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_IOProcessor`
- 2 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _dspCallbacks;
@"<HAL_DSP_HostCallbacks>" _hostCallbacks;
```

## Properties

```
@property (T^v,N,V_dspCallbacks) dspCallbacks;
@property (T@"<HAL_DSP_HostCallbacks>",&,N,V_hostCallbacks) hostCallbacks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HALBypass_IOProcessor init];
-[DSP_HALBypass_IOProcessor dealloc];
-[DSP_HALBypass_IOProcessor negotiateConfigurationChange:error:];
-[DSP_HALBypass_IOProcessor adaptToConfigurationChange:withCallbacks:error:];
-[DSP_HALBypass_IOProcessor getProcessorPropertySet];
-[DSP_HALBypass_IOProcessor simulateConfigurationChange:error:];
-[DSP_HALBypass_IOProcessor dspCallbacks];
-[DSP_HALBypass_IOProcessor hostCallbacks];
-[DSP_HALBypass_IOProcessor setDspCallbacks:];
-[DSP_HALBypass_IOProcessor setHostCallbacks:];
```
