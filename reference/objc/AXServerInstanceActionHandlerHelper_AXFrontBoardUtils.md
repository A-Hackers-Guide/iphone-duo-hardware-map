# `AXServerInstanceActionHandlerHelper`

- Image: [`/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`](../userland/System__Library__PrivateFrameworks__AXFrontBoardUtils.framework__AXFrontBoardUtils.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _actionHandlers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionHandlersLock;
i _registrationMessageKey;
i _actionResultMessageKey;
```

## Properties

```
@property (Ti,R,N,V_registrationMessageKey) registrationMessageKey;
@property (Ti,R,N,V_actionResultMessageKey) actionResultMessageKey;
```

## Instance methods

```
-[AXServerInstanceActionHandlerHelper handleActionHandlerRegistrationMessage:];
-[AXServerInstanceActionHandlerHelper initWithRegistrationMessageKey:actionResultMessageKey:];
-[AXServerInstanceActionHandlerHelper notifyActionOccurredWithType:payload:];
-[AXServerInstanceActionHandlerHelper _addActionHandlerIfNeeded:forClientPort:];
-[AXServerInstanceActionHandlerHelper _removeActionHandler:];
-[AXServerInstanceActionHandlerHelper actionResultMessageKey];
-[AXServerInstanceActionHandlerHelper registrationMessageKey];
```
