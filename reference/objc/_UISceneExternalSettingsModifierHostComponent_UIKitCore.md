# `_UISceneExternalSettingsModifierHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `_UISceneExternalSettingsModifierHost`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UISSceneHostingExternalSettingsModifierClient" _client;
@"NSSet" _settingsModifiers;
B _hasFetchedModifiers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BSServiceConnectionEndpoint",C,N) externalSettingsModifierEndpoint;
@property (TB,N) participatesInExternalSettingsModification;
```

## Instance methods

```
-[_UISceneExternalSettingsModifierHostComponent sceneWillActivate:];
-[_UISceneExternalSettingsModifierHostComponent sceneDidInvalidate:withContext:];
-[_UISceneExternalSettingsModifierHostComponent participatesInExternalSettingsModification];
-[_UISceneExternalSettingsModifierHostComponent scene:willUpdateSettings:];
-[_UISceneExternalSettingsModifierHostComponent externalSettingsModifierEndpoint];
-[_UISceneExternalSettingsModifierHostComponent setExternalSettingsModifierEndpoint:];
-[_UISceneExternalSettingsModifierHostComponent setParticipatesInExternalSettingsModification:];
```
