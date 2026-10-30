# `SBHarmonyController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"CBClient" _client;
@"SBHarmonySettings" _harmonySettings;
@"NSMutableArray" _suppressionAssertions;
q _suppressedWhitePointAdaptationEnabled;
q _suppressedBlueLightReductionEnabled;
B _supportsWhitePointAdaptation;
B _supportsBlueLightReduction;
```

## Properties

```
@property (TB,R,N,V_supportsWhitePointAdaptation) supportsWhitePointAdaptation;
@property (TB,N,GisWhitePointAdaptationEnabled) whitePointAdaptationEnabled;
@property (Tq,N) whitePointAdaptivityStyle;
@property (TB,R,N,V_supportsBlueLightReduction) supportsBlueLightReduction;
@property (T@"SBHarmonySettings",R,N) harmonySettings;
```

## Instance methods

```
-[SBHarmonyController init];
-[SBHarmonyController setWhitePointAdaptivityStyle:];
-[SBHarmonyController whitePointAdaptivityStyle];
-[SBHarmonyController supportsBlueLightReduction];
-[SBHarmonyController harmonySettings];
-[SBHarmonyController setWhitePointAdaptationEnabled:];
-[SBHarmonyController _adaptationClient];
-[SBHarmonyController isWhitePointAdaptationEnabled];
-[SBHarmonyController setWhitePointAdaptationStrength:forWhitePointAdaptivityStyle:];
-[SBHarmonyController setWhitePointAdaptivityStyle:animationSettings:];
-[SBHarmonyController setWhitePointAdaptivityStyleWithStyles:animationSettings:];
-[SBHarmonyController supportsWhitePointAdaptation];
-[SBHarmonyController transitionFromWhitePointAdaptivityStyleWithStyles:toWhitePointAdaptivityStyleWithStyles:fromPercentage:toPercentage:animationSettings:];
-[SBHarmonyController whitePointAdaptationStrengthForWhitePointAdaptivityStyle:];
```
