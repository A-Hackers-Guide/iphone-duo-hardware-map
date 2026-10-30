# `_UIActionWhenIdle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSInvocation" _invocation;
```

## Properties

```
@property (T@"NSInvocation",&,N,V_invocation) invocation;
```

## Class methods

```
+[_UIActionWhenIdle actionWhenIdleWithTarget:selector:object:];
```

## Instance methods

```
-[_UIActionWhenIdle invoke];
-[_UIActionWhenIdle setInvocation:];
-[_UIActionWhenIdle initWithInvocation:];
-[_UIActionWhenIdle addObserverToRunLoop];
-[_UIActionWhenIdle invalidate];
-[_UIActionWhenIdle invocation];
-[_UIActionWhenIdle isValid];
-[_UIActionWhenIdle initWithTarget:selector:object:];
```
