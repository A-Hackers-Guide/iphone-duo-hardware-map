# `FBProcessExecutionContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 17 instance variables, 17 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _waitForDebugger;
B _disableASLR;
B _checkForLeaks;
B _enableMTE;
B _forSceneActivation;
@"RBSProcessIdentity" _identity;
@"NSArray" _arguments;
@"NSDictionary" _environment;
@"NSURL" _standardOutputURL;
@"NSURL" _standardErrorURL;
@"OSLaunchdDeveloperToolsOptions" _developerToolsOptions;
q _launchIntent;
@"<FBProcessWatchdogProviding>" _watchdogProvider;
d _watchdogExtension;
@"NSString" _overrideExecutablePath;
@"FBSProcessExecutableSlice" _overrideExecutableSlice;
@? _completion;
```

## Properties

```
@property (T@"NSArray",C,N,V_arguments) arguments;
@property (T@"NSDictionary",C,N,V_environment) environment;
@property (T@"NSURL",&,N,V_standardOutputURL) standardOutputURL;
@property (T@"NSURL",&,N,V_standardErrorURL) standardErrorURL;
@property (TB,N,V_waitForDebugger) waitForDebugger;
@property (TB,N,V_disableASLR) disableASLR;
@property (TB,N,V_checkForLeaks) checkForLeaks;
@property (TB,N,V_enableMTE) enableMTE;
@property (T@"OSLaunchdDeveloperToolsOptions",C,N,V_developerToolsOptions) developerToolsOptions;
@property (TB,N,V_forSceneActivation) forSceneActivation;
@property (Tq,N,V_launchIntent) launchIntent;
@property (T@"<FBProcessWatchdogProviding>",&,N,V_watchdogProvider) watchdogProvider;
@property (Td,N,V_watchdogExtension) watchdogExtension;
@property (T@"NSString",C,N,V_overrideExecutablePath) overrideExecutablePath;
@property (T@"FBSProcessExecutableSlice",&,N,V_overrideExecutableSlice) overrideExecutableSlice;
@property (T@"RBSProcessIdentity",C,N,V_identity) identity;
@property (T@?,C,N,V_completion) completion;
```

## Instance methods

```
-[FBProcessExecutionContext setCompletion:];
-[FBProcessExecutionContext setOverrideExecutablePath:];
-[FBProcessExecutionContext setEnvironment:];
-[FBProcessExecutionContext completion];
-[FBProcessExecutionContext arguments];
-[FBProcessExecutionContext mutableCopyWithZone:];
-[FBProcessExecutionContext setWaitForDebugger:];
-[FBProcessExecutionContext setCheckForLeaks:];
-[FBProcessExecutionContext setWatchdogProvider:];
-[FBProcessExecutionContext overrideExecutablePath];
-[FBProcessExecutionContext overrideExecutableSlice];
-[FBProcessExecutionContext developerToolsOptions];
-[FBProcessExecutionContext setDisableASLR:];
-[FBProcessExecutionContext forSceneActivation];
-[FBProcessExecutionContext setIdentity:];
-[FBProcessExecutionContext setForSceneActivation:];
-[FBProcessExecutionContext standardErrorURL];
-[FBProcessExecutionContext standardOutputURL];
-[FBProcessExecutionContext initWithIdentity:];
-[FBProcessExecutionContext setArguments:];
-[FBProcessExecutionContext watchdogProvider];
-[FBProcessExecutionContext disableASLR];
-[FBProcessExecutionContext waitForDebugger];
-[FBProcessExecutionContext launchIntent];
-[FBProcessExecutionContext setStandardErrorURL:];
-[FBProcessExecutionContext setDeveloperToolsOptions:];
-[FBProcessExecutionContext identity];
-[FBProcessExecutionContext copyOrUpdateForSceneActivationWithSettings:];
-[FBProcessExecutionContext setStandardOutputURL:];
-[FBProcessExecutionContext setOverrideExecutableSlice:];
-[FBProcessExecutionContext watchdogExtension];
-[FBProcessExecutionContext setLaunchIntent:];
-[FBProcessExecutionContext copyWithZone:];
-[FBProcessExecutionContext checkForLeaks];
-[FBProcessExecutionContext environment];
-[FBProcessExecutionContext setWatchdogExtension:];
-[FBProcessExecutionContext _initWithExecutionContext:];
-[FBProcessExecutionContext enableMTE];
-[FBProcessExecutionContext setEnableMTE:];
```
