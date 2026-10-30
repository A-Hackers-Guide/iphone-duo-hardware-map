# `SecExternalPreSharedKey`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSData" _external_identity;
@"NSData" _epsk;
@"NSData" _context;
```

## Properties

```
@property (T@"NSData",&,V_external_identity) external_identity;
@property (T@"NSData",&,V_epsk) epsk;
@property (T@"NSData",&,V_context) context;
```

## Instance methods

```
-[SecExternalPreSharedKey setContext:];
-[SecExternalPreSharedKey context];
-[SecExternalPreSharedKey initWithExternalIdentity:::];
-[SecExternalPreSharedKey epsk];
-[SecExternalPreSharedKey external_identity];
-[SecExternalPreSharedKey setEpsk:];
-[SecExternalPreSharedKey setExternal_identity:];
```
