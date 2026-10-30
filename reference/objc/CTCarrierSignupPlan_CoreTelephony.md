# `CTCarrierSignupPlan`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTPlan`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _url;
@"NSString" _type;
q _option;
@"NSArray" _identifiers;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_url) url;
@property (T@"NSString",R,N,V_type) type;
@property (Tq,R,N,V_option) option;
@property (T@"NSArray",R,N,V_identifiers) identifiers;
```

## Class methods

```
+[CTCarrierSignupPlan supportsSecureCoding];
```

## Instance methods

```
-[CTCarrierSignupPlan identifiers];
-[CTCarrierSignupPlan option];
-[CTCarrierSignupPlan type];
-[CTCarrierSignupPlan encodeWithCoder:];
-[CTCarrierSignupPlan description];
-[CTCarrierSignupPlan initWithCoder:];
-[CTCarrierSignupPlan isEqual:];
-[CTCarrierSignupPlan name];
-[CTCarrierSignupPlan url];
-[CTCarrierSignupPlan initWithName:url:type:];
-[CTCarrierSignupPlan initWithName:url:type:option:identifiers:];
```
