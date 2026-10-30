# `_MLServer`

- Image: [`/System/Library/PrivateFrameworks/RemoteCoreML.framework/RemoteCoreML`](../userland/System__Library__PrivateFrameworks__RemoteCoreML.framework__RemoteCoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"_MLNetworking" _nwObj;
@"_MLNetworkOptions" _nwOptions;
@"_MLNetworkPacket" _packet;
@? _loadFunction;
@? _predictFunction;
@? _unLoadFunction;
@? _textFunction;
@"NSObject<OS_dispatch_queue>" _q;
```

## Properties

```
@property (T@"_MLNetworking",R,N,V_nwObj) nwObj;
@property (T@"_MLNetworkOptions",R,N,V_nwOptions) nwOptions;
@property (T@"_MLNetworkPacket",R,N,V_packet) packet;
@property (T@?,C,N,V_loadFunction) loadFunction;
@property (T@?,C,N,V_predictFunction) predictFunction;
@property (T@?,C,N,V_unLoadFunction) unLoadFunction;
@property (T@?,C,N,V_textFunction) textFunction;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_q) q;
```

## Instance methods

```
-[_MLServer stop];
-[_MLServer start];
-[_MLServer initWithOptions:];
-[_MLServer q];
-[_MLServer packet];
-[_MLServer predictFunction];
-[_MLServer setTextCommand:];
-[_MLServer setLoadCommand:];
-[_MLServer doReceive:context:isComplete:error:];
-[_MLServer loadFunction];
-[_MLServer nwObj];
-[_MLServer nwOptions];
-[_MLServer setLoadFunction:];
-[_MLServer setPredictCommand:];
-[_MLServer setPredictFunction:];
-[_MLServer setTextFunction:];
-[_MLServer setUnLoadCommand:];
-[_MLServer setUnLoadFunction:];
-[_MLServer textFunction];
-[_MLServer unLoadFunction];
```
