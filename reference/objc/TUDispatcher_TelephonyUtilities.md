# `TUDispatcher`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_dispatchQueue) dispatchQueue;
```

## Class methods

```
+[TUDispatcher dispatcherWithIdentifier:];
+[TUDispatcher dispatcherWithQueue:];
```

## Instance methods

```
-[TUDispatcher dispatchQueue];
-[TUDispatcher initWithQueue:];
-[TUDispatcher init];
-[TUDispatcher initWithIdentifier:];
-[TUDispatcher boostQualityOfService];
-[TUDispatcher dispatchAsynchronousBlock:];
-[TUDispatcher dispatchSynchronousBlock:];
-[TUDispatcher qosUserInteractiveDispatchBlockForBlock:];
```
