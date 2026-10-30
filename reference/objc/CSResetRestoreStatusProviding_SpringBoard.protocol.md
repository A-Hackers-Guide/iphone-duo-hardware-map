# `CSResetRestoreStatusProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisRestoring) restoring;
@property (Tq,R,N) restoreState;
@property (TB,R,N,GisResetting) resetting;
@property (Tq,R,N) resetState;
```

## Instance methods

```
-[CSResetRestoreStatusProviding resetState];
-[CSResetRestoreStatusProviding isRestoring];
-[CSResetRestoreStatusProviding restoreState];
-[CSResetRestoreStatusProviding isResetting];
```
