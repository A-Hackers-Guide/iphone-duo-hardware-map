# `LACADMUser`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACADMUserProtocol`
- 0 instance variables, 13 properties, 10 instance methods, 9 class methods

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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACADMUser currentUser];
+[LACADMUser allLocalUsers];
+[LACADMUser findUserByID:searchParent:];
+[LACADMUser findUserByName:searchParent:];
+[LACADMUser isUserNameUnique:searchParent:];
+[LACADMUser namesFromUsersWithUIDs:];
+[LACADMUser namesFromUsersWithUIDs:presentInGroupWithName:];
+[LACADMUser rootUser];
+[LACADMUser shouldDisplayUser:];
```

## Instance methods

```
-[LACADMUser userID];
-[LACADMUser isAdministrator];
-[LACADMUser fullName];
-[LACADMUser groupName];
-[LACADMUser name];
-[LACADMUser isDeviceOwner];
-[LACADMUser isDirectAdministrator];
-[LACADMUser isGuestUser];
-[LACADMUser isMemberOfGroupWithName:];
-[LACADMUser userGUID];
```
