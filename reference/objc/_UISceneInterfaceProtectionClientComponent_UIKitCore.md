# `_UISceneInterfaceProtectionClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UIWindowSceneTraitSource`, `FBSSceneObserver`
- 5 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
{?="hasRegisteredForWindowNotifications"b1} _flags;
@"UIScene" _uiScene;
@"NSHashTable" _disabledUserInteractionWindows;
@"_UIWindowSceneTraitProvider" _traitProvider;
@"UISceneSystemProtectionManager" _sceneSystemProtectionManager;
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
-[_UISceneInterfaceProtectionClientComponent windowDidMoveToScene:];
-[_UISceneInterfaceProtectionClientComponent scene:didUpdateSettings:];
-[_UISceneInterfaceProtectionClientComponent traitOverridesForTraitProvider:];
-[_UISceneInterfaceProtectionClientComponent setScene:];
-[_UISceneInterfaceProtectionClientComponent dealloc];
-[_UISceneInterfaceProtectionClientComponent windowDidMoveToNilScene:];
-[_UISceneInterfaceProtectionClientComponent windowWillMoveToScene:];
```
