# `NWAdvertiseDescriptor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_advertise_descriptor>" _internalDescriptor;
```

## Properties

```
@property (T@"NSObject<OS_nw_advertise_descriptor>",&,N,V_internalDescriptor) internalDescriptor;
@property (T@"NSString",R,N) bonjourServiceDomain;
@property (T@"NSString",R,N) bonjourServiceType;
@property (T@"NSString",R,N) bonjourServiceName;
@property (T@"NSData",&,N) txtRecord;
```

## Instance methods

```
-[NWAdvertiseDescriptor txtRecord];
-[NWAdvertiseDescriptor initWithDescriptor:];
-[NWAdvertiseDescriptor setTxtRecord:];
-[NWAdvertiseDescriptor privateDescription];
-[NWAdvertiseDescriptor descriptionWithIndent:showFullContent:];
-[NWAdvertiseDescriptor bonjourServiceType];
-[NWAdvertiseDescriptor description];
-[NWAdvertiseDescriptor copyWithZone:];
-[NWAdvertiseDescriptor bonjourServiceDomain];
-[NWAdvertiseDescriptor bonjourServiceName];
-[NWAdvertiseDescriptor initWithName:type:domain:];
-[NWAdvertiseDescriptor internalDescriptor];
-[NWAdvertiseDescriptor setInternalDescriptor:];
```
