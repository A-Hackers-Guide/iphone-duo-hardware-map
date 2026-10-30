# `MicActivityServiceDelegate`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MicActivityClientProtocol`, `SelfConfiguringClient`, `DSPPropertySupervisor`, `NSXPCProcessConnectionHandler`
- 2 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
{MicActivityContext="_vptr$DSPProcessorPropertyHandler"^^?"mPropertySet"@"<DSPProcessorPropertySet>""mClientConnections"{unique_ptr<MicActivityClientConnections, std::default_delete<MicActivityClientConnections>>=""{?="__ptr_"^{MicActivityClientConnections}}}} mMicActivityContext;
{SelfConfigureGateway="mHandler"@"<SelfConfigureHandler>""mSelfConfigureHandleSet"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}} mSelfConfigureGateway;
```

## Instance methods

```
-[MicActivityServiceDelegate propertyChanged:];
-[MicActivityServiceDelegate processArrived:];
-[MicActivityServiceDelegate clientArrived:andEndpoint:];
-[MicActivityServiceDelegate clientDisappeared:];
-[MicActivityServiceDelegate clientSubmittedReferenceDevice:andDeviceUID:];
-[MicActivityServiceDelegate disableMicrophoneActivityDetection:];
-[MicActivityServiceDelegate enableMicrophoneActivityDetection:];
-[MicActivityServiceDelegate listenForMicrophoneActivity:reply:];
-[MicActivityServiceDelegate processDisappeared:];
-[MicActivityServiceDelegate selfConfigureMAD];
-[MicActivityServiceDelegate setDSPProcessorPropertySet:];
-[MicActivityServiceDelegate setSelfConfigureHandler:];
-[MicActivityServiceDelegate stopListeningForMicrophoneActivity:];
-[MicActivityServiceDelegate submitReferenceStreamUID:withReply:];
```
