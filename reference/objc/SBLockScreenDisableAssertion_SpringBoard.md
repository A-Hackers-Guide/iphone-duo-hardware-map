# `SBLockScreenDisableAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUILockScreenDisableAssertion`
- 3 instance variables, 0 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"SBFAuthenticationAssertion" _disableLockAssertion;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
```

## Class methods

```
+[SBLockScreenDisableAssertion initialize];
```

## Instance methods

```
-[SBLockScreenDisableAssertion dealloc];
-[SBLockScreenDisableAssertion invalidate];
-[SBLockScreenDisableAssertion description];
-[SBLockScreenDisableAssertion initWithIdentifier:];
-[SBLockScreenDisableAssertion initWithIdentifier:lockScreenCoordinator:];
```
