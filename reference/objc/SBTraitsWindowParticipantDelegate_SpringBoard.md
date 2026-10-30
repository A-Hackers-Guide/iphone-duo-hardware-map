# `SBTraitsWindowParticipantDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTraitsParticipantDelegate`
- 6 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _visibleWindows;
@"NSMapTable" _participantOwningWindowMapTable;
@"NSMutableArray" _tempOwningWindowHidden;
@"NSMutableArray" _tempOwningWindowVisible;
@"NSMutableDictionary" _tempLastPreferredZOrder;
@"NSMutableDictionary" _tempLastSupportedOrientations;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTraitsWindowParticipantDelegate _activeOrientationDeterminingParticipantRoles];
```

## Instance methods

```
-[SBTraitsWindowParticipantDelegate init];
-[SBTraitsWindowParticipantDelegate participantAssociatedWindows:];
-[SBTraitsWindowParticipantDelegate didChangeSettingsForParticipant:context:];
-[SBTraitsWindowParticipantDelegate updatePreferencesForParticipant:updater:];
-[SBTraitsWindowParticipantDelegate appendDescriptionForParticipant:withBuilder:multilinePrefix:];
-[SBTraitsWindowParticipantDelegate participantAssociatedSceneIdentityTokens:];
-[SBTraitsWindowParticipantDelegate participantWillInvalidate:];
-[SBTraitsWindowParticipantDelegate _autorotationPreventionReasons:];
-[SBTraitsWindowParticipantDelegate _isWindowContentVisible:];
-[SBTraitsWindowParticipantDelegate _validatedSupportedInterfaceOrientations:forWindow:];
-[SBTraitsWindowParticipantDelegate _validationFailureReasonForWindow:];
-[SBTraitsWindowParticipantDelegate setParticipant:ownedByWindow:];
-[SBTraitsWindowParticipantDelegate validateSettingsForParticipant:validator:];
-[SBTraitsWindowParticipantDelegate windowDidUpdatePreferredWindowLevel:ownedParticipant:];
-[SBTraitsWindowParticipantDelegate windowDidUpdateSupportedOrientations:ownedParticipant:];
-[SBTraitsWindowParticipantDelegate windowWillBecomeHidden:ownedParticipant:];
-[SBTraitsWindowParticipantDelegate windowWillBecomeVisible:ownedParticipant:];
```
