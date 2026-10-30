# `DSP_HAL_Mock_IOProcessor`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_IOProcessor`
- 5 instance variables, 9 properties, 21 instance methods, 0 class methods

## Instance variables

```
i _featureFlag;
^v _dspCallbacks;
@"<HAL_DSP_HostCallbacks>" _hostCallbacks;
@"DSP_HAL_Mock_PropertySet" _processorProperties;
{function<DSP_HAL_Mock_TestHooks ()>="__f_"{__value_func<DSP_HAL_Mock_TestHooks ()>="__buf_"(type="__data"[24C])"__f_"^v}} _testHookFetcher;
```

## Properties

```
@property (T^v,N,V_dspCallbacks) dspCallbacks;
@property (T@"<HAL_DSP_HostCallbacks>",&,N,V_hostCallbacks) hostCallbacks;
@property (Ti,N,V_featureFlag) featureFlag;
@property (T@"DSP_HAL_Mock_PropertySet",&,N,V_processorProperties) processorProperties;
@property (T{function<DSP_HAL_Mock_TestHooks ()>={__value_func<DSP_HAL_Mock_TestHooks ()>=(type=[24C])^v}},N,V_testHookFetcher) testHookFetcher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HAL_Mock_IOProcessor init];
-[DSP_HAL_Mock_IOProcessor dealloc];
-[DSP_HAL_Mock_IOProcessor negotiateConfigurationChange:error:];
-[DSP_HAL_Mock_IOProcessor adaptToConfigurationChange:withCallbacks:error:];
-[DSP_HAL_Mock_IOProcessor getProcessorPropertySet];
-[DSP_HAL_Mock_IOProcessor simulateConfigurationChange:error:];
-[DSP_HAL_Mock_IOProcessor featureFlag];
-[DSP_HAL_Mock_IOProcessor setFeatureFlag:];
-[DSP_HAL_Mock_IOProcessor testHookFetcher];
-[DSP_HAL_Mock_IOProcessor basic_negotiateConfigurationChange:error:];
-[DSP_HAL_Mock_IOProcessor callAdaptHook:];
-[DSP_HAL_Mock_IOProcessor callNegotiateHook:];
-[DSP_HAL_Mock_IOProcessor conference_negotiateConfigurationChange:error:];
-[DSP_HAL_Mock_IOProcessor dspCallbacks];
-[DSP_HAL_Mock_IOProcessor hostCallbacks];
-[DSP_HAL_Mock_IOProcessor processorProperties];
-[DSP_HAL_Mock_IOProcessor setDspCallbacks:];
-[DSP_HAL_Mock_IOProcessor setHostCallbacks:];
-[DSP_HAL_Mock_IOProcessor setProcessorProperties:];
-[DSP_HAL_Mock_IOProcessor setTestHookFetcher:];
-[DSP_HAL_Mock_IOProcessor spatial_negotiateConfigurationChange:error:];
```
