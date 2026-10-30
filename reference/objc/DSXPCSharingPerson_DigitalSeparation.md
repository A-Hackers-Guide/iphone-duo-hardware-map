# `DSXPCSharingPerson`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSPersonDescribable`
- 12 instance variables, 11 properties, 35 instance methods, 2 class methods

## Instance variables

```
@"CNContact" _contact;
@"NSMutableSet" _sources;
@"NSMutableDictionary" _participantsBySource;
@"NSString" _identifier;
@"NSMutableSet" _emailAddresses;
@"NSMutableDictionary" _unblockedEmails;
@"NSMutableSet" _names;
@"NSMutableSet" _phoneNumbers;
@"NSMutableDictionary" _sharedResourcesBySource;
@"NSMutableDictionary" _shareDirectionBySourceName;
@"NSMapTable" _shareDirectionByResource;
@"NSNumber" _priority;
```

## Properties

```
@property (T@"CNContact",R,N,V_contact) contact;
@property (T@"NSArray",R,N) sourceNames;
@property (T@"NSArray",R,C,N) sortedSourceNames;
@property (T@"NSArray",R,C,N) sortedUnsavedUnblockedEmails;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayGivenName;
@property (T@"NSArray",R,N) termsOfAddress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSXPCSharingPerson initialize];
+[DSXPCSharingPerson sortedXPCArray:];
```

## Instance methods

```
-[DSXPCSharingPerson contact];
-[DSXPCSharingPerson addName:];
-[DSXPCSharingPerson init];
-[DSXPCSharingPerson displayName];
-[DSXPCSharingPerson hash];
-[DSXPCSharingPerson isEqual:];
-[DSXPCSharingPerson termsOfAddress];
-[DSXPCSharingPerson sourceNames];
-[DSXPCSharingPerson isBlockedEmail:];
-[DSXPCSharingPerson localizedDetail];
-[DSXPCSharingPerson isUnsavedEmail:];
-[DSXPCSharingPerson _setPriority];
-[DSXPCSharingPerson addSource:sharedResource:participant:deviceOwnerRole:];
-[DSXPCSharingPerson alertTextForSource:];
-[DSXPCSharingPerson blockUnsavedEmailAddresses:];
-[DSXPCSharingPerson detailTextForSource:];
-[DSXPCSharingPerson displayGivenName];
-[DSXPCSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:contact:];
-[DSXPCSharingPerson initWithSource:sharedResource:participant:deviceOwnerRole:unknownHandle:];
-[DSXPCSharingPerson isIdentity:];
-[DSXPCSharingPerson isMe:];
-[DSXPCSharingPerson participationForSources:];
-[DSXPCSharingPerson removeSources:];
-[DSXPCSharingPerson shareDirectionForSharedResource:];
-[DSXPCSharingPerson shareDirectionForSourceName:];
-[DSXPCSharingPerson sharedResourcesForSourceName:];
-[DSXPCSharingPerson sharingSourcesForUnsavedUnblockedEmail:];
-[DSXPCSharingPerson sortedSourceNames];
-[DSXPCSharingPerson sortedUnsavedUnblockedEmails];
-[DSXPCSharingPerson updateContactFromIdentity:];
-[DSXPCSharingPerson updateKnownEmailAddressesForContact];
-[DSXPCSharingPerson updateKnownEmailAddressesForParticipant:source:];
-[DSXPCSharingPerson updateKnownNameForParticipant:];
-[DSXPCSharingPerson updateKnownPhoneNumbersForParticipant:];
-[DSXPCSharingPerson updateShareDirectionForParticipant:source:sharedResource:deviceOwnerRole:];
```
