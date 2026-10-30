# `SBAccessoryConnectionInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCConnectionInfoDelegateProtocol`
- 2 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"ACCConnectionInfo" _connectionInfo;
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAccessoryConnectionInfoProvider sharedInstance];
```

## Instance methods

```
-[SBAccessoryConnectionInfoProvider accessoryEndpointInfoPropertyChanged:properties:forConnection:];
-[SBAccessoryConnectionInfoProvider removeObserver:];
-[SBAccessoryConnectionInfoProvider init];
-[SBAccessoryConnectionInfoProvider dealloc];
-[SBAccessoryConnectionInfoProvider accessoryEndpointAttached:transportType:protocol:properties:forConnection:];
-[SBAccessoryConnectionInfoProvider addObserver:];
-[SBAccessoryConnectionInfoProvider accessoryConnectionType:];
-[SBAccessoryConnectionInfoProvider accessoryEndpointDetached:forConnection:];
-[SBAccessoryConnectionInfoProvider accessoryEndpointTransportType:connection:];
-[SBAccessoryConnectionInfoProvider accessoryInfoForEndpoint:connection:withReply:];
```
