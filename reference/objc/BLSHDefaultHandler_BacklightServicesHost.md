# `BLSHDefaultHandler`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 5 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _key;
@"NSArray" _attributes;
@"BLSAssertion" _lock_assertion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHDefaultHandler handlerForKey:attributes:];
```

## Instance methods

```
-[BLSHDefaultHandler dealloc];
-[BLSHDefaultHandler invalidate];
-[BLSHDefaultHandler description];
-[BLSHDefaultHandler initWithKey:attributes:];
-[BLSHDefaultHandler updateForNewValue:];
```
