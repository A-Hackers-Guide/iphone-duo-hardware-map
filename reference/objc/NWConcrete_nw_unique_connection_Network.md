# `NWConcrete_nw_unique_connection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OS_nw_unique_connection`
- 9 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_endpoint>" endpoint;
[436c] service;
Q receivedSequenceNumber;
Q uniqueID;
[16C] uuid;
@"NWConcrete_nw_connection" connection;
i dupedSocketFD;
b1 isIncoming;
b1 usesASQUIC;
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
-[NWConcrete_nw_unique_connection init];
-[NWConcrete_nw_unique_connection dealloc];
-[NWConcrete_nw_unique_connection description];
```
