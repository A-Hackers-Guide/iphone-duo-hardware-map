# `BLSHLocalAssertionAttributeHandler`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHAssertionAttributeHandler`
- 3 instance variables, 6 properties, 7 instance methods, 4 class methods

## Instance variables

```
@"NSMutableDictionary" _entries;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHLocalAssertionService" _service;
```

## Properties

```
@property (T@"BLSHLocalAssertionService",R,W,N,V_service) service;
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHLocalAssertionAttributeHandler entryClass];
+[BLSHLocalAssertionAttributeHandler attributeBaseClass];
+[BLSHLocalAssertionAttributeHandler attributeClasses];
+[BLSHLocalAssertionAttributeHandler registerHandlerForService:];
```

## Instance methods

```
-[BLSHLocalAssertionAttributeHandler display];
-[BLSHLocalAssertionAttributeHandler initForService:];
-[BLSHLocalAssertionAttributeHandler service];
-[BLSHLocalAssertionAttributeHandler attributeClasses];
-[BLSHLocalAssertionAttributeHandler setupService];
-[BLSHLocalAssertionAttributeHandler activateAttributes:fromAssertion:forService:];
-[BLSHLocalAssertionAttributeHandler deactivateAttributes:fromAssertion:forService:];
```
