# `NWConcrete_nw_txt_record`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_txt_record`
- 6 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
* buffer;
Q data_len;
Q max_data_len;
{mutex="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}} lock;
b1 is_dictionary;
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
-[NWConcrete_nw_txt_record init];
-[NWConcrete_nw_txt_record dealloc];
-[NWConcrete_nw_txt_record description];
```
