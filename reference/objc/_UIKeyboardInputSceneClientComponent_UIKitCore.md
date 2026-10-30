# `_UIKeyboardInputSceneClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSSceneObserver`
- 9 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _didRealizeUISceneNotificationToken;
@"FBSSceneLayer" _forwardedKeyboardLayer;
@"_UIKeyboardInputScene" _keyboardInputScene;
@"UIScene<_UISceneUIWindowHosting>" _pairedUIScene;
@"NSHashTable" _observers;
q _currentLegacyOrientation;
B _hasEnqueuedGeometryCallout;
@"FBSScene" _pairedScene;
@"UIWindow" _forwardingKeyboardWindow;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardInputSceneClientComponent scene:didUpdateSettings:];
-[_UIKeyboardInputSceneClientComponent setScene:];
-[_UIKeyboardInputSceneClientComponent _fbsSceneDidRealizeUIScene:];
-[_UIKeyboardInputSceneClientComponent screenOrientationDidChange:];
-[_UIKeyboardInputSceneClientComponent invalidate];
-[_UIKeyboardInputSceneClientComponent scene:didUpdateClientSettings:];
```
