# `_UIViewServiceLegacyClientSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewServiceDeputyManagerDelegate`
- 7 instance variables, 7 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSXPCConnection" _connection;
@"_UIViewServiceSessionManager" _manager;
@"_UIViewServiceDeputyManager" _deputyManager;
@"_UIAsyncInvocation" _invalidationInvocation;
@? _terminationHandler;
@"NSUUID" _uniqueIdentifier;
```

## Properties

```
@property (T@?,C,N,V_terminationHandler) terminationHandler;
@property (T@"_UIViewServiceSessionManager",R,W,V_manager) manager;
@property (T@"NSUUID",R,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewServiceLegacyClientSession initialize];
+[_UIViewServiceLegacyClientSession sessionWithConnection:manager:];
```

## Instance methods

```
-[_UIViewServiceLegacyClientSession _objc_initiateDealloc];
-[_UIViewServiceLegacyClientSession terminationHandler];
-[_UIViewServiceLegacyClientSession dealloc];
-[_UIViewServiceLegacyClientSession manager];
-[_UIViewServiceLegacyClientSession uniqueIdentifier];
-[_UIViewServiceLegacyClientSession setTerminationHandler:];
-[_UIViewServiceLegacyClientSession _invalidateUnconditionallyThen:];
-[_UIViewServiceLegacyClientSession _registerSessionForDefaultDeputies];
-[_UIViewServiceLegacyClientSession deputy:didFailWithError:];
-[_UIViewServiceLegacyClientSession deputyManager:didUpdateExportedInterface:];
-[_UIViewServiceLegacyClientSession registerDeputyClass:withConnectionHandler:];
-[_UIViewServiceLegacyClientSession unregisterDeputyClass:];
-[_UIViewServiceLegacyClientSession viewControllerOperator:didCreateServiceViewControllerOfClass:];
```
