# `SBSAIndicatorMitosisSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 8 instance variables, 8 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"NSString" _prefix;
@"SBSAIndicatorMitosisPhaseSettings" _kickingPhaseSettings;
@"SBSAIndicatorMitosisPhaseSettings" _kickedPhaseSettings;
@"SBSAIndicatorMitosisPhaseSettings" _preparingToSettlePhaseSettings;
@"SBSAIndicatorMitosisPhaseSettings" _settlingPhaseSettings;
q _interSensorIndicatorAppearanceTransitionBeginPhase;
q _microIndicatorTranslationTransitionBeginPhase;
q _microIndicatorAppearanceTransitionBeginPhase;
```

## Properties

```
@property (T@"NSString",&,N,V_prefix) prefix;
@property (T@"SBSAIndicatorMitosisPhaseSettings",&,N,V_kickingPhaseSettings) kickingPhaseSettings;
@property (T@"SBSAIndicatorMitosisPhaseSettings",&,N,V_kickedPhaseSettings) kickedPhaseSettings;
@property (T@"SBSAIndicatorMitosisPhaseSettings",&,N,V_preparingToSettlePhaseSettings) preparingToSettlePhaseSettings;
@property (T@"SBSAIndicatorMitosisPhaseSettings",&,N,V_settlingPhaseSettings) settlingPhaseSettings;
@property (Tq,N,V_interSensorIndicatorAppearanceTransitionBeginPhase) interSensorIndicatorAppearanceTransitionBeginPhase;
@property (Tq,N,V_microIndicatorTranslationTransitionBeginPhase) microIndicatorTranslationTransitionBeginPhase;
@property (Tq,N,V_microIndicatorAppearanceTransitionBeginPhase) microIndicatorAppearanceTransitionBeginPhase;
```

## Class methods

```
+[SBSAIndicatorMitosisSettings ignoresKey:];
+[SBSAIndicatorMitosisSettings settingsControllerModule];
```

## Instance methods

```
-[SBSAIndicatorMitosisSettings setPrefix:];
-[SBSAIndicatorMitosisSettings setDefaultValues];
-[SBSAIndicatorMitosisSettings prefix];
-[SBSAIndicatorMitosisSettings setDefaultReversedCompactValues];
-[SBSAIndicatorMitosisSettings interSensorIndicatorAppearanceTransitionBeginPhase];
-[SBSAIndicatorMitosisSettings kickedPhaseSettings];
-[SBSAIndicatorMitosisSettings kickingPhaseSettings];
-[SBSAIndicatorMitosisSettings microIndicatorAppearanceTransitionBeginPhase];
-[SBSAIndicatorMitosisSettings microIndicatorTranslationTransitionBeginPhase];
-[SBSAIndicatorMitosisSettings preparingToSettlePhaseSettings];
-[SBSAIndicatorMitosisSettings setDefaultBabyJindoValues];
-[SBSAIndicatorMitosisSettings setDefaultCompactValues];
-[SBSAIndicatorMitosisSettings setDefaultCustomValues];
-[SBSAIndicatorMitosisSettings setDefaultReversedBabyJindoValues];
-[SBSAIndicatorMitosisSettings setDefaultReversedCustomValues];
-[SBSAIndicatorMitosisSettings setInterSensorIndicatorAppearanceTransitionBeginPhase:];
-[SBSAIndicatorMitosisSettings setKickedPhaseSettings:];
-[SBSAIndicatorMitosisSettings setKickingPhaseSettings:];
-[SBSAIndicatorMitosisSettings setMicroIndicatorAppearanceTransitionBeginPhase:];
-[SBSAIndicatorMitosisSettings setMicroIndicatorTranslationTransitionBeginPhase:];
-[SBSAIndicatorMitosisSettings setPreparingToSettlePhaseSettings:];
-[SBSAIndicatorMitosisSettings setSettlingPhaseSettings:];
-[SBSAIndicatorMitosisSettings settlingPhaseSettings];
```
