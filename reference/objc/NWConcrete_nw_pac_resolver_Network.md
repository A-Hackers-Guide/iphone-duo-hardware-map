# `NWConcrete_nw_pac_resolver`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_pac_resolver`
- 15 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
@? result_block;
@"NSObject<OS_nw_context>" context;
^{__CFURL=} endpointURL;
^{__CFURL=} pacURL;
^{__CFString=} pacScript;
^{__CFData=} auditToken;
^{__CFString=} bundleIdentifier;
^{__CFRunLoopSource=} pacResolver;
^{__CFRunLoopTimer=} timeoutTimer;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} runloopLock;
[75c] logging_id_str;
b1 https_is_opaque;
b1 use_tls;
b1 should_trust_invalid_certs;
b1 is_dry_run;
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
-[NWConcrete_nw_pac_resolver init];
-[NWConcrete_nw_pac_resolver dealloc];
```
