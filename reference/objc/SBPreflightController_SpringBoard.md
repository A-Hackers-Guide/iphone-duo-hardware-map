# `SBPreflightController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _scenesToCancelTokens;
@"NSMutableDictionary" _scenesToCompletionHandlers;
```

## Properties

```
@property (TB,R,N) isInPreflight;
```

## Instance methods

```
-[SBPreflightController init];
-[SBPreflightController description];
-[SBPreflightController isInPreflight];
-[SBPreflightController requiresPreflightForApplication:];
-[SBPreflightController callCompletionHandlersForScene:preflightResult:];
-[SBPreflightController preflightLaunchForScene:withCompletionHandler:];
-[SBPreflightController scene:completedPreflightWithError:];
```
