# `LACClientInfo`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bundleId;
@"NSString" _displayName;
```

## Properties

```
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (T@"NSString",R,N,V_displayName) displayName;
```

## Class methods

```
+[LACClientInfo supportsSecureCoding];
+[LACClientInfo emptyClientInfo];
```

## Instance methods

```
-[LACClientInfo displayName];
-[LACClientInfo bundleId];
-[LACClientInfo encodeWithCoder:];
-[LACClientInfo description];
-[LACClientInfo initWithCoder:];
-[LACClientInfo initWithBundleId:displayName:];
```
