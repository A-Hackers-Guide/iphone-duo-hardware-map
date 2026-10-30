# `SBLockScreenActionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _actionProviders;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_actionProviders) actionProviders;
```

## Instance methods

```
-[SBLockScreenActionManager init];
-[SBLockScreenActionManager actionProviders];
-[SBLockScreenActionManager runUnlockAction];
-[SBLockScreenActionManager _clearActionOnAllProviders];
-[SBLockScreenActionManager currentLockScreenActionContext];
-[SBLockScreenActionManager currentLockScreenActionContextActionSource:];
-[SBLockScreenActionManager registerLockScreenActionProvider:forSource:];
-[SBLockScreenActionManager setActionProviders:];
```
