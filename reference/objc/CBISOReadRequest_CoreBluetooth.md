# `CBISOReadRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
I _missedReads;
@? _completionHandler;
@"NSData" _data;
@"NSError" _error;
```

## Properties

```
@property (T@"NSData",&,N,V_data) data;
@property (T@"NSError",C,N,V_error) error;
@property (TI,N,V_missedReads) missedReads;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[CBISOReadRequest setError:];
-[CBISOReadRequest setCompletionHandler:];
-[CBISOReadRequest completionHandler];
-[CBISOReadRequest data];
-[CBISOReadRequest error];
-[CBISOReadRequest setData:];
-[CBISOReadRequest setMissedReads:];
-[CBISOReadRequest missedReads];
```
