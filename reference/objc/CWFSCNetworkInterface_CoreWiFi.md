# `CWFSCNetworkInterface`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{__SCDynamicStore=} _storeRef;
B _isMonitoringEvents;
@"NSString" _interfaceName;
@"NSString" _hardwareAddress;
@? _eventHandler;
```

## Properties

```
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (T@"NSString",R,C,N,V_hardwareAddress) hardwareAddress;
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFSCNetworkInterface IPv4SubnetMasks];
-[CWFSCNetworkInterface IPv4Addresses];
-[CWFSCNetworkInterface __startEventMonitoring];
-[CWFSCNetworkInterface IPv6Addresses];
-[CWFSCNetworkInterface eventHandler];
-[CWFSCNetworkInterface setEventHandler:];
-[CWFSCNetworkInterface startEventMonitoring];
-[CWFSCNetworkInterface __IPv4StateConfig];
-[CWFSCNetworkInterface isMonitoringEvents];
-[CWFSCNetworkInterface init];
-[CWFSCNetworkInterface dealloc];
-[CWFSCNetworkInterface stopEventMonitoring];
-[CWFSCNetworkInterface interfaceName];
-[CWFSCNetworkInterface IPv6PrefixLengths];
-[CWFSCNetworkInterface initWithInterfaceName:];
-[CWFSCNetworkInterface __IPv6StateConfig];
-[CWFSCNetworkInterface IPv6Flags];
-[CWFSCNetworkInterface hardwareAddress];
-[CWFSCNetworkInterface IPv4BroadcastAddresses];
-[CWFSCNetworkInterface __linkStateConfig];
-[CWFSCNetworkInterface __networkInterfaceHardwareAddress];
-[CWFSCNetworkInterface airPortSetupConfiguration];
-[CWFSCNetworkInterface airPortStateConfiguration];
-[CWFSCNetworkInterface isLinkActive];
```
