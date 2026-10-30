# `SBDraggingSystemManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDraggingSystemMonitorDelegate`
- 4 instance variables, 4 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"UIDraggingSystemSession" _currentSession;
@"<BSInvalidatable>" _routingKeysAssertion;
@"NSHashTable" _observers;
@"NSMapTable" _commandeerReasons;
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
+[SBDraggingSystemManager sharedInstance];
```

## Instance methods

```
-[SBDraggingSystemManager removeObserver:];
-[SBDraggingSystemManager addObserver:];
-[SBDraggingSystemManager dragSessionDidBegin:];
-[SBDraggingSystemManager dragSessionDidEnd:];
-[SBDraggingSystemManager touchRoutingPolicyForBeginningDragSessionWithInfo:];
-[SBDraggingSystemManager _invalidateRoutingKeysAssertion];
-[SBDraggingSystemManager _acquireRoutingKeysAssertion];
-[SBDraggingSystemManager cancelActiveDraggingSystemSession];
-[SBDraggingSystemManager setCommandeered:forDraggingSystemSession:forReason:];
-[SBDraggingSystemManager setCommandeered:forDropSession:forReason:];
```
