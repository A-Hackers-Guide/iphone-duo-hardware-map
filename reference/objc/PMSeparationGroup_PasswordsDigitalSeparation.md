# `PMSeparationGroup`

- Image: [`/System/Library/DigitalSeparation/SharingSources/PasswordsDigitalSeparation.bundle/PasswordsDigitalSeparation`](../userland/System__Library__DigitalSeparation__SharingSources__PasswordsDigitalSeparation.bundle__PasswordsDigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSSharedResource`
- 2 instance variables, 10 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _participants;
@"KCSharingGroup" _group;
```

## Properties

```
@property (T@"KCSharingGroup",R,N,V_group) group;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayDetail;
@property (T@"NSArray",R,C,N,V_participants) participants;
@property (Tq,R,N) visibility;
@property (TQ,?,R,N) participationAccess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PMSeparationGroup visibility];
-[PMSeparationGroup displayName];
-[PMSeparationGroup group];
-[PMSeparationGroup description];
-[PMSeparationGroup participants];
-[PMSeparationGroup displayDetail];
-[PMSeparationGroup initWithGroup:participants:];
```
