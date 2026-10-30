# `_NSCFServer`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _enableCoprocessorInterface;
q _type;
q _listenerPort;
@"NSString" _interface;
@"NSDictionary" _configuration;
@"NSNumber" _listenerID;
@"NSObject<OS_tcp_listener>" _listener;
```

## Properties

```
@property (Tq,V_type) type;
@property (Tq,V_listenerPort) listenerPort;
@property (T@"NSString",&,V_interface) interface;
@property (T@"NSDictionary",&,V_configuration) configuration;
@property (TB,GisCoprocessorInterfaceEnabled,V_enableCoprocessorInterface) enableCoprocessorInterface;
```

## Class methods

```
+[_NSCFServer stopAll];
+[_NSCFServer adressesForInterface:];
+[_NSCFServer startSocksServerWithPort:];
```

## Instance methods

```
-[_NSCFServer init];
-[_NSCFServer stop];
-[_NSCFServer initWithType:];
-[_NSCFServer dealloc];
-[_NSCFServer setConfiguration:];
-[_NSCFServer start];
-[_NSCFServer setInterface:];
-[_NSCFServer interface];
-[_NSCFServer configuration];
-[_NSCFServer setType:];
-[_NSCFServer type];
-[_NSCFServer initWithType:port:];
-[_NSCFServer initWithType:port:interface:];
-[_NSCFServer isCoprocessorInterfaceEnabled];
-[_NSCFServer listenerPort];
-[_NSCFServer setEnableCoprocessorInterface:];
-[_NSCFServer setListenerPort:];
```
