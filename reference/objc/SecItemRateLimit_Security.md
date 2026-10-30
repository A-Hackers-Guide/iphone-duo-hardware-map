# `SecItemRateLimit`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 14 instance methods, 3 class methods

## Instance variables

```
B _forceEnabled;
@"NSObject<OS_dispatch_queue>" _dataQueue;
i _roCapacity;
i _rwCapacity;
d _roRate;
d _rwRate;
d _limitMultiplier;
@"NSDate" _roBucket;
@"NSDate" _rwBucket;
```

## Properties

```
@property (Ti,R,N,V_roCapacity) roCapacity;
@property (Td,R,N,V_roRate) roRate;
@property (Ti,R,N,V_rwCapacity) rwCapacity;
@property (Td,R,N,V_rwRate) rwRate;
@property (Td,R,N,V_limitMultiplier) limitMultiplier;
@property (T@"NSDate",R,N,V_roBucket) roBucket;
@property (T@"NSDate",R,N,V_rwBucket) rwBucket;
```

## Class methods

```
+[SecItemRateLimit instance];
+[SecItemRateLimit getStaticRateLimit];
+[SecItemRateLimit resetStaticRateLimit];
```

## Instance methods

```
-[SecItemRateLimit limitMultiplier];
-[SecItemRateLimit rwBucket];
-[SecItemRateLimit init];
-[SecItemRateLimit isModifyingAPICallWithinLimits];
-[SecItemRateLimit forceEnabled:];
-[SecItemRateLimit rwCapacity];
-[SecItemRateLimit isEnabled];
-[SecItemRateLimit shouldCountAPICalls];
-[SecItemRateLimit consumeTokenFromBucket:];
-[SecItemRateLimit rwRate];
-[SecItemRateLimit roCapacity];
-[SecItemRateLimit isReadOnlyAPICallWithinLimits];
-[SecItemRateLimit roBucket];
-[SecItemRateLimit roRate];
```
