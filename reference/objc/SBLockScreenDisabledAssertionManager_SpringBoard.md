# `SBLockScreenDisabledAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAutoUnlockRule`
- 1 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _disableLockScreenIfPossibleAssertions;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenDisabledAssertionManager init];
-[SBLockScreenDisabledAssertionManager addLockScreenDisableAssertion:];
-[SBLockScreenDisabledAssertionManager shouldAutoUnlockForSource:];
-[SBLockScreenDisabledAssertionManager description];
-[SBLockScreenDisabledAssertionManager removeLockScreenDisableAssertion:];
-[SBLockScreenDisabledAssertionManager isLockScreenDisabledForAssertion];
```
