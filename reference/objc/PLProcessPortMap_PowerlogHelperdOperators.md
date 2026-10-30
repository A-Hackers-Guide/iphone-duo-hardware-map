# `PLProcessPortMap`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _strictLookupMap;
@"NSMutableDictionary" _lenientLookupMap;
@"NSMutableDictionary" _localPortOnlyLookupMap;
@"NSMutableDictionary" _ipAddrLookupMap;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_strictLookupMap) strictLookupMap;
@property (T@"NSMutableDictionary",&,V_lenientLookupMap) lenientLookupMap;
@property (T@"NSMutableDictionary",&,V_localPortOnlyLookupMap) localPortOnlyLookupMap;
@property (T@"NSMutableDictionary",&,V_ipAddrLookupMap) ipAddrLookupMap;
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
```

## Class methods

```
+[PLProcessPortMap sharedInstance];
```

## Instance methods

```
-[PLProcessPortMap setWorkQueue:];
-[PLProcessPortMap init];
-[PLProcessPortMap workQueue];
-[PLProcessPortMap dealloc];
-[PLProcessPortMap ipAddrLookupMap];
-[PLProcessPortMap strictLookupMap];
-[PLProcessPortMap clearPortMap];
-[PLProcessPortMap clearPortMapInternal];
-[PLProcessPortMap dictFromNetPortInfo:];
-[PLProcessPortMap getLookupKeys:];
-[PLProcessPortMap isAddressIPV4:];
-[PLProcessPortMap keyForIPAddrLookup:withSourceAddress:];
-[PLProcessPortMap keyForlenientLookup:withPort:withProtocol:];
-[PLProcessPortMap keyForlocalPortLookup:withProtocol:];
-[PLProcessPortMap keyFromAddress:withPort:withSourceAddress:withSourcePort:withProtocol:];
-[PLProcessPortMap lenientLookupMap];
-[PLProcessPortMap localPortOnlyLookupMap];
-[PLProcessPortMap pidAndProcessNameForDestAddress:withDestPort:withSourceAddress:withSourcePort:withProtocol:];
-[PLProcessPortMap reconstructPortMap];
-[PLProcessPortMap reconstructPortMapInternal];
-[PLProcessPortMap setIpAddrLookupMap:];
-[PLProcessPortMap setLenientLookupMap:];
-[PLProcessPortMap setLocalPortOnlyLookupMap:];
-[PLProcessPortMap setStrictLookupMap:];
```
