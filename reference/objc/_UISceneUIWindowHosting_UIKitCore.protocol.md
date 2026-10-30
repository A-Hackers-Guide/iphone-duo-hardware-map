# `_UISceneUIWindowHosting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 14 instance methods, 1 class methods

## Properties

```
@property (T@"UIScreen",R,N) _screen;
@property (Tq,R,N) _interfaceOrientation;
@property (T@"<UICoordinateSpace>",R,N) _coordinateSpace;
@property (T@"UITraitCollection",R,N) _traitCollection;
@property (T@"UIStatusBarManager",R,N) _statusBarManager;
@property (class, TB,R,N) _hostsWindows;
```

## Class methods

```
+[_UISceneUIWindowHosting _hostsWindows];
```

## Instance methods

```
-[_UISceneUIWindowHosting _screen];
-[_UISceneUIWindowHosting _interfaceOrientation];
-[_UISceneUIWindowHosting _attachWindow:];
-[_UISceneUIWindowHosting _detachWindow:];
-[_UISceneUIWindowHosting _traitCollection];
-[_UISceneUIWindowHosting _allWindowsIncludingInternalWindows:onlyVisibleWindows:];
-[_UISceneUIWindowHosting _coordinateSpace];
-[_UISceneUIWindowHosting _screenDidChangeFromScreen:toScreen:];
-[_UISceneUIWindowHosting _statusBarManager];
-[_UISceneUIWindowHosting _updateVisibleWindowOrderWithTest:];
-[_UISceneUIWindowHosting _windowUpdatedProperties:];
-[_UISceneUIWindowHosting _windowUpdatedVisibility:];
-[_UISceneUIWindowHosting _zombifyWindow:];
-[_UISceneUIWindowHosting _allWindowsForInvalidation];
```
