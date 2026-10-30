# `CWFEAP8021X`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
^{__SCDynamicStore=} _storeRef;
B _isMonitoringEvents;
@"NSString" _interfaceName;
@? _eventHandler;
```

## Properties

```
@property (T@"NSString",R,C,N,V_interfaceName) interfaceName;
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFEAP8021X __startEventMonitoring];
-[CWFEAP8021X eventHandler];
-[CWFEAP8021X setEventHandler:];
-[CWFEAP8021X startEventMonitoring];
-[CWFEAP8021X isMonitoringEvents];
-[CWFEAP8021X init];
-[CWFEAP8021X dealloc];
-[CWFEAP8021X stopEventMonitoring];
-[CWFEAP8021X interfaceName];
-[CWFEAP8021X initWithInterfaceName:];
-[CWFEAP8021X clientStatus:];
-[CWFEAP8021X controlMode:];
-[CWFEAP8021X controlState:];
-[CWFEAP8021X supplicantState:];
```
