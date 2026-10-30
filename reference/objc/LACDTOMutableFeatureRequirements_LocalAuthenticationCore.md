# `LACDTOMutableFeatureRequirements`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOFeatureRequirements`
- 1 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
? requirements;
```

## Properties

```
@property (T@"NSArray",N,C) requirements;
@property (TB,N,R) hasUnsatisfiedRequirements;
@property (T@"NSString",N,R) description;
@property (Tq,N,R) hash;
```

## Class methods

```
+[LACDTOMutableFeatureRequirements nullInstance];
```

## Instance methods

```
-[LACDTOMutableFeatureRequirements init];
-[LACDTOMutableFeatureRequirements hash];
-[LACDTOMutableFeatureRequirements description];
-[LACDTOMutableFeatureRequirements requirements];
-[LACDTOMutableFeatureRequirements isEqual:];
-[LACDTOMutableFeatureRequirements setRequirements:];
-[LACDTOMutableFeatureRequirements addRequirement:];
-[LACDTOMutableFeatureRequirements hasUnsatisfiedRequirements];
-[LACDTOMutableFeatureRequirements isSatisfied:];
```
