# `OrchestratorClientIOLapseHandler`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
I mDeviceID;
{unique_ptr<IOLapseHandler, std::default_delete<IOLapseHandler>>=""{?="__ptr_"^{IOLapseHandler}}} mLapseHandler;
```

## Instance methods

```
-[OrchestratorClientIOLapseHandler init];
-[OrchestratorClientIOLapseHandler installClientLapseHandler:data:];
-[OrchestratorClientIOLapseHandler createHALLapseEventListeners:];
-[OrchestratorClientIOLapseHandler destroyHALLapseEventListeners];
-[OrchestratorClientIOLapseHandler ioHasStartedOnDevice:];
```
