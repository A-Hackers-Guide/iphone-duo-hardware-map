# `BLSHLocalCountingAssertionAttributeHandler`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHLocalAssertionAttributeHandler`
- 2 instance variables, 0 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _lock_entryDictionary;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _countingDictionaryLock;
```

## Class methods

```
+[BLSHLocalCountingAssertionAttributeHandler entryClass];
+[BLSHLocalCountingAssertionAttributeHandler attributeBaseClass];
+[BLSHLocalCountingAssertionAttributeHandler attributeClasses];
```

## Instance methods

```
-[BLSHLocalCountingAssertionAttributeHandler initForService:];
-[BLSHLocalCountingAssertionAttributeHandler activateWithFirstEntry:];
-[BLSHLocalCountingAssertionAttributeHandler countingTargetForEntry:];
-[BLSHLocalCountingAssertionAttributeHandler deactivateWithFinalEntry:];
-[BLSHLocalCountingAssertionAttributeHandler entriesForCountingTarget:];
```
