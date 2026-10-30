# `ValidationResponse`

- Image: [`/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity`](../userland/System__Library__PrivateFrameworks__EDPSecurity.framework__EDPSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B isTrusted;
@"NSData" validatedData;
@"NSArray" certificateChain;
```

## Properties

```
@property (T@"NSData",&,N,VvalidatedData) validatedData;
@property (TB,N,VisTrusted) isTrusted;
@property (T@"NSArray",&,N,VcertificateChain) certificateChain;
```

## Instance methods

```
-[ValidationResponse isTrusted];
-[ValidationResponse setIsTrusted:];
-[ValidationResponse validatedData];
-[ValidationResponse certificateChain];
-[ValidationResponse setCertificateChain:];
-[ValidationResponse setValidatedData:];
```
