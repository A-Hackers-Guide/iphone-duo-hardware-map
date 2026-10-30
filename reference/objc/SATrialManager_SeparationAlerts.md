# `SATrialManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"TRIClient" _client;
@"NSMutableDictionary" _updateTokens;
@? _updateHandler;
```

## Properties

```
@property (T@"TRIClient",&,N,V_client) client;
@property (T@"NSMutableDictionary",&,N,V_updateTokens) updateTokens;
@property (T@?,C,N,V_updateHandler) updateHandler;
```

## Instance methods

```
-[SATrialManager updateHandler];
-[SATrialManager setUpdateHandler:];
-[SATrialManager init];
-[SATrialManager dealloc];
-[SATrialManager registerHandler:];
-[SATrialManager setClient:];
-[SATrialManager client];
-[SATrialManager configurationForNamespace:];
-[SATrialManager handleUpdateForNamespace:];
-[SATrialManager registerNamespace:];
-[SATrialManager setUpdateTokens:];
-[SATrialManager unregisterNamespace:];
-[SATrialManager updateTokens];
-[SATrialManager valueForFactor:inNamespace:];
```
