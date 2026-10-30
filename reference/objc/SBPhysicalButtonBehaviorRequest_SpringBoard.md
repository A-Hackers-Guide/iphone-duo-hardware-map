# `SBPhysicalButtonBehaviorRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
Q _physicalButtonBehavior;
Q _identifier;
Q _generation;
@"FBScene" _scene;
@"BSAuditToken" _requestingProcessAuditToken;
```

## Properties

```
@property (TQ,R,N,V_physicalButtonBehavior) physicalButtonBehavior;
@property (TQ,R,N,V_identifier) identifier;
@property (TQ,R,N,V_generation) generation;
@property (T@"FBScene",R,W,N,V_scene) scene;
@property (T@"BSAuditToken",R,N,V_requestingProcessAuditToken) requestingProcessAuditToken;
```

## Instance methods

```
-[SBPhysicalButtonBehaviorRequest identifier];
-[SBPhysicalButtonBehaviorRequest generation];
-[SBPhysicalButtonBehaviorRequest scene];
-[SBPhysicalButtonBehaviorRequest isEqual:];
-[SBPhysicalButtonBehaviorRequest initWithPhysicalButtonConfiguration:generation:identifier:scene:];
-[SBPhysicalButtonBehaviorRequest physicalButtonBehavior];
-[SBPhysicalButtonBehaviorRequest requestingProcessAuditToken];
```
