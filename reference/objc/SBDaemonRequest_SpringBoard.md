# `SBDaemonRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@? _enabler;
@? _disabler;
```

## Properties

```
@property (T@?,C,N,V_enabler) enabler;
@property (T@?,C,N,V_disabler) disabler;
```

## Class methods

```
+[SBDaemonRequest requestWithEnabler:disabler:];
```

## Instance methods

```
-[SBDaemonRequest enabler];
-[SBDaemonRequest disabler];
-[SBDaemonRequest dispatchDisablerOnQueue:];
-[SBDaemonRequest dispatchEnablerOnQueue:];
-[SBDaemonRequest setDisabler:];
-[SBDaemonRequest setEnabler:];
```
