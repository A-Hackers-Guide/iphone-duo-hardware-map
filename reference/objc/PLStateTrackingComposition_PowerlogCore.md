# `PLStateTrackingComposition`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _workQueue;
@"NSMutableDictionary" _executeBlockCache;
@"NSMutableArray" _stateChangeNotifications;
Q _stateChangeMask;
@"NSDate" _systemStateChangeTime;
@"NSMutableDictionary" _stateIDToStateMap;
@"NSMutableDictionary" _entryKeyToStateMap;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_workQueue) workQueue;
@property (T@"NSMutableDictionary",&,V_executeBlockCache) executeBlockCache;
@property (T@"NSMutableArray",&,V_stateChangeNotifications) stateChangeNotifications;
@property (TQ,V_stateChangeMask) stateChangeMask;
@property (T@"NSDate",&,V_systemStateChangeTime) systemStateChangeTime;
@property (T@"NSMutableDictionary",&,V_stateIDToStateMap) stateIDToStateMap;
@property (T@"NSMutableDictionary",&,V_entryKeyToStateMap) entryKeyToStateMap;
```

## Class methods

```
+[PLStateTrackingComposition sharedInstance];
+[PLStateTrackingComposition registerState:];
```

## Instance methods

```
-[PLStateTrackingComposition setWorkQueue:];
-[PLStateTrackingComposition init];
-[PLStateTrackingComposition workQueue];
-[PLStateTrackingComposition handleStateChange:];
-[PLStateTrackingComposition stateChanged:];
-[PLStateTrackingComposition initializeState];
-[PLStateTrackingComposition stateChangeMask];
-[PLStateTrackingComposition entryKeyToStateMap];
-[PLStateTrackingComposition executeBlockCache];
-[PLStateTrackingComposition getCurrState:];
-[PLStateTrackingComposition getLastState:];
-[PLStateTrackingComposition getState:beforeDate:];
-[PLStateTrackingComposition getStateBeforeSystemStateChange:];
-[PLStateTrackingComposition getStateChangeTime:];
-[PLStateTrackingComposition getSystemStateChangeTime];
-[PLStateTrackingComposition registerForListeners];
-[PLStateTrackingComposition registerForStates:withOperator:withBlock:];
-[PLStateTrackingComposition setEntryKeyToStateMap:];
-[PLStateTrackingComposition setExecuteBlockCache:];
-[PLStateTrackingComposition setStateChangeMask:];
-[PLStateTrackingComposition setStateChangeNotifications:];
-[PLStateTrackingComposition setStateIDToStateMap:];
-[PLStateTrackingComposition setSystemStateChangeTime:];
-[PLStateTrackingComposition stateChangeNotifications];
-[PLStateTrackingComposition stateIDToStateMap];
-[PLStateTrackingComposition systemStateChangeTime];
-[PLStateTrackingComposition triggerBlocks];
```
