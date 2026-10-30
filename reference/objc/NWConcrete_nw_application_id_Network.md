# `NWConcrete_nw_application_id`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_application_id`
- 11 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
[16C] uuid;
I signature_length;
[32C] signature_data;
* originating_process;
* bundle_id;
[16C] persona_id;
B is_bundle_id_external;
{?="val"[8I]} audit_token;
i pid;
i system_service;
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
-[NWConcrete_nw_application_id dealloc];
-[NWConcrete_nw_application_id redactedDescription];
-[NWConcrete_nw_application_id description];
```
