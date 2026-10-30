# `UIAvoidanceClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIAvoidanceObject`
- 0 instance variables, 4 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",R,N) blockades;
@property (T@"<UIAvoidanceClientDelegate>",&,N) avoidanceController;
@property (T@"<UIAvoidanceClientApplicator>",&,N) avoidanceApplicator;
@property (T@"NSValue",&,N) avoidancePosition;
```

## Instance methods

```
-[UIAvoidanceClient addBlockadeWithIdentifier:];
-[UIAvoidanceClient avoidanceApplicator];
-[UIAvoidanceClient avoidanceController];
-[UIAvoidanceClient avoidancePosition];
-[UIAvoidanceClient blockades];
-[UIAvoidanceClient removeBlockadeWithIdentifier:];
-[UIAvoidanceClient setAvoidanceApplicator:];
-[UIAvoidanceClient setAvoidanceController:];
-[UIAvoidanceClient setAvoidancePosition:];
```
