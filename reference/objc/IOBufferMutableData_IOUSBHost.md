# `IOBufferMutableData`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSMutableData`
- 4 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _bytes;
Q _length;
I _bufferID;
@? _deallocator;
```

## Properties

```
@property (T@?,C,V_deallocator) deallocator;
```

## Instance methods

```
-[IOBufferMutableData setID:];
-[IOBufferMutableData deallocator];
-[IOBufferMutableData setDeallocator:];
-[IOBufferMutableData dealloc];
-[IOBufferMutableData length];
-[IOBufferMutableData mutableBytes];
-[IOBufferMutableData bytes];
-[IOBufferMutableData setLength:];
-[IOBufferMutableData bufferID];
-[IOBufferMutableData initWithBytesNoCopy:length:bufferID:deallocator:];
```
