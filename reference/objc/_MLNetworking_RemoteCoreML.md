# `_MLNetworking`

- Image: [`/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`](../userland/System__Library__PrivateFrameworks__RemoteCoreML.framework__RemoteCoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isClient;
@"NSObject<OS_nw_connection>" _connection;
@"NSObject<OS_nw_listener>" _listener;
@"_MLNetworkOptions" _nwOptions;
@"NSObject<OS_nw_protocol_stack>" _protocol_stack;
@"NSObject<OS_nw_parameters>" _parameters;
@"NSObject<OS_os_log>" _logType;
@"NSObject<OS_dispatch_queue>" _q;
```

## Properties

```
@property (T@"NSObject<OS_nw_connection>",&,N,V_connection) connection;
@property (T@"NSObject<OS_nw_listener>",R,N,V_listener) listener;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"NSObject<OS_nw_protocol_stack>",R,N,V_protocol_stack) protocol_stack;
@property (T@"NSObject<OS_nw_parameters>",R,N,V_parameters) parameters;
@property (TB,R,N,V_isClient) isClient;
@property (T@"NSObject<OS_os_log>",R,N,V_logType) logType;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
```

## Instance methods

```
-[_MLNetworking parameters];
-[_MLNetworking stop];
-[_MLNetworking logType];
-[_MLNetworking listener];
-[_MLNetworking connection];
-[_MLNetworking setConnection:];
-[_MLNetworking isClient];
-[_MLNetworking startConnection];
-[_MLNetworking sendData:];
-[_MLNetworking q];
-[_MLNetworking initConnection:];
-[_MLNetworking receiveLoop:];
-[_MLNetworking setListenerReceiveDataCallBack:];
-[_MLNetworking initListener:];
-[_MLNetworking nwOptions];
-[_MLNetworking protocol_stack];
-[_MLNetworking restartConnection];
-[_MLNetworking setReceiveDataCallBack:];
```
