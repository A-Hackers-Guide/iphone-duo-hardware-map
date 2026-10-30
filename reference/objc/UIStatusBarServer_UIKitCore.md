# `UIStatusBarServer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 6 instance methods, 19 class methods

## Instance variables

```
@"<UIStatusBarServerClient>" _statusBar;
^{__CFRunLoopSource=} _source;
```

## Properties

```
@property (T@"<UIStatusBarServerClient>",&,N,V_statusBar) statusBar;
```

## Class methods

```
+[UIStatusBarServer _statusBarData];
+[UIStatusBarServer _cachedTimeStringFromData:];
+[UIStatusBarServer _updateStatusBarDataAnimated:];
+[UIStatusBarServer addStatusBarItem:];
+[UIStatusBarServer addStyleOverrides:];
+[UIStatusBarServer getDoubleHeightStatusStringForStyle:];
+[UIStatusBarServer getGlowAnimationEndTimeForStyle:];
+[UIStatusBarServer getGlowAnimationStateForStyle:];
+[UIStatusBarServer getStatusBarData];
+[UIStatusBarServer getStatusBarOverrideData];
+[UIStatusBarServer getStyleOverrides];
+[UIStatusBarServer permanentizeStatusBarOverrideData];
+[UIStatusBarServer postDoubleHeightStatusString:forStyle:];
+[UIStatusBarServer postGlowAnimationState:forStyle:];
+[UIStatusBarServer postStatusBarData:withActions:];
+[UIStatusBarServer postStatusBarOverrideData:];
+[UIStatusBarServer removeStatusBarItem:];
+[UIStatusBarServer removeStyleOverrides:];
+[UIStatusBarServer runServer];
```

## Instance methods

```
-[UIStatusBarServer statusBar];
-[UIStatusBarServer setStatusBar:];
-[UIStatusBarServer dealloc];
-[UIStatusBarServer _receivedStatusBarData:actions:animated:];
-[UIStatusBarServer _receivedStyleOverrides:];
-[UIStatusBarServer initWithStatusBar:];
```
