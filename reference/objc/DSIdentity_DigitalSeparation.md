# `DSIdentity`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSIdentifiable`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 14 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayName;
@"NSString" _identifier;
@"NSPersonNameComponents" _identityNameComponents;
@"NSString" _email;
@"NSString" _phone;
```

## Properties

```
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"NSPersonNameComponents",&,N,V_identityNameComponents) identityNameComponents;
@property (T@"NSString",&,N,V_email) email;
@property (T@"NSString",&,N,V_phone) phone;
@property (T@"NSString",R,N) ds_identifier;
@property (T@"NSString",&,N,V_displayName) displayName;
@property (T@"NSString",R,C,N) unifiedContactIdentifier;
@property (T@"NSPersonNameComponents",R,C,N) nameComponents;
@property (T@"NSString",R,C,N) emailAddress;
@property (T@"NSString",R,C,N) phoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSIdentity supportsSecureCoding];
```

## Instance methods

```
-[DSIdentity phoneNumber];
-[DSIdentity emailAddress];
-[DSIdentity email];
-[DSIdentity identifier];
-[DSIdentity displayName];
-[DSIdentity phone];
-[DSIdentity setDisplayName:];
-[DSIdentity initWithContact:];
-[DSIdentity initWithIdentity:];
-[DSIdentity setIdentifier:];
-[DSIdentity nameComponents];
-[DSIdentity encodeWithCoder:];
-[DSIdentity initWithCoder:];
-[DSIdentity copyWithZone:];
-[DSIdentity isEqual:];
-[DSIdentity setPhone:];
-[DSIdentity initWithEmail:];
-[DSIdentity setEmail:];
-[DSIdentity unifiedContactIdentifier];
-[DSIdentity isLikeIdentity:];
-[DSIdentity ds_identifier];
-[DSIdentity identityNameComponents];
-[DSIdentity initWithPhone:];
-[DSIdentity setIdentityNameComponents:];
```
