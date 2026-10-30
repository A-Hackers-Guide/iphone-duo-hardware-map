# `LAAccessKey`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<LAKeyStoreKey>" _key;
@"NSString" _identifier;
@"LAACL" _acl;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"LAACL",R,N,V_acl) acl;
```

## Instance methods

```
-[LAAccessKey acl];
-[LAAccessKey identifier];
-[LAAccessKey initWithKey:];
-[LAAccessKey isEqual:];
-[LAAccessKey armInContext:completion:];
-[LAAccessKey armInContext:options:completion:];
-[LAAccessKey initWithACL:];
-[LAAccessKey unlockKey:inContext:userInfo:completion:];
```
