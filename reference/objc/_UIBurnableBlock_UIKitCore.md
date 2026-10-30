# `_UIBurnableBlock`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _timer;
@? _block;
```

## Instance methods

```
-[_UIBurnableBlock dealloc];
-[_UIBurnableBlock _cancelTimerIfNeeded];
-[_UIBurnableBlock initWithTimeout:block:defaultInputProvider:];
-[_UIBurnableBlock performWithInput:];
```
