# `BLSAssertionAcquisitionObserver`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionObserving`
- 2 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@? _lock_completion;
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
+[BLSAssertionAcquisitionObserver observerWithCompletion:];
```

## Instance methods

```
-[BLSAssertionAcquisitionObserver assertion:didCancelWithError:];
-[BLSAssertionAcquisitionObserver assertion:didFailToAcquireWithError:];
-[BLSAssertionAcquisitionObserver assertionWasAcquired:];
```
