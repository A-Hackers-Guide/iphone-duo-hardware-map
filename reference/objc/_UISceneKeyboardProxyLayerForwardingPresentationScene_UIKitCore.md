# `_UISceneKeyboardProxyLayerForwardingPresentationScene`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `_UIScenePresentationViewObserver`, `_UISceneKeyboardProxyLayerForwardingPresentationEnvironment`, `_UIScenePresentationManagerPrioritizedPresenterObserver`, `UIScenePresenterObserver`
- 4 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"_UIScenePresenter" _prioritizedPresenter;
@"FBSSceneIdentityToken" _keyboardOwnerIdentityToken;
@"FBScene" _scene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBSSceneIdentityToken",R,N,V_keyboardOwnerIdentityToken) keyboardOwnerIdentityToken;
```

## Instance methods

```
-[_UISceneKeyboardProxyLayerForwardingPresentationScene sceneDidInvalidate:withContext:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene presentationView:didMoveToWindow:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene removeObserver:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene notifyObserversDidUpdateKeyboardLayers];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene dealloc];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene keyboardOwnerIdentityToken];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene addObserver:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene _presentationManager:willPrioritizePresenter:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene description];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene scenePresenter:didUpdateContext:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene notifyObserversDidMoveToWindow:];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene keyboardLayers];
-[_UISceneKeyboardProxyLayerForwardingPresentationScene scene:didUpdateClientSettings:];
```
