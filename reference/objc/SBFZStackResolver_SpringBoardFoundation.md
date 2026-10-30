# `SBFZStackResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `SBFZStackResolvedPolicyProvider`
- 11 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _sortedParticipants;
@"NSHashTable" _zStackHUDViews;
@"<BSInvalidatable>" _stateCaptureHandle;
@"NSMutableArray" _participants;
@"NSMapTable" _participantObservers;
@"NSMapTable" _associatedUIByParticipantIdentifier;
@"NSMutableSet" _structurallyPositionedParticipantIdentifiers;
@"NSArray" _policies;
@"NSString" _resolvedStackDescription;
@"NSString" _debugIdentifier;
@"SBFZStackParticipant" _highestZStackParticipant;
```

## Properties

```
@property (T@"NSArray",R,C,N) _registeredParticipants;
@property (T@"SBFZStackParticipant",R,N,G_highestZStackParticipant,V_highestZStackParticipant) highestZStackParticipant;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFZStackResolver debugDescription];
-[SBFZStackResolver init];
-[SBFZStackResolver dealloc];
-[SBFZStackResolver description];
-[SBFZStackResolver appendDescriptionToStream:];
-[SBFZStackResolver _highestZStackParticipant];
-[SBFZStackResolver _registeredParticipants];
-[SBFZStackResolver _updateZStackHUDViews];
-[SBFZStackResolver _zStackHUDRows];
-[SBFZStackResolver acquireParticipantWithIdentifier:delegate:];
-[SBFZStackResolver addObserver:ofParticipantWithIdentifier:];
-[SBFZStackResolver associatedViewForParticipant:];
-[SBFZStackResolver associatedViewForParticipantWithIdentifier:];
-[SBFZStackResolver displayContentModeTransitionIsFullySelfManaged];
-[SBFZStackResolver displayContentModeTransitionResolutionForParticipant:];
-[SBFZStackResolver displayContentModeTransitionStackResolution];
-[SBFZStackResolver initWithDebugIdentifier:];
-[SBFZStackResolver isParticipantStructurallyPositioned:];
-[SBFZStackResolver makeZStackHUDView];
-[SBFZStackResolver removeObserver:ofParticipantWithIdentifier:];
-[SBFZStackResolver resolutionForPolicyClass:participant:];
-[SBFZStackResolver settingsOfParticipantWithIdentifier:];
-[SBFZStackResolver sortedParticipantIdentifiers];
```
