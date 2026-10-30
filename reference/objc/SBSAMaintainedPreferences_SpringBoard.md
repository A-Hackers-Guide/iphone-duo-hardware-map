# `SBSAMaintainedPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SBSABlockMutating`
- 2 instance variables, 6 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"SBSAIndicatorAppearanceStateContext" _indicatorAppearanceStateContext;
@"NSDictionary" _blankingRegionAppearanceStateContextsByRegionIdentifier;
```

## Properties

```
@property (T@"SBSAIndicatorAppearanceStateContext",&,N,S_setIndicatorAppearanceStateContext:,V_indicatorAppearanceStateContext) indicatorAppearanceStateContext;
@property (T@"NSDictionary",C,N,S_setBlankingRegionAppearanceStateContextsByRegionIdentifier:,V_blankingRegionAppearanceStateContextsByRegionIdentifier) blankingRegionAppearanceStateContextsByRegionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAMaintainedPreferences initialize];
+[SBSAMaintainedPreferences instanceWithBlock:];
+[SBSAMaintainedPreferences mutatorClass];
```

## Instance methods

```
-[SBSAMaintainedPreferences hash];
-[SBSAMaintainedPreferences description];
-[SBSAMaintainedPreferences copyWithZone:];
-[SBSAMaintainedPreferences isEqual:];
-[SBSAMaintainedPreferences copyWithBlock:];
-[SBSAMaintainedPreferences membersForCoder];
-[SBSAMaintainedPreferences indicatorAppearanceStateContext];
-[SBSAMaintainedPreferences _setBlankingRegionAppearanceStateContextsByRegionIdentifier:];
-[SBSAMaintainedPreferences _setIndicatorAppearanceStateContext:];
-[SBSAMaintainedPreferences blankingRegionAppearanceStateContextsByRegionIdentifier];
```
