# `_UISceneClassicModeExternalSettingsModifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISSceneHostingSettingsModifier`
- Protocols: `BSDescriptionStreaming`
- 3 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _mainDisplayConfiguration;
{CGSize="width"d"height"d} _maximumPortraitSize;
@"BSCornerRadiusConfiguration" _cornerRadiusConfiguration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneClassicModeExternalSettingsModifier supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UISceneClassicModeExternalSettingsModifier debugDescription];
-[_UISceneClassicModeExternalSettingsModifier succinctDescription];
-[_UISceneClassicModeExternalSettingsModifier description];
-[_UISceneClassicModeExternalSettingsModifier appendDescriptionToStream:];
-[_UISceneClassicModeExternalSettingsModifier encodeWithBSXPCCoder:];
-[_UISceneClassicModeExternalSettingsModifier initWithBSXPCCoder:];
-[_UISceneClassicModeExternalSettingsModifier initWithMainDisplayConfiguration:maximumPortraitSize:cornerRadiusConfiguration:];
-[_UISceneClassicModeExternalSettingsModifier updaterForProposedSettings:withSettingsDiff:];
```
