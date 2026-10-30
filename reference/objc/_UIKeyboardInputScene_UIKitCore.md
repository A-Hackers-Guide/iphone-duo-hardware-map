# `_UIKeyboardInputScene`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindowScene`
- Protocols: `_UIRemoteKeyboardWindowDelegate`, `_UIKeyboardInputSceneClientComponentObserver`
- 2 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"UIRemoteKeyboardWindow" _remoteKeyboardWindow;
```

## Properties

```
@property (T@"UIScene",R,N) _targetScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardInputScene _remoteKeyboardWindowWillInvalidate:];
-[_UIKeyboardInputScene initWithSession:connectionOptions:];
-[_UIKeyboardInputScene _keyboardScene];
-[_UIKeyboardInputScene convertRectFromPairedSceneToKeyboardScene:];
-[_UIKeyboardInputScene _completeGeometryUpdatesWithTransitionContext:];
-[_UIKeyboardInputScene keyboardInputSceneRelativeGeometryDidUpdate:];
-[_UIKeyboardInputScene convertRectFromKeyboardSceneToPairedScene:];
-[_UIKeyboardInputScene addKeyboardSceneObserver:];
-[_UIKeyboardInputScene _targetScene];
-[_UIKeyboardInputScene _shouldAllowFencing];
-[_UIKeyboardInputScene removeKeyboardSceneObserver:];
```
