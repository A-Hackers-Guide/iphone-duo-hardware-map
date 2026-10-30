# `SAUIElementViewProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SAElementViewProviding`, `SAUIElementLayoutAxisObserving`
- 0 instance variables, 4 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",R,N) leadingView;
@property (T@"UIView",R,N) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
```

## Instance methods

```
-[SAUIElementViewProviding minimalView];
-[SAUIElementViewProviding trailingView];
-[SAUIElementViewProviding leadingView];
-[SAUIElementViewProviding detachedMinimalView];
```
