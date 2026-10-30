# `_PLDisplayCBPropertyObserver`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBTargetedPropertyObserver`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _forDisplayX;
@"PLDisplayAgent" _agent;
@"NSSet" _properties;
@"NSObject<OS_dispatch_queue>" _notifyQueue;
@"CBHandle" _handle;
```

## Properties

```
@property (T@"PLDisplayAgent",W,N,V_agent) agent;
@property (T@"NSSet",&,N,V_properties) properties;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_notifyQueue) notifyQueue;
@property (T@"CBHandle",&,N,V_handle) handle;
@property (TB,N,V_forDisplayX) forDisplayX;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_PLDisplayCBPropertyObserver properties];
-[_PLDisplayCBPropertyObserver agent];
-[_PLDisplayCBPropertyObserver setProperties:];
-[_PLDisplayCBPropertyObserver notifyQueue];
-[_PLDisplayCBPropertyObserver handle];
-[_PLDisplayCBPropertyObserver setAgent:];
-[_PLDisplayCBPropertyObserver setHandle:];
-[_PLDisplayCBPropertyObserver setNotifyQueue:];
-[_PLDisplayCBPropertyObserver observeValue:forKey:andHandle:withContext:];
-[_PLDisplayCBPropertyObserver setForDisplayX:];
-[_PLDisplayCBPropertyObserver forDisplayX];
-[_PLDisplayCBPropertyObserver initWithAgent:properties:];
```
