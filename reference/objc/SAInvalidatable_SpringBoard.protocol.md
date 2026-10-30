# `SAInvalidatable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisValid) valid;
@property (T@"NSDate",?,R,C,N) creationDate;
```

## Instance methods

```
-[SAInvalidatable invalidateWithReason:];
-[SAInvalidatable addInvalidationBlock:];
-[SAInvalidatable isValid];
-[SAInvalidatable creationDate];
```
