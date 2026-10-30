# `CTSubscriberAlgorithmEAPAKA`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTSubscriberAlgorithm`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSData" _rand;
@"NSData" _autn;
```

## Properties

```
@property (T@"NSData",&,N,V_rand) rand;
@property (T@"NSData",&,N,V_autn) autn;
```

## Class methods

```
+[CTSubscriberAlgorithmEAPAKA supportsSecureCoding];
```

## Instance methods

```
-[CTSubscriberAlgorithmEAPAKA encodeWithCoder:];
-[CTSubscriberAlgorithmEAPAKA initWithCoder:];
-[CTSubscriberAlgorithmEAPAKA autn];
-[CTSubscriberAlgorithmEAPAKA rand];
-[CTSubscriberAlgorithmEAPAKA setAutn:];
-[CTSubscriberAlgorithmEAPAKA setRand:];
```
