# `TUContinuityCallInfo`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isBranded;
B _isEmergency;
B _handlesBlocked;
@"NSString" _callIdentifier;
@"NSString" _callerIdSubstring;
@"NSString" _displayName;
@"NSDictionary" _contactIdentifiersByHandle;
@"NSString" _senderIdentityShortName;
@"NSString" _senderIdentityName;
@"NSData" _handlesHash;
```

## Properties

```
@property (T@"NSString",R,N,V_callIdentifier) callIdentifier;
@property (T@"NSString",R,N,V_callerIdSubstring) callerIdSubstring;
@property (T@"NSString",R,N,V_displayName) displayName;
@property (TB,R,N,V_isBranded) isBranded;
@property (TB,R,N,V_isEmergency) isEmergency;
@property (T@"NSDictionary",R,N,V_contactIdentifiersByHandle) contactIdentifiersByHandle;
@property (T@"NSString",R,N,V_senderIdentityShortName) senderIdentityShortName;
@property (T@"NSString",R,N,V_senderIdentityName) senderIdentityName;
@property (T@"NSData",R,N,V_handlesHash) handlesHash;
@property (TB,R,N,V_handlesBlocked) handlesBlocked;
```

## Class methods

```
+[TUContinuityCallInfo supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityCallInfo isEmergency];
-[TUContinuityCallInfo displayName];
-[TUContinuityCallInfo encodeWithCoder:];
-[TUContinuityCallInfo description];
-[TUContinuityCallInfo initWithCoder:];
-[TUContinuityCallInfo copyWithZone:];
-[TUContinuityCallInfo callIdentifier];
-[TUContinuityCallInfo callerIdSubstring];
-[TUContinuityCallInfo contactIdentifiersByHandle];
-[TUContinuityCallInfo handlesBlocked];
-[TUContinuityCallInfo handlesHash];
-[TUContinuityCallInfo initWithCallIdentifier:callerIdSubstring:displayName:isBranded:isEmergency:contactIdentifiersByHandle:senderIdentityShortName:senderIdentityName:handlesHash:handlesBlocked:];
-[TUContinuityCallInfo isBranded];
-[TUContinuityCallInfo senderIdentityName];
-[TUContinuityCallInfo senderIdentityShortName];
```
