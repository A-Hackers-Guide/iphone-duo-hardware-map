# `CTServiceDescriptor`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 3 instance variables, 5 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"NSString" _identifier;
q _domain;
@"NSNumber" _instance;
```

## Properties

```
@property (Tq,N,V_domain) domain;
@property (T@"NSNumber",&,N,V_instance) instance;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
```

## Class methods

```
+[CTServiceDescriptor supportsSecureCoding];
+[CTServiceDescriptor telephonyDescriptorWithInstance:];
+[CTServiceDescriptor descriptorWithSubscriptionContext:];
```

## Instance methods

```
-[CTServiceDescriptor setDomain:];
-[CTServiceDescriptor ct_shortDescription];
-[CTServiceDescriptor setInstance:];
-[CTServiceDescriptor domain];
-[CTServiceDescriptor identifier];
-[CTServiceDescriptor ct_shortName];
-[CTServiceDescriptor instance];
-[CTServiceDescriptor encodeWithCoder:];
-[CTServiceDescriptor hash];
-[CTServiceDescriptor description];
-[CTServiceDescriptor initWithCoder:];
-[CTServiceDescriptor copyWithZone:];
-[CTServiceDescriptor isEqual:];
-[CTServiceDescriptor initWithDomain:instance:];
```
