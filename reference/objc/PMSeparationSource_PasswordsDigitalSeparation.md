# `PMSeparationSource`

- Image: [`/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`](../userland/System__Library__DigitalSeparation__SharingSources__PasswordsDigitalSeparation.bundle__PasswordsDigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSSource`
- 1 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"CNContactStore" _contactStore;
```

## Properties

```
@property (T@"NSString",R,C,N) name;
@property (T@"NSArray",?,R,C,N) resourceNames;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PMSeparationSource init];
-[PMSeparationSource name];
-[PMSeparationSource stopAllSharingWithCompletion:];
-[PMSeparationSource _participantIdentityWithHandle:];
-[PMSeparationSource _fetchGroupsExcludingInvitationsWithCompletionHandler:];
-[PMSeparationSource _groupsAndParticipantsMatchingHandle:completionHandler:];
-[PMSeparationSource _leaveGroup:completionHandler:];
-[PMSeparationSource _passwordsGroupWithGroup:];
-[PMSeparationSource _passwordsParticipantWithParticipant:];
-[PMSeparationSource _removeAllOtherParticipantsFromGroup:completionHandler:];
-[PMSeparationSource _removeParticipant:fromGroup:completionHandler:];
-[PMSeparationSource _stopSharingWithGroup:completionHandler:];
-[PMSeparationSource _stopSharingWithGroups:completionHandler:];
-[PMSeparationSource _stopSharingWithParticipant:inGroup:completionHandler:];
-[PMSeparationSource _stopSharingWithParticipantsMatchingHandle:completionHandler:];
-[PMSeparationSource fetchSharedResourcesWithCompletion:];
-[PMSeparationSource stopSharing:withCompletion:];
-[PMSeparationSource stopSharingWithParticipant:completion:];
```
