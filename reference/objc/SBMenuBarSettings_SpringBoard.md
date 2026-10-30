# `SBMenuBarSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 14 instance variables, 14 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _alwaysVisibleOnExternalDisplay;
d _menuDismissYThresholdForPointer;
d _menuRevealDelay;
d _menuTitleSpacing;
d _fullscreenPeekDuration;
d _backgroundBlurContentOverhang;
d _entryAnimationDuration;
d _entryAnimationMass;
d _entryAnimationStiffness;
d _entryAnimationDamping;
d _exitAnimationDuration;
d _exitAnimationMass;
d _exitAnimationStiffness;
d _exitAnimationDamping;
```

## Properties

```
@property (Td,N,V_menuDismissYThresholdForPointer) menuDismissYThresholdForPointer;
@property (Td,N,V_menuRevealDelay) menuRevealDelay;
@property (Td,N,V_menuTitleSpacing) menuTitleSpacing;
@property (Td,N,V_fullscreenPeekDuration) fullscreenPeekDuration;
@property (TB,N,V_alwaysVisibleOnExternalDisplay) alwaysVisibleOnExternalDisplay;
@property (Td,N,V_backgroundBlurContentOverhang) backgroundBlurContentOverhang;
@property (Td,N,V_entryAnimationDuration) entryAnimationDuration;
@property (Td,N,V_entryAnimationMass) entryAnimationMass;
@property (Td,N,V_entryAnimationStiffness) entryAnimationStiffness;
@property (Td,N,V_entryAnimationDamping) entryAnimationDamping;
@property (Td,N,V_exitAnimationDuration) exitAnimationDuration;
@property (Td,N,V_exitAnimationMass) exitAnimationMass;
@property (Td,N,V_exitAnimationStiffness) exitAnimationStiffness;
@property (Td,N,V_exitAnimationDamping) exitAnimationDamping;
```

## Class methods

```
+[SBMenuBarSettings settingsControllerModule];
```

## Instance methods

```
-[SBMenuBarSettings setDefaultValues];
-[SBMenuBarSettings menuDismissYThresholdForPointer];
-[SBMenuBarSettings menuRevealDelay];
-[SBMenuBarSettings alwaysVisibleOnExternalDisplay];
-[SBMenuBarSettings backgroundBlurContentOverhang];
-[SBMenuBarSettings entryAnimationDamping];
-[SBMenuBarSettings entryAnimationDuration];
-[SBMenuBarSettings entryAnimationMass];
-[SBMenuBarSettings entryAnimationStiffness];
-[SBMenuBarSettings exitAnimationDamping];
-[SBMenuBarSettings exitAnimationDuration];
-[SBMenuBarSettings exitAnimationMass];
-[SBMenuBarSettings exitAnimationStiffness];
-[SBMenuBarSettings fullscreenPeekDuration];
-[SBMenuBarSettings menuTitleSpacing];
-[SBMenuBarSettings setAlwaysVisibleOnExternalDisplay:];
-[SBMenuBarSettings setBackgroundBlurContentOverhang:];
-[SBMenuBarSettings setEntryAnimationDamping:];
-[SBMenuBarSettings setEntryAnimationDuration:];
-[SBMenuBarSettings setEntryAnimationMass:];
-[SBMenuBarSettings setEntryAnimationStiffness:];
-[SBMenuBarSettings setExitAnimationDamping:];
-[SBMenuBarSettings setExitAnimationDuration:];
-[SBMenuBarSettings setExitAnimationMass:];
-[SBMenuBarSettings setExitAnimationStiffness:];
-[SBMenuBarSettings setFullscreenPeekDuration:];
-[SBMenuBarSettings setMenuDismissYThresholdForPointer:];
-[SBMenuBarSettings setMenuRevealDelay:];
-[SBMenuBarSettings setMenuTitleSpacing:];
```
