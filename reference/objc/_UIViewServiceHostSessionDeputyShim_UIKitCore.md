# `_UIViewServiceHostSessionDeputyShim`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewServiceHostSessionDelegate`
- 11 instance variables, 6 properties, 17 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSError" _lock_terminationError;
@? _lock_terminationHandler;
AB _lock_isTerminated;
@"_UIAsyncInvocation" _terminateInvocation;
@? _lock_connectionHandler;
@"_UIAsyncInvocation" _cancellationInvocation;
@"NSString" _loggingIdentifier;
@"NSArray" _deputyInterfaces;
@"_UIViewServiceHostSession" _session;
@"NSXPCConnection" _serviceConnection;
```

## Properties

```
@property (Ti,R,N) servicePID;
@property (T{?=[8I]},R,N) serviceAuditToken;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIViewServiceHostSessionDeputyShim initialize];
+[_UIViewServiceHostSessionDeputyShim connectToViewService:appBundleViewServiceBundleIdentifier:deputyInterfaces:connectionHandler:];
```

## Instance methods

```
-[_UIViewServiceHostSessionDeputyShim _objc_initiateDealloc];
-[_UIViewServiceHostSessionDeputyShim debugDescription];
-[_UIViewServiceHostSessionDeputyShim dealloc];
-[_UIViewServiceHostSessionDeputyShim _viewServiceHostSessionDidConnectToClient:];
-[_UIViewServiceHostSessionDeputyShim succinctDescription];
-[_UIViewServiceHostSessionDeputyShim disconnect];
-[_UIViewServiceHostSessionDeputyShim setTerminationHandler:];
-[_UIViewServiceHostSessionDeputyShim description];
-[_UIViewServiceHostSessionDeputyShim appendDescriptionToStream:];
-[_UIViewServiceHostSessionDeputyShim _viewServiceHostSessionDidInvalidate:withError:];
-[_UIViewServiceHostSessionDeputyShim serviceAuditToken];
-[_UIViewServiceHostSessionDeputyShim callConnectionHandlerWithError:];
-[_UIViewServiceHostSessionDeputyShim _terminateUnconditionallyThen:];
-[_UIViewServiceHostSessionDeputyShim _terminateWithError:];
-[_UIViewServiceHostSessionDeputyShim connectToDeputyWithInterface:fromExportedHostingObject:connectionHandler:];
-[_UIViewServiceHostSessionDeputyShim createSessionForService:appBundleViewServiceBundleIdentifier:];
-[_UIViewServiceHostSessionDeputyShim servicePID];
```
