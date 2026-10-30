# `DSContactIdentity`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSIdentifiable`
- 4 instance variables, 8 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _email;
@"NSString" _phone;
@"NSPersonNameComponents" nameComponents;
@"NSString" unifiedContactIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N,VunifiedContactIdentifier) unifiedContactIdentifier;
@property (T@"NSPersonNameComponents",R,C,N,VnameComponents) nameComponents;
@property (T@"NSString",R,C,N) emailAddress;
@property (T@"NSString",R,C,N) phoneNumber;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSContactIdentity phoneNumber];
-[DSContactIdentity emailAddress];
-[DSContactIdentity nameComponents];
-[DSContactIdentity unifiedContactIdentifier];
-[DSContactIdentity initWithEmail:withPhone:];
```
