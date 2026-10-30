# `NWConcrete_nw_fd_wrapper`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_fd_wrapper`
- 5 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
i fd;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
Q guard;
b1 guarded;
b1 do_not_guard;
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
-[NWConcrete_nw_fd_wrapper dealloc];
-[NWConcrete_nw_fd_wrapper description];
```
