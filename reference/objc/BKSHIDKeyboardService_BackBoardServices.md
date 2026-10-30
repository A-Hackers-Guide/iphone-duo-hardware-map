# `BKSHIDKeyboardService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSKeyboardServiceServerToClientIPC`
- 7 instance variables, 4 properties, 5 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSCompoundAssertion" _observerAssertion;
@"BSCompoundAssertion" _proxiesAssertion;
B _lock_currentlyObserving;
@"BSOrderedDictionary" _lock_senderIDToDevice;
@"NSMutableDictionary" _lock_pendingLayoutUpdatesBySenderID;
@"BSServiceConnection" _connection;
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
+[BKSHIDKeyboardService sharedInstance];
+[BKSHIDKeyboardService new];
```

## Instance methods

```
-[BKSHIDKeyboardService init];
-[BKSHIDKeyboardService addKeyboardObserver:];
-[BKSHIDKeyboardService allKeyboardDevices];
-[BKSHIDKeyboardService keyboardDeviceForSenderID:];
-[BKSHIDKeyboardService setConnectedKeyboards:withReply:];
```
