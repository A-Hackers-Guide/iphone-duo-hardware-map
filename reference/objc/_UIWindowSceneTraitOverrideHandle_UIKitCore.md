# `_UIWindowSceneTraitOverrideHandle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneTraitSource`, `BSInvalidatable`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _didRealizeUISceneNotificationToken;
@"NSString" _componentKey;
@"UITraitCollection" _traitOverrides;
@"_UIWindowSceneTraitProvider" __traitProvider;
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
-[_UIWindowSceneTraitOverrideHandle traitOverridesForTraitProvider:];
-[_UIWindowSceneTraitOverrideHandle dealloc];
-[_UIWindowSceneTraitOverrideHandle invalidate];
-[_UIWindowSceneTraitOverrideHandle _setupProviderForUIWindowScene:];
-[_UIWindowSceneTraitOverrideHandle _handleUISceneRealizationNotification:];
-[_UIWindowSceneTraitOverrideHandle _setupProviderForFBSScene:];
```
