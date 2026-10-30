# `_UISTouchAuthenticationVerifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _thresholds;
@"UISTransform3DGrader" _lenientGrader;
@"UISTransform3DGrader" _strictGrader;
B _shouldSuppressInauthenticTouches;
```

## Properties

```
@property (TB,R,N,V_shouldSuppressInauthenticTouches) shouldSuppressInauthenticTouches;
```

## Class methods

```
+[_UISTouchAuthenticationVerifier shouldAuthenticateServiceBundleId:];
+[_UISTouchAuthenticationVerifier verifierForServiceBundleId:];
```

## Instance methods

```
-[_UISTouchAuthenticationVerifier shouldSuppressInauthenticTouches];
-[_UISTouchAuthenticationVerifier transformGradeFailureReasonsForRecord:];
-[_UISTouchAuthenticationVerifier verifyRecord:];
```
