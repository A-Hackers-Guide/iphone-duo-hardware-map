# `WiFiRemoteClientCountryCodeMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiRemoteClientCountryCodeMonitorXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 2 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@? _setCountryCodeHandler;
```

## Properties

```
@property (T@?,C,N,V_setCountryCodeHandler) setCountryCodeHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiRemoteClientCountryCodeMonitor beginMonitoring];
-[WiFiRemoteClientCountryCodeMonitor startConnectionUsingProxy:completionHandler:];
-[WiFiRemoteClientCountryCodeMonitor init];
-[WiFiRemoteClientCountryCodeMonitor exportedInterface];
-[WiFiRemoteClientCountryCodeMonitor endMonitoring];
-[WiFiRemoteClientCountryCodeMonitor exportedObject];
-[WiFiRemoteClientCountryCodeMonitor setCountryCode:];
-[WiFiRemoteClientCountryCodeMonitor setCountryCodeHandler];
-[WiFiRemoteClientCountryCodeMonitor setSetCountryCodeHandler:];
```
