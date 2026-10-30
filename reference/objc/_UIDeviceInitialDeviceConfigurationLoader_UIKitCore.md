# `_UIDeviceInitialDeviceConfigurationLoader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"UISDeviceContext" _context;
B _hasRequestedPreload;
```

## Properties

```
@property (T@"UISDeviceContext",R,N) initialDeviceContext;
```

## Class methods

```
+[_UIDeviceInitialDeviceConfigurationLoader sharedLoader];
```

## Instance methods

```
-[_UIDeviceInitialDeviceConfigurationLoader _startPreloadInitialDeviceContext];
-[_UIDeviceInitialDeviceConfigurationLoader initialDeviceContext];
```
