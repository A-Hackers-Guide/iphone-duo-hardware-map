# `SBSAAnimatedTransitionDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAAnimatedTransitionDescribing`, `SBSAAnimatedTransitionMilestoneProviding`, `SBSABlockMutating`, `SBSADescriptionDebugSource`
- 5 instance variables, 9 properties, 20 instance methods, 4 class methods

## Instance variables

```
@"NSUUID" _animatedTransitionIdentifier;
@"SBFFluidBehaviorSettings" _behaviorSettings;
@"NSString" _responsibleProviderDebugString;
@"NSSet" _milestones;
@"NSMutableDictionary" _keyPathsToAuxillaryBehaviorSettingsMap;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setAnimatedTransitionIdentifier:,V_animatedTransitionIdentifier) animatedTransitionIdentifier;
@property (T@"SBFFluidBehaviorSettings",C,N,S_setBehaviorSettings:,V_behaviorSettings) behaviorSettings;
@property (T@"NSMutableDictionary",C,N,S_setKeyPathsToAuxillaryBehaviorSettingsMap:,V_keyPathsToAuxillaryBehaviorSettingsMap) keyPathsToAuxillaryBehaviorSettingsMap;
@property (T@"NSString",C,N,S_setResponsibleProviderDebugString:,V_responsibleProviderDebugString) responsibleProviderDebugString;
@property (T@"NSSet",C,N,S_setMilestones:,V_milestones) milestones;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAAnimatedTransitionDescription initialize];
+[SBSAAnimatedTransitionDescription animatedTransitionDescriptionWithAnimatedTransitionIdentifier:behaviorSettings:milestones:responsibleProvider:];
+[SBSAAnimatedTransitionDescription instanceWithBlock:];
+[SBSAAnimatedTransitionDescription mutatorClass];
```

## Instance methods

```
-[SBSAAnimatedTransitionDescription hash];
-[SBSAAnimatedTransitionDescription description];
-[SBSAAnimatedTransitionDescription copyWithZone:];
-[SBSAAnimatedTransitionDescription isEqual:];
-[SBSAAnimatedTransitionDescription copyWithBlock:];
-[SBSAAnimatedTransitionDescription membersForCoder];
-[SBSAAnimatedTransitionDescription milestones];
-[SBSAAnimatedTransitionDescription _setMilestones:];
-[SBSAAnimatedTransitionDescription _setAnimatedTransitionIdentifier:];
-[SBSAAnimatedTransitionDescription _setBehaviorSettings:];
-[SBSAAnimatedTransitionDescription _setKeyPathsToAuxillaryBehaviorSettingsMap:];
-[SBSAAnimatedTransitionDescription _setResponsibleProviderDebugString:];
-[SBSAAnimatedTransitionDescription animatedTransitionIdentifier];
-[SBSAAnimatedTransitionDescription auxillaryBehaviorSettingsForKeyPath:];
-[SBSAAnimatedTransitionDescription behaviorSettings];
-[SBSAAnimatedTransitionDescription copyBySettingAuxillaryBehaviorSettings:forKeyPath:];
-[SBSAAnimatedTransitionDescription initWithAnimatedTransitionDescription:];
-[SBSAAnimatedTransitionDescription keyPathsToAuxillaryBehaviorSettingsMap];
-[SBSAAnimatedTransitionDescription keyPathsWithAuxillaryBehaviorSettings];
-[SBSAAnimatedTransitionDescription responsibleProviderDebugString];
```
