# `_UISystemIconAppearanceSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneComponentProviding`
- 4 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<UITraitChangeRegistration>" _sceneTraitObserver;
{?="hasFetchedInitialAppearance"I} _flags;
@"UIScene" _scene;
@"_UISystemIconAppearance" _appearance;
```

## Properties

```
@property (T@"UITraitCollection",?,R,N) _traitOverrides;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISystemIconAppearanceSceneComponent _scene];
-[_UISystemIconAppearanceSceneComponent _traitOverrides];
-[_UISystemIconAppearanceSceneComponent _sceneWillInvalidate:];
-[_UISystemIconAppearanceSceneComponent initWithScene:];
-[_UISystemIconAppearanceSceneComponent _setScene:];
-[_UISystemIconAppearanceSceneComponent _beginObservingSystemIconAppearanceChanges];
-[_UISystemIconAppearanceSceneComponent _getCurrentIconAppearance];
-[_UISystemIconAppearanceSceneComponent _stopObservingSystemIconAppearanceChanges];
-[_UISystemIconAppearanceSceneComponent _systemIconAppearanceDidChange];
```
