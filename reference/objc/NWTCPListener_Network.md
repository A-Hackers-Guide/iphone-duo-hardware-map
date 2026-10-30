# `NWTCPListener`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NWEndpoint" _localEndpoint;
@"NSError" _error;
@"NSObject<OS_nw_listener>" _internalListener;
@"NWParameters" _parameters;
@"NWEndpoint" _endpoint;
@"NSString" _launchdKey;
@"<NWTCPListenerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSObject<OS_nw_listener>",&,V_internalListener) internalListener;
@property (T@"NWParameters",&,V_parameters) parameters;
@property (T@"NWEndpoint",&,V_endpoint) endpoint;
@property (T@"NSString",&,V_launchdKey) launchdKey;
@property (T@"<NWTCPListenerDelegate>",W,V_delegate) delegate;
@property (T@"NSError",&,V_error) error;
@property (T@"NWEndpoint",&,V_localEndpoint) localEndpoint;
```

## Instance methods

```
-[NWTCPListener handleError:];
-[NWTCPListener setError:];
-[NWTCPListener localEndpoint];
-[NWTCPListener parameters];
-[NWTCPListener setLocalEndpoint:];
-[NWTCPListener setEndpoint:];
-[NWTCPListener setParameters:];
-[NWTCPListener endpoint];
-[NWTCPListener error];
-[NWTCPListener setDelegate:];
-[NWTCPListener delegate];
-[NWTCPListener startInternal];
-[NWTCPListener initWithParameters:delegate:];
-[NWTCPListener cancel];
-[NWTCPListener handleNewConnection:];
-[NWTCPListener initWithBonjourServiceEndpoint:parameters:delegate:];
-[NWTCPListener initWithLaunchdKey:parameters:delegate:];
-[NWTCPListener initWithParameters:delegate:launchdKey:bonjourEndpoint:];
-[NWTCPListener internalListener];
-[NWTCPListener launchdKey];
-[NWTCPListener setInternalListener:];
-[NWTCPListener setLaunchdKey:];
```
