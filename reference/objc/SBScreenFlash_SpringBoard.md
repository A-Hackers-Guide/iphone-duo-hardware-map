# `SBScreenFlash`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _flashCompletionBlocks;
@"UIScreen" _screen;
@"UIWindow" _flashWindow;
@"UIView" _flashView;
B _windowVisible;
```

## Class methods

```
+[SBScreenFlash mainScreenFlasher];
```

## Instance methods

```
-[SBScreenFlash initWithScreen:];
-[SBScreenFlash _tearDown];
-[SBScreenFlash _createUIWithColor:];
-[SBScreenFlash _orderWindowFrontAndThenOut:withColor:];
-[SBScreenFlash _orderWindowOut:];
-[SBScreenFlash flashColor:withCompletion:];
-[SBScreenFlash flashWhiteWithCompletion:];
```
