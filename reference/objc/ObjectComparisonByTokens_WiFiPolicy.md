# `ObjectComparisonByTokens`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 17 instance methods, 1 class methods

## Instance variables

```
Q _sameTokensCount;
Q _diffTokensCount;
Q _distance;
@ _obj1;
@ _obj2;
@ _reference;
```

## Properties

```
@property (TQ,N,V_sameTokensCount) sameTokensCount;
@property (TQ,N,V_diffTokensCount) diffTokensCount;
@property (TQ,N,V_distance) distance;
@property (T@,&,N,V_obj1) obj1;
@property (T@,&,N,V_obj2) obj2;
@property (T@,&,N,V_reference) reference;
```

## Class methods

```
+[ObjectComparisonByTokens addComparison:to:ifMinOverlap:];
```

## Instance methods

```
-[ObjectComparisonByTokens distance];
-[ObjectComparisonByTokens setDistance:];
-[ObjectComparisonByTokens description];
-[ObjectComparisonByTokens reference];
-[ObjectComparisonByTokens setReference:];
-[ObjectComparisonByTokens diffTokensCount];
-[ObjectComparisonByTokens sameTokensCount];
-[ObjectComparisonByTokens accountForadditionalLength];
-[ObjectComparisonByTokens incrementDistanceWith:];
-[ObjectComparisonByTokens incrementTokensWith:];
-[ObjectComparisonByTokens initWithObj1:obj2:reference:];
-[ObjectComparisonByTokens obj1];
-[ObjectComparisonByTokens obj2];
-[ObjectComparisonByTokens setDiffTokensCount:];
-[ObjectComparisonByTokens setObj1:];
-[ObjectComparisonByTokens setObj2:];
-[ObjectComparisonByTokens setSameTokensCount:];
```
