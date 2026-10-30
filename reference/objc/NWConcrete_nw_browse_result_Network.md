# `NWConcrete_nw_browse_result`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_browse_result`
- 9 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" endpoint;
@"NSObject<OS_nw_array>" interfaces;
@"NSObject<OS_nw_txt_record>" txt_record;
* description;
* logging_description;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
b1 immutable;
b1 discovered_from_path;
b6 __pad_bits;
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
-[NWConcrete_nw_browse_result dealloc];
-[NWConcrete_nw_browse_result redactedDescription];
-[NWConcrete_nw_browse_result description];
```
