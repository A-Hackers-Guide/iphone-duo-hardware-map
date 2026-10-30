# `CTPlanSignUpDetails`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _signUpUrl;
@"NSString" _signUpUrlType;
```

## Properties

```
@property (T@"NSString",&,N,V_signUpUrl) signUpUrl;
@property (T@"NSString",&,N,V_signUpUrlType) signUpUrlType;
```

## Class methods

```
+[CTPlanSignUpDetails supportsSecureCoding];
```

## Instance methods

```
-[CTPlanSignUpDetails encodeWithCoder:];
-[CTPlanSignUpDetails description];
-[CTPlanSignUpDetails initWithCoder:];
-[CTPlanSignUpDetails isEqual:];
-[CTPlanSignUpDetails initWithSignUpUrl:signUpUrlType:];
-[CTPlanSignUpDetails setSignUpUrl:];
-[CTPlanSignUpDetails setSignUpUrlType:];
-[CTPlanSignUpDetails signUpUrl];
-[CTPlanSignUpDetails signUpUrlType];
```
