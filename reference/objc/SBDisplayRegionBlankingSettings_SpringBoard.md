# `SBDisplayRegionBlankingSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _displacementEffectEnabled;
q _blankingRegionDiameterPx;
d _pillExtensionDelay;
d _pillCollapseDelay;
@"SBSABlankingRegionTransitionSettings" _blankingRegionAppearSettings;
@"SBSABlankingRegionTransitionSettings" _blankingRegionDisappearSettings;
```

## Properties

```
@property (Tq,N,V_blankingRegionDiameterPx) blankingRegionDiameterPx;
@property (Td,N,V_pillExtensionDelay) pillExtensionDelay;
@property (Td,N,V_pillCollapseDelay) pillCollapseDelay;
@property (TB,N,GisDisplacementEffectEnabled,V_displacementEffectEnabled) displacementEffectEnabled;
@property (T@"SBSABlankingRegionTransitionSettings",&,N,V_blankingRegionAppearSettings) blankingRegionAppearSettings;
@property (T@"SBSABlankingRegionTransitionSettings",&,N,V_blankingRegionDisappearSettings) blankingRegionDisappearSettings;
```

## Class methods

```
+[SBDisplayRegionBlankingSettings settingsControllerModule];
```

## Instance methods

```
-[SBDisplayRegionBlankingSettings setDefaultValues];
-[SBDisplayRegionBlankingSettings blankingRegionDisappearSettings];
-[SBDisplayRegionBlankingSettings blankingRegionAppearSettings];
-[SBDisplayRegionBlankingSettings blankingRegionDiameterPx];
-[SBDisplayRegionBlankingSettings isDisplacementEffectEnabled];
-[SBDisplayRegionBlankingSettings pillCollapseDelay];
-[SBDisplayRegionBlankingSettings pillExtensionDelay];
-[SBDisplayRegionBlankingSettings setBlankingRegionAppearSettings:];
-[SBDisplayRegionBlankingSettings setBlankingRegionDiameterPx:];
-[SBDisplayRegionBlankingSettings setBlankingRegionDisappearSettings:];
-[SBDisplayRegionBlankingSettings setDisplacementEffectEnabled:];
-[SBDisplayRegionBlankingSettings setPillCollapseDelay:];
-[SBDisplayRegionBlankingSettings setPillExtensionDelay:];
```
