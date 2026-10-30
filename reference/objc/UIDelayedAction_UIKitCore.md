# `UIDelayedAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@ m_target;
: m_action;
@ m_userInfo;
d m_delay;
@"NSTimer" m_timer;
B m_canceled;
@"NSString" m_runLoopMode;
@"NSDate" m_startDate;
```

## Properties

```
@property (T@"NSDate",R,Vm_startDate) _startDate;
@property (TB,R,Vm_canceled) _canceled;
@property (T@,&,Vm_target) target;
@property (T@,&,Vm_userInfo) userInfo;
```

## Instance methods

```
-[UIDelayedAction touch];
-[UIDelayedAction init];
-[UIDelayedAction userInfo];
-[UIDelayedAction dealloc];
-[UIDelayedAction unschedule];
-[UIDelayedAction setUserInfo:];
-[UIDelayedAction scheduled];
-[UIDelayedAction delay];
-[UIDelayedAction setTarget:];
-[UIDelayedAction target];
-[UIDelayedAction timerFired:];
-[UIDelayedAction cancel];
-[UIDelayedAction touchWithDelay:];
-[UIDelayedAction _canceled];
-[UIDelayedAction _startDate];
-[UIDelayedAction initWithTarget:action:userInfo:delay:];
-[UIDelayedAction initWithTarget:action:userInfo:delay:mode:];
```
