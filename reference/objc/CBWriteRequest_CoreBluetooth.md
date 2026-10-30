# `CBWriteRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSError" _error;
[16{iovec="iov_base"^v"iov_len"Q}] _iov;
^{iovec=^vQ} _iop;
i _ion;
Q _offset;
B _endOfData;
@? _completion;
@"NSArray" _dataArray;
```

## Properties

```
@property (T@?,C,N,V_completion) completion;
@property (T@"NSArray",&,N,V_dataArray) dataArray;
@property (TB,N,V_endOfData) endOfData;
@property (T@"NSError",R,N,V_error) error;
```

## Instance methods

```
-[CBWriteRequest setCompletion:];
-[CBWriteRequest completion];
-[CBWriteRequest error];
-[CBWriteRequest dataArray];
-[CBWriteRequest endOfData];
-[CBWriteRequest setDataArray:];
-[CBWriteRequest setEndOfData:];
```
