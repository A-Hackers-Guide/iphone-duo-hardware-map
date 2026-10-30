# `CTAuthenticationToken`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
q _scope;
@"NSString" _token;
```

## Properties

```
@property (Tq,R,N,V_scope) scope;
@property (T@"NSString",R,C,N,V_token) token;
```

## Class methods

```
+[CTAuthenticationToken supportsSecureCoding];
```

## Instance methods

```
-[CTAuthenticationToken scope];
-[CTAuthenticationToken encodeWithCoder:];
-[CTAuthenticationToken description];
-[CTAuthenticationToken initWithCoder:];
-[CTAuthenticationToken token];
-[CTAuthenticationToken initWithScope:token:];
```
