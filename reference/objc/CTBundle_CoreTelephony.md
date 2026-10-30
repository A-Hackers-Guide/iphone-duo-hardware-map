# `CTBundle`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _type;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
```

## Class methods

```
+[CTBundle supportsSecureCoding];
```

## Instance methods

```
-[CTBundle ct_shortDescription];
-[CTBundle init];
-[CTBundle ct_shortName];
-[CTBundle setType:];
-[CTBundle type];
-[CTBundle encodeWithCoder:];
-[CTBundle description];
-[CTBundle initWithCoder:];
-[CTBundle copyWithZone:];
-[CTBundle initWithBundleType:];
```
