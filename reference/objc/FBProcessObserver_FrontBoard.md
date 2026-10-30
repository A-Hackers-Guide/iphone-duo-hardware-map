# `FBProcessObserver`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessObserver`, `FBApplicationProcessObserver`
- 15 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<FBProcessObserver>" _observer;
Q _observerAddress;
# _observerClass;
B _supportsWillExit;
B _supportsDidExit;
B _supportsStateDidChange;
B _supportsApplicationDidExit;
B _supportsApplicationWillLaunch;
B _supportsApplicationDidLaunch;
B _supportsApplicationDebugState;
i _invalidated;
i _calledWillExit;
i _calledDidExit;
i _calledWillLaunch;
i _calledDidLaunch;
```

## Properties

```
@property (T@"<FBProcessObserver>",R,W,N,V_observer) observer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBProcessObserver observer];
-[FBProcessObserver applicationProcessDidExit:withContext:];
-[FBProcessObserver applicationProcessWillLaunch:];
-[FBProcessObserver process:stateDidChangeFromState:toState:];
-[FBProcessObserver invalidate];
-[FBProcessObserver processDidExit:];
-[FBProcessObserver initWithObserver:];
-[FBProcessObserver hash];
-[FBProcessObserver applicationProcessDebuggingStateDidChange:];
-[FBProcessObserver isEqual:];
-[FBProcessObserver applicationProcessDidLaunch:];
-[FBProcessObserver processWillExit:];
```
