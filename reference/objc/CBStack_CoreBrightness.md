# `CBStack`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
Q _length;
@ _objectToPop;
@"NSMutableArray" _stack;
```

## Properties

```
@property (TQ,V_length) length;
@property (T@,R,N,V_objectToPop) objectToPop;
@property (T@"NSMutableArray",R,N,V_stack) stack;
```

## Instance methods

```
-[CBStack initWithLength:];
-[CBStack clear];
-[CBStack init];
-[CBStack dealloc];
-[CBStack length];
-[CBStack stack];
-[CBStack setLength:];
-[CBStack objectToPop];
-[CBStack popObj];
-[CBStack printStack];
-[CBStack pushObj:];
```
