# `UIScreenMode`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayMode" _mode;
B _isMainScreen;
d _scale;
```

## Properties

```
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N) pixelAspectRatio;
```

## Class methods

```
+[UIScreenMode _screenModeForDisplayMode:mainScreen:actualDisplayScale:];
```

## Instance methods

```
-[UIScreenMode _displayMode];
-[UIScreenMode size];
-[UIScreenMode pixelAspectRatio];
-[UIScreenMode description];
-[UIScreenMode initWithDisplayMode:mainScreen:actualDisplayScale:];
```
