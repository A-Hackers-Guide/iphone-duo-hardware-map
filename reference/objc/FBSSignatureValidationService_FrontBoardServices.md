# `FBSSignatureValidationService`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSApplicationTrustDataProvider`
- 2 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<_FBSMISInterfaceWrapper>" _misInterfaceWrapper;
B _authoritative;
```

## Properties

```
@property (TB,N,V_authoritative) authoritative;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSignatureValidationService init];
-[FBSSignatureValidationService _initWithMISInterfaceWrapper:];
-[FBSSignatureValidationService _logTrustState:forApp:reason:];
-[FBSSignatureValidationService _validateApp:];
-[FBSSignatureValidationService _validateAppStoreApp:];
-[FBSSignatureValidationService _validateNonAppStoreApp:];
-[FBSSignatureValidationService authoritative];
-[FBSSignatureValidationService setAuthoritative:];
-[FBSSignatureValidationService signatureVersionForApp:];
-[FBSSignatureValidationService trustStateForApplication:];
```
