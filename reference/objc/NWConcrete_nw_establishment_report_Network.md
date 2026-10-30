# `NWConcrete_nw_establishment_report`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_establishment_report`
- 13 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
Q attempt_started_after_milliseconds;
Q duration_milliseconds;
Q resolution_started_after_milliseconds;
Q flow_started_after_milliseconds;
@"NSObject<OS_nw_array>" proxy_endpoints;
@"NSObject<OS_nw_array>" proxied_next_hop_endpoints;
i privacy_stance;
@"NSObject<OS_nw_array>" protocol_reports;
@"NSObject<OS_nw_array>" resolution_reports;
I previous_attempt_count;
b1 proxy_configured;
b1 used_proxy;
b7 __pad_bits;
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
-[NWConcrete_nw_establishment_report init];
-[NWConcrete_nw_establishment_report dealloc];
-[NWConcrete_nw_establishment_report description];
```
