# `SBTraitsOrientationSupportTreeNodesSpecifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTraitsOrientationStageComponent`
- Protocols: `TRAPreferencesStageTreeNodesSpecifying`
- 1 instance variables, 6 properties, 2 instance methods, 2 class methods

## Instance variables

```
Q _supportedOrientations;
```

## Properties

```
@property (TQ,R,N,V_supportedOrientations) supportedOrientations;
@property (T@"NSNumber",R,N) componentOrder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTraitsOrientationSupportTreeNodesSpecifier findParentForParticipant:nodeSpecifications:];
+[SBTraitsOrientationSupportTreeNodesSpecifier findParticipantWithRole:nodeSpecifications:];
```

## Instance methods

```
-[SBTraitsOrientationSupportTreeNodesSpecifier supportedOrientations];
-[SBTraitsOrientationSupportTreeNodesSpecifier updateStageTreeNodesSpecifications:stageParticipantsRoles:context:];
```
