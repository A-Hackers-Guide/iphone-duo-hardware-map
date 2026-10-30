# `LACADMUserProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isAdministrator;
@property (TB,R,N) isDirectAdministrator;
@property (TB,R,N) isGuestUser;
@property (T@"NSString",R,N) groupName;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) fullName;
@property (Tq,R,N) userID;
@property (T@"NSUUID",R,N) userGUID;
@property (TB,R,N) isDeviceOwner;
```

## Instance methods

```
-[LACADMUserProtocol userID];
-[LACADMUserProtocol isAdministrator];
-[LACADMUserProtocol fullName];
-[LACADMUserProtocol groupName];
-[LACADMUserProtocol name];
-[LACADMUserProtocol isDeviceOwner];
-[LACADMUserProtocol isDirectAdministrator];
-[LACADMUserProtocol isGuestUser];
-[LACADMUserProtocol isMemberOfGroupWithName:];
-[LACADMUserProtocol userGUID];
```
