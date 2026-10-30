# `_UIFocusTreeLockItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _lockCallStackSymbols;
@"NSMutableArray" _unlockCallStackSymbols;
B _didSoftAssert;
B _didCleanup;
@"<UIFocusEnvironment>" _unsafeEnvironment;
@? _finalUnlockHandler;
@"<UIFocusEnvironment>" _environment;
@"NSString" _environmentDescription;
Q _lockCount;
d _lockTime;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",R,W,N,V_environment) environment;
@property (T@"NSString",R,N,V_environmentDescription) environmentDescription;
@property (TQ,R,N,V_lockCount) lockCount;
@property (Td,R,N,V_lockTime) lockTime;
@property (T@"NSArray",R,N,V_lockCallStackSymbols) lockCallStackSymbols;
@property (T@"NSArray",R,N,V_unlockCallStackSymbols) unlockCallStackSymbols;
```

## Instance methods

```
-[_UIFocusTreeLockItem validate];
-[_UIFocusTreeLockItem dealloc];
-[_UIFocusTreeLockItem description];
-[_UIFocusTreeLockItem _cleanup:];
-[_UIFocusTreeLockItem lock];
-[_UIFocusTreeLockItem unlock];
-[_UIFocusTreeLockItem environment];
-[_UIFocusTreeLockItem environmentDescription];
-[_UIFocusTreeLockItem initWithEnvironment:finalUnlockHandler:];
-[_UIFocusTreeLockItem lockCallStackSymbols];
-[_UIFocusTreeLockItem lockCount];
-[_UIFocusTreeLockItem lockTime];
-[_UIFocusTreeLockItem unlockCallStackSymbols];
```
