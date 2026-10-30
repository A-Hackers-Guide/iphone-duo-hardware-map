# `SBPIPStashVisualSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
q _userInterfaceStyle;
d _startBlurTransition;
d _completeBlurTransition;
@"SBPIPStashMaterialSettings" _lightModeMaterialSettings;
@"SBPIPStashMaterialSettings" _darkModeMaterialSettings;
```

## Properties

```
@property (Tq,N,V_userInterfaceStyle) userInterfaceStyle;
@property (Td,N,V_startBlurTransition) startBlurTransition;
@property (Td,N,V_completeBlurTransition) completeBlurTransition;
@property (T@"SBPIPStashMaterialSettings",&,N,V_lightModeMaterialSettings) lightModeMaterialSettings;
@property (T@"SBPIPStashMaterialSettings",&,N,V_darkModeMaterialSettings) darkModeMaterialSettings;
```

## Class methods

```
+[SBPIPStashVisualSettings ignoresKey:];
+[SBPIPStashVisualSettings settingsControllerModule];
```

## Instance methods

```
-[SBPIPStashVisualSettings userInterfaceStyle];
-[SBPIPStashVisualSettings setUserInterfaceStyle:];
-[SBPIPStashVisualSettings setDefaultValues];
-[SBPIPStashVisualSettings completeBlurTransition];
-[SBPIPStashVisualSettings darkModeMaterialSettings];
-[SBPIPStashVisualSettings lightModeMaterialSettings];
-[SBPIPStashVisualSettings materialSettingsForUserInterfaceStyle:];
-[SBPIPStashVisualSettings setCompleteBlurTransition:];
-[SBPIPStashVisualSettings setDarkModeMaterialSettings:];
-[SBPIPStashVisualSettings setLightModeMaterialSettings:];
-[SBPIPStashVisualSettings setStartBlurTransition:];
-[SBPIPStashVisualSettings startBlurTransition];
```
