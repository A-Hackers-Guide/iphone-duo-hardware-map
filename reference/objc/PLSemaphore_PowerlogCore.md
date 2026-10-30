# `PLSemaphore`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 18 instance methods, 1 class methods

## Instance variables

```
d _timeout;
@"NSMutableSet" _interestedObjects;
@"NSMutableSet" _pendingDoneObjects;
@"NSString" _key;
@"NSCondition" _pendingObjectsLock;
```

## Properties

```
@property (T@"NSCondition",&,V_pendingObjectsLock) pendingObjectsLock;
@property (Td,V_timeout) timeout;
@property (T@"NSMutableSet",&,V_interestedObjects) interestedObjects;
@property (T@"NSMutableSet",&,V_pendingDoneObjects) pendingDoneObjects;
@property (T@"NSString",&,V_key) key;
@property (TB,R) isActive;
```

## Class methods

```
+[PLSemaphore sharedSemaphoreForKey:];
```

## Instance methods

```
-[PLSemaphore setKey:];
-[PLSemaphore timeout];
-[PLSemaphore setTimeout:];
-[PLSemaphore initWithKey:];
-[PLSemaphore isActive];
-[PLSemaphore key];
-[PLSemaphore interestedObjects];
-[PLSemaphore pendingDoneObjects];
-[PLSemaphore pendingObjectsLock];
-[PLSemaphore setInterestedObjects:];
-[PLSemaphore setPendingDoneObjects:];
-[PLSemaphore setPendingObjectsLock:];
-[PLSemaphore signalDoneByObject:];
-[PLSemaphore signalInterestByObject:];
-[PLSemaphore signalNonInterestByObject:];
-[PLSemaphore signalStartListening];
-[PLSemaphore waitWithBlock:];
-[PLSemaphore waitWithBlockSync:];
```
