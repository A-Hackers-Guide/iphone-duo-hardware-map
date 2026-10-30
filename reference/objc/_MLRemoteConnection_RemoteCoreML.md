# `_MLRemoteConnection`

- Image: [`/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`](../userland/System__Library__PrivateFrameworks__RemoteCoreML.framework__RemoteCoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_connection>" _connection;
@"_MLNetworking" _nwObj;
@"_MLNetworkOptions" _nwOptions;
@"_MLNetworkPacket" _packet;
@"NSMutableData" _outputResult;
Q _jobCount;
@"NSObject<OS_dispatch_semaphore>" _semaphore;
@"NSObject<OS_dispatch_queue>" _q;
```

## Properties

```
@property (T@"NSObject<OS_nw_connection>",R,N,V_connection) connection;
@property (T@"_MLNetworking",R,N,V_nwObj) nwObj;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"_MLNetworkPacket",R,N,V_packet) packet;
@property (T@"NSMutableData",&,N,V_outputResult) outputResult;
@property (TQ,R,N,V_jobCount) jobCount;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_semaphore) semaphore;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
```

## Instance methods

```
-[_MLRemoteConnection jobCount];
-[_MLRemoteConnection semaphore];
-[_MLRemoteConnection initWithOptions:];
-[_MLRemoteConnection connection];
-[_MLRemoteConnection q];
-[_MLRemoteConnection loadFromURL:options:error:];
-[_MLRemoteConnection outputResult];
-[_MLRemoteConnection packet];
-[_MLRemoteConnection doReceive:context:isComplete:error:];
-[_MLRemoteConnection nwObj];
-[_MLRemoteConnection nwOptions];
-[_MLRemoteConnection predictionFromURL:features:output:options:error:];
-[_MLRemoteConnection send:options:];
-[_MLRemoteConnection sendDataAndWaitForAcknowledgementOrTimeout:];
-[_MLRemoteConnection setOutputResult:];
-[_MLRemoteConnection unloadFromURL:options:error:];
```
