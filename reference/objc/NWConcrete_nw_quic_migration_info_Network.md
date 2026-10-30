# `NWConcrete_nw_quic_migration_info`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_quic_migration_info`
- 5 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_interface>" interface;
@"NSObject<OS_nw_endpoint>" remote_endpoint;
@"NSObject<OS_nw_endpoint>" local_endpoint;
b1 random_connection_id;
b63 flags;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWConcrete_nw_quic_migration_info init];
-[NWConcrete_nw_quic_migration_info dealloc];
```
