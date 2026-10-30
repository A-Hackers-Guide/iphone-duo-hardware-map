# `SecOfferedPAKEIdentity`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
S _pake_scheme;
@"NSData" _client_identity;
@"NSData" _server_identity;
```

## Properties

```
@property (T@"NSData",&,V_client_identity) client_identity;
@property (T@"NSData",&,V_server_identity) server_identity;
@property (TS,V_pake_scheme) pake_scheme;
```

## Instance methods

```
-[SecOfferedPAKEIdentity client_identity];
-[SecOfferedPAKEIdentity server_identity];
-[SecOfferedPAKEIdentity setPake_scheme:];
-[SecOfferedPAKEIdentity initWithClientIdentity:::];
-[SecOfferedPAKEIdentity pake_scheme];
-[SecOfferedPAKEIdentity setClient_identity:];
-[SecOfferedPAKEIdentity setServer_identity:];
```
