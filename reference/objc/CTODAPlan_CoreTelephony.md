# `CTODAPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTPlan`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _inBuddy;
@"NSString" _mcc;
@"NSString" _mnc;
@"NSString" _gid1;
@"NSString" _gid2;
@"NSString" _setupURL;
@"NSString" _handoffToken;
```

## Properties

```
@property (T@"NSString",R,N,V_mcc) mcc;
@property (T@"NSString",R,N,V_mnc) mnc;
@property (T@"NSString",R,N,V_gid1) gid1;
@property (T@"NSString",R,N,V_gid2) gid2;
@property (T@"NSString",R,N,V_setupURL) setupURL;
@property (T@"NSString",R,N,V_handoffToken) handoffToken;
@property (TB,R,N,V_inBuddy) inBuddy;
```

## Class methods

```
+[CTODAPlan supportsSecureCoding];
```

## Instance methods

```
-[CTODAPlan mnc];
-[CTODAPlan encodeWithCoder:];
-[CTODAPlan description];
-[CTODAPlan initWithCoder:];
-[CTODAPlan mcc];
-[CTODAPlan isEqual:];
-[CTODAPlan inBuddy];
-[CTODAPlan gid1];
-[CTODAPlan gid2];
-[CTODAPlan handoffToken];
-[CTODAPlan initWithSetupUrl:mcc:mnc:gid1:gid2:handoffToken:inBuddy:];
-[CTODAPlan setupURL];
```
