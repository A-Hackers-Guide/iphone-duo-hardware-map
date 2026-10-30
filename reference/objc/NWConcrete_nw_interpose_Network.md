# `NWConcrete_nw_interpose`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_interpose`
- 9 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
[16C] client_uuid;
i delegated_pid;
i delegated_upid;
@"NSObject<OS_nw_path_evaluator>" evaluator;
@"NSObject<OS_nw_dictionary>" flows;
@? flow_event_handler;
@"NSObject<OS_nw_context>" context;
@"NSObject<OS_dispatch_queue>" client_queue;
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
-[NWConcrete_nw_interpose dealloc];
```
