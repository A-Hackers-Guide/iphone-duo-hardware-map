# `ACCNavigationProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation`](../userland/System__Library__PrivateFrameworks__AccessoryNavigation.framework__AccessoryNavigation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSString" _providerUID;
@"NSXPCConnection" _serverConnection;
@"<ACCNavigationXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
@"NSMutableArray" _delegates;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCNavigationXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"NSMutableArray",&,N,V_delegates) delegates;
@property (T@"NSString",&,N,V_providerUID) providerUID;
```

## Instance methods

```
-[ACCNavigationProvider setDelegates:];
-[ACCNavigationProvider delegates];
-[ACCNavigationProvider initWithDelegate:];
-[ACCNavigationProvider connectToServer];
-[ACCNavigationProvider setRemoteObject:];
-[ACCNavigationProvider serverConnection];
-[ACCNavigationProvider dealloc];
-[ACCNavigationProvider accessories];
-[ACCNavigationProvider providerUID];
-[ACCNavigationProvider remoteObject];
-[ACCNavigationProvider setAccessories:];
-[ACCNavigationProvider setServerConnection:];
-[ACCNavigationProvider setProviderUID:];
-[ACCNavigationProvider accessoryForUID:];
-[ACCNavigationProvider accessoryNavigationAttached:componentList:];
-[ACCNavigationProvider accessoryNavigationDetached:];
-[ACCNavigationProvider accessoryNavigationObjectDetection:componentIdList:updateInfo:];
-[ACCNavigationProvider accessoryNavigationStartRouteGuidance:componentIdList:options:];
-[ACCNavigationProvider accessoryNavigationStopRouteGuidance:componentIdList:];
-[ACCNavigationProvider delegatesImplementing:];
-[ACCNavigationProvider detachAllAccessories];
-[ACCNavigationProvider objectDetection:startComponentIdList:objectTypes:];
-[ACCNavigationProvider objectDetection:stopComponentIdList:];
-[ACCNavigationProvider routeGuidance:laneGuidanceInfo:componentIdList:];
-[ACCNavigationProvider routeGuidance:maneuverUpdateInfo:componentIdList:];
-[ACCNavigationProvider routeGuidance:updateInfo:componentIdList:];
```
