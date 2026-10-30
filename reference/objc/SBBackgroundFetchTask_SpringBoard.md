# `SBBackgroundFetchTask`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"FBSApplicationInfo" _appInfo;
i _sequenceNumber;
@"RBSAssertion" _lock_assertion;
@? _lock_completionHandler;
B _lock_finished;
```

## Class methods

```
+[SBBackgroundFetchTask _nextSequenceNumber];
```

## Instance methods

```
-[SBBackgroundFetchTask dealloc];
-[SBBackgroundFetchTask execute];
-[SBBackgroundFetchTask description];
```
