# `SBLockScreenGlobalSuppressionAppearanceProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalAppearanceProviding`
- 4 instance variables, 13 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _dimmingActive;
B _buddySuppressionActive;
B _remoteContentHidesTime;
q _remoteContentWhitePointReduction;
```

## Properties

```
@property (TB,N,GisDimmingActive,V_dimmingActive) dimmingActive;
@property (TB,N,GisBuddySuppressionActive,V_buddySuppressionActive) buddySuppressionActive;
@property (TB,N,V_remoteContentHidesTime) remoteContentHidesTime;
@property (Tq,N,V_remoteContentWhitePointReduction) remoteContentWhitePointReduction;
@property (T@"NSString",R,C,N) appearanceIdentifier;
@property (T@"NSSet",R,C,N) components;
@property (T@"_UILegibilitySettings",R,N) legibilitySettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBLockScreenGlobalSuppressionAppearanceProvider conformsToCSAppearanceProviding];
-[SBLockScreenGlobalSuppressionAppearanceProvider appearanceIdentifier];
-[SBLockScreenGlobalSuppressionAppearanceProvider components];
-[SBLockScreenGlobalSuppressionAppearanceProvider legibilitySettings];
-[SBLockScreenGlobalSuppressionAppearanceProvider coverSheetIdentifier];
-[SBLockScreenGlobalSuppressionAppearanceProvider participantState];
-[SBLockScreenGlobalSuppressionAppearanceProvider isDimmingActive];
-[SBLockScreenGlobalSuppressionAppearanceProvider _hasAnySuppression];
-[SBLockScreenGlobalSuppressionAppearanceProvider isBuddySuppressionActive];
-[SBLockScreenGlobalSuppressionAppearanceProvider remoteContentHidesTime];
-[SBLockScreenGlobalSuppressionAppearanceProvider remoteContentWhitePointReduction];
-[SBLockScreenGlobalSuppressionAppearanceProvider setBuddySuppressionActive:];
-[SBLockScreenGlobalSuppressionAppearanceProvider setDimmingActive:];
-[SBLockScreenGlobalSuppressionAppearanceProvider setRemoteContentHidesTime:];
-[SBLockScreenGlobalSuppressionAppearanceProvider setRemoteContentWhitePointReduction:];
```
