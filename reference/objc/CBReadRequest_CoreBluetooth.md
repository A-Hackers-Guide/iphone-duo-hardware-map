# `CBReadRequest`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
* _bufferPtr;
@"NSError" _error;
Q _length;
@? _completion;
@"NSData" _data;
Q _minLength;
Q _maxLength;
@"NSMutableData" _bufferData;
```

## Properties

```
@property (T@"NSMutableData",&,N,V_bufferData) bufferData;
@property (T@"NSData",&,N,V_data) data;
@property (T@?,C,N,V_completion) completion;
@property (T@"NSError",R,N,V_error) error;
@property (TQ,R,N,V_length) length;
@property (TQ,N,V_minLength) minLength;
@property (TQ,N,V_maxLength) maxLength;
```

## Instance methods

```
-[CBReadRequest setCompletion:];
-[CBReadRequest completion];
-[CBReadRequest data];
-[CBReadRequest length];
-[CBReadRequest error];
-[CBReadRequest setData:];
-[CBReadRequest maxLength];
-[CBReadRequest minLength];
-[CBReadRequest setMaxLength:];
-[CBReadRequest setMinLength:];
-[CBReadRequest bufferData];
-[CBReadRequest setBufferData:];
```
