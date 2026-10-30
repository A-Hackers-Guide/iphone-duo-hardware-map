# `UIScreenshotService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIScene" _scene;
@"<UIScreenshotServiceDelegate>" _delegate;
@"<UIScreenshotServiceDelegate>" _privateDelegate;
```

## Properties

```
@property (T@"<UIScreenshotServiceDelegate>",W,N,V_privateDelegate) privateDelegate;
@property (T@"<UIScreenshotServiceDelegate>",W,N,V_delegate) delegate;
@property (T@"UIWindowScene",R,W,N) windowScene;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIScreenshotService _scene];
-[UIScreenshotService privateDelegate];
-[UIScreenshotService initWithScene:];
-[UIScreenshotService setDelegate:];
-[UIScreenshotService setPrivateDelegate:];
-[UIScreenshotService delegate];
-[UIScreenshotService _setScene:];
-[UIScreenshotService windowScene];
```
