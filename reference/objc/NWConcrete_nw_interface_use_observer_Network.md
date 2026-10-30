# `NWConcrete_nw_interface_use_observer`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_interface_use_observer`
- 4 instance variables, 4 properties, 1 instance methods, 0 class methods

## Instance variables

```
* notification_name;
{retained_ptr<NSObject<OS_dispatch_queue> *>="m_obj"@"NSObject<OS_dispatch_queue>""m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} client_queue;
{retained_ptr<void (^)(bool)>="m_obj"@?"m_should_release"b1"__pad_bits"b7"__pad_bytes"[7C]} update_block;
i notify_token;
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
-[NWConcrete_nw_interface_use_observer dealloc];
```
