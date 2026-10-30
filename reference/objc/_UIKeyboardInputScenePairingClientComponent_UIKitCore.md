# `_UIKeyboardInputScenePairingClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSSceneObserver`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _didRealizeUISceneNotificationToken;
B _isRequestingKeyboardScene;
@"NSHashTable" _observers;
@"FBSScene" _pairedKeyboardScene;
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
-[_UIKeyboardInputScenePairingClientComponent removeObserver:];
-[_UIKeyboardInputScenePairingClientComponent scene:didUpdateSettings:];
-[_UIKeyboardInputScenePairingClientComponent setScene:];
-[_UIKeyboardInputScenePairingClientComponent _fbsSceneDidRealizeUIScene:];
-[_UIKeyboardInputScenePairingClientComponent addObserver:];
-[_UIKeyboardInputScenePairingClientComponent invalidate];
-[_UIKeyboardInputScenePairingClientComponent applicationDidReloadKeyboardArbiterState:];
-[_UIKeyboardInputScenePairingClientComponent sceneWillInvalidate:];
```
