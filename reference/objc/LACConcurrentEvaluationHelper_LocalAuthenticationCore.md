# `LACConcurrentEvaluationHelper`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"_TtC23LocalAuthenticationCore32LACConcurrentEvaluationAllowList" allowList;
@"LACFlags" flags;
@"LACSDKHelper" sdkHelper;
```

## Properties

```
@property (T@"_TtC23LocalAuthenticationCore32LACConcurrentEvaluationAllowList",N,&,VallowList) allowList;
@property (T@"LACFlags",N,&,Vflags) flags;
@property (T@"LACSDKHelper",N,&,VsdkHelper) sdkHelper;
@property (TB,N,R) isConcurrentEvaluationAvailable;
@property (TB,N,R) isConcurrentEvaluationEnabled;
```

## Class methods

```
+[LACConcurrentEvaluationHelper sharedInstance];
```

## Instance methods

```
-[LACConcurrentEvaluationHelper setFlags:];
-[LACConcurrentEvaluationHelper flags];
-[LACConcurrentEvaluationHelper init];
-[LACConcurrentEvaluationHelper allowList];
-[LACConcurrentEvaluationHelper setAllowList:];
-[LACConcurrentEvaluationHelper isConcurrentEvaluationAvailable];
-[LACConcurrentEvaluationHelper isClientAllowListedWithClientInfo:];
-[LACConcurrentEvaluationHelper isConcurrentEvaluationEnabled];
-[LACConcurrentEvaluationHelper isConcurrentEvaluationEnabledForClientInfo:];
-[LACConcurrentEvaluationHelper sdkHelper];
-[LACConcurrentEvaluationHelper setSdkHelper:];
```
