# `CTConnectionPair`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
B fStarted;
@"NSObject<OS_dispatch_queue>" fQueue;
@"<CTConnectionPairDelegate>" fDelegate;
q fConnectionPairState;
@"NSObject<OS_nw_connection>" fConnection1;
@"NSObject<OS_nw_endpoint>" fEndpoint1;
@"NSObject<OS_nw_parameters>" fParameters1;
i fConnectionState1;
@"NSObject<OS_nw_connection>" fConnection2;
@"NSObject<OS_nw_endpoint>" fEndpoint2;
@"NSObject<OS_nw_parameters>" fParameters2;
i fConnectionState2;
```

## Instance methods

```
-[CTConnectionPair dealloc];
-[CTConnectionPair start];
-[CTConnectionPair connectionStateChanged:connectionId:];
-[CTConnectionPair initWithQueue:delegate:endpoint1:parameters1:endpoint2:parameter2:];
-[CTConnectionPair receiveData:];
-[CTConnectionPair sendData:usingConnection:completion:];
-[CTConnectionPair updatePairState:];
```
