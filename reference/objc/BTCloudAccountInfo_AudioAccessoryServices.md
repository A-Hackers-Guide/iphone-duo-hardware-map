# `BTCloudAccountInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _isSignedIn;
B _manateeAvailable;
@"NSString" _accountIdentifier;
@"NSString" _loginID;
```

## Properties

```
@property (TB,N,V_isSignedIn) isSignedIn;
@property (TB,N,V_manateeAvailable) manateeAvailable;
@property (T@"NSString",&,N,V_accountIdentifier) accountIdentifier;
@property (T@"NSString",&,N,V_loginID) loginID;
```

## Class methods

```
+[BTCloudAccountInfo supportsSecureCoding];
```

## Instance methods

```
-[BTCloudAccountInfo setAccountIdentifier:];
-[BTCloudAccountInfo setLoginID:];
-[BTCloudAccountInfo manateeAvailable];
-[BTCloudAccountInfo accountIdentifier];
-[BTCloudAccountInfo encodeWithCoder:];
-[BTCloudAccountInfo loginID];
-[BTCloudAccountInfo description];
-[BTCloudAccountInfo initWithCoder:];
-[BTCloudAccountInfo isSignedIn];
-[BTCloudAccountInfo setManateeAvailable:];
-[BTCloudAccountInfo setIsSignedIn:];
```
