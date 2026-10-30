# `IsolatedCoreAudioXPCService`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IsolatedCoreAudioClientNSXPCListenerDelegate`
- Protocols: `IsolatedCoreAudioServerProtocol`
- 1 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<ServerSideAudioSwitchboard>="__ptr_"^{ServerSideAudioSwitchboard}"__cntrl_"^{__shared_weak_count}} _mServerSideSwitchboard;
```

## Properties

```
@property (T{shared_ptr<ServerSideAudioSwitchboard>=^{ServerSideAudioSwitchboard}^{__shared_weak_count}},N,V_mServerSideSwitchboard) mServerSideSwitchboard;
```

## Instance methods

```
-[IsolatedCoreAudioXPCService init];
-[IsolatedCoreAudioXPCService checkInForIsolatedAudioSharedResources:with:];
-[IsolatedCoreAudioXPCService checkOutForIsolatedAudioSharedResources:];
-[IsolatedCoreAudioXPCService getWorkgroupForIsolatedAudio:with:];
-[IsolatedCoreAudioXPCService initWithClientReaper:];
-[IsolatedCoreAudioXPCService mServerSideSwitchboard];
-[IsolatedCoreAudioXPCService setMServerSideSwitchboard:];
-[IsolatedCoreAudioXPCService startIsolatedAudioForUseCase:atTime:with:];
-[IsolatedCoreAudioXPCService startIsolatedAudioForUseCase:with:];
-[IsolatedCoreAudioXPCService stopIsolatedAudioForUseCase:with:];
```
