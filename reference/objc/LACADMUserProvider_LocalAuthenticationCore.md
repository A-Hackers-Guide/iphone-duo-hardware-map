# `LACADMUserProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACADMUserProviding`
- 0 instance variables, 4 properties, 9 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACADMUserProvider sharedInstance];
```

## Instance methods

```
-[LACADMUserProvider currentUser];
-[LACADMUserProvider allLocalUsers];
-[LACADMUserProvider findUserByID:searchParent:];
-[LACADMUserProvider findUserByName:searchParent:];
-[LACADMUserProvider isUserNameUnique:searchParent:];
-[LACADMUserProvider namesFromUsersWithUIDs:];
-[LACADMUserProvider namesFromUsersWithUIDs:presentInGroupWithName:];
-[LACADMUserProvider rootUser];
-[LACADMUserProvider shouldDisplayUser:];
```
