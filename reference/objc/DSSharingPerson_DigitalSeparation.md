# `DSSharingPerson`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"CNContact" _contact;
@"NSMutableDictionary" _sources;
@"NSMutableDictionary" _participantsBySource;
@"NSMutableDictionary" _sharedResourcesBySource;
@"NSString" _identifier;
@"NSMutableSet" _emailAddresses;
@"NSMutableSet" _names;
@"NSMutableSet" _phoneNumbers;
@"NSMutableDictionary" _shareDirectionBySourceName;
@"NSMapTable" _shareDirectionByResource;
```

## Properties

```
@property (Tq,R,N) score;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayGivenName;
@property (T@"NSString",R,C,N) localizedDetail;
@property (T@"NSArray",R,C,N) sortedSourceNames;
@property (T@"NSArray",R,C,N) allSources;
@property (T@"CNContact",R,N) contact;
@property (T@"NSArray",R,N) termsOfAddress;
```

## Class methods

```
+[DSSharingPerson initialize];
```

## Instance methods

```
-[DSSharingPerson contact];
-[DSSharingPerson init];
-[DSSharingPerson displayName];
-[DSSharingPerson score];
-[DSSharingPerson valueForKey:];
-[DSSharingPerson hash];
-[DSSharingPerson isEqual:];
-[DSSharingPerson termsOfAddress];
-[DSSharingPerson allSources];
-[DSSharingPerson localizedDetail];
-[DSSharingPerson addSource:sharedResource:participant:deviceOwnerRole:];
-[DSSharingPerson contactMatchingIdentity:];
-[DSSharingPerson displayGivenName];
-[DSSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:];
-[DSSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:contact:];
-[DSSharingPerson initWithSource:sharedResource:unknownParticipant:deviceOwnerRole:];
-[DSSharingPerson isMe:];
-[DSSharingPerson participationForSourceName:];
-[DSSharingPerson removeParticipant:fromSource:];
-[DSSharingPerson removeSourceWithName:];
-[DSSharingPerson shareDirectionForSharedResource:];
-[DSSharingPerson shareDirectionForSourceName:];
-[DSSharingPerson sharedResourcesForSourceName:];
-[DSSharingPerson sortedSourceNames];
-[DSSharingPerson stopAllSharingOnQueue:completion:];
-[DSSharingPerson stopSharingSourceNames:queue:completion:];
-[DSSharingPerson stopSharingSources:queue:completion:];
-[DSSharingPerson updateContactFromIdentity:];
-[DSSharingPerson updateContactFromParticipant:];
-[DSSharingPerson updateKnownEmailAddressesForParticipant:];
-[DSSharingPerson updateKnownNameForParticipant:];
-[DSSharingPerson updateKnownPhoneNumbersForParticipant:];
-[DSSharingPerson updateShareDirectionForParticipant:source:sharedResource:deviceOwnerRole:];
```
