# `_UIRemoteViewControllerConnectionRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 0 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"_UIRemoteViewService" _service;
@? _handler;
@"NSString" _viewServiceBundleIdentifier;
@"NSString" _viewControllerClassName;
@"NSUUID" _contextToken;
@"UITraitCollection" _traits;
@"_UIRemoteViewControllerLegacyImpl" _legacyImpl;
# _remoteViewControllerClass;
@"<_UIViewServiceDeputyXPCInterface>" _serviceViewControllerDeputyInterface;
@"_UIAsyncInvocation" _cancelInvocationForCurrentOperation;
@"_UIRemoteViewControllerConnectionInfo" _connectionInfo;
@"NSObject<OS_dispatch_queue>" _queue;
B _isCancelledOrComplete;
@"NSError" _error;
@"_UIAsyncInvocation" _requestCancellationInvocation;
```

## Class methods

```
+[_UIRemoteViewControllerConnectionRequest __requestRemoteViewController:service:fromServiceWithBundleIdentifier:traitCollection:legacyImpl:serviceViewControllerDeputyInterface:connectionHandler:];
+[_UIRemoteViewControllerConnectionRequest requestViewController:fromServiceWithBundleIdentifier:traitCollection:legacyImpl:serviceViewControllerDeputyInterface:connectionHandler:];
+[_UIRemoteViewControllerConnectionRequest requestViewControllerWithService:traitCollection:legacyImpl:remoteViewControllerClass:serviceViewControllerDeputyInterface:connectionHandler:];
```

## Instance methods

```
-[_UIRemoteViewControllerConnectionRequest dealloc];
-[_UIRemoteViewControllerConnectionRequest _cancelWithError:];
-[_UIRemoteViewControllerConnectionRequest _connectToServiceViewController];
-[_UIRemoteViewControllerConnectionRequest _cancelUnconditionallyThen:];
-[_UIRemoteViewControllerConnectionRequest _connectToDeputyWithInterface:fromExportedHostingObject:successHandler:];
-[_UIRemoteViewControllerConnectionRequest _connectToPlugInKitService];
-[_UIRemoteViewControllerConnectionRequest _connectToTextEffectsOperator];
-[_UIRemoteViewControllerConnectionRequest _connectToViewControllerControlMessageDeputy];
-[_UIRemoteViewControllerConnectionRequest _connectToViewControllerOperator];
-[_UIRemoteViewControllerConnectionRequest _connectToViewService];
-[_UIRemoteViewControllerConnectionRequest _didFinishEstablishingConnection];
-[_UIRemoteViewControllerConnectionRequest _sendServiceTextEffectsRequest];
-[_UIRemoteViewControllerConnectionRequest _sendServiceViewControllerRequest];
```
