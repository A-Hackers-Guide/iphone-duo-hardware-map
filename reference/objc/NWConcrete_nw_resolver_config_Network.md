# `NWConcrete_nw_resolver_config`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_resolver_config`
- 7 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
{retained_ptr<NSObject<OS_xpc_object> *>="m_obj"@"NSObject<OS_xpc_object>""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} dictionary;
[16C] identifier;
{retained_ptr<NSObject<OS_dispatch_source> *>="m_obj"@"NSObject<OS_dispatch_source>""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} kernel_event_source;
{retained_ptr<NSObject<OS_nw_fd_wrapper> *>="m_obj"@"NSObject<OS_nw_fd_wrapper>""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} kernel_event_wrapper;
{retained_ptr<NSObject<OS_nw_fd_wrapper> *>="m_obj"@"NSObject<OS_nw_fd_wrapper>""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} agent_fd;
{unfair_mutex="m_mutex"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
I generation;
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
-[NWConcrete_nw_resolver_config init];
-[NWConcrete_nw_resolver_config dealloc];
-[NWConcrete_nw_resolver_config description];
```
