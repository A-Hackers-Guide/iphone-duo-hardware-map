# `IsolatedCoreAudioUseCaseConnection`

- Image: [`/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`](../userland/System__Library__PrivateFrameworks__IsolatedCoreAudioClient.framework__IsolatedCoreAudioClient.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
I useCaseID;
i _pid;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (Ti,N,V_pid) pid;
@property (TI,N,VuseCaseID) useCaseID;
```

## Instance methods

```
-[IsolatedCoreAudioUseCaseConnection setPid:];
-[IsolatedCoreAudioUseCaseConnection initWithConnection:];
-[IsolatedCoreAudioUseCaseConnection invalidate];
-[IsolatedCoreAudioUseCaseConnection pid];
-[IsolatedCoreAudioUseCaseConnection connection];
-[IsolatedCoreAudioUseCaseConnection setConnection:];
-[IsolatedCoreAudioUseCaseConnection useCaseID];
-[IsolatedCoreAudioUseCaseConnection setUseCaseID:];
```
