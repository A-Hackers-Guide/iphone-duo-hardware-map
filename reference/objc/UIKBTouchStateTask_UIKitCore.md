# `UIKBTouchStateTask`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"UIKBTouchState" _touchState;
@? _task;
B _isBusy;
```

## Properties

```
@property (T@"UIKBTouchState",R,N,V_touchState) touchState;
@property (T@?,R,C,N,V_task) task;
@property (TB,N,V_isBusy) isBusy;
```

## Class methods

```
+[UIKBTouchStateTask touchStateTaskForTouchState:andTask:];
```

## Instance methods

```
-[UIKBTouchStateTask compare:];
-[UIKBTouchStateTask isBusy];
-[UIKBTouchStateTask task];
-[UIKBTouchStateTask copyWithZone:];
-[UIKBTouchStateTask initWithTouchState:andTask:];
-[UIKBTouchStateTask setIsBusy:];
-[UIKBTouchStateTask touchState];
```
