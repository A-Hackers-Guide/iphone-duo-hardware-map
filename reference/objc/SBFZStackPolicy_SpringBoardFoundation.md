# `SBFZStackPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _preferencesByParticipantUUID;
@"NSMutableDictionary" _resolutionsByParticipantUUID;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,G_resolutionsByParticipantUUID,V_resolutionsByParticipantUUID) resolutionsByParticipantUUID;
```

## Class methods

```
+[SBFZStackPolicy resolutionOrder];
+[SBFZStackPolicy preferenceClass];
+[SBFZStackPolicy resolutionClass];
```

## Instance methods

```
-[SBFZStackPolicy init];
-[SBFZStackPolicy _resolutionsByParticipantUUID];
-[SBFZStackPolicy _resolveForSortedParticipants:gatheredPreferences:];
-[SBFZStackPolicy didRegisterWithResolver:];
-[SBFZStackPolicy preferenceForParticipant:];
-[SBFZStackPolicy resolutionForParticipant:];
-[SBFZStackPolicy resolveSettingsForOrderedParticipants:updateHandler:];
```
