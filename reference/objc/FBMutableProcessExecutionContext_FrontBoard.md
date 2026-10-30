# `FBMutableProcessExecutionContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBProcessExecutionContext`
- 0 instance variables, 15 properties, 1 instance methods, 0 class methods

## Properties

```
@property (T@"RBSProcessIdentity",C,D,N) identity;
@property (T@"NSArray",C,D,N) arguments;
@property (T@"NSDictionary",C,D,N) environment;
@property (T@"NSURL",&,D,N) standardOutputURL;
@property (T@"NSURL",&,D,N) standardErrorURL;
@property (TB,D,N) waitForDebugger;
@property (TB,D,N) disableASLR;
@property (TB,D,N) checkForLeaks;
@property (TB,D,N) enableMTE;
@property (T@"OSLaunchdDeveloperToolsOptions",C,D,N) developerToolsOptions;
@property (Tq,D,N) launchIntent;
@property (T@"<FBProcessWatchdogProviding>",&,D,N) watchdogProvider;
@property (T@"NSString",C,D,N) overrideExecutablePath;
@property (T@"FBSProcessExecutableSlice",&,D,N) overrideExecutableSlice;
@property (T@?,C,D,N) completion;
```

## Instance methods

```
-[FBMutableProcessExecutionContext copyWithZone:];
```
