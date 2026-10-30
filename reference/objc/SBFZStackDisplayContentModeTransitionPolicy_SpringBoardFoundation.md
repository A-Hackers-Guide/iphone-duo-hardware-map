# `SBFZStackDisplayContentModeTransitionPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBFZStackPolicy`
- 1 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"SBFZStackResolver" _resolver;
```

## Properties

```
@property (T@"SBFZStackResolver",W,N,V_resolver) resolver;
```

## Class methods

```
+[SBFZStackDisplayContentModeTransitionPolicy resolutionOrder];
+[SBFZStackDisplayContentModeTransitionPolicy preferenceClass];
+[SBFZStackDisplayContentModeTransitionPolicy resolutionClass];
```

## Instance methods

```
-[SBFZStackDisplayContentModeTransitionPolicy resolver];
-[SBFZStackDisplayContentModeTransitionPolicy setResolver:];
-[SBFZStackDisplayContentModeTransitionPolicy _dispositionForParticipant:atIndex:highestOpaqueIndex:boundaryIndex:];
-[SBFZStackDisplayContentModeTransitionPolicy _hasCloneSourceForParticipant:];
-[SBFZStackDisplayContentModeTransitionPolicy _isParticipantPotentiallyVisible:];
-[SBFZStackDisplayContentModeTransitionPolicy didRegisterWithResolver:];
-[SBFZStackDisplayContentModeTransitionPolicy resolveSettingsForOrderedParticipants:updateHandler:];
```
