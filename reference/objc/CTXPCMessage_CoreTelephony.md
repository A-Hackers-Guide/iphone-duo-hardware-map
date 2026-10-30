# `CTXPCMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `CTXPCLogging`
- 1 instance variables, 3 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _namedArguments;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_namedArguments) namedArguments;
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
```

## Class methods

```
+[CTXPCMessage supportsSecureCoding];
+[CTXPCMessage allowedClassesForArguments];
+[CTXPCMessage isSensitiveMessage];
```

## Instance methods

```
-[CTXPCMessage ct_shortDescription];
-[CTXPCMessage init];
-[CTXPCMessage ct_shortName];
-[CTXPCMessage encodeWithCoder:];
-[CTXPCMessage description];
-[CTXPCMessage initWithCoder:];
-[CTXPCMessage isEqual:];
-[CTXPCMessage initWithNamedArguments:];
-[CTXPCMessage namedArguments];
-[CTXPCMessage setNamedArguments:];
```
