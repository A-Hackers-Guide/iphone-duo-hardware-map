# `SBStatusBarContainer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 4 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIStatusBar" _statusBar;
@"SBStatusBarReusePool" _reusePool;
@"<SBStatusBarCoordinateSpaceProviding>" _coordinateSpaceProvider;
@"NSString" _reason;
```

## Properties

```
@property (T@"UIStatusBar",W,N,V_statusBar) statusBar;
@property (T@"SBStatusBarReusePool",W,N,V_reusePool) reusePool;
@property (T@"<SBStatusBarCoordinateSpaceProviding>",W,N,V_coordinateSpaceProvider) coordinateSpaceProvider;
@property (T@"NSString",&,N,V_reason) reason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStatusBarContainer statusBar];
-[SBStatusBarContainer setStatusBar:];
-[SBStatusBarContainer succinctDescriptionBuilder];
-[SBStatusBarContainer dealloc];
-[SBStatusBarContainer reusePool];
-[SBStatusBarContainer setReason:];
-[SBStatusBarContainer descriptionWithMultilinePrefix:];
-[SBStatusBarContainer succinctDescription];
-[SBStatusBarContainer description];
-[SBStatusBarContainer reason];
-[SBStatusBarContainer descriptionBuilderWithMultilinePrefix:];
-[SBStatusBarContainer coordinateSpaceProvider];
-[SBStatusBarContainer setCoordinateSpaceProvider:];
-[SBStatusBarContainer setReusePool:];
```
