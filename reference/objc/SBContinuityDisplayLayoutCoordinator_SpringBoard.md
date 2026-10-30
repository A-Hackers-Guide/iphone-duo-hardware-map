# `SBContinuityDisplayLayoutCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 3 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayLayoutPublisher" _rootPublisher;
@"<BSInvalidatable>" _suppression;
@"BSZeroingWeakReference" _currentPublisher;
```

## Properties

```
@property (T@"FBSDisplayLayoutPublisher",R,N,V_rootPublisher) rootPublisher;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuityDisplayLayoutCoordinator dealloc];
-[SBContinuityDisplayLayoutCoordinator start];
-[SBContinuityDisplayLayoutCoordinator invalidate];
-[SBContinuityDisplayLayoutCoordinator activateForPublisher:];
-[SBContinuityDisplayLayoutCoordinator initWithRootPublisher:];
-[SBContinuityDisplayLayoutCoordinator rootPublisher];
```
