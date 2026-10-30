# `NWConcrete_nw_path_observer`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_path_observer`
- 6 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" client_queue;
@? update_block;
@"NSObject<OS_nw_dictionary>" known_paths;
@"NSObject<OS_nw_fd_wrapper>" fd;
^v source;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
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
-[NWConcrete_nw_path_observer init];
-[NWConcrete_nw_path_observer dealloc];
```
