# `NWConcrete_nw_resolution_report`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_resolution_report`
- 12 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q milliseconds;
* provider_name;
* extended_dns_error_extra_text;
@"NSObject<OS_nw_endpoint>" successful_endpoint;
@"NSObject<OS_nw_endpoint>" preferred_endpoint;
@"NSObject<OS_nw_array>" resolved_endpoints;
I endpoint_count;
i source;
i protocol;
S extended_dns_error_code;
b1 received_svcb;
b1 received_ech_config;
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
-[NWConcrete_nw_resolution_report init];
-[NWConcrete_nw_resolution_report dealloc];
-[NWConcrete_nw_resolution_report description];
```
