# `SBIndirectTouchLifecycleMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`
- 2 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"UIHoverGestureRecognizer",&,N,V_hoverGestureRecognizer) hoverGestureRecognizer;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIndirectTouchLifecycleMonitor setHoverGestureRecognizer:];
-[SBIndirectTouchLifecycleMonitor removeObserver:];
-[SBIndirectTouchLifecycleMonitor addObserver:];
-[SBIndirectTouchLifecycleMonitor initWithSystemGestureManager:];
-[SBIndirectTouchLifecycleMonitor setObservers:];
-[SBIndirectTouchLifecycleMonitor hoverGestureRecognizer];
-[SBIndirectTouchLifecycleMonitor observers];
-[SBIndirectTouchLifecycleMonitor handleHoverEvent:];
-[SBIndirectTouchLifecycleMonitor systemGestureHoverLocationInView:];
```
