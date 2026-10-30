# `_UIFenceTask`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
Q _identifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
@"BKSProcessAssertion" _assertion;
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
+[_UIFenceTask _processRequiresFenceAssertions];
```

## Instance methods

```
-[_UIFenceTask init];
-[_UIFenceTask dealloc];
-[_UIFenceTask invalidate];
```
