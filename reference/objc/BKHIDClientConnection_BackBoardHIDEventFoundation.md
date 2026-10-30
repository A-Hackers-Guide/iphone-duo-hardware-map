# `BKHIDClientConnection`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
^{__IOHIDEventSystemConnection=} _lock_connection;
q _versionedPID;
i _pid;
I _task;
@"NSString" _bundleID;
@"NSString" _lastPathComponent;
{atomic_flag="_Value"AB} _invalid;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (T@"NSString",R,C,N,V_lastPathComponent) lastPathComponent;
@property (Ti,R,N,V_pid) pid;
@property (Tq,R,N,V_versionedPID) versionedPID;
@property (TI,R,N,V_task) task;
@property (T@"NSString",R,C,N) succinctDescriptionOfRemoteProcess;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKHIDClientConnection connectionWithConnection:];
```

## Instance methods

```
-[BKHIDClientConnection dealloc];
-[BKHIDClientConnection versionedPID];
-[BKHIDClientConnection initWithConnection:];
-[BKHIDClientConnection invalidate];
-[BKHIDClientConnection pid];
-[BKHIDClientConnection connection];
-[BKHIDClientConnection hash];
-[BKHIDClientConnection description];
-[BKHIDClientConnection lastPathComponent];
-[BKHIDClientConnection bundleID];
-[BKHIDClientConnection task];
-[BKHIDClientConnection succinctDescriptionOfRemoteProcess];
-[BKHIDClientConnection isEqual:];
-[BKHIDClientConnection copyConnection];
```
