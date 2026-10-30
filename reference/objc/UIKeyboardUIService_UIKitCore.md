# `UIKeyboardUIService`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`
- 4 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"BSServiceConnectionListener" _bsConnectionlistener;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"CAContext" _context;
@"NSMutableArray" _slots;
```

## Properties

```
@property (T@"CAContext",R,N) context;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardUIService serviceInterface];
+[UIKeyboardUIService sharedService];
```

## Instance methods

```
-[UIKeyboardUIService listener:didReceiveConnection:withContext:];
-[UIKeyboardUIService init];
-[UIKeyboardUIService dealloc];
-[UIKeyboardUIService context];
-[UIKeyboardUIService clearSlots];
-[UIKeyboardUIService createContext];
-[UIKeyboardUIService createSlot:];
```
