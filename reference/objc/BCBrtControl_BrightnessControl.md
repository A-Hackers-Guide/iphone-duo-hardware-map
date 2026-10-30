# `BCBrtControl`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 13 properties, 29 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _id;
B _isValid;
@"NSMutableDictionary" _capabilities;
d _maxNits;
d _midNits;
d _minNits;
@"NSUUID" _containerID;
^{__CFUUID=} _cfContainerID;
I _displayService;
B _multipleControlEnabled;
@? _displayInvalidHandler;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",R) logHandle;
@property (T@"NSObject<OS_dispatch_queue>",R) queue;
@property (T^{__CFUUID=},R) cfContainerID;
@property (T@"NSUUID",R,V_containerID) containerID;
@property (Td,R,V_maxNits) maxNits;
@property (Td,R,V_minNits) minNits;
@property (T@,R,C) ID;
@property (T@"NSDictionary",R,V_capabilities) capabilities;
@property (TB,V_multipleControlEnabled) multipleControlEnabled;
@property (TQ,R) hash;
@property (TB,R,V_isValid) isValid;
@property (T@?,C,V_displayInvalidHandler) displayInvalidHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,V_callbackQueue) callbackQueue;
```

## Class methods

```
+[BCBrtControl copyAllAvailableControls];
+[BCBrtControl copyAvailableControls];
+[BCBrtControl newMonitorForAllControlsWithHandler:error:];
+[BCBrtControl newMonitorWithHandler:error:];
```

## Instance methods

```
-[BCBrtControl ID];
-[BCBrtControl init];
-[BCBrtControl logHandle];
-[BCBrtControl dealloc];
-[BCBrtControl copyProperty:error:];
-[BCBrtControl containerID];
-[BCBrtControl queue];
-[BCBrtControl setCallbackQueue:];
-[BCBrtControl isValid];
-[BCBrtControl callbackQueue];
-[BCBrtControl capabilities];
-[BCBrtControl hash];
-[BCBrtControl isEqual:];
-[BCBrtControl minNits];
-[BCBrtControl maxNits];
-[BCBrtControl setNitsAsync:completionHandler:];
-[BCBrtControl _checkIsValid:];
-[BCBrtControl _runOnCallbackQueue:];
-[BCBrtControl cfContainerID];
-[BCBrtControl copyModuleIdentifier];
-[BCBrtControl displayInvalidHandler];
-[BCBrtControl getNitsWithError:];
-[BCBrtControl multipleControlEnabled];
-[BCBrtControl setDisplayInvalidHandler:];
-[BCBrtControl setDisplayService:];
-[BCBrtControl setMultipleControlEnabled:];
-[BCBrtControl setNits:error:];
-[BCBrtControl setProperty:value:error:];
-[BCBrtControl setPropertyAync:value:completionHandler:];
```
