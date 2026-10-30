# `NWUDPListener`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NWEndpoint" _localEndpoint;
@"NSError" _error;
@"NSObject<OS_nw_listener>" _internalListener;
@"NWParameters" _parameters;
@"NWEndpoint" _endpoint;
@"<NWUDPListenerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSObject<OS_nw_listener>",&,V_internalListener) internalListener;
@property (T@"NWParameters",&,V_parameters) parameters;
@property (T@"NWEndpoint",&,V_endpoint) endpoint;
@property (T@"<NWUDPListenerDelegate>",W,V_delegate) delegate;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NWEndpoint",&,N,V_localEndpoint) localEndpoint;
```

## Instance methods

```
-[NWUDPListener handleError:];
-[NWUDPListener setError:];
-[NWUDPListener localEndpoint];
-[NWUDPListener parameters];
-[NWUDPListener setLocalEndpoint:];
-[NWUDPListener setEndpoint:];
-[NWUDPListener setParameters:];
-[NWUDPListener endpoint];
-[NWUDPListener error];
-[NWUDPListener setDelegate:];
-[NWUDPListener delegate];
-[NWUDPListener initWithParameters:delegate:];
-[NWUDPListener handleConnection:];
-[NWUDPListener internalListener];
-[NWUDPListener setInternalListener:];
```
