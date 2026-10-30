# `CTPendingPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTPlan`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSString" _smdpURL;
@"NSString" _matchingID;
@"NSString" _iccidHash;
@"NSString" _signUpUrl;
@"NSString" _signUpUrlType;
```

## Properties

```
@property (T@"NSString",&,N,V_signUpUrl) signUpUrl;
@property (T@"NSString",&,N,V_signUpUrlType) signUpUrlType;
@property (T@"NSString",&,N,V_iccidHash) iccidHash;
@property (T@"NSString",R,N,V_smdpURL) smdpURL;
@property (T@"NSString",R,N,V_matchingID) matchingID;
```

## Class methods

```
+[CTPendingPlan supportsSecureCoding];
```

## Instance methods

```
-[CTPendingPlan encodeWithCoder:];
-[CTPendingPlan description];
-[CTPendingPlan initWithCoder:];
-[CTPendingPlan copyWithZone:];
-[CTPendingPlan isEqual:];
-[CTPendingPlan smdpURL];
-[CTPendingPlan iccidHash];
-[CTPendingPlan initWithSmdpURL:matchingID:iccidHash:];
-[CTPendingPlan matchingID];
-[CTPendingPlan setIccidHash:];
-[CTPendingPlan setSignUpUrl:];
-[CTPendingPlan setSignUpUrlType:];
-[CTPendingPlan signUpUrl];
-[CTPendingPlan signUpUrlType];
```
