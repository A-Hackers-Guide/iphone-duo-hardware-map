# `_UIKeyboardResponderOverrideSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIScene" _scene;
@"UIView" _commonView;
@"NSMutableArray" _keyboardResponderOverrides;
```

## Properties

```
@property (T@"NSMutableArray",C,N,V_keyboardResponderOverrides) keyboardResponderOverrides;
@property (T@"_UIKeyboardResponderOverrideInfo",R,N,GpreferredKeyboardResponderOverride) preferredKeyboardResponderOverride;
@property (T@"UIView",W,N,V_commonView) commonView;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardResponderOverrideSceneComponent _scene];
-[_UIKeyboardResponderOverrideSceneComponent preferredKeyboardResponderOverride];
-[_UIKeyboardResponderOverrideSceneComponent setCommonView:];
-[_UIKeyboardResponderOverrideSceneComponent _sceneWillInvalidate:];
-[_UIKeyboardResponderOverrideSceneComponent initWithScene:];
-[_UIKeyboardResponderOverrideSceneComponent setKeyboardResponderOverrides:];
-[_UIKeyboardResponderOverrideSceneComponent commonView];
-[_UIKeyboardResponderOverrideSceneComponent pushPreferredKeyboardResponderOverride:];
-[_UIKeyboardResponderOverrideSceneComponent _setScene:];
-[_UIKeyboardResponderOverrideSceneComponent keyboardResponderOverrides];
-[_UIKeyboardResponderOverrideSceneComponent removePreferredKeyboardResponderOverride:];
```
