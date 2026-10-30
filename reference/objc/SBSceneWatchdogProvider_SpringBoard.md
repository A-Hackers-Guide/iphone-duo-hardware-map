# `SBSceneWatchdogProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBProcessWatchdogProviding`
- 2 instance variables, 4 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"FBSProcessWatchdogPolicy" _explicitPolicy;
@"FBApplicationProcessWatchdogPolicy" _defaultProcessWatchdogProvider;
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
+[SBSceneWatchdogProvider defaultSceneWatchdogProvider];
+[SBSceneWatchdogProvider disabledSceneWatchdogProvider];
```

## Instance methods

```
-[SBSceneWatchdogProvider watchdogPolicyForProcess:eventContext:];
-[SBSceneWatchdogProvider initAsDisabled:];
-[SBSceneWatchdogProvider _scaleProvisions:byFactor:];
```
