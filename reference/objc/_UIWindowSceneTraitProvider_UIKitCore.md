# `_UIWindowSceneTraitProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneComponentProviding`
- 2 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UIScene" _scene;
@"<_UIWindowSceneTraitSource>" _source;
```

## Properties

```
@property (T@"<_UIWindowSceneTraitSource>",W,N,V_source) source;
@property (T@"UITraitCollection",?,R,N) _traitOverrides;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIWindowSceneTraitProvider _scene];
-[_UIWindowSceneTraitProvider _traitOverrides];
-[_UIWindowSceneTraitProvider initWithScene:];
-[_UIWindowSceneTraitProvider setSource:];
-[_UIWindowSceneTraitProvider invalidateTraitOverrides];
-[_UIWindowSceneTraitProvider _setScene:];
-[_UIWindowSceneTraitProvider source];
```
