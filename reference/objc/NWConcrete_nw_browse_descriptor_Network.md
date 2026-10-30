# `NWConcrete_nw_browse_descriptor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_browse_descriptor`
- 23 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
i type;
* bonjour_type;
* bonjour_domain;
* description;
* logging_description;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
@"NSObject<OS_dispatch_data>" custom_data;
@? browse_block;
* application_service_name;
* bundle_id;
I device_types;
I scope;
i invitation_scope;
i rssi_threshold;
@"NSObject<OS_nw_array>" device_filters;
* predicate;
Q predicate_len;
Q custom_service_length;
* custom_service;
b1 include_txt_record;
b1 sign_results;
b1 discover_application_service_endpoints_only;
b5 __pad_bits;
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
-[NWConcrete_nw_browse_descriptor init];
-[NWConcrete_nw_browse_descriptor dealloc];
-[NWConcrete_nw_browse_descriptor redactedDescription];
-[NWConcrete_nw_browse_descriptor description];
```
