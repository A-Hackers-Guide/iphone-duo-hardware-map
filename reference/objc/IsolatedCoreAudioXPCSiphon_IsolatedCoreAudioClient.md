# `IsolatedCoreAudioXPCSiphon`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IsolatedCoreAudioClientNSXPCListenerDelegate`
- Protocols: `IsolatedCoreAudioSiphonProtocol`
- 3 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _reverseConnections;
{shared_ptr<IsolatedCoreAudioSiphon>="__ptr_"^{IsolatedCoreAudioSiphon}"__cntrl_"^{__shared_weak_count}} _mSiphon;
{shared_ptr<SiphonClientMap>="__ptr_"^{SiphonClientMap}"__cntrl_"^{__shared_weak_count}} _mClientMap;
```

## Properties

```
@property (T{shared_ptr<IsolatedCoreAudioSiphon>=^{IsolatedCoreAudioSiphon}^{__shared_weak_count}},N,V_mSiphon) mSiphon;
@property (T{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}},N,V_mClientMap) mClientMap;
@property (T@"NSMutableSet",&,N,V_reverseConnections) reverseConnections;
```

## Class methods

```
+[IsolatedCoreAudioXPCSiphon initClientMap];
```

## Instance methods

```
-[IsolatedCoreAudioXPCSiphon init];
-[IsolatedCoreAudioXPCSiphon dealloc];
-[IsolatedCoreAudioXPCSiphon mSiphon];
-[IsolatedCoreAudioXPCSiphon connectToUseCase:endpoint:];
-[IsolatedCoreAudioXPCSiphon createClientReaper];
-[IsolatedCoreAudioXPCSiphon initWithClientMap:andServer:];
-[IsolatedCoreAudioXPCSiphon mClientMap];
-[IsolatedCoreAudioXPCSiphon requestAudio:atTime:atSample:with:];
-[IsolatedCoreAudioXPCSiphon reverseConnections];
-[IsolatedCoreAudioXPCSiphon setAudioAvailabilityCallback:usingXPC:with:];
-[IsolatedCoreAudioXPCSiphon setAudioLapseCallback:usingXPC:with:];
-[IsolatedCoreAudioXPCSiphon setMClientMap:];
-[IsolatedCoreAudioXPCSiphon setMSiphon:];
-[IsolatedCoreAudioXPCSiphon setReverseConnections:];
-[IsolatedCoreAudioXPCSiphon startIO:targetTime:with:];
-[IsolatedCoreAudioXPCSiphon startIO:with:];
-[IsolatedCoreAudioXPCSiphon stopIO:with:];
```
