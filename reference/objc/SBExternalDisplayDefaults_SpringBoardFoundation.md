# `SBExternalDisplayDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- Protocols: `SBDisplayArrangementPreferenceProvider`
- 0 instance variables, 11 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"NSDictionary",&,D,N) displayModeSettingsMap;
@property (TI,D,N) arrangementEdge;
@property (Td,D,N) arrangementOffset;
@property (TB,D,N,GisMirroringEnabled) mirroringEnabled;
@property (TB,D,N,GisNonInteractiveCompanionScenesEnabledForAll) nonInteractiveCompanionScenesEnabledForAll;
@property (Td,D,N) contentsScale;
@property (TB,D,N) allowWirelessDisplaysForExtendedDisplayMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExternalDisplayDefaults description];
-[SBExternalDisplayDefaults _bindAndRegisterDefaults];
-[SBExternalDisplayDefaults _saveDisplaySettingsMapToStore:];
-[SBExternalDisplayDefaults _constructDisplaySettingsMap];
-[SBExternalDisplayDefaults displayModeSettingsForDisplay:];
-[SBExternalDisplayDefaults displaySupportsExtendedDisplayMode:];
-[SBExternalDisplayDefaults observeDisplayModeSettingsOnQueue:withBlock:];
-[SBExternalDisplayDefaults resetPrototypeSettingAdjustableDefaults];
-[SBExternalDisplayDefaults setDisplayModeSettings:forDisplaysMatchingPredicates:];
```
