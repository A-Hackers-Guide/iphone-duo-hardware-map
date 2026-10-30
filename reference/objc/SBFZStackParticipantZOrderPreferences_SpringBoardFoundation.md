# `SBFZStackParticipantZOrderPreferences`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBFZStackParticipant" _participant;
@"<SBFZStackParticipantZOrderUIAssociation>" _associatedUI;
d _levelWithinAssociatedUI;
```

## Properties

```
@property (TB,R,N,GisStructurallyPositioned) structurallyPositioned;
@property (Tq,R,N) legacyPriority;
@property (T@"SBFZStackParticipant",R,W,N,V_participant) participant;
@property (T@"<SBFZStackParticipantZOrderUIAssociation>",&,N,V_associatedUI) associatedUI;
@property (Td,N,V_levelWithinAssociatedUI) levelWithinAssociatedUI;
@property (T@"NSNumber",R,N) commonParticipantIdentifierForLegacySorting;
```

## Instance methods

```
-[SBFZStackParticipantZOrderPreferences participant];
-[SBFZStackParticipantZOrderPreferences compare:];
-[SBFZStackParticipantZOrderPreferences initWithParticipant:];
-[SBFZStackParticipantZOrderPreferences associatedUI];
-[SBFZStackParticipantZOrderPreferences commonParticipantIdentifierForLegacySorting];
-[SBFZStackParticipantZOrderPreferences compareByLegacyPriority:];
-[SBFZStackParticipantZOrderPreferences isStructurallyPositioned];
-[SBFZStackParticipantZOrderPreferences legacyPriority];
-[SBFZStackParticipantZOrderPreferences levelWithinAssociatedUI];
-[SBFZStackParticipantZOrderPreferences setAssociatedUI:];
-[SBFZStackParticipantZOrderPreferences setLevelWithinAssociatedUI:];
-[SBFZStackParticipantZOrderPreferences sortableUI];
```
