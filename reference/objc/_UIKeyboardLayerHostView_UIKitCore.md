# `_UIKeyboardLayerHostView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISceneLayerHostView`
- Protocols: `FBSceneObserver`
- 8 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@? _sceneLayerMatchingPredicate;
@"FBScene" _owningScene;
@"FBScene" _keyboardScene;
@"<BSInvalidatable>" _keyboardSceneAvailabilityObserver;
@"FBSSceneClientSettingsDiffInspector" _keyboardSceneClientSettingsDiffInspector;
@"FBSSceneIdentityToken" _keyboardPreferredHostIdentity;
B _isPaired;
@"<UIScenePresenter>" _presenter;
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
-[_UIKeyboardLayerHostView dealloc];
-[_UIKeyboardLayerHostView _initWithLayer:owningScene:keyboardMatchingPredicate:];
-[_UIKeyboardLayerHostView setInheritsSecurity:];
-[_UIKeyboardLayerHostView _setKeyboardScene:];
-[_UIKeyboardLayerHostView setCurrentPresentationContext:];
-[_UIKeyboardLayerHostView initWithKeyboardLayer:owningScene:];
-[_UIKeyboardLayerHostView _updatePairingState];
-[_UIKeyboardLayerHostView scene:didUpdateClientSettings:];
-[_UIKeyboardLayerHostView initWithKeyboardProxyLayer:owningScene:];
```
