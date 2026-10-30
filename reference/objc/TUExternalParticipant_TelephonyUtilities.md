# `TUExternalParticipant`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCoding`
- 4 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" identifier;
? displayName;
? info;
q status;
```

## Properties

```
@property (T@"NSNumber",N,R,Videntifier) identifier;
@property (T@"NSString",N,R) displayName;
@property (T@"NSData",N,R) info;
@property (Tq,N,R,Vstatus) status;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[TUExternalParticipant supportsSecureCoding];
```

## Instance methods

```
-[TUExternalParticipant info];
-[TUExternalParticipant identifier];
-[TUExternalParticipant init];
-[TUExternalParticipant displayName];
-[TUExternalParticipant status];
-[TUExternalParticipant encodeWithCoder:];
-[TUExternalParticipant description];
-[TUExternalParticipant initWithCoder:];
-[TUExternalParticipant initWithIdentifier:displayName:info:status:];
```
