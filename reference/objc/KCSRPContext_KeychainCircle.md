# `KCSRPContext`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
^{ccsrp_ctx=^{ccdigest_info}^{ccdh_gp}^{ccrng_state}{?=b1b1b1b16}[1Q]} _context;
^{ccrng_state=^?} _rng;
@"NSString" _user;
```

## Properties

```
@property (T^{ccsrp_ctx=^{ccdigest_info}^{ccdh_gp}^{ccrng_state}{?=b1b1b1b16}[1Q]},V_context) context;
@property (T^{ccrng_state=^?},V_rng) rng;
@property (T@"NSString",&,V_user) user;
```

## Class methods

```
+[KCSRPContext createWithUser:digestInfo:group:randomSource:];
```

## Instance methods

```
-[KCSRPContext isAuthenticated];
-[KCSRPContext setUser:];
-[KCSRPContext dealloc];
-[KCSRPContext setContext:];
-[KCSRPContext user];
-[KCSRPContext context];
-[KCSRPContext rng];
-[KCSRPContext setRng:];
-[KCSRPContext dataForPassword:];
-[KCSRPContext getKey];
-[KCSRPContext initWithUser:digestInfo:group:randomSource:];
-[KCSRPContext userNameString];
```
