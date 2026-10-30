# `PMSeparationParticipantIdentity`

- Image: [`/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`](../userland/System__Library__DigitalSeparation__SharingSources__PasswordsDigitalSeparation.bundle__PasswordsDigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSIdentifiable`
- 3 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _contactIdentifier;
@"NSString" _emailAddress;
@"NSString" _phoneNumber;
```

## Properties

```
@property (T@"NSString",R,C,N,V_contactIdentifier) unifiedContactIdentifier;
@property (T@"NSPersonNameComponents",R,C,N) nameComponents;
@property (T@"NSString",R,C,N,V_emailAddress) emailAddress;
@property (T@"NSString",R,C,N,V_phoneNumber) phoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PMSeparationParticipantIdentity phoneNumber];
-[PMSeparationParticipantIdentity emailAddress];
-[PMSeparationParticipantIdentity initWithEmailAddress:];
-[PMSeparationParticipantIdentity initWithContactIdentifier:];
-[PMSeparationParticipantIdentity nameComponents];
-[PMSeparationParticipantIdentity initWithPhoneNumber:];
-[PMSeparationParticipantIdentity unifiedContactIdentifier];
```
