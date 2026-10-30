# `DSPController`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<HAL_DSP_Factory>" admFactory;
@"CoreAudioOrchestration_ADM_Loader" admLoader;
@"<HAL_DSP_IOProcessor>" dspIOProcessor;
{HAL_DSP_IOCallbacks="m_registerClientCallback"{function<void (unsigned int)>="__f_"{__value_func<void (unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}}"m_ioCallback"{function<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>="__f_"{__value_func<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>="__buf_"(type="__data"[24C])"__f_"^v}}"m_unregisterClientCallback"{function<void (unsigned int)>="__f_"{__value_func<void (unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}}"m_beginProcessingCallback"{function<void (unsigned int)>="__f_"{__value_func<void (unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}}"m_endProcessingCallback"{function<void (unsigned int)>="__f_"{__value_func<void (unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}}} admCallbacks;
@"<ADMConfigurationProtocol>" admConfigurator;
@"ADMDSPHostCallbacks" admHostCallbacks;
@"ADMDSPProcessorPropertySet" admPropertySet;
```

## Instance methods

```
-[DSPController dealloc];
-[DSPController negotiateConfigurationChange:error:];
-[DSPController getProcessorPropertySet];
-[DSPController startIO];
-[DSPController adaptToConfigurationChange:error:inputStreamIndicesInIOProc:outputStreamIndicesInIOProc:frameBufferSize:];
-[DSPController initWithBundleID:withLogger:andADMConfigurator:andHALDSPFactory:andHostCallbacks:];
-[DSPController stopIO];
```
