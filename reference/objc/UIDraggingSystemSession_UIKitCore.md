# `UIDraggingSystemSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _commandeered;
@"UIDraggingSystemSessionInfo" _info;
@"UIDraggingSystemTouchRoutingPolicy" _routingPolicy;
@"<_DUIServerSessionSystemApp>" _serverSession;
```

## Properties

```
@property (T@"UIDraggingSystemSessionInfo",&,N,V_info) info;
@property (T@"UIDraggingSystemTouchRoutingPolicy",&,N,V_routingPolicy) routingPolicy;
@property (T@"<_DUIServerSessionSystemApp>",&,N,G_serverSession,V_serverSession) serverSession;
@property (TB,N,GisCommandeered,V_commandeered) commandeered;
```

## Instance methods

```
-[UIDraggingSystemSession info];
-[UIDraggingSystemSession setInfo:];
-[UIDraggingSystemSession cancel];
-[UIDraggingSystemSession _indexOfDragItemInSession:];
-[UIDraggingSystemSession _serverSession];
-[UIDraggingSystemSession commandeerImmediately];
-[UIDraggingSystemSession isCommandeered];
-[UIDraggingSystemSession loadURLForItem:completion:];
-[UIDraggingSystemSession loadUserActivityForItem:completion:];
-[UIDraggingSystemSession requestDragContinuationEndpointWithCompletion:];
-[UIDraggingSystemSession routingPolicy];
-[UIDraggingSystemSession setCommandeered:];
-[UIDraggingSystemSession setRoutingPolicy:];
-[UIDraggingSystemSession setServerSession:];
```
