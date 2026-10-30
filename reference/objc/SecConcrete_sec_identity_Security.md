# `SecConcrete_sec_identity`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_sec_identity`
- 12 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{__SecIdentity=} identity;
^{__CFArray=} certs;
@? sign_block;
@? decrypt_block;
@"NSObject<OS_dispatch_queue>" operation_queue;
S type;
@"NSObject<OS_dispatch_data>" spake2_context;
@"NSObject<OS_dispatch_data>" client_identity;
@"NSObject<OS_dispatch_data>" server_identity;
@"NSObject<OS_dispatch_data>" client_password_verifier;
@"NSObject<OS_dispatch_data>" server_password_verifier;
@"NSObject<OS_dispatch_data>" registration_record;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SecConcrete_sec_identity dealloc];
-[SecConcrete_sec_identity initWithIdentity:];
-[SecConcrete_sec_identity initWithCertificates:signBlock:decryptBlock:queue:];
-[SecConcrete_sec_identity initWithIdentityAndCertificates:certificates:];
-[SecConcrete_sec_identity initWithSPAKE2PLUSV1Context:clientIdentity:serverIdentity:clientPasswordVerifier:serverPasswordVerifier:registrationRecord:];
```
