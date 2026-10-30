# `DSXPCSharedResource`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSSharedResource`, `NSSecureCoding`
- 5 instance variables, 14 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _participantArray;
@"NSString" _name;
@"NSString" _detail;
@"NSNumber" _resourceVisibility;
@"NSNumber" _access;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_detail) detail;
@property (T@"NSNumber",N,V_resourceVisibility) resourceVisibility;
@property (T@"NSNumber",N,V_access) access;
@property (T@"NSArray",&,N,V_participantArray) participantArray;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) displayDetail;
@property (T@"NSArray",R,C,N) participants;
@property (Tq,R,N) visibility;
@property (TQ,?,R,N) participationAccess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSXPCSharedResource supportsSecureCoding];
```

## Instance methods

```
-[DSXPCSharedResource visibility];
-[DSXPCSharedResource displayName];
-[DSXPCSharedResource detail];
-[DSXPCSharedResource access];
-[DSXPCSharedResource encodeWithCoder:];
-[DSXPCSharedResource setAccess:];
-[DSXPCSharedResource setName:];
-[DSXPCSharedResource initWithCoder:];
-[DSXPCSharedResource setDetail:];
-[DSXPCSharedResource participants];
-[DSXPCSharedResource name];
-[DSXPCSharedResource initWithResource:];
-[DSXPCSharedResource displayDetail];
-[DSXPCSharedResource participationAccess];
-[DSXPCSharedResource initPrivateResourceWithName:detail:participants:];
-[DSXPCSharedResource participantArray];
-[DSXPCSharedResource resourceVisibility];
-[DSXPCSharedResource setParticipantArray:];
-[DSXPCSharedResource setResourceVisibility:];
```
