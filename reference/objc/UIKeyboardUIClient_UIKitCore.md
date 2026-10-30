# `UIKeyboardUIClient`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"BSServiceConnection<BSServiceConnectionClient>" _connection;
@"<UIKeyboardUIServiceProtocol>" _remoteTarget;
```

## Class methods

```
+[UIKeyboardUIClient sharedInstance];
+[UIKeyboardUIClient serviceInterface];
```

## Instance methods

```
-[UIKeyboardUIClient init];
-[UIKeyboardUIClient dealloc];
-[UIKeyboardUIClient _initConnectionIfNeeded];
-[UIKeyboardUIClient setKeyboardAlpha:force:];
-[UIKeyboardUIClient snapshotViewForOptions:];
```
