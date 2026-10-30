# `SBAmbientChargerConnectionInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAccessoryConnectionInfoProviderObserver`
- 4 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBAccessoryConnectionInfoProvider" _accessoryConnectionInfoProvider;
@"NSString" _connectedChargerConnectionUUID;
@"<SBAmbientChargerConnectionInfoProviderDelegate>" _delegate;
@"NSString" _currentConnectedChargerId;
```

## Properties

```
@property (T@"NSString",C,N,S_setCurrentConnectedChargerId:,V_currentConnectedChargerId) currentConnectedChargerId;
@property (T@"<SBAmbientChargerConnectionInfoProviderDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisChargerConnected) chargerConnected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAmbientChargerConnectionInfoProvider accessoryConnectionInfoProvider:accessoryEndpointAttached:transportType:protocol:properties:forConnection:];
-[SBAmbientChargerConnectionInfoProvider initWithDelegate:];
-[SBAmbientChargerConnectionInfoProvider dealloc];
-[SBAmbientChargerConnectionInfoProvider setDelegate:];
-[SBAmbientChargerConnectionInfoProvider delegate];
-[SBAmbientChargerConnectionInfoProvider accessoryConnectionInfoProvider:accessoryEndpointDetached:forConnection:];
-[SBAmbientChargerConnectionInfoProvider _setCurrentConnectedChargerId:];
-[SBAmbientChargerConnectionInfoProvider currentConnectedChargerId];
-[SBAmbientChargerConnectionInfoProvider isChargerConnected];
```
