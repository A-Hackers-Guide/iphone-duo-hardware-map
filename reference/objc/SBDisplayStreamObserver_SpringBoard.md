# `SBDisplayStreamObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 7 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"SBStateDumpManager" _manager;
B _invalidated;
@"NSString" _domain;
@"CADisplay" _display;
@? _updateBlock;
```

## Properties

```
@property (T@"NSString",R,C,N,V_domain) domain;
@property (T@"CADisplay",R,N,V_display) display;
@property (T@?,R,C,N,V_updateBlock) updateBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayStreamObserver display];
-[SBDisplayStreamObserver domain];
-[SBDisplayStreamObserver updateBlock];
-[SBDisplayStreamObserver invalidate];
-[SBDisplayStreamObserver initWithDomain:display:block:manager:];
```
