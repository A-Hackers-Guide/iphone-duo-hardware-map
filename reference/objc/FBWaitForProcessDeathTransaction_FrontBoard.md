# `FBWaitForProcessDeathTransaction`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBTransaction`
- Protocols: `FBProcessManagerObserver`
- 3 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FBProcess" _process;
d _timeout;
@"BSAbsoluteMachTimer" _timer;
```

## Properties

```
@property (T@"FBProcess",R,N,V_process) process;
@property (Td,R,N,V_timeout) timeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBWaitForProcessDeathTransaction _canBeInterrupted];
-[FBWaitForProcessDeathTransaction _didComplete];
-[FBWaitForProcessDeathTransaction _begin];
-[FBWaitForProcessDeathTransaction _customizedDescriptionProperties];
-[FBWaitForProcessDeathTransaction processManager:didAddProcess:];
-[FBWaitForProcessDeathTransaction process];
-[FBWaitForProcessDeathTransaction timeout];
-[FBWaitForProcessDeathTransaction processManager:didRemoveProcess:];
-[FBWaitForProcessDeathTransaction initWithProcess:];
-[FBWaitForProcessDeathTransaction initWithProcess:timeout:];
```
